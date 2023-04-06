import React, { Component } from "react";
import Cmp3 from "./Cmp3";
import { ManavProvider } from "./manavContext";
import { UserProvider } from "./userContext";
class App extends Component {
  render() {
    return (
      <>
        <ManavProvider value="Swa">
          <UserProvider value="Manav">
            <Cmp3></Cmp3>
          </UserProvider>
        </ManavProvider>
      </>
    );
  }
}

export default App;
