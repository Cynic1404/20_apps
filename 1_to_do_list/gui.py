import functions
import PySimpleGUI as sg

lable = sg.Text("Type to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add = sg.Button("Add")
clear_button = sg.Button("Clear")
complete_button = sg.Button("Complete")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
completed_tasks_text = sg.Multiline(functions.show_tasks(file_name='files/finished.txt', as_string=True), size=[45, 10])
clear_finished_tasks_list_button = sg.Button("Clear the list")
list_box = sg.Listbox(values=functions.show_tasks(), size=[45, 10], key='tasks', enable_events=True)

layout = [[lable],[input_box], [add, clear_button], [list_box],[complete_button, edit_button, delete_button], [completed_tasks_text], [clear_finished_tasks_list_button]]
window = sg.Window('To-Do list', layout=layout, font=("Helvetica", 20))


def clear_input():
    window['todo'].update('')


def delete_confirmation(todo_to_delete):
    event = sg.popup_ok_cancel(f"Do you want to remove the '{todo_to_delete}' record", "Press cancel to stop",
                               title="Are you sure?")
    print(event)
    return event

def clear_finish_tasks_list():
    event = sg.popup_ok_cancel(f"Do you want to clear the finished tasks list", "Press cancel to stop",
                               title="Are you sure?")
    print(event)
    return event

while True:
    event, values = window.read()
    # print(event)
    # print(values)
    match event:
        case "Add":
            if values["todo"] != '':
                functions.add_row(gui_string=values["todo"])
                clear_input()
                window['tasks'].update(functions.show_tasks())
        case "Clear":
            clear_input()
        case "Complete":
            if values['tasks']:
                todo_to_complete = values['tasks'][0]
                todos = functions.show_tasks()
                completed_tasks = functions.show_tasks(file_name='files/finished.txt')
                index = todos.index(todo_to_complete)
                completed_tasks.append(todos.pop(index))
                functions.write_file(todos)
                functions.write_file(text=completed_tasks, filename='files/finished.txt')
                window['tasks'].update(functions.show_tasks())
                clear_input()
                completed_tasks_text.update(
                    functions.show_tasks(file_name='files/finished.txt', as_string=True))
        case "Edit":
            if values['tasks']:
                todo_to_edit = values['tasks'][0]
                if values['todo']:
                    new_todo = values['todo']
                    todos = functions.show_tasks()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + "\n"
                    functions.write_file(todos)
                    window['tasks'].update(functions.show_tasks())
                    clear_input()
        case "Delete":
            if values['tasks']:
                todo_to_delete = values['tasks'][0]
                if delete_confirmation(todo_to_delete.replace('\n',"")) == "OK":
                    todos = functions.show_tasks()
                    index = todos.index(todo_to_delete)
                    todos.pop(index)
                    functions.write_file(todos)
                    window['tasks'].update(functions.show_tasks())
                    clear_input()
        case "Clear the list":
            if clear_finish_tasks_list() == "OK":
                functions.write_file(text="", filename='files/finished.txt')
                completed_tasks_text.update(functions.show_tasks(file_name='files/finished.txt', as_string=True))

        case sg.WIN_CLOSED:
            break

window.close()
