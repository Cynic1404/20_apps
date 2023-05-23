import functions
from random import shuffle
import PySimpleGUI as sg
lable=sg.Text("Type to do")
input_box = sg.InputText(tooltip="Enter todo")
button = sg.Button("Add")

content = [lable, input_box, button]
# content = [[lable], [input_box], [button]]
# shuffle(content)
layout = [content]
window = sg.Window('To-Do list', layout=layout)
window.read()
window.close()

