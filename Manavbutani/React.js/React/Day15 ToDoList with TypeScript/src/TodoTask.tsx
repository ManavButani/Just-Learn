import React from "react";
import { ITask } from "./interfaces";

interface Props {
    task: ITask,
    key: number,
    // completeTask(taskNameToDelete: string): DetailedHTMLProps<<ButtonHTMLAttribute<HTMLButtonElement>>>
    // completeTask(taskNameToDelete: string): null
    completeTask: React.MouseEventHandler<HTMLButtonElement>,
}

const TodoTask = ({ task, key, completeTask }: Props) => {
    return (<>
        <span>{task.Task}</span>
        <span>{task.Deadline}</span>
        <button onClick={completeTask}>X</button>
    </>)
}

export default TodoTask