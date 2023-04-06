import React, { useEffect, useState } from 'react'
import { GET_USER, ADMIN_ROLE } from '../constants'
import axios from 'axios'
import { toast } from "react-toastify"
import 'react-toastify/dist/ReactToastify.css';
import '../css/createVm.css'
import errorHandler from '../utils/CreateVmUtils';
import { onFinish, handleGuestOsChange } from '../utils/CreateVmUtils';
import { GET_FOLDERS_API, GET_DATASTORES_API, GET_GUEST_OS_API, GET_DESCRIPTION_API, PROJECT_KEY } from '../constants';
import { useParams } from 'react-router-dom'
import {
    Button,
    Form,
    Input,
    InputNumber,
    Select,
    Typography,
    Space,
    Spin,
    Radio
} from 'antd';

const CreateVM = () => {

    const [authorized, setAuthorized] = useState(true)
    const { Title } = Typography;
    const [folderName, setFolderName] = useState([]);
    const [datastore, setDatastore] = useState([]);
    const [guestos, setGuestOS] = useState({});
    const [loading, setLoading] = useState(false);
    const [vmLoading, setVmLoading] = useState(0)
    const [osList, setOsList] = useState([]);
    const [option, setOption] = useState('windows');

    let vmData = {
        "vm_name": "",
        "folder": "",
        "datastore": "",
        "guestos": "",
        "disksize": "",
        "memory": "",
        "cpu": ""
    }

    const [field, setField] = useState({
        name: "",
        diskSizeText: 1,
        diskSizeUnit: 'MB',
        memory: 1,
        cpu: 1,
        datastore: '',
        guestosTitle: '',
        guestosValue: ''
    });

    const [error, setError] = useState({
        diskError: '',
        memError: '',
        cpuError: '',
        submitError: ''
    })

    const JIRA_KEY = {
        key: useParams().id,
        mode : "CREATE"
    }

    useEffect(() => {
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
            console.log(response.data)
            if (response.status === 200) {
                if (response.data["user"]["code"] === ADMIN_ROLE) {
                    setAuthorized(false)
                } else {
                    setAuthorized(true)
                    axios({
                        url: GET_FOLDERS_API,
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
                                const folders = response.data.folders
                                setFolderName(folders)
                            } else {
                                toast.error("Folders are not loaded")
                            }
                        })
                        .catch(error => {
                            console.log(error)
                        })

                    axios({
                        url: GET_DATASTORES_API,
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
                                const datastores = response.data.datastores
                                setDatastore(datastores)
                            } else {
                                toast.error("Datastores are not loaded")
                            }
                        })
                        .catch(error => {
                            console.log(error)
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
                            } else {
                                toast.error("Guest OS are not loaded")
                            }
                        })
                        .catch(error => {
                            console.log(error)
                        })

                    axios({
                        url: GET_DESCRIPTION_API,
                        // url:"http://172.20.11.108:5000/issue/description",
                        method: "POST",
                        data: JIRA_KEY,
                        headers: {
                            "Authorization": `Bearer ${localStorage.getItem("VMT_TOKEN")}`,
                            "Content-Type": 'application/json'
                        },
                        validateStatus: function (status) {
                            return status >= 200
                        }
                    })
                        .then(response => {
                            if (response.status === 200) {
                                console.log(response.data)
                                console.log(`${PROJECT_KEY}-${response.data.employee_name}-${response.data.employee_id}-${response.data.guest_os_title}-${JIRA_KEY.key} `)
                                setField({
                                    name: `${PROJECT_KEY}-${response.data.employee_name}-${response.data.employee_id}-${response.data.guest_os_title}-${JIRA_KEY.key} `,
                                    diskSizeText: response.data.disk_text,
                                    diskSizeUnit: response.data.disk_unit,
                                    memory: response.data.memory,
                                    cpu: response.data.cpu,
                                    guestosTitle: response.data.guest_os_title,
                                    guestosValue: response.data.guest_os_value,
                                })

                            } else {
                                toast.error("Disk, Memory, guestOS and CPU are not loaded")
                            }
                        })
                        .catch(error => {
                            console.log(error)
                        })
                    setLoading(true)
                }
            } else {
                toast.error(response.data.message)
            }
        }).catch((err) => {
            console.log(err)
        })
    }, [])

    return (
        <>
            {
                authorized ? loading ? <><div className='main_div'>
                    <div className='create_vm'>
                        <Form
                            labelCol={{ span: 4 }}
                            wrapperCol={{ span: 14 }}
                            style={{ maxWidth: 1000 }}
                            onFinish={(value) => { onFinish(value, vmData, error, setError, field, setVmLoading, JIRA_KEY) }}
                        >
                            <Title // Form's Title
                                className='form_title'
                                level={3}
                            >
                                Create VM
                            </Title>
                            <Form.Item name="VM Name" label="VM Name">
                                <Input disabled placeholder={field.name} />
                            </Form.Item>
                            <Form.Item name="Folder" label="Folder" rules={[{ required: true, message: 'folder is required' }]}>
                                <Select>
                                    {
                                        folderName.map((item) => {
                                            if (item.type === "VIRTUAL_MACHINE") {
                                                return <Select.Option key={item.folder} value={item.folder}>{item.name}/{item.folder}</Select.Option>
                                            }
                                        })
                                    }
                                </Select>
                            </Form.Item>
                            <Form.Item name="Datastore" label="Datastore" rules={[{ required: true, message: 'Datastore is required' }]}>
                                <Select value={field.datastore}
                                    onChange={(value) => {
                                        setField({ ...field, datastore: value });
                                        errorHandler(value, "datastore", datastore, field, setField, error, setError)
                                    }
                                    }>
                                    {
                                        datastore.map((item) => {
                                            return <Select.Option key={item.name} value={item.datastore}>{item.name}/{item.datastore}</Select.Option>
                                        })
                                    }
                                </Select>
                            </Form.Item>
                            <Form.Item name="guestOS" label="Guest OS" style={{ marginBottom: '0px' }} required >
                                <Input.Group >
                                    <Form.Item style={{ marginBottom: '10px' }}>
                                        <Radio.Group value={option} onChange={(e) => { handleGuestOsChange(e, guestos, setOsList, setOption) }}>
                                            <Radio.Button value="windows">Windows</Radio.Button>
                                            <Radio.Button value="linux">Linux</Radio.Button>
                                            <Radio.Button value="other">Other</Radio.Button>

                                        </Radio.Group>
                                    </Form.Item>
                                    <Form.Item rules={[{ required: true, message: 'Guestos is required' }]}>
                                        <Select value={field.guestosTitle} onChange={(value, title) => setField({ ...field, guestosValue: value, guestosTitle: title })} >
                                            {
                                                osList.map((item) => {
                                                    return <Select.Option key={item.title} value={item.value}>{item.title}</Select.Option>
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
                                            value={field.diskSizeText} onChange={(value) => { errorHandler(value, "diskText", datastore, field, setField, error, setError) }} />
                                        <Select style={{ width: '65px' }} defaultValue='MB' value={field.diskSizeUnit} onChange={(value) => { errorHandler(value, "diskUnit", datastore, field, setField, error, setError) }}>
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
                                    value={field.memory} onChange={(value) => { errorHandler(value, "memory", datastore, field, setField, error, setError) }}
                                    rules={[
                                        { required: true, message: 'Memory is required' }
                                    ]}
                                    placeholder="GB" />
                                {error.memError !== '' && <p className='custom_error'>{error.memError}</p>}
                            </Form.Item>

                            <Form.Item name="CPU" label="CPU" required >
                                <InputNumber
                                    value={field.cpu} onChange={(value) => { errorHandler(value, "cpu", datastore, field, setField, error, setError) }}
                                    rules={[{ required: true, message: 'CPU is required' }]} />
                                {error.cpu !== '' && <p className='custom_error'>{error.cpuError}</p>}
                            </Form.Item>
                            {error.submitError !== '' && <><p style={{ textAlign: 'center', marginBottom: '5px' }} className='custom_error'>{error.submitError}</p></>}
                            <div className='button-div'>
                                <Form.Item name="submit">
                                    <Button className='create_btn' htmlType="submit" loading={vmLoading}>
                                        Create
                                    </Button>
                                </Form.Item>
                            </div>
                        </Form>
                    </div>
                </div></> : <div className='loading'>
                    <Space size="middle">
                        <Spin size="large" />
                    </Space>
                </div> : <div className='loading'><h1>401 Unauthorized</h1></div>
            }
        </>
    )
}

export default CreateVM
