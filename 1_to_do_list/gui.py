import functions
import PySimpleGUI as sg

lable = sg.Text("Type to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add = sg.Button("Add")
clear_button = sg.Button("Clear")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
list_box = sg.Listbox(values=functions.show_ennumerated_tasks(), size=[45, 10], key='tasks', enable_events=True)

layout = [[lable, input_box, add, clear_button], [list_box, edit_button, delete_button]]
window = sg.Window('To-Do list', layout=layout, font=("Helvetica", 20))


def clear_input():
    window['todo'].update('')


def delete_confirmation(todo_to_delete):
    event = sg.popup_ok_cancel(f"Do you want to remove the '{todo_to_delete}' record", "Press cancel to stop",
                               title="Are you sure?")
    print(event)
    return event


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            if values["todo"] != '':
                functions.add_row(gui_string=values["todo"])
                clear_input()
                window['tasks'].update(functions.show_ennumerated_tasks())
        case "Clear":
            clear_input()
        case "Edit":
            todo_to_edit = values['tasks'][0]
            if values['todo']:
                new_todo = values['todo']
                todos = functions.show_ennumerated_tasks()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_file(todos)
                window['tasks'].update(functions.show_ennumerated_tasks())
                clear_input()
        case "Delete":
            if values['tasks']:
                todo_to_delete = values['tasks'][0]
                if delete_confirmation(todo_to_delete) == "OK":
                    todos = functions.show_ennumerated_tasks()
                    index = todos.index(todo_to_delete)
                    todos.pop(index)
                    functions.write_file(todos)
                    window['tasks'].update(functions.show_ennumerated_tasks())
                    clear_input()

        case sg.WIN_CLOSED:
            break

window.close()
