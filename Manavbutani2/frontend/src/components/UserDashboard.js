import React, { useEffect, useState } from 'react'
import { Table, Input } from 'antd';
import { UserOutlined } from "@ant-design/icons"
import axios from "axios"
import { toast } from 'react-toastify';
import { Space, Spin } from 'antd';
import { GET_USER_ISSUES_API, GET_USER, USER_ROLE } from '../constants';
import {columns} from "../utils/UserDashBoardUtils"

const UserDashboard = ({setSelected}) => {

    const [authorized, setAuthorized] = useState(true)
    const [issues, setIssues] = useState([]);
    const [loading, setLoading] = useState(false);
    const [value, setValue] = useState('');
    const [filteredData, setFilteredData] = useState([])

    useEffect(() => {
        setSelected(['1'])
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
                if (response.data["user"]["code"] !== USER_ROLE) {
                    setAuthorized(false)
                } else {
                    setAuthorized(true)
                    axios({
                        url: GET_USER_ISSUES_API,
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
                            setIssues(response.data.data)
                            console.log(response.data.data)
                            setFilteredData(response.data.data)
                            setLoading(true)
                        }
                    }).catch((error) => {
                        console.log(error)
                    })
                }
            } else {
                toast.error(response.data.error.message)
            }
        }).catch((err) => {
            console.log(err)
        })
    }, [])

    return (
        <>
            {
                authorized ? loading ? <div>
                    <div className='search-name-filter'>
                        <Input
                            placeholder="Search Assignee"
                            className='search-input-assignee'
                            value={value}
                            onChange={e => {
                                const currValue = e.target.value;
                                setValue(currValue);
                                const filtered = issues.filter(entry =>
                                    entry.assignee.replace(" ", "").toLowerCase().includes(currValue.replace(" ", "").toLowerCase())
                                );
                                setFilteredData(filtered)
                            }}
                            prefix={<UserOutlined />}
                        />
                    </div>
                    <Table bordered pagination={{ pageSizeOptions: ["10", "20"], showSizeChanger: true }} columns={columns} dataSource={filteredData} />
                </div> : <div className='loading'>
                    <Space size="middle">
                        <Spin size="large" />
                    </Space>
                </div> : <div className='loading'><h1>401 Unauthorized</h1></div>
            }
        </>
    )
}

export default UserDashboard