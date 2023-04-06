import React, { Component } from "react";
import Cmp3 from "./Cmp3";

export const ManavContext = React.createContext();
export const UserContext = React.createContext();
class App extends Component {
  render() {
    return (
      <>
        <ManavContext.Provider value="Jinesh">
          <UserContext.Provider value="Manav">
            <Cmp3></Cmp3>
          </UserContext.Provider>
        </ManavContext.Provider>
      </>
    );
  }
}

export default App;
