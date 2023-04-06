import React from 'react'
import axios from "axios"
import { toast } from 'react-toastify';
import { Space, Button } from 'antd';
import { COMMENT_API, CLOSE_ISSUE, IN_PROGRESS_URL, GET_DESCRIPTION_API, DELETE_VM_API, ADD_LABEL_API, GET_ADMIN_ISSUES_API } from '../constants';
import { Link } from 'react-router-dom';

export const closeIssue = async (ticket_id,setProgressLoading,setListLoading) => {
    setProgressLoading((prev) => {
        return prev.map((progress) => {
            if (progress.id === ticket_id) {
                progress.closeLoading = 1
            }
            return progress
        })
    })
    await axios({
        method : "POST",
        url : `${CLOSE_ISSUE}/${ticket_id}`,
        headers : {
            "Authorization" : `Bearer ${localStorage.getItem('VMT_TOKEN')}`,
        },
        validateStatus : function (status) {
            return status >= 200
        }
    }).then((response) => {
        if (response.status === 200) {
            toast.success(response.data.message)
            setListLoading(true)
        } else {
            toast.error(response.data.error.message)
        }
        setProgressLoading((prev) => {
            return prev.map((progress) => {
                if (progress.id === ticket_id) {
                    progress.closeLoading = 0
                }
                return progress
            })
        })
    }).catch((error) => {
        console.log(error)
    })
}

export const showModal = (id,setOpen,setCurrentId) => {
  setOpen(true);
  setCurrentId(id)
};

export const handleOk = async (currentId, modalText, setConfirmLoading,setOpen) => {
    setConfirmLoading(true);
    await axios({
        method : "POST",
        url : COMMENT_API,
        headers : {
            "Authorization" : `Bearer ${localStorage.getItem('VMT_TOKEN')}`
        },
        data : {
            "id" : currentId,
            "body" : modalText
        },
        validateStatus : function (status) {
            return status >= 200
        }
    }).then((response) => {
        if (response.status === 201) {
            toast.success("Comment added successfully.")
        } else {
            toast.error("Something went wrong.")
        }
    }).catch((error) => {
        console.log(error)
    })
    setOpen(false);
    setConfirmLoading(false);
};

export const handleCancel = (setOpen) => {
  setOpen(false);
};

export const inProgress = async (id,setProgressLoading,setListLoading) => {
    setProgressLoading((prev) => {
        return prev.map((progress) => {
            if (progress.id === id) {
                progress.inProgressLoading = 1
            }
            return progress
        })
    })
    await axios({
        method : "POST",
        url : IN_PROGRESS_URL,
        headers : {
            "Authorization" : `Bearer ${localStorage.getItem('VMT_TOKEN')}`
        },
        data : {
            "key" : id
        },
        validateStatus : function (status) {
            return status >= 200
        }
    }).then((response) => {
        console.log(response.data)
        if (response.status === 200) {
            toast.success(`${id} put in In progress.`)
            setListLoading(true)
        } else {
            toast.error("Something went wrong.")
        }
        setProgressLoading((prev) => {
            return prev.map((progress) => {
                if (progress.id === id) {
                    progress.inProgressLoading = 0
                }
                return progress
            })
        })
    }).catch((error) => {
        console.log(error)
    })
}

export const getAdminIssue = async (setIssues, setDeleteIssue, setProgressLoading, setCreateFilteredData, setDeleteFilteredData, setLoading) => {
    axios({
        url: GET_ADMIN_ISSUES_API,
        method: "GET",
        headers: {
            "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`,
        },
        validateStatus: function (status) {
            return status >= 200
        }
    }).then((response) => {
        if (response.data.error) {
            toast.error(response.data.error.message)
        } else {
            let createIssueList = []
            let deleteIssueList = []
            response.data.data.map((item)=> {
                if(item['label'][0] === "Create_VM"){
                     createIssueList.push(item)
                }else {
                     deleteIssueList.push(item)
                }
            })
            setIssues(createIssueList)
            setDeleteIssue(deleteIssueList)
            response.data.data.map((ticket) => {
                setProgressLoading((prev) => {
                    return [...prev,{id : ticket.ticket_id,inProgressLoading : 0,closeLoading : 0, deleteLoading : 0}]
                })
            })
            setCreateFilteredData(createIssueList)
            setDeleteFilteredData(deleteIssueList)
            setLoading(true)
        }
    }).catch((error) => {
        console.log(error)
    })
}

const deleteVM = async (ticket_id, setIssues, setDeleteIssue, setProgressLoading, setCreateFilteredData, setDeleteFilteredData, setLoading) => {
    const answer = prompt("Enter 'DELETE below to delete this VM'")
    if (answer === "DELETE") {
        setProgressLoading((prev) => {
            return prev.map((progress) => {
                if (progress.id === ticket_id) {
                    progress.deleteLoading = 1
                }
                return progress
            })
        })
        axios({
            url: GET_DESCRIPTION_API,
            // url:"http://172.20.11.108:5000/issue/description",
            method: "POST",
            data: {
                key : ticket_id,
                mode : "DELETE"
            },
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
            },
            validateStatus: function (status) {
                return status !== 200 || status !== 201
            }
        })
            .then(async (response) => {
                if (response.status === 200) {
                    await axios({
                        method : "DELETE",
                        url : DELETE_VM_API,
                        data : {
                            vmId : response.data.vm_id
                        },
                        headers: {
                            "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
                        },
                        validateStatus: function (status) {
                            return status !== 200 || status !== 201
                        }
                    }).then((res) => {
                        console.log(res.data)
                        if(res.status === 200){
                            axios({
                                method: "PUT",
                                url: ADD_LABEL_API,
                                data: {
                                    key: ticket_id,
                                    label: "Deleted"
                                },
                                headers: {
                                    "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
                                },
                                validateStatus: function (status) {
                                    return status !== 200 || status !== 201
                                }
                            }).then( (response) => {
                                if(response.status === 200) {
                                    getAdminIssue(setIssues, setDeleteIssue, setProgressLoading, setCreateFilteredData, setDeleteFilteredData, setLoading)
                                }
                                setProgressLoading((prev) => {
                                    return prev.map((progress) => {
                                        if (progress.id === ticket_id) {
                                            progress.deleteLoading = 0
                                        }
                                        return progress
                                    })
                                })
                            }
                            ).catch( (error) => {
                                toast.error("Something went wrong")
                            }
                            )
                            toast.success(res.data.message)
                        }
                        else
                            toast.error("Something went wrong")
                    }).catch((err) => {
                        toast.error("Something went wrong.")
                    })
                } else {
                    toast.error("Something went wrong.")
                }
                setProgressLoading((prev) => {
                    return prev.map((progress) => {
                        if (progress.id === ticket_id) {
                            progress.deleteLoading = 0
                        }
                        return progress
                    })
                })
            })
            .catch(error => {
                toast.error("Something went wrong.")
            })
    } else {
        toast.error("Invalid input")
    }
}

export const columns = (mode, setOpen, setCurrentId,progressLoading,setProgressLoading, setListLoading, setIssues, setDeleteIssue, setCreateFilteredData, setDeleteFilteredData, setLoading) => {
    return [
        {
            title: 'ID',
            dataIndex: 'ticket_id',
            render : (text,record) => <a href={record.url} target="_blank">{text}</a>
        },
        {
            title: "Reporter",
            dataIndex: 'reporter',
        },
        {
            title: 'Status',
            dataIndex: 'status',
            filters: [
                {
                    text: 'Open',
                    value: 'Open',
                },
                {
                    text: 'In Progress',
                    value: 'In Progress',
                },
                {
                    text: 'In Review',
                    value: 'In Review',
                },
                {
                    text: 'Approved',
                    value: 'Approved',
                },
                {
                    text: 'Cancelled',
                    value: 'Cancelled',
                },
                {
                    text: 'Untriage',
                    value: 'Untriage',
                },
            ],
            filterMode: 'tree',
            filterSearch: true,
            sorter: (a, b) => a.status.localeCompare(b.status),
            onFilter: (value, record) => record.status.startsWith(value),
        },
        {
            title: 'Priority',
            dataIndex: 'priority',
            filters: [
                {
                    text: 'Blocker',
                    value: 'Blocker',
                },
                {
                    text: 'Critical',
                    value: 'Critical',
                },
                {
                    text: 'Major',
                    value: 'Major',
                },
                {
                    text: 'Minor',
                    value: 'Minor',
                },
                {
                    text: 'Trivial',
                    value: 'Trivial',
                },
                {
                    text: 'Cosmetic',
                    value: 'Cosmetic',
                },
            ],
            filterMode: 'tree',
            filterSearch: true,
            sorter: (a, b) => a.priority.localeCompare(b.priority),
            onFilter: (value, record) => record.priority.startsWith(value),
        },
        {
            title: 'Action',
            key: 'action',
            render: (_, record) => (
              <Space size="middle">
                {
                    console.log(record)
                }
                <Button type="primary" className='admin-action-btn' onClick={() => {showModal(record.ticket_id,setOpen,setCurrentId)}}>Comment</Button>
                {
                    record.status !== "In Progress" ? <Button type="primary" className='admin-action-btn' loading={progressLoading.find(progress => progress.id == record.ticket_id).inProgressLoading} onClick={() => {inProgress(record.ticket_id,setProgressLoading,setListLoading)}}>In Progress</Button> : null
                }
                {
                    mode === "Create" ?
                        record.status === "In Progress" ? record.label.find((element) => element === "Created") !== undefined ? null : <Button type="primary" className='admin-action-btn'><Link to={`/create/vm/${record.ticket_id}`}>Create VM</Link></Button> : null 
                        // record.status === "In Progress" ? <Button type="primary" className='admin-action-btn'><Link to={`/create/vm/${record.ticket_id}`}>Create VM</Link></Button> : null
                     : record.status === "In Progress" ? record.label.find((element) => element === "Deleted") !== undefined ? null : <Button type="primary" className='admin-action-btn' loading={progressLoading.find(progress => progress.id == record.ticket_id).deleteLoading}  onClick={() => {deleteVM(record.ticket_id, setIssues, setDeleteIssue, setProgressLoading, setCreateFilteredData, setDeleteFilteredData, setLoading)}}>Delete VM</Button> : null
                }
                {
                    record.status === "In Progress" ? <Button type="primary" className='admin-action-btn' loading={progressLoading.find(progress => progress.id == record.ticket_id).closeLoading} onClick={() => {closeIssue(record.ticket_id, setProgressLoading,setListLoading)}}>Close Issue</Button> : null
                }
              </Space>
            ),
        },
    ]
}
