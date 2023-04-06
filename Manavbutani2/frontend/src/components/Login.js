import '../css/login.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { useEffect, useState } from 'react';
import axios from 'axios'
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useNavigate } from "react-router-dom"
import { CHECK_ROLE, ADMIN_ROLE, USER_ROLE, ADMIN_DASHBOARD, USER_DASHBOARD } from '../constants';
import { updateUser, validateInput } from "../utils/LoginUtils"
import {Button} from "antd"

function Login() {

  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)
  const [loginLoading, setLoginLoading] = useState(false)

  const [user, setUser] = useState({
    username: '',
    password: ''
  })

  const [isError, setError] = useState("")

  useEffect(() => {
    setLoading(false)
    axios({
      method: "GET",
      url: CHECK_ROLE,
      headers: {
        "Authorization": `Bearer ${localStorage.getItem('VMT_TOKEN')}`
      },
      validateStatus: function (status) {
        return status >= 200
      }
    }).then((response) => {
      if (response.status === 200) {
        if (response.data["role"] === ADMIN_ROLE) {
          return navigate(ADMIN_DASHBOARD)
        } else {
          return navigate(USER_DASHBOARD)
        }
      }
      setLoading(true)
    }).catch((error) => {
      console.log(error)
    })
  }, [])

  return (
    <>
      {loading ? <><ToastContainer />
        <div className='login-container'>
          <div className='logo'>VMT</div>
          <div className='center-icon'>
            <FontAwesomeIcon icon="fa-circle-user" />
          </div>
          <div className="title">
            <h2>Login to your Account</h2>
          </div>
          <div className='error-block'>
            <p>{isError}</p>
          </div>

          <div className='form-control'>
            <form onSubmit={(e) => { validateInput(e, user, setError, navigate, setLoginLoading) }}>

              <input type="text" name="username" placeholder={'Username'} value={user.username} onChange={(e) => { updateUser(e, user, setUser) }}></input>
              <input type="password" name="password" placeholder={'Password'} value={user.password} onChange={(e) => { updateUser(e, user, setUser) }}></input>
              <Button htmlType="submit" loading={loginLoading}>Login</Button>

            </form>
          </div>
        </div></> : null}
    </>
  );
}

export default Login;