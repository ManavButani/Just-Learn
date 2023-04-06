import React from 'react'

function Person({obj}) {
  return (
    <div>
      <h1>Hello {obj.name} , Welcome on your {obj.Age} birthday</h1>
    </div>
  )
}

export default Person