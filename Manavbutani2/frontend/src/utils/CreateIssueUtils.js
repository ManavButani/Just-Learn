import axios from "axios";
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { CREATE_ISSUE_API, USER_DASHBOARD } from "../constants";


export const createIssue = async (data, navigate, setIssueLoading) => {

    await axios({
        url: CREATE_ISSUE_API,
        // url:"http://172.20.11.108:5000/create/issue",
        method: "POST",
        headers: {
            "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`,
        },
        data: data,
        validateStatus: function (status) {
            return status >= 200
        }
    })
        .then(response => {
            if (response.status !== 200) {
                toast.error("something went Wrong")
            }
            else {
                return navigate(USER_DASHBOARD)
            }
        })
        .catch(error => {
            toast.error("something went Wrong")
        });
    setIssueLoading(false)
}


export function errorHandler(value, name, field, setField, error, setError) {

    if (name === "diskText") {
        setField({ ...field, diskSizeText: value });
    } else if (name === "diskUnit") {
        setField({ ...field, diskSizeUnit: value });
    } else if (name === "memory") {
        setField({ ...field, memory: value });
    } else if (name === "cpu") {
        setField({ ...field, cpu: value });
    }
    if (name === "diskText" && value < 1) {
        setError({ ...error, diskError: "Enter valid disk size" });
    }
    else if (name === "diskText" && value > 0) {
        setError({ ...error, diskError: "" });
    }
    else if (name === "memory" && value < 1) {
        setError({ ...error, memError: "Enter valid Memory" });
    } else if (name === "memory" && value > 0) {
        setError({ ...error, memError: "" });
    } else if (name === "cpu" && value < 1) {
        setError({ ...error, cpuError: "Enter valid CPU count" });
    } else if (name === "cpu" && value > 0) {
        setError({ ...error, cpuError: "" });
    }
}

export const onFinish = (values, navigate, error, setError, field, setIssueLoading, issueFlag) => {
    setIssueLoading(true)
    if (error.diskError === "" && error.memError === "" && error.cpuError === "") {
        setError({ ...error, submitError: '' })
        var data = {}
        if (issueFlag) {
            data = {
                ...values,
                component_name: "VM Creation",
                key: 'VBBT',
                assignee_name: "kush.mistry",
                type_name: "Task",
                ticket_label: "Create_VM",
                description: "Disk: " + field.diskSizeText + " " + field.diskSizeUnit + ", Memory(GB): " + field.memory + ", CPU: " + field.cpu + ", Guest OS: " + values.GuestOS + ", Employee Name: " + field.employeeName + ", Employee Id: " + field.employeeId
                // values.assignee_name.toLowerCase().replace(" ", "."),
            }
        } else {
            data = {
                ...values,
                component_name: "VM Creation",
                key: 'VBBT',
                assignee_name: "kush.mistry",
                type_name: "Task",
                ticket_label: "Delete_VM",
                description: "VM Name: " + values.VmName.split("~")[0] + ", VM Id: " + values.VmName.split("~")[1]
                // values.assignee_name.toLowerCase().replace(" ", "."),
            }
        }
        console.log(data)
        createIssue(data, navigate, setIssueLoading)
    }
    else {
        setError({ ...error, submitError: "Please enter valid Data." })
    }
}

export const handleGuestOsChange = (event, setOption, setOsList, guestos) => {

    switch (event.target.value) {
        case 'windows':
            setOsList(guestos.windows)
            setOption('windows')
            break;
        case 'linux':
            setOsList(guestos.linux)
            setOption('linux')
            break;
        case 'other':
            setOsList(guestos.others)
            setOption('other')
            break;
        default:
            break;
    }
}
