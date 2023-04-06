"""Create Api for VM creation
"""
import requests
import os
import json

from flask import request
from pathlib import Path
from app import app
from utils import decrypt
from constants import (
    SESSION_API_URL,
    FOLDER_API_URL,
    DATASTORE_API_URL,
    CHECK_ROLE,
    CREATE_VM_API_URL,
    ADMIN_ROLE,
    DELETE_VM_API_URL,
    GET_VM_API_URL
)
from dotenv import load_dotenv

env_path = Path("../", ".env")
load_dotenv(dotenv_path=env_path)

VM_USERNAME = os.getenv("VM_USERNAME")
VM_PASSWORD = os.getenv("VM_PASSWORD")


def get_session_key():
    """function use for getting the session key from the VmWare cis rest api

    Returns:
        dict: returns the auth and session key
    """
    try:
        username = VM_USERNAME
        password = decrypt(VM_PASSWORD).decode()
        auth = (username, password)
        session_response = requests.post(
            SESSION_API_URL, auth=auth, verify=False, timeout=30
        )
        if session_response.status_code != 200:
            return {
                "error": {
                    "message": "Something went wrong"
                }
            }, session_response.status_code
        SESSION_KEY = session_response.json()["value"]
        return {
            "SESSION_KEY": SESSION_KEY,
            "auth": auth
        }
    except Exception as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500


@app.route("/folders", methods=["GET"])
def get_folder():
    """this function get all the folders from the vSphere client using vcenter api

    Returns:
        dict: returns the folder information
    """
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, response.status_code
        if response.json()['user']['code'] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        session_dict = get_session_key()
        print("above")
        headers = {"vmware-api-session-id": session_dict["SESSION_KEY"]}
        # headers = {"vmware-api-session-id": "788be2fbc4f88efa66bcaba9cdd5b4af"}
        response = requests.get(
            FOLDER_API_URL,
            headers=headers,
            auth=session_dict["auth"],
            verify=False,
            timeout=30,
        )

        if response.status_code != 200:
            print("not 200")
            print(response.json()["value"]["messages"][0]["default_message"])
            return {
                "error": {
                    "message": response.json()["value"]["messages"][0]["default_message"]
                }
            }, response.status_code
            # return {
            #     "error": {
            #         "message": "Something went wrong"
            #     }
            # }, response.status_code
        return {
            "folders": response.json()["value"]
        }, 200
    except Exception as error_message:
        print("in")
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500


@app.route("/datastores", methods=["GET"])
def get_datastore():
    """this function get all the datastores from the vSphere client using vcenter api

    Returns:
        dict: returns the datastore information
    """
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, response.status_code
        if response.json()['user']['code'] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        session_dict = get_session_key()
        headers = {"vmware-api-session-id": session_dict["SESSION_KEY"]}
        response = requests.get(
            DATASTORE_API_URL,
            headers=headers,
            auth=session_dict["auth"],
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": "Something went wrong"
                }
            }, response.status_code
        return {
            "datastores": response.json()["value"]
        }, 200
    except Exception as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500


@app.route("/guestos", methods=["GET"])
def guest_os():
    """this function get all the guest os versions from the JSON file

    Returns:
        dict: returns the guest os information
    """
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, response.status_code
        if response.json()['user']['code'] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        with open("guest_os.json", "r") as file:
            json_data = json.load(file)
            return {
                "guestos": json_data
            }, 200
    except FileNotFoundError as error_message:
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


@app.route("/vm", methods=["POST"])
def create_vm():
    """this function create the vm in Vsphere client

    Returns:
        dict: return the VM ID
    """
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, response.status_code
        if response.json()['user']['code'] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        session_dict = get_session_key()
        headers = {"vmware-api-session-id": session_dict["SESSION_KEY"]}
        data = request.get_json()
        print(data)
        payload = {
            "spec": {
                "guest_OS": data.get("guestos"),
                "placement": {
                    "folder": data.get("folder"),
                    "datastore": data.get("datastore"),
                    "host": "host-12",
                },
                "cpu": {"count": data.get("cpu")},
                "memory": {"size_MiB": data.get("memory")},
                "name": data.get("vm_name"),
                "disks": [{"new_vmdk": {"capacity": data.get("disksize")}}],
            }
        }
        print(payload)
        response = requests.post(
            CREATE_VM_API_URL, headers=headers, json=payload, verify=False, timeout=30
        )
        print(response.json())
        if response.status_code != 200:
            return {
                "error": {
                    "message": "Something went wrong"
                }
            }, response.status_code
        return {
            "value": response.json()["value"]
        }, 200
    except Exception as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500

@app.route("/delete/vm", methods=["delete"])
def delete_vm():
    """this function delete the vm in Vsphere client

    Returns:
        dict: return simple message(successful or not)
    """
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, response.status_code
        if response.json()['user']['code'] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        session_dict = get_session_key()
        headers = {"vmware-api-session-id": session_dict["SESSION_KEY"]}
        data = request.get_json()
        vmId = data["vmId"].strip()
        url = f"{DELETE_VM_API_URL}{vmId}"
        response = requests.delete(
            url=url, headers=headers, verify=False, timeout=30
        )
        print(response)
        if response.status_code == 200:
            return {
                "message": "VM deleted successfully"
            }, 200
        return {
                "error": {
                    "message": "Something went wrong"
                }
            }, response.status_code
    except Exception as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500

@app.route("/vm/list", methods=["GET"])
def Vm_list():
    """this function get the vm list from Vsphere client

    Returns:
        dict: return vm list
    """
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        response = requests.get(
            url=CHECK_ROLE,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
            timeout=30,
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": response.json()["message"]
                }
            }, response.status_code
        if response.json()['user']['code'] == ADMIN_ROLE:
            return {
                "error": {
                    "message": "Unauthorized"
                }
            }, 401
        session_dict = get_session_key()
        headers = {"vmware-api-session-id": session_dict["SESSION_KEY"]}
        response = requests.get(
            GET_VM_API_URL, headers=headers, verify=False, timeout=30
        )
        if response.status_code != 200:
            return {
                "error": {
                    "message": "Something went wrong"
                }
            }, response.status_code
        return {
            "vm_list": response.json()["value"]
        }, 200
    except Exception as error_message:
        return {
            "error": {
                "message": str(error_message)
            }
        }, 500