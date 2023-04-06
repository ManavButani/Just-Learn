import React, { useState, useEffect } from 'react'
import { onFinish, errorHandler, handleGuestOsChange } from '../utils/CreateIssueUtils';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { GET_USER, GET_ASSIGNEES, PRIORITY_LIST, LOCATION_LIST, GET_GUEST_OS_API, USER_ROLE, GET_VM_API } from '../constants'
import { toast } from 'react-toastify';
import '../css/createIssue.css'
import 'react-toastify/dist/ReactToastify.css';
import {
    Button,
    Form,
    Input,
    Select,
    Typography,
    InputNumber,
    Radio,
    Spin,
    Space
} from 'antd';

const { Title } = Typography
const CreateJiraTicket = ({ setSelected }) => {

    const [guestos, setGuestOS] = useState({});
    const [osList, setOsList] = useState([]);
    const [option, setOption] = useState('windows');
    const [issueOption, setIssueOption] = useState('create')
    const navigate = useNavigate()
    const [assigneeList, setAssigneeList] = useState([])
    const [vmList, setVmList] = useState([])
    const [authorized, setAuthorized] = useState(true)
    const [issueLoading, setIssueLoading] = useState(false)
    const [loading, setLoading] = useState(false)
    const [issueFlag, setIssueFlag] = useState(true)
    const [field, setField] = useState({
        diskSizeText: null,
        diskSizeUnit: 'GB',
        memory: null,
        cpu: null,
        guestOs: null,
        employeeId: 0,
        employeeName: null,
        vmName: '',
        vmId: 0
    });
    const [error, setError] = useState({
        diskError: '',
        memError: '',
        cpuError: '',
        submitError: ''
    })

    useEffect(() => {
        setSelected(['2'])
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
                    setField({...field , employeeId:response.data["user"]["employee_id"] , employeeName:response.data["user"]["username"] })
                    axios({
                        method: 'GET',
                        url: GET_ASSIGNEES,
                        headers: {
                            "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
                        },
                        validateStatus: function (status) {
                            return status >= 200
                        }
                    })
                        .then(response => {
                            if (response.status == 200) {
                                setAssigneeList(response.data.assignees)
                            }
                        })

                    axios({
                        url: GET_VM_API,
                        method: "GET",
                        headers: {
                            "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
                        },
                        validateStatus: function (status) {
                            return status >= 200
                        }
                    })
                        .then(response => {
                            if (response.status === 200) {
                                // console.log(response.data.vm_list)
                                setVmList(response.data.vm_list)
                            } else {
                                toast.error("Vm are not loaded")
                            }
                        })
                        .catch(error => {
                            console.log(error)
                        })
                }
            } else {
                toast.error(response.data.message)
            }
        }).catch((err) => {
            console.log(err)
        })

        axios({
            url: GET_GUEST_OS_API,
            method: "GET",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`
            },
            validateStatus: function (status) {
                return status >= 200
            }
        })
            .then(response => {
                if (response.status === 200) {
                    const guestos = response.data.guestos
                    setGuestOS(guestos)
                    setOsList(guestos.windows)
                    setLoading(true)
                } else {
                    toast.error("Guest OS are not loaded")
                }
            })
            .catch(error => {
                console.log(error)
            })
    }, [])

    return (
        <>
            {
                authorized ? loading ?
                    <div>
                        <div className='main_div'>
                            <div className='create_issue'>
                                <Form
                                    labelCol={{ span: 4 }}
                                    wrapperCol={{ span: 14 }}
                                    style={{ maxWidth: 1000 }}
                                    onFinish={(e) => { onFinish(e, navigate, error, setError, field, setIssueLoading, issueFlag) }}
                                >
                                    <Title
                                        className='form_title'
                                        level={3}
                                    >
                                        Create Issue
                                    </Title>
                                
                                    <Form.Item  style={{ marginLeft: '168px', marginBottom: '10px' }}>
                                        <Radio.Group value={issueOption}
                                            onChange={(event) => {
                                                if (event.target.value === "delete") {
                                                    setIssueFlag(false)
                                                    setIssueOption("delete")
                                                } else {
                                                    setIssueFlag(true)
                                                    setIssueOption("create")
                                                }
                                            }}>
                                            <Radio.Button value="create">Create Vm Ticket</Radio.Button>
                                            <Radio.Button value="delete">Delete Vm Ticket</Radio.Button>
                                        </Radio.Group>
                                    </Form.Item>

                                    <Form.Item name="type_name" label="Issue Type">
                                        <Input disabled placeholder='Task' />
                                    </Form.Item>

                                    <Form.Item name="summary" label="Summary" rules={[{ required: true, message: 'Summary is required' }]}>
                                        <Input placeholder='Summary' />
                                    </Form.Item>

                                    <Form.Item name="comment" label="Comment" rules={[{ required: true, message: 'Description is required' }]}>
                                        <Input.TextArea rows={4} />
                                    </Form.Item>

                                    <Form.Item name="priority_id" label="Priority" rules={[{ required: true, message: 'Priority is required' }]}>
                                        <Select >
                                            {
                                                PRIORITY_LIST.map((item) => {
                                                    return <Select.Option key={item.priority_name} value={item.priority_id}>
                                                        <img className="priority_icon" src={item.icon_url}></img>
                                                        {item.priority_name}
                                                    </Select.Option>
                                                })
                                            }
                                        </Select>
                                    </Form.Item>

                                    <Form.Item name="assignee_name" label="Assignee" rules={[{ required: true, message: 'folder is required' }]}>
                                        <Select>
                                            {
                                                assigneeList.map((item) => {
                                                    return <Select.Option key={item.firstName + " " + item.lastName} value={item.firstName + " " + item.lastName}></Select.Option>
                                                })
                                            }
                                        </Select>
                                    </Form.Item>
                                    {
                                        issueFlag ?
                                            <>
                                                <Form.Item label="Guest OS" style={{ marginBottom: '0px' }} required>
                                                    <Input.Group >
                                                        <Form.Item style={{ marginBottom: '10px' }}>
                                                            <Radio.Group value={option} onChange={(event) => handleGuestOsChange(event, setOption, setOsList, guestos)}>
                                                                <Radio.Button value="windows">Windows</Radio.Button>
                                                                <Radio.Button value="linux">Linux</Radio.Button>
                                                                <Radio.Button value="other">Other</Radio.Button>
                                                            </Radio.Group>
                                                        </Form.Item>
                                                        <Form.Item name="GuestOS" rules={[{ required: true, message: 'Guestos is required' }]}>
                                                            <Select  >
                                                                {
                                                                    osList.map((item) => {
                                                                        return <Select.Option key={item.title} value={item.title + "(" + item.value + ")"}>{item.title}</Select.Option>
                                                                    })
                                                                }
                                                            </Select>
                                                        </Form.Item>
                                                    </Input.Group>
                                                </Form.Item>

                                                <div className='disk_size'>
                                                    <Form.Item name="Disk size" label="Disk Size" required>
                                                        <Input.Group compact>
                                                            <InputNumber rules={[{ required: true, message: 'Disk Size is required' }]}
                                                                value={field.diskSizeText} onChange={(value) => { errorHandler(value, "diskText", field, setField, error, setError) }} />
                                                            <Select style={{ width: '65px' }} defaultValue='MB' value={field.diskSizeUnit} onChange={(value) => { errorHandler(value, "diskUnit", field, setField, error, setError) }}>
                                                                <Select.Option value="MB">MB</Select.Option>
                                                                <Select.Option value="GB">GB</Select.Option>
                                                                <Select.Option value="TB">TB</Select.Option>
                                                            </Select>
                                                        </Input.Group>
                                                        {error.diskError !== '' ? <p className='custom_error'>{error.diskError}</p> : null}
                                                    </Form.Item>
                                                </div>

                                                <Form.Item name="Memory" label="Memory (GB)" required >
                                                    <InputNumber
                                                        value={field.memory} onChange={(value) => { errorHandler(value, "memory", field, setField, error, setError) }}
                                                        rules={[
                                                            { required: true, message: 'Memory is required' }
                                                        ]}
                                                        placeholder="GB" />
                                                    {error.memError !== '' && <p className='custom_error'>{error.memError}</p>}
                                                </Form.Item>

                                                <Form.Item name="CPU" label="CPU" required >
                                                    <InputNumber
                                                        value={field.cpu} onChange={(value) => { errorHandler(value, "cpu", field, setField, error, setError) }}
                                                        rules={[{ required: true, message: 'CPU is required' }]} />
                                                    {error.cpu !== '' && <p className='custom_error'>{error.cpuError}</p>}
                                                </Form.Item>
                                            </>
                                            :
                                            <>
                                                <Form.Item  name="VmName" label="Vm Name" rules={[{ required: true, message: 'VM is required' }]}>
                                                    {/* {console.log("vmlist: ", vmList)} */}
                                                    <Select >
                                                        {
                                                            vmList.map((item) => {
                                                                if (item.name.includes("-"+field.employeeId+"-")) {
                                                                    return <Select.Option key={item.vm} value={item.name + "~"+item.vm}>{item.name}</Select.Option>
                                                                }
                                                            })
                                                        }
                                                    </Select>
                                                </Form.Item>
                                            </>
                                    }
                                    <Form.Item name="location" label="Location" rules={[{ required: true, message: 'Location is required' }]}>
                                        <Select >
                                            {
                                                LOCATION_LIST.map((item) => {
                                                    return <Select.Option key={item.location} value={item.location}></Select.Option>
                                                })
                                            }
                                        </Select>
                                    </Form.Item>

                                    {error.submitError !== '' && <><p style={{ textAlign: 'center', marginBottom: '5px' }} className='custom_error'>{error.submitError}</p></>}

                                    <div className='button-div'>
                                        <Button className='create_btn admin-action-btn' type="primary" htmlType="submit" loading={issueLoading}>
                                            Create Issue
                                        </Button>
                                    </div>
                                </Form>
                            </div>
                        </div>
                    </div> : <div className='loading'>
                        <Space size="middle">
                            <Spin size="large" />
                        </Space>
                    </div> : <div className='loading'><h1>401 Unauthorized</h1></div>
            }
        </>
    )
}


export default CreateJiraTicket
