$(document).ready(function () { 
    // mandatory for jquery

    // add
    $('#add-btn').click(function () {
        const taskText = $('#task-input').val().trim(); 

        if (taskText === '') {
            alert('Please enter a task');
            return;
        }

        const taskItem = `
            <li>
                <span class="task-text">${taskText}</span>
                <input type="checkbox" class="complete-checkbox">
                <button class="edit-btn">Edit</button>
                <button class="delete-btn">Delete</button>
            </li>
        `;

        $('#task-list').append(taskItem);
        $('#task-input').val('');
    });

    // delete
    $('#task-list').on('click', '.delete-btn', function () {
        $(this).parent().remove();
    });

    // edit
    $('#task-list').on('click', '.edit-btn', function () {
        const taskSpan = $(this).siblings('.task-text');
        const currentText = taskSpan.text();

        const newText = prompt('Update task:', currentText);

        if (newText !== null && newText.trim() !== '') {
            taskSpan.text(newText);
        }
    });

    // Complete task (checkbox)
    $('#task-list').on('change', '.complete-checkbox', function () {
        const taskText = $(this).siblings('.task-text');

        if (this.checked) {
            taskText.addClass('completed');
        } else {
            taskText.removeClass('completed');
        }
    });
});