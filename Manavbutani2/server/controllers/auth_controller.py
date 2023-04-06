"""Check user credentials in AD and return respective data based on validation
"""
import base64
import datetime
import json
import os
from pathlib import Path

import jwt
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from dotenv import load_dotenv
from flask import request
from jwt import ExpiredSignatureError, InvalidSignatureError
from ldap3 import ALL, SUBTREE, Connection, Server
from ldap3.core.exceptions import LDAPBindError

from app import app
from graphql import USERS_PAYLOAD, DESIGNATION_PAYLOAD, user_variable
from constants import ADMIN_ROLE, USER_ROLE, ALGORITHM, ADMIN_CODE, SENIOR_ADMIN_CODE, PADDING
from utils import encrypt,decrypt

env_path = Path("../", ".env")
load_dotenv(dotenv_path=env_path)

IV = os.getenv("IV").encode("utf-8")
KEY = os.getenv("KEY")
JWT_KEY = os.getenv("JWT_KEY")
AD_SERVER_URL = os.getenv("AD_SERVER_URL")
AD_DOMAIN_NAME = os.getenv("AD_DOMAIN_NAME")
OU = os.getenv("OU")
GRAPHQL_URL = os.getenv("GRAPHQL_URL")
EMAIL_DOMAIN = os.getenv("EMAIL_DOMAIN")


@app.route("/login", methods=["POST"])
def login():
    """this is login api for VMT app, check the username and password to the AD credentials and
    after request the hrms endpoint and get the user details for further use

    Returns:
        dict: return the Auth token, token and user data
    """
    try:
        data = request.get_json()
        username = data.get("username")
        firstName = username.split('.')[0]
        lastName = username.split('.')[1]
        email = f"{firstName}.{lastName}@{EMAIL_DOMAIN}"
        enc = base64.b64decode(data.get("password"))
        cipher = AES.new(KEY.encode("utf-8"), AES.MODE_CBC, IV)
        password = unpad(cipher.decrypt(enc), PADDING)
        password = password.decode("utf-8", "ignore")
        server_uri = AD_SERVER_URL
        server = Server(server_uri, get_info=ALL)
        connection = Connection(
            server, f"{AD_DOMAIN_NAME}\\{username}", password=password, authentication="NTLM"
        )
        connection.bind()
        connection.search(
            search_base=f"OU={OU},DC={AD_DOMAIN_NAME},DC=LOCAL",
            search_filter=f"(sAMAccountName={username})",
            search_scope=SUBTREE,
            attributes=["*"],
        )
        results = connection.entries
        if len(results) == 0:
            return {
                "error": {
                    "message": "Invalid username or password"
                }
            }, 401
        response = requests.get(
            url=GRAPHQL_URL,
            json={"query": USERS_PAYLOAD, "variables": user_variable(email)},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": "Error occur from HRMS getUser api"
                }
            }, response.status_code
        user = response.json()["data"]["getUserDetail"]
        designation_response = requests.get(
            url=GRAPHQL_URL,
            json={"query": DESIGNATION_PAYLOAD},
            verify=False,
            timeout=30,
        )
        if designation_response.status_code != 200:
            return {
                "error": {
                    "message": "Error occur from HRMS designation_type api"
                }
            }, designation_response.status_code
        designation = list(
            filter(
                lambda data: data["code"] == user["designation"],
                designation_response.json()["data"]["dropdown"],
            )
        )
        jira_basic_auth = encrypt(
            base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        ).decode("utf-8", "ignore")
        if user["designation"] == ADMIN_CODE or user["designation"] == SENIOR_ADMIN_CODE:
            code = ADMIN_ROLE
        else:
            code = USER_ROLE
        user_data = {
            "username": username,
            "employee_id": user["empCode"],
            "email": user["email"],
            "designation": designation[0]["value"],
            "code": code,
            "jira_basic_auth": jira_basic_auth,
        }
        token = jwt.encode(
            {
                "user": user_data,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            },
            key=JWT_KEY,
            algorithm=ALGORITHM,
        )
        token = json.dumps(token)
        return {
            "data": {
                "code": code,
                "token": encrypt(token).decode("utf-8")
            },
        }, 200
    except LDAPBindError as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500
    except Exception as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500


@app.route("/user", methods=["GET"])
def get_user():
    """Decrypt token and return data to user

    Returns:
        Object: error and data
    """
    try:
        encrypted_token = request.headers["Authorization"].split(" ")[1]
        token = decrypt(encrypted_token).decode("ascii")
        token = token[1 : len(token) - 1]
        data = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
        data["user"].pop("jira_basic_auth")
        user = data["user"]
        return {"error": False, "user": user}, 200
    except ExpiredSignatureError:
        return {
            "error": {
                "message": "Token expired"
            }
        }, 500
    except InvalidSignatureError:
        return {
            "error": {
                "message": "Invalid Token"
            }
        }, 500
    except Exception as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500
