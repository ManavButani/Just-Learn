import React, { Component } from 'react'
import { UserConsumer } from './userContext'

class Cmp3 extends Component {
  render() {
    return (
      <div>
        <UserConsumer>
          {(value_)=>{
              return <h1>Hello , {value_}</h1>
          }}
        </UserConsumer>
      </div>
    )
  }
}

export default Cmp3
