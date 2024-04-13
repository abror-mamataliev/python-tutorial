from tkinter import Tk, Label, Button

tk = Tk()
tk.title("Hello, World!")

label = Label(tk, text="Hello, World!")
label.pack()

button = Button(tk, text="Quit", command=tk.quit)
button.pack()

tk.mainloop()
