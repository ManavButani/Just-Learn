import axios from "axios";
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { CREATE_VM_API, ADD_LABEL_API } from "../constants";

function unitToBytes(diskSizeUnit) {
    let unitVlaue = 1;
    if (diskSizeUnit === 'MB') {
        unitVlaue = 1000000;
    } else if (diskSizeUnit === 'GB') {
        unitVlaue = 1000000000;
    } else {
        unitVlaue = 1000000000000;
    }
    return unitVlaue;
}

const onFinish = (values, vmData, error, setError, field, setVmLoading, JIRA_KEY) => {
    setVmLoading(1)
    if (error.cpuError === '' && error.diskError === '' && error.memError === '') {
        console.log(field.name)
        setError({ ...error, submitError: "" });
        vmData.vm_name = field.name;
        vmData.cpu = field.cpu;
        vmData.folder = values.Folder;
        vmData.datastore = values.Datastore;
        vmData.memory = field.memory * 1024;
        vmData.guestos = field.guestosValue;
        vmData.disksize = field.diskSizeText * unitToBytes(field.diskSizeUnit);
        createVm(vmData, setVmLoading, JIRA_KEY)
    } else {
        setError({ ...error, submitError: "Please enter valid data" });
        setVmLoading(0)
    }
};

function errorHandler(value, name, datastore, field, setField, error, setError) {
    if (name === "datastore") {
        const freeSpace = datastore.map((store) => {
            if (store.datastore === value) {
                return store.free_space;
            }
        })
        if (field.diskSizeText * unitToBytes(field.diskSizeUnit) > freeSpace[0]) {
            setError({ ...error, diskError: "Available free space: " + (freeSpace[0] / 1000000000).toFixed(2) + " GB" });
        } else {
            setError({ ...error, diskError: "" });
        }
    } else {
        const freeSpace = datastore.map((store) => {
            if (store.datastore === field.datastore) {
                return store.free_space;
            }
        })
        if (name === "diskText") {
            setField({ ...field, diskSizeText: value });
        } else if (name === "diskUnit") {
            setField({ ...field, diskSizeUnit: value });
        } else if (name === "memory") {
            setField({ ...field, memory: value });
        } else if (name === "cpu") {
            setField({ ...field, cpu: value });
        }

        if (name === "diskText") {
            if (value > 0) {
                if (value * unitToBytes(field.diskSizeUnit) > freeSpace[0]) {
                    setError({ ...error, diskError: "Available free space: " + (freeSpace[0] / 1000000000).toFixed(2) + " GB" });
                } else {
                    setError({ ...error, diskError: "" });
                }
            } else {
                setError({ ...error, diskError: "Enter valid Disk Size" });
            }
        } else if (name === "diskUnit") {
            if (field.diskSizeText > 0) {
                if (field.diskSizeText * unitToBytes(value) > freeSpace[0]) {
                    setError({ ...error, diskError: "Available free space: " + (freeSpace[0] / 1000000000).toFixed(2) + " GB" });
                } else {
                    setError({ ...error, diskError: "" });
                }
            } else {
                setError({ ...error, diskError: "Enter valid Disk Size" });
            }
        } else if (name === "memory" && value < 1) {
            setError({ ...error, memError: "Enter valid Memory" });
        } else if (name === "memory" && value > 0) {
            setError({ ...error, memError: "" });
        } else if (name === "cpu" && value < 1) {
            setError({ ...error, cpuError: "Enter valid CPU count" });
        } else if (name === "cpu" && value > 0) {
            setError({ ...error, cpuError: "" });
        }
    }
}
function createVm(vmData, setVmLoading, JIRA_KEY) {
    axios({
        url: CREATE_VM_API,
        method: "POST",
        data: vmData,
        headers: {
            "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`,
            "Content-Type": 'application/json'
        },
        validateStatus: function (status) {
            return status >= 200
        }

    }
    )
        .then(response => {
            if (response.status === 200) {
                toast.success(response.data.value + " Created")
                axios({
                    method: "PUT",
                    url: ADD_LABEL_API,
                    data: {
                        key: JIRA_KEY.key,
                        label: "Created"
                    },
                    headers: {
                        "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
                    },
                    validateStatus: function (status) {
                        return status !== 200 || status !== 201
                    }
                }).then((response) => {
                    if (response.status !== 200) {
                        toast.error("Something went wrong.")
                    }
                }
                ).catch((error) => {
                    toast.error("Something went wrong")
                }
                )
            } else {
                toast.error(response.data.error.message)
            }
            setVmLoading(0)
        })
        .catch(error => {
            console.log(error)
        })
}

const handleGuestOsChange = (event, guestos, setOsList, setOption) => {
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
    }
}

export default errorHandler;
export { onFinish, handleGuestOsChange};
