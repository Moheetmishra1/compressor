import functionforpyproject
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter tool")
add_button = sg.Button("Add")
window = sg.Window("My To-do app",layout=[[label],[input_box,add_button]])
window.read() #This method display the window
window.close() #this close the window