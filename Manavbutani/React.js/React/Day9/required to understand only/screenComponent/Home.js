import React, { useRef } from "react";
import { useDispatch } from "react-redux";

import {
  redirectToErrorPage,
  redirectToSuccessPage,
  redirectToWrongPassword,
} from "../state/action";

const Home = () => {
  const dispatch = useDispatch();
  let email = useRef("");
  let password = useRef("");

  let data = {
    name: "Manav Butani",
    email: "manav@gmail.com",
    password: "123",
  };

  let handleSubmit = () => {
    if (email.current.value === data.email) {
      console.log(email);
      console.log(password);
      if (password.current.value === data.password) {
        dispatch(redirectToSuccessPage());
      } else {
        dispatch(redirectToWrongPassword());
      }
    } else {
      dispatch(redirectToErrorPage());
    }
  };
  return (
    <>
      UserName:
      <input
        type="text"
        ref={email}
        onChange={(event) => {
          return event.target.value;
        }}
      />
      <br />
      Password:
      <input
        type="text"
        ref={password}
        onChange={(event) => {
          return event.target.value;
        }}
      />
      <br />
      <button type="submit" onClick={handleSubmit}>
        Submit
      </button>
    </>
  );
};

export default Home;
