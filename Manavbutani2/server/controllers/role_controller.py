"""Check role of user and admin for authorization
"""
import os
from pathlib import Path

import jwt
import requests
from dotenv import load_dotenv
from flask import request
from jwt import ExpiredSignatureError, InvalidSignatureError

from app import app
from graphql import USERS_PAYLOAD, user_variable
from constants import ADMIN_ROLE, USER_ROLE, ADMIN_CODE, SENIOR_ADMIN_CODE
from utils import decrypt

env_path = Path("../", ".env")
load_dotenv(dotenv_path=env_path)

JWT_KEY = os.getenv("JWT_KEY")
GRAPHQL_URL = os.getenv("GRAPHQL_URL")
EMAIL_DOMAIN = os.getenv("EMAIL_DOMAIN")


@app.route("/check-auth", methods=["GET"])
def check_auth():
    """Check token for authorization and expired token

    Returns:
        Object: Token is valid or not and respective error message
    """
    try:
        encrypted_token = request.headers["Authorization"].split(" ")[1]
        token = decrypt(encrypted_token).decode("ascii")
        token = token[1 : len(token) - 1]
        data = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
        data["user"].pop("jira_basic_auth")
        user = data["user"]
        username = user["username"]
        first_name = username.split('.')[0]
        last_name = username.split('.')[1]
        email = f"{first_name}.{last_name}@{EMAIL_DOMAIN}"
        response = requests.get(
            url=GRAPHQL_URL,
            json={"query": USERS_PAYLOAD, "variables": user_variable(email)},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": "Something went wrong"
                }
            }, response.status_code
        employees = response.json()["data"]["getUserDetail"]
        if employees["empCode"] == data["user"]["employee_id"] and (
                    (
                        (
                            employees["designation"] == ADMIN_CODE
                            or employees["designation"] == SENIOR_ADMIN_CODE
                        )
                       and data["user"]["code"] == ADMIN_ROLE
                    )
                    or (
                        (
                            employees["designation"] != ADMIN_CODE
                            and employees["designation"] != SENIOR_ADMIN_CODE
                        )
                        and data["user"]["code"] == USER_ROLE
                    )
                ) :
                return {"error": False, "user": user}, 200

        return {
            "error": {
                "message": "Unauthorized"
            }
        }, response.status_code
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
