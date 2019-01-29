###Python File for Building GUI Visual Elements###

from Tkinter import Tk, Button, Label

class GUI:
    def __init__(self, master):
        ##Set Master
        self.master = master

        ##Set GUI Title
        master.title("SDRC URC Driver Station")
        ##TODO:  Add Window Icon

        ##Add Status Labels
        self.connection_header = Label(master, text = "Rover Status", bg = 'gray', font=(None, 30))
        self.connection_header.grid(row=0, column=4)
        self.connection_label = Label(master, text = "Disconnected", bg = 'red', font=(None, 30))
        self.connection_label.grid(row=1, column=4)
        #self.vbat_label = Label(master, text="VBat = ?V")
        #self.vbat_label.grid(row=0, column = 1)

        ##Add Enable/Disable Buttons
        #Row 1
        #Button 1
        self.button_label = Label(master, text = "<button> Status", bg = 'gray', font=(None, 20))
        self.button_label.grid(row=2, column=2)
        self.enable_button = Button(master, text="Enable", bg='green', width = 10, height = 3, command=self.button1en)  ##TODO:  Add command to handle button press
        self.enable_button.grid(row=3, column = 1)
        self.disable_button = Button(master, text="Disable", bg='red', width = 10, height = 3, command=self.button1dis)  ##TODO:  Add command to handle button press
        self.disable_button.grid(row = 3, column = 3)

        #Button 2
        self.button2_label = Label(master, text = "<button 2> Status", bg = 'gray', font=(None, 20))
        self.button2_label.grid(row=2, column=6)
        self.enable_button2 = Button(master, text="Enable", bg='green', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.enable_button2.grid(row=3, column = 5)
        self.disable_button2 = Button(master, text="Disable", bg='red', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.disable_button2.grid(row = 3, column = 7)

        #Row 2
        #Button 3
        self.button3_label = Label(master, text = "<button 3> Status", bg = 'gray', font=(None, 20))
        self.button3_label.grid(row=5, column=2)
        self.enable_button3 = Button(master, text="Enable", bg='green', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.enable_button3.grid(row=6, column = 1)
        self.disable_button3 = Button(master, text="Disable", bg='red', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.disable_button3.grid(row = 6, column = 3)

        #Button 4
        self.button4_label = Label(master, text = "<button 4>Status", bg = 'gray', font=(None, 20))
        self.button4_label.grid(row=5, column=6)
        self.enable_button4 = Button(master, text="Enable", bg='green', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.enable_button4.grid(row=6, column = 5)
        self.disable_button4 = Button(master, text="Disable", bg='red', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.disable_button4.grid(row = 6, column = 7)


    #Button 1 enable/disable data
    def button1en(self):
        self.button_label.config(text="Button1 Enabled")
        self.button_label.config(bg = 'green')
    def button1dis(self):
        self.button_label.config(text="Button2 Disabled")
        self.button_label.config(bg = 'red')





if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.mainloop()