import React, { useEffect } from "react";

const App = () => {
  let firstname, lastname, surname, submit;

  let firstkeyupfunc = (e) => {
    if (e.keyCode === 13) {
      lastname.focus();
    }
  };

  let lastkeyupfunc = (e) => {
    if (e.keyCode === 13) {
      surname.focus();
    }
  };

  let defaultkeyupfunc = (e) => {
    if (e.keyCode === 13) {
      submit.focus();
    }
  };

  let handleSubmit = () => {
    alert("Welcome");
  };
  return (
    <div>
      firstname:
      <input
        type="text"
        ref={(input) => {
          firstname = input;
        }}
        onKeyUp={firstkeyupfunc}
      />
      <br />
      lastname:
      <input
        type="text"
        ref={(input) => {
          lastname = input;
        }}
        onKeyUp={lastkeyupfunc}
      />
      <br />
      surname:
      <input
        type="text"
        ref={(input) => {
          surname = input;
        }}
        onKeyUp={defaultkeyupfunc}
      />
      <button
        type="submit"
        onClick={handleSubmit}
        ref={(input) => {
          submit = input;
        }}
      >
        submit
      </button>
      <br />
    </div>
  );
};

export default App;
