import PySimpleGUI as sg
label1 = sg.Text("Select files")
input1 = sg.Input()
choose_button = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FileBrowse("Choose", file_types=("*.txt"))

window = sg.Window("File Compressor", layout=[[label1], [input1, choose_button], [label2],[ input2, choose_button2]])
window.read()