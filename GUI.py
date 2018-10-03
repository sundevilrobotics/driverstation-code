###Python File for Building GUI Visual Elements###

from tkinter import Tk, Button, Label

class GUI:
    def __init__(self, master):
        ##Set Master
        self.master = master

        ##Set GUI Title
        master.title("SDRC URC Driver Station")
        ##TODO:  Add Window Icon

        ##Add Status Labels
        self.connection_label = Label(master, text = "Disconnected", bg = 'red')
        self.connection_label.pack()
        self.vbat_label = Label(master, text="VBat = ?V")
        self.vbat_label.pack()

        ##Add Enable/Disable Buttons
        self.enable_button = Button(master, text="Enable", bg='green', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.enable_button.pack()
        self.disable_button = Button(master, text="Disable", bg='red', width = 10, height = 3)  ##TODO:  Add command to handle button press
        self.disable_button.pack()

if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.mainloop()