import datetime

import functions




if __name__ == '__main__':
    while True:
        print(datetime.datetime.now().strftime("It's %B %d, %H:%M"))
        option = input('Type add, show, or exit \n')
        if option.startswith("add") and len(option.split()) > 1:
            functions.add_row(string_to_check=option)
        else:
            match option:
                case "add":
                    functions.add_row()
                case "show":
                    functions.show_tasks()
                case "edit":
                    functions.edit()
                case "complete":
                    functions.complete()
                case "finished":
                    functions.show_finished_tasks()
                case "exit":
                    quit()
                case other:
                    print('wrong option, try again\n')
