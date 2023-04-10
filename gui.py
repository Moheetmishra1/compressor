import functionforpyproject
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter tool",key="todo")
add_button = sg.Button("Add")
window = sg.Window("My To-do app",
                   layout=[[label],[input_box,add_button]],
                   font=('Helvetical',20))
while True:
    event,values=window.read()
    print(event)  #This method display the window
    print(values)
    match event:
        case "Add":
            todos = functionforpyproject.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functionforpyproject.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close() #this close the window