import React from "react";
import Success from "./screenComponent/Success";
import Error from "./screenComponent/Error";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./screenComponent/Home";
import WrongPassword from "./screenComponent/WrongPassword";

const Links = () => {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/error" element={<Error />}></Route>
          <Route path="/success" element={<Success />}></Route>
          <Route path="/wrongpass" element={<WrongPassword />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
};

export default Links;
