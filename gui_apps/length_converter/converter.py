
import PySimpleGUI as sg

feet_lable = sg.Text("Input feet")
inch_lable = sg.Text("Input inch")
feet_input_box = sg.InputText(tooltip="Enter feet", key="feet")
inch_input_box = sg.InputText(tooltip="Enter inch", key="inch")
convert_button = sg.Button("Convert")
result = sg.Text()


layout = [[feet_lable, feet_input_box],[inch_lable, inch_input_box], [convert_button, result]]
window = sg.Window('Converter', layout=layout, font=("Helvetica", 20))

def pop_up_notification(text):
    return sg.popup_ok(text, title="Error", font=("Helvetica", 20))

def convert(feet, inch):
    feet=float(feet)+float(inch)/12
    return round(float(feet)/3.281, 3)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            feet = values['feet']
            inch = values['inch']
            if feet == '' or inch == '':
                pop_up_notification("Fill all forms")
            elif not feet.isdigit() or not inch.isdigit():
                pop_up_notification("It takes only digits")
            else:
                result.update(f"{convert(feet, inch)}m")
    if event == sg.WIN_CLOSED:
            break

window.close()
