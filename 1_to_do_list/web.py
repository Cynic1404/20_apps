import streamlit as st
import functions
import streamlit_scrollable_textbox as stx



def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)
    print(st.session_state)
    if todo+"\n" not in st.session_state:
        todos.append(todo+"\n")
        functions.write_file(todos)
        st.session_state["new_todo"]=""
    else:
        st.session_state["new_todo"]="DUPLICATE"






todos = functions.show_tasks()
st.title("My Todo app")
st.subheader("List of tasks")
for index, task in enumerate(functions.show_tasks()):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        finished_tasks = functions.show_finished_tasks(print_ennumerated=False)
        task_to_finish=todos.pop(index)
        functions.write_file(todos)
        finished_tasks.append(task_to_finish)
        functions.write_file(finished_tasks, filename='files/finished.txt')
        del st.session_state[task]
        st.experimental_rerun()


todo_input = st.text_input(label="opa", label_visibility="hidden", placeholder="Enter a todo", on_change=add_todo, key="new_todo")



st.subheader("List of finished tasks")
stx.scrollableTextbox("".join(functions.show_finished_tasks(print_ennumerated=False)), height=300)
clear_button=st.button("Clear the list of finished tasks")
if clear_button:
    functions.write_file(text="", filename='files/finished.txt')
    st.experimental_rerun()
