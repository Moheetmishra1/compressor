import functionforpyproject
import PySimpleGUI as sg
import time
now = time.strftime("%b-%d,%Y %H:%M:%S")
print("It is ", now)

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter tool", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functionforpyproject.get_todos(), key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
Complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-do app",
                   layout=[[label], [input_box, add_button], [list_box, edit_button, Complete_button],
                   [exit_button]],
                   font=('Helvetical', 20))
while True:
    event, values=window.read()
    print(event)  #This method display the window
    print(values)
    match event:
        case "Add":
            List = functionforpyproject.get_todos()
            new_todo = values['todo']+f"[{now}]"+'\n'
            List.append(new_todo)
            functionforpyproject.write_todos(List)
            window['todos'].update(values=List)
        case "Edit":
             todo_to_edit = values["todos"][0]

             new_todo = values["todo"]+f"[{now}]"'\n'

             List = functionforpyproject.get_todos()
             index = List.index(todo_to_edit)
             List[index] = new_todo
             functionforpyproject.write_todos(List)
             window['todos'].update(values=List)
        case 'todos':
           window['todo'].update(value=values['todos'][0])
        case 'Complete':
            lists = functionforpyproject.get_todos()
            lists.remove(values['todos'][0])
            functionforpyproject.write_todos(lists)
            window['todos'].update(values=lists)
            window["todo"].update(value=' ')
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close() #this close the window