"""Perform  operations like get jira issues of specific user and create request for VM
"""
import os
from pathlib import Path

import jwt
import requests
from dotenv import load_dotenv
from flask import request
from jwt import ExpiredSignatureError, InvalidSignatureError

from app import app
from constants import (ADMIN_ROLE, CHECK_ROLE,JIRA_ADMIN_URL, JIRA_BASE_URL, USER_ROLE, CLOSE_ID, EPIC_ID)
from utils import decrypt

env_path = Path("../", ".env")
load_dotenv(dotenv_path=env_path)

JWT_KEY = os.getenv("JWT_KEY")


@app.route("/admin/issues", methods=["GET"])
def get_admin_issue():
    """Check authorization and return issues for specific user"""
    try:
        token = request.headers["Authorization"].split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=20,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, 400
        if response.json()["user"]["code"] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        decrypted_token = decrypt(token).decode("ascii")
        decrypted_token = decrypted_token[1: len(decrypted_token) - 1]
        user_data = jwt.decode(
            decrypted_token, key=JWT_KEY, algorithms=["HS256"])
        jira_auth = decrypt(
            user_data["user"]["jira_basic_auth"]).decode("ascii")
        jira_response = requests.get(
            url=JIRA_ADMIN_URL +
            user_data["user"]["username"] + " ORDER BY priority",
            headers={"Authorization": f"Basic {jira_auth}"},
            verify=False,
            timeout=20,
        )
        if jira_response.status_code == 200:
            issues = []
            for i in jira_response.json()["issues"]:
                issue = {
                    "ticket_id": i["key"],
                    "reporter": i["fields"]["reporter"]["displayName"],
                    "status": i["fields"]["status"]["name"],
                    "priority": i["fields"]["priority"]["name"],
                    "url": "https://10.50.4.37:8443/browse/" + i["key"],
                    "label": i["fields"]["labels"], 
                }
                issues.append(issue)
            return {"error": False, "data": issues}, 200
        return {
            "error": {
                "message": "Something went wrong"
            }
        }, 400
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


@app.route("/comment", methods=["POST"])
def add_comment():
    """Add comment to specific jira ticket

    Returns:
        response: error and message to acknowledge
    """
    try:
        token = request.headers["Authorization"].split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=20,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, 400
        if response.json()["user"]["code"] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        id = request.json["id"]
        decrypted_token = decrypt(token).decode("ascii")
        decrypted_token = decrypted_token[1: len(decrypted_token) - 1]
        user_data = jwt.decode(
            decrypted_token, key=JWT_KEY, algorithms=["HS256"])
        jira_auth = decrypt(
            user_data["user"]["jira_basic_auth"]).decode("ascii")
        jira_response = requests.post(
            url=JIRA_BASE_URL + f"issue/{id}/comment",
            headers={"Authorization": f"Basic {jira_auth}"},
            json={"body": request.json["body"]},
            verify=False,
            timeout=10,
        )
        if jira_response.status_code == 201:
            return {"error": False, "message": "Comment added successfully."}, 201
        return {
            "error": {
                "message": "Something went wrong"
            }
        }, 400
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


@app.route("/issue/close/<id>", methods=["POST"])
def close_issue(id):
    """Close jira issue

    Returns:
        Object: error and message for acknowledge
    """
    try:
        token = request.headers["Authorization"].split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=20,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, 400
        if response.json()["user"]["code"] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        decrypted_token = decrypt(token).decode("ascii")
        decrypted_token = decrypted_token[1: len(decrypted_token) - 1]
        user_data = jwt.decode(
            decrypted_token, key=JWT_KEY, algorithms=["HS256"])
        jira_auth = decrypt(
            user_data["user"]["jira_basic_auth"]).decode("ascii")
        print(JIRA_BASE_URL +
              f"issue/{id}/transitions?expand=transitions.fields")
        jira_response = requests.post(
            url=JIRA_BASE_URL +
            f"issue/{id}/transitions?expand=transitions.fields",
            headers={"Authorization": f"Basic {jira_auth}"},
            json={
                "update": {
                    "comment": [
                        {
                            "add": {
                                "body": "Task done."
                            }
                        }
                    ],
                    "worklog": [
                        {
                            "add": {
                                "timeSpent": "1m"
                            }
                        }
                    ]
                },
                "fields": {
                    "resolution": {
                        "name": "Done"
                    },
                    "customfield_10000": EPIC_ID
                },
                "transition": {
                    "id": CLOSE_ID
                }
            },
            verify=False,
            timeout=10,
        )
        if jira_response.status_code == 204:
            return {"error": False, "message": "Issue closed successfully."}, 200
        return {
            "error": {
                "message": "Something went wrong"
            }
        }, 400
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
