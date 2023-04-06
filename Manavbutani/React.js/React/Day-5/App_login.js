import React, { useState } from "react";
import { Button } from "@material-ui/core";
import { TextField } from "@material-ui/core";

function App() {
  let [email, setEmail] = useState("");
  let [password, setPassword] = useState("");
  let [validation, setValidation] = useState("");
  let [click, setClick] = useState(false);

  let userData = [
    { email: "manav@gmail.com", password: "123", name: "Manav Butani" },
  ];
  const handleSubmit = (event) => {
    event.preventDefault();

    const user = userData.find(
      (user) => user.email === email && user.password === password
    );

    if (user) {
      setValidation(user.name);
      setClick(true);
    } else {
      setValidation("");
    }
  };

  return (
    <>
      <center>

      {click && validation !== "" ? (
          <h1>welcome, {validation}</h1>
        ) : click && validation === "" ? (
          <h2>Invalid Email or Password</h2>
        ) : (
          <h1>Please Login</h1>
        )}
        
        <form onSubmit={handleSubmit}>
          <TextField
            id="filled-basic"
            label="Email"
            variant="filled"
            value={email}
            onChange={(event) => {
              setEmail(event.target.value);
            }}
          />

          <br />
          <br />
          <TextField
            id="filled-basic"
            label="Password"
            variant="filled"
            value={password}
            onChange={(event) => {
              setPassword(event.target.value);
            }}
          />
          <br />
          <br />

          <Button variant="contained" color="secondary" type="submit">
            Login
          </Button>
        </form>
        
      </center>
    </>
  );
}

export default App;
