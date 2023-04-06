export const columns = [
    {
        title: 'ID',
        dataIndex: 'ticket_id',
        render: (text, record) => <a href={record.url} target="_blank">{text}</a>
    },
    {
        title: "Assignee",
        dataIndex: 'assignee',
    },
   
    {
        title: "Label",
        dataIndex: 'labels',
        filters: [
            {
                text: 'Create_VM',
                value: 'Create_VM',
            },
            {
                text: 'Delete_VM',
                value: 'Delete_VM',
            },
        ],
        render: (labels) => <p>{labels[0]}</p>,
        filterMode: 'tree',
        filterSearch: true,
        sorter: (a, b) => a.labels[0].localeCompare(b.labels[0]),
        onFilter: (value, record) => record.labels[0].startsWith(value),
    },
    {
        title: 'Status',
        dataIndex: 'status',
        filters: [
            {
                text: 'Open',
                value: 'Open',
            },
            {
                text: 'In Progress',
                value: 'In Progress',
            },
            {
                text: 'In Review',
                value: 'In Review',
            },
            {
                text: 'Approved',
                value: 'Approved',
            },
            {
                text: 'Cancelled',
                value: 'Cancelled',
            },
            {
                text: 'Untriage',
                value: 'Untriage',
            },
        ],
        filterMode: 'tree',
        filterSearch: true,
        sorter: (a, b) => a.status.localeCompare(b.status),
        onFilter: (value, record) => record.status.startsWith(value),
    },
    {
        title: 'Priority',
        dataIndex: 'priority',
        filters: [
            {
                text: 'Blocker',
                value: 'Blocker',
            },
            {
                text: 'Critical',
                value: 'Critical',
            },
            {
                text: 'Major',
                value: 'Major',
            },
            {
                text: 'Minor',
                value: 'Minor',
            },
            {
                text: 'Trivial',
                value: 'Trivial',
            },
            {
                text: 'Cosmetic',
                value: 'Cosmetic',
            },
        ],
        filterMode: 'tree',
        filterSearch: true,
        sorter: (a, b) => a.priority.localeCompare(b.priority),
        onFilter: (value, record) => record.priority.startsWith(value),
    },
];