import React from 'react'

const Manav = React.createContext("Swaminarayan")
const ManavProvider = Manav.Provider
const ManavConsumer = Manav.Consumer

export {ManavConsumer, ManavProvider}