from tkinter import *
import random

# window class
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # all needed buttons + button positions
        rockButton = Button(self, text="Rock", command=self.clickRockButton)
        rockButton.place(x=0, y=0)

        paperButton = Button(self, text="Paper", command=self.clickPaperButton)
        paperButton.place(x=50, y=0)

        scissorButton = Button(self, text="Scissor", command=self.clickScissorButton)
        scissorButton.place(x=100, y=0)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=160, y=0)

        self.outputLabel = Label(self, text="")
        self.outputLabel.place(x=10, y=50)

    # functions called by clicking on one of the buttons
    def clickRockButton(self):
        plc = "rock"
        output = self.randomChoice(plc)
        self.display(output)

    def clickPaperButton(self):
        plc = "paper"
        output = self.randomChoice(plc)
        self.display(output)

    def clickScissorButton(self):
        plc = "scissor"
        output = self.randomChoice(plc)
        self.display(output)

    def clickExitButton(self):
        exit()

    # random choice (rock/paper/scissor) function
    # pcc = choice of computer, plc = choice of player
    def randomChoice(self, plc):
        selection = ['rock', 'paper', 'scissor']
        pcc = random.choice(selection)

        # check who won the game (computer or player)
        if plc=="rock" and pcc=="paper":
            result = ['Loss!', plc, pcc]
        if plc == "rock" and pcc == "scissor":
            result = ['Win!', plc, pcc]
        if plc == "rock" and pcc == "rock":
            result = ['Tie!', plc, pcc]
        
        if plc=="paper" and pcc=="paper":
            result = ['Tie!', plc, pcc]
        if plc == "paper" and pcc == "scissor":
            result = ['Loss!', plc, pcc]
        if plc == "paper" and pcc == "rock":
            result = ['Win!', plc, pcc]

        if plc=="scissor" and pcc=="paper":
            result = ['Win!', plc, pcc]
        if plc == "scissor" and pcc == "scissor":
            result = ['Tie!', plc, pcc]
        if plc == "scissor" and pcc == "rock":
            result = ['Loss!', plc, pcc]
        
        return result

    # function to display result in window
    def display(self, output):
        self.outputLabel.configure(text=output[0] + '\n Your Choice: ' + output[1] + '\n Computers Choice: ' + output[2])

# initialize tkinter and show window
root = Tk()
app = Window(root)
root.wm_title("Game Window")
root.geometry("200x150")
root.mainloop()