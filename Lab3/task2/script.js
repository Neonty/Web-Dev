const input = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

function createTodoElement(taskValue) {
    const li = document.createElement('li');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', () => toggleTaskStatus(li));

    const span = document.createElement('span');
    span.className = 'todo-text';
    span.innerText = taskValue;

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.innerText = 'Delete';
    deleteBtn.addEventListener('click', () => deleteTask(li));

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(deleteBtn);

    return li;
}

function addTask() {
    const taskValue = input.value.trim();
    if (taskValue === "") return;

    const todoItem = createTodoElement(taskValue);
    todoList.appendChild(todoItem);
    
    input.value = "";
}

function toggleTaskStatus(taskElement) {
    taskElement.classList.toggle('completed');
}

function deleteTask(taskElement) {
    todoList.removeChild(taskElement);
}

addBtn.addEventListener('click', addTask);

input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTask();
});