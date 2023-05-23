import functions
import PySimpleGUI as sg
lable=sg.Text("Type to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
button = sg.Button("Add")
clear_button = sg.Button("Clear")
edit_button = sg.Button("Edit")
list_box =sg.Listbox(values=functions.show_ennumerated_tasks(), size=[45,10], key='tasks', enable_events=True)

content = [[lable, input_box, button, clear_button], [list_box, edit_button]]
layout = [content]
window = sg.Window('To-Do list', layout=content, font=("Helvetica", 20))

def clear_input():
    window['todo'].update('')

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            if values["todo"]!='':
                functions.add_row(gui_string=values["todo"])
                clear_input()
                window['tasks'].update(functions.show_ennumerated_tasks())
        case "Clear":
            clear_input()
        case "Edit":
            todo_to_edit = values['tasks'][0]
            new_todo = values['todo']

            todos = functions.show_ennumerated_tasks()
            index = todos.index(todo_to_edit)
            todos[index]=new_todo+"\n"
            functions.write_file(todos)
            window['tasks'].update(functions.show_ennumerated_tasks())
            clear_input()
        case sg.WIN_CLOSED:
            break



window.close()

