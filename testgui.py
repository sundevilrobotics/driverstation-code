###Python File for Building GUI Visual Elements###
from Tkinter import Tk, Button, Label
import ttk
from functools import partial

window = Tk()
window.title("SDRC URC Driver Station")
tab_control = ttk.Notebook(window, width=800, height=800)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='State 1')
tab_control.add(tab2, text='State 2')
tab_control.add(tab3, text='State 3')

#tab 1
lbl1 = Label(tab1, text= 'button 1 <command>')
lbl1.grid(column=2, row=2)
button1_label = Label(tab1, text = " Status ", bg = 'gray', font=(None, 20))
button1_label.grid(row=4, column=2)
enable_button = Button(tab1, bg = 'red', text="Enable", width = 10, height = 3, command=lambda: switch_button_status(text="button 1 enabled", enabled=True, label=button1_label))
enable_button.grid(row=4, column=1)
disable_button = Button(tab1, bg = 'red', text="Disable", width = 10, height = 3, command=lambda: switch_button_status(text="button 1 enabled", enabled=False, label=button1_label))
disable_button.grid(row = 4, column = 3)







#tab 2
lbl2 = Label(tab2, text= 'something cool here')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')


def switch_button_status(text, enabled, label):
    color = 'green' if enabled else 'red'
    label.config(text=text)
    label.config(bg=color)


window.mainloop()