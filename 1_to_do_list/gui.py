import functions
import PySimpleGUI as sg
lable=sg.Text("Type to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")

button = sg.Button("Add")
clear_button = sg.Button("Clear")

content = [lable, input_box, button, clear_button]
layout = [content]
window = sg.Window('To-Do list', layout=[content], font=("Helvetica", 20))

def clear_input():
    window['todo'].update('')

while True:
    event, values = window.read()
    match event:
        case "Add":
            if values["todo"]!='':
                functions.add_row(gui_string=values["todo"])
                clear_input()
        case "Clear":
            clear_input()
        case sg.WIN_CLOSED:
            break
    print(event)


window.close()

