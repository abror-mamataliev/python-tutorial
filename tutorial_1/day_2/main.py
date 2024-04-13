from tkinter import (
    Button,
    Frame,
    Label,
    Tk,
)

root = Tk()
root.title("Day 2")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

buttons = [
    ("AC", 1, 0), ("%", 1, 1), ("!", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("-/+", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
]

first, second, operator = None, None, None


def on_click(text):
    global first, second, operator
    if text.isdigit():
        if operator is None:
            first = int(str(first or 0) + text)
            output["text"] = str(first)
        else:
            second = int(str(second or 0) + text)
        output["text"] = str(first) if second is None else str(second)
    elif text in ["+", "-", "*", "/"]:
        operator = text
    elif text == "=" and first is not None and second is not None and operator is not None:
        match operator:
            case "+":
                result = first + second
            case "-":
                result = first - second
            case "*":
                result = first * second
            case "/":
                result = first / second if second != 0 else "Error"
            case _:
                result = second
        output["text"] = result
        if result == "Error":
            first, second, operator = None, None, None
        else:
            first, second, operator = result, None, None
    elif text == "%" and first is not None:
        output["text"] = str(first / 100)
    elif text == "!" and first is not None:
        result = 1
        for i in range(1, first + 1):
            result *= i
        output["text"] = str(result)
    elif text == "AC":
        first, second, operator = None, None, None
        output["text"] = "0"


output = Label(
    frame,
    text="0",
    font=("Helvetica", 48),
    anchor="se",
    width=9,
    height=1
)
output.grid(row=0, columnspan=4)

for text, row, column in buttons:
    button = Button(
        frame,
        text=text,
        font=("Helvetica", 24, "bold"),
        width=4,
        height=1,
        command=lambda t=text: on_click(t)
    )
    button.grid(row=row, column=column)

root.mainloop()
