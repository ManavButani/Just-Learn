"""controller use to create a jira ticket using jira rest api."""
import os
import jwt
import requests
from app import app
from constants import (
    CHECK_ROLE,
    JIRA_CREATE_ISSUE_URL,
    JIRA_BASE_URL,
    IN_PROGRESS_ID,
    TRIAGE_ID,
    ADMIN_ROLE,
    ALGORITHM
)
from dotenv import load_dotenv
from flask import request
from graphql import ALL_USERS_PAYLOAD, ALL_USERS_VARIABLES
from jira import JIRAError
from utils import decrypt

load_dotenv()
JWT_KEY = os.getenv("JWT_KEY")
GRAPHQL_URL = os.getenv("GRAPHQL_URL")


@app.route("/assignees", methods=["GET"])
def get_assignees():
    """Give the list of IT admins

    Returns:
        dict: Array of IT admins
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
        response = requests.get(
            url=GRAPHQL_URL,
            json={"query": ALL_USERS_PAYLOAD,
                  "variables": ALL_USERS_VARIABLES},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {"error": {"message": "Something went wrong"}}, response.status_code
        employees = response.json()["data"]["allUser"]
        users = list(
            filter(
                lambda employee: employee["designation"] == "25"
                or employee["designation"] == "26",
                employees,
            )
        )
        return {"assignees": users}, 200

    except Exception as error:
        return {"error": {"message": str(error)}}, 500


@app.route("/create/issue", methods=["POST"])
def create_jira_issue():
    """authenticate user using passed token and crate a jira ticket using jira rest api.
    Returns:
        object: if successful then return id,key,and link of ticket.
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
        encrypted_token = request.headers.get("Authorization").split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {encrypted_token}"},
            verify=False,
            timeout=20,
        )
        if response.status_code != 200:
            return {
                "error": {"message": response.json()["message"]}
            }, response.status_code

        json_data = request.get_json()
        payload = {
            "fields": {
                "labels" : [
                    json_data.get("ticket_label")
                ],
                "summary": json_data.get("summary"),
                "issuetype": {"name": json_data.get("type_name")},
                "project": {"key": json_data.get("key")},
                "assignee": {"name": json_data.get("assignee_name")},
                "description": json_data.get("description"),
                "components": [{"name": json_data.get("component_name")}],
                "customfield_11131": {"value": json_data.get("location")},
                "priority": {"id": json_data.get("priority_id")},
            }
        }

        token = decrypt(encrypted_token).decode("ascii")
        token = token[1: len(token) - 1]
        data = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
        credentials = decrypt(data["user"]["jira_basic_auth"]).decode("ascii")
        jira_response = requests.post(
            url=JIRA_CREATE_ISSUE_URL,
            headers={"Authorization": f"Basic {credentials}"},
            json=payload,
            verify=False,
            timeout=30,
        )

        if jira_response.status_code != 201:
            return {
                "error": {
                    "message": jira_response.json()["errorMessages"],
                    "errors": jira_response.json()["errors"],
                }
            }, jira_response.status_code
        return {"ticket_data": jira_response.json()}, 200

    except JIRAError as error:
        return {"error": {"message": error.text}}, 500

    except Exception as error:
        return {"error": {"message": str(error)}}, 500


@app.route("/transitions", methods=["POST"])
def make_in_progress():
    """Make a Jira issue in "In Progress"

    Returns:
        dict: acknowledge using JSON
    """
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
    json_data = request.get_json()
    key = json_data.get("key")
    encrypted_token = request.headers.get("Authorization").split(" ")[1]
    token = decrypt(encrypted_token).decode("ascii")
    token = token[1: len(token) - 1]
    data = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
    credentials = decrypt(data["user"]["jira_basic_auth"]).decode("ascii")

    response = triage_ticket(credentials, key, TRIAGE_ID)
    if "error" in response:
        return response, 500
    response = triage_ticket(credentials, key, IN_PROGRESS_ID)
    print(response)
    if "error" in response:
        return response, 500
    else:
        return response, 200


def triage_ticket(credentials, ticket_key, id):
    """call jira Rest api for a transition.

    Args:
        ticket_key (string): ticket key for a transition
        id (string): appropriate id for transition

    Returns:
       object: if successful then return success message of ticket.
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
        payload = {"transition": {"id": str(id)}}

        response = requests.post(
            url=f"{JIRA_BASE_URL}issue/{ticket_key}/transitions",
            headers={"Authorization": f"Basic {credentials}"},
            json=payload,
            verify=False,
            timeout=30,
        )
        if response.status_code != 204:
            return {
                "error": {
                    "errorsMessage": response.json()["errorMessages"],
                    "errors": response.json()["errors"],
                }
            }
        else:
            return {"message": "transition changed"}

    except Exception as error:
        return {"error": {"message": str(error)}}


@app.route("/issue/description", methods=["POST"])
def get_issue_description():
    """this function return description of ticket.

    Returns:
        object: disk_size, disk_unit, memory, cpu.
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
        json_data = request.get_json()
        ticket_key = json_data.get("key")
        mode = json_data.get("mode")
        encrypted_token = request.headers.get("Authorization").split(" ")[1]
        token = decrypt(encrypted_token).decode("ascii")
        token = token[1: len(token) - 1]
        data = jwt.decode(token, JWT_KEY, algorithms=[ALGORITHM])
        credentials = decrypt(data["user"]["jira_basic_auth"]).decode("ascii")
        response = requests.get(
            url=f"{JIRA_BASE_URL}search?jql=key={ticket_key}",
            headers={"Authorization": f"Basic {credentials}"},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["errorMessages"],
                    "errors": response.json()["errors"],
                }
            }, response.status_code
        else:
            description = response.json()["issues"][0]["fields"]["description"]
            if mode == "CREATE":
                disk_text = description.split(",")[0].split(":")[1].split(" ")[1]
                disk_unit = description.split(",")[0].split(":")[1].split(" ")[2]
                memory = description.split(",")[1].split(":")[1].split(" ")[1]
                cpu = description.split(",")[2].split(":")[1].split(" ")[1]
                guest_os_title = description.split(
                    ",")[3].split(":")[1].split("(")[0].strip()
                guest_os_value = description.split(",")[3].split(
                    ":")[1].split("(")[1].split(")")[0]
                employee_name = description.split(",")[4].split(":")[
                    1].split(" ")[1]
                employee_id = description.split(",")[5].split(":")[1].split(" ")[1]

                return {
                    "disk_text": disk_text,
                    "disk_unit": disk_unit,
                    "memory": memory,
                    "cpu": cpu,
                    "guest_os_title": guest_os_title,
                    "guest_os_value": guest_os_value,
                    "employee_name": employee_name,
                    "employee_id": employee_id
                }, 200
            elif mode == "DELETE":
                return {
                    "vm_name" : description.split(",")[0].split(":")[1],
                    "vm_id" : description.split(",")[1].split(":")[1]
                }, 200
            else:
                return {
                    "error" : {
                    "message" : "Invalid mode"
                    }
                }, 500

    except Exception as error:
        return {"error": {"message": str(error)}}, 500
    
@app.route("/add/label", methods=["PUT"])
def add_label():
    """add a new Jira label"

    Returns:
        dict: acknowledge using JSON
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
        json_data = request.get_json()
        issue_id = json_data["key"]
        payload = {
                    "update":{
                        "labels":[
                            {
                                "add":json_data["label"]
                            }
                        ]
                    }
                }
        encrypted_token = request.headers.get("Authorization").split(" ")[1]
        token = decrypt(encrypted_token).decode("ascii")
        token = token[1: len(token) - 1]
        data = jwt.decode(token, JWT_KEY, algorithms=["HS256"])
        credentials = decrypt(data["user"]["jira_basic_auth"]).decode("ascii")
        response = requests.put(
            url=f"https://10.50.4.37:8443/rest/api/2/issue/{issue_id}",
            headers={"Authorization": f"Basic {credentials}"},
            json=payload,
            verify=False,
            timeout=30,
        )
        if response.status_code == 204:
            return {
                "message": "label added successfully"
            }, 200
        return {
            "error" : {
                "message" : "label not added"
                }
            }, 500
    except Exception as error:
        return {"error": {"message": str(error)}}, 500