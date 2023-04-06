import axios from 'axios'
import CryptoJS from "crypto-js";
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { ADMIN_DASHBOARD, ADMIN_ROLE, LOGIN_API, USER_DASHBOARD } from '../constants';

export const updateUser = (e, user, setUser) => {
    const value = e.target.value
    setUser({
        ...user,
        [e.target.name]: value
    })
}

export const validateInput = (e, user, setError, navigate, setLoginLoading) => {
    e.preventDefault()

    if (user.username === "" || user.password === "") {
        setError("Username and Password is Required")
    }
    else if (user.username === "") {
        setError("Username is Required")
    }
    else if (user.password === "") {
        setError("Password is Required")
    }
    else {
        setError("")
        authUser(user, setError, navigate, setLoginLoading)
    }
}

export const authUser = async (user, setError, navigate, setLoginLoading) => {
    setLoginLoading(true)
    const key = CryptoJS.enc.Utf8.parse(process.env.REACT_APP_AUTH_KEY);
    const iv = CryptoJS.enc.Utf8.parse(process.env.REACT_APP_AUTH_IV)
    const encrypted = CryptoJS.AES.encrypt(user.password, key, { iv: iv, mode: CryptoJS.mode.CBC });
    const data = {
        username: user.username.trim(),
        password: encrypted.toString()
    }
    await axios({
        method: 'POST',
        url: LOGIN_API,
        data: data,
        validateStatus: function (status) {
            return status >= 200
        }
    })
        .then(response => {
            if (response.status === 200) {
                if (response.data.data.token) {
                    localStorage.setItem("VMT_TOKEN", response.data.data.token);
                    if (response.data.data.code === ADMIN_ROLE) {
                        return navigate(ADMIN_DASHBOARD)
                    }
                    return navigate(USER_DASHBOARD)
                }
            }
            else if (response.data.error) {
                setError("Invalid Username or Password")
            }
        })
        .catch(error => {
            toast.error("something went Wrong")
        });
    setLoginLoading(false)
}