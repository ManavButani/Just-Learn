import React, { Component } from 'react'
import Cmp3 from './Cmp3'
import { UserProvider } from './userContext'
class App extends Component {
  render() {
    return (
      <>
        <UserProvider value="Manav"> 
          <Cmp3 ></Cmp3>
        </UserProvider>
      </>
    )
  }
}

export default App
