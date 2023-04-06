import React, { useEffect, useState } from 'react'
import { Table, Input } from 'antd';
import { UserOutlined } from "@ant-design/icons"
import axios from "axios"
import { toast } from 'react-toastify';
import { Space, Spin, Modal } from 'antd';
import { GET_ADMIN_ISSUES_API, GET_USER, ADMIN_ROLE } from '../constants';
import { handleCancel, handleOk, columns, getAdminIssue } from "../utils/AdminDashBoardUtils"
import "../css/adminDashboard.css"

const AdminDashboard = ({setSelected}) => {

    const { TextArea } = Input;
    const [authorized, setAuthorized] = useState(true)
    const [issues, setIssues] = useState([]);
    const [deleteIssue, setDeleteIssue] = useState([]);
    const [createFiltered, setCreateFilteredData] = useState([])
    const [deleteFiltered, setDeleteFilteredData] = useState([])
    const [loading, setLoading] = useState(false);
    const [value, setValue] = useState('');
    const [open, setOpen] = useState(false);
    const [confirmLoading, setConfirmLoading] = useState(false);
    const [modalText, setModalText] = useState('Content of the modal');
    const [currentId, setCurrentId] = useState()
    const [progressLoading, setProgressLoading] = useState([])
    const [listLoading, setListLoading] = useState(false)

    useEffect(() => {
        setSelected(['1'])
        setListLoading(false)
        axios({
            method: "GET",
            url: GET_USER,
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
            },
            validateStatus: function (status) {
                return status >= 200
            }
        }).then((response) => {
            if (response.status === 200) {
                if (response.data["user"]["code"] === ADMIN_ROLE) {
                    setAuthorized(false)
                } else {
                    setAuthorized(true)
                    getAdminIssue(setIssues, setDeleteIssue, setProgressLoading, setCreateFilteredData, setDeleteFilteredData, setLoading)
                    // axios({
                    //     url: GET_ADMIN_ISSUES_API,
                    //     method: "GET",
                    //     headers: {
                    //         "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`,
                    //     },
                    //     validateStatus: function (status) {
                    //         return status >= 200
                    //     }
                    // }).then((response) => {
                    //     if (response.data.error) {
                    //         toast.error(response.data.error.message)
                    //     } else {
                    //         // console.log(response.data.data[0]['label'][0])
                    //         // console.log(response.data.data)
                    //         let createIssueList = []
                    //         let deleteIssueList = []
                    //         response.data.data.map((item)=> {
                    //             if(item['label'][0] === "Create_VM"){
                    //                  createIssueList.push(item)
                    //             }else {
                    //                  deleteIssueList.push(item)
                    //             }
                    //         })
                    //         setIssues(createIssueList)
                    //         setDeleteIssue(deleteIssueList)
                    //         response.data.data.map((ticket) => {
                    //             setProgressLoading((prev) => {
                    //                 return [...prev,{id : ticket.ticket_id,inProgressLoading : 0,closeLoading : 0}]
                    //             })
                    //         })
                    //         setCreateFilteredData(createIssueList)
                    //         setDeleteFilteredData(deleteIssueList)
                    //         setLoading(true)
                    //     }
                    // }).catch((error) => {
                    //     console.log(error)
                    // })
                }
            } else {
                toast.error(response.data.error.message)
            }
        }).catch((err) => {
            console.log(err)
        })
    }, [listLoading])

    return (
        <>
            {
                authorized ? loading ? <div>
                    <div className='search-name-filter'>
                        <Input
                            placeholder="Search Reporter"
                            className='search-input-assignee'
                            value={value}
                            onChange={e => {
                                const currValue = e.target.value;
                                setValue(currValue);
                                const createFiltered = issues.filter(entry =>
                                    entry.reporter.replace(" ", "").toLowerCase().includes(currValue.replace(" ", "").toLowerCase())
                                );
                                const deleteFiltered = deleteIssue.filter(entry =>
                                    entry.reporter.replace(" ", "").toLowerCase().includes(currValue.replace(" ", "").toLowerCase())
                                );
                                setCreateFilteredData(createFiltered)
                                setDeleteFilteredData(deleteFiltered)
                            }}
                            prefix={<UserOutlined />}
                        />
                    </div>
                    <Modal
                        title="Add Comment"
                        open={open}
                        onOk={() => { handleOk(currentId, modalText, setConfirmLoading, setOpen) }}
                        confirmLoading={confirmLoading}
                        onCancel={() => { handleCancel(setOpen) }}
                    >
                        <TextArea rows={4} onChange={(e) => { setModalText(e.target.value) }} placeholder="Add your comments here..." />
                    </Modal>
                    {/* <Table bordered pagination={{ pageSizeOptions: ["10", "20"], showSizeChanger: true }} columns={columns(setOpen, setCurrentId, progressLoading, setProgressLoading, setListLoading)} dataSource={filteredData} /> */}
                    <div className='tag_issue'><h2>Created Issue</h2></div>
                    <Table bordered pagination={{ pageSizeOptions: ["10", "20"], showSizeChanger: true }} columns={columns("Create", setOpen, setCurrentId,progressLoading,setProgressLoading, setListLoading, setIssues, setDeleteIssue, setCreateFilteredData, setDeleteFilteredData, setLoading)} dataSource={createFiltered} />
                    <div className='tag_issue'><h2>Deleted Issue</h2></div>
                    <Table bordered pagination={{ pageSizeOptions: ["10", "20"], showSizeChanger: true }} columns={columns("Delete", setOpen, setCurrentId,progressLoading,setProgressLoading, setListLoading, setIssues, setDeleteIssue, setCreateFilteredData, setDeleteFilteredData, setLoading)} dataSource={deleteFiltered} />
                </div> : <div className='loading'>
                    <Space size="middle">
                        <Spin size="large" />
                    </Space>
                </div> : <div className='loading'><h1>401 Unauthorized</h1></div>
            }
        </>
    )
}

export default AdminDashboard