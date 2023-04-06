import React, { ChangeEvent, useState } from 'react'
import { ITask } from './interfaces'
import TodoTask from "./TodoTask"

const App: React.FC = () => {
  const [task, setTask] = useState<string>("")
  const [deadline, setDeadline] = useState<number>(0)
  const [todoList, setTodoList] = useState<ITask[]>([])


  let handleChange = (event: ChangeEvent<HTMLInputElement>): void => {
    if (event.target.name === "task") {
      setTask(event.target.value)
    } else {
      setDeadline(Number(event.target.value))
    }
  }

  let addTask = (): void => {
    const newTask = { Task: task, Deadline: deadline }
    setTodoList([...todoList, newTask])
    setTask("")
    setDeadline(0)
  }

  let completeTask = (taskNameToDelete: string): void => {
    setTodoList(todoList.filter((task) => {
      return task.Task !== taskNameToDelete
    }))
  }
  return (
    <>
      <input type="text" onChange={handleChange} name='task' />
      <input type="number" onChange={handleChange} name='deadline' />
      <button onClick={addTask}>Add Task</button>
      {todoList.map((task: ITask, key: number) => {
        return <TodoTask key={key} task={task} completeTask={completeTask} />

      })}
    </>
  )
}

export default App
