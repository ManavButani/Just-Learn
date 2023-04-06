export const BASE_URL = "http://127.0.0.1:5000"
export const GET_USER_ISSUES_API = `${BASE_URL}/user/issues`
export const GET_ADMIN_ISSUES_API = `${BASE_URL}/admin/issues`
export const CHECK_ROLE = `${BASE_URL}/check-auth`
export const LOGIN_API = `${BASE_URL}/login`
export const COMMENT_API = `${BASE_URL}/comment`
export const CLOSE_ISSUE = `${BASE_URL}/issue/close`
export const GET_USER = `${BASE_URL}/user`
export const ADMIN_ROLE = "01"
export const USER_ROLE = "02"
export const GET_FOLDERS_API = `${BASE_URL}/folders`
export const GET_DATASTORES_API = `${BASE_URL}/datastores`
export const GET_GUEST_OS_API = `${BASE_URL}/guestos`
export const CREATE_VM_API = `${BASE_URL}/vm`
export const GET_DESCRIPTION_API = `${BASE_URL}/issue/description`
export const PROJECT_KEY = "VBBT"
export const LOGIN = "/login"
export const CREATE_VM = "/create/vm/:id"
export const ADMIN_DASHBOARD = "/admin/dashboard"
export const USER_DASHBOARD = "/user/dashboard"
export const CREATE_ISSUE = "/create/issue"
export const IN_PROGRESS_URL = `${BASE_URL}/transitions`
export const GET_ASSIGNEES = `${BASE_URL}/assignees`
export const CREATE_ISSUE_API = `${BASE_URL}/create/issue`
export const GET_VM_API = `${BASE_URL}/vm/list`
export const DELETE_VM_API = `${BASE_URL}/delete/vm`
export const ADD_LABEL_API = `${BASE_URL}/add/label`
export const LOCATION_LIST = [
    {
        "location": "Crest House - Ahmedabad"
    },
    {
        "location": "Pune"
    },
    {
        "location": "Bangalore"
    },
    {
        "location": "U.S Office"
    }
]
export const PRIORITY_LIST = [
    {
        "priority_name": "Bloker",
        "priority_id": "1",
        "icon_url": "https://10.50.4.37:8443/images/icons/priorities/blocker.svg"
    },
    {
        "priority_name": "Critical",
        "priority_id": "2",
        "icon_url": "https://10.50.4.37:8443/images/icons/priorities/critical.svg"
    },
    {
        "priority_name": "Major",
        "priority_id": "3",
        "icon_url": "https://10.50.4.37:8443/images/icons/priorities/major.svg"
    },
    {
        "priority_name": "Minor",
        "priority_id": "4",
        "icon_url": "https://10.50.4.37:8443/images/icons/priorities/minor.svg"
    },
    {
        "priority_name": "Trivial",
        "priority_id": "5",
        "icon_url": "https://10.50.4.37:8443/images/icons/priorities/trivial.svg"
    },
    {
        "priority_name": "Cosmetic",
        "priority_id": "6",
        "icon_url": "https://10.50.4.37:8443/images/icons/priorities/trivial.svg"
    }
]