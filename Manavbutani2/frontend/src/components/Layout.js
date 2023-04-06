import {
    MenuFoldOutlined,
    MenuUnfoldOutlined,
    PoweroffOutlined,
    PlusOutlined,
    DashboardFilled
} from '@ant-design/icons';
import { Layout, Menu, theme } from 'antd';
import React, { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom"
import "../css/layout.css"
import axios from "axios"
import { Space, Spin } from 'antd';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { CHECK_ROLE, ADMIN_ROLE, ADMIN_DASHBOARD, USER_DASHBOARD, CREATE_ISSUE} from '../constants';

const { Header, Sider, Content } = Layout;

const VMTLayout = ({ selected, children }) => {
    const [collapsed, setCollapsed] = useState(false);
    const [user, setUser] = useState()
    const [fullName, setFullName] = useState("")
    const [path, setPath] = useState(false)
    const [loading, setLoading] = useState(false);
    const [menus, setMenus] = useState([])

    const navigate = useNavigate()
    const {
        token: { colorBgContainer },
    } = theme.useToken();

    const logout = () => {
        localStorage.removeItem("VMT_TOKEN")
        return navigate("/login")
    }

    useEffect(() => {
        let token = localStorage.getItem("VMT_TOKEN")
        if (token === null) {
            navigate("/login")
        } else {
            axios({
                method: "GET",
                url: CHECK_ROLE,
                headers: {
                    "Authorization": `Bearer ${token}`
                },
                validateStatus : function(status){
                    return status >= 200
                }
            }).then((response) => {
                if (response.data.error) {
                    return navigate("/login")
                } else {
                    if (response.data.role == ADMIN_ROLE) {
                        setMenus([
                            {
                                key: '1',
                                icon: <DashboardFilled style={{ fontSize: "18px" }} />,
                                label: 'Dashboard',
                                onClick: () => {
                                    navigate(ADMIN_DASHBOARD)
                                },
                            }
                        ])
                    } else {
                        setMenus([
                            {
                                key: '1',
                                icon: <DashboardFilled style={{ fontSize: "18px" }} />,
                                label: 'Dashboard',
                                onClick: () => {
                                    navigate(USER_DASHBOARD)
                                },
                            },
                            {
                                key: '2',
                                icon: <PlusOutlined style={{ fontSize: "18px", strokeWidth : "40", stroke : "white" }} />,
                                label: 'Create Jira Ticket',
                                onClick: () => {
                                    navigate(CREATE_ISSUE)
                                },
                            }
                        ])
                    }
                }      
                let userData = response.data.user
                setFullName(userData.username.split(".")[0].charAt(0).toUpperCase() + userData.username.split(".")[0].slice(1) + " " + userData.username.split(".")[1].charAt(0).toUpperCase() + userData.username.split(".")[1].slice(1))
                setUser(userData)
                setPath(true)
                setLoading(true)
            }).catch((error) => {
                console.log(error)
            })
        }
    }, [])

    return <>
        {loading ? path ? <><ToastContainer /><Layout className='layout'>
            <Sider trigger={null} collapsible collapsed={collapsed} style={{ background: "#263238" }} width={250}>
                <div className="logo" />
                {
                    collapsed ? <div style={{marginTop : "85%"}}></div> : <div className='profile'>
                        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/1200px-Default_pfp.svg.png' height={150} />
                        <div className='profile-details'>
                            <p>{fullName}</p>
                            <p>{user.designation}</p>
                        </div>
                    </div>
                }
                <Menu
                    className='menu'
                    theme="dark"
                    mode="inline"
                    selectedKeys={selected}
                    items={menus}
                />
            </Sider>
            <Layout className="site-layout">
                <Header
                    style={{
                        paddingLeft: "2%",
                        background: "#263238",
                        color: "white"
                    }}
                >
                    <div className='navbar-items'>
                        <div className='navbar-items-left'>
                            {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
                                className: 'trigger',
                                onClick: () => setCollapsed(!collapsed),
                                style: { "fontSize": "18px" }
                            })}
                            <span className='navbar-title'>VMT</span>
                        </div>
                        <div className='navbar-items-right'>
                            <PoweroffOutlined onClick={logout} style={{ fontSize: "18px" }}/>
                        </div>
                    </div>
                </Header>
                <Content
                    style={{
                        padding: 24,
                        minHeight: 280,
                        background: "white",
                        overflow : "scroll",
                        position : "relative",
                        top : "8%",
                        paddingBottom : "5%"
                    }}
                >
                    {children}
                </Content>
            </Layout>
        </Layout></> : null : <div className='loading'>
            <Space size="middle">
                <Spin size="large" />
            </Space>
        </div>}
    </>;
};
export default VMTLayout;