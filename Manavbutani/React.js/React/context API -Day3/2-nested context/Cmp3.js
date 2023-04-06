import React, { Component } from "react";
import { ManavConsumer, ManavProvider } from "./manavContext";
import { UserConsumer } from "./userContext";

class Cmp3 extends Component {
  render() {
    return (
      <div>
        <ManavConsumer>
          {(swa) => (
            <UserConsumer>
              {(value_) => {
                return <h1>Hello , {value_}, {swa}</h1>;
              }}
            </UserConsumer>
          )}
        </ManavConsumer>
      </div>
    );
  }
}

export default Cmp3;
