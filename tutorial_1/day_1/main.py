from tkinter import (
    Button,
    Frame,
    Label,
    Tk,
)

root = Tk()
root.title("Day 1")
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
equal = False


def on_click(text):
    global first, second, operator, equal
    if text.isdigit():
        if operator is None:
            if equal:
                first, second, operator = None, None, None
                equal = False
            first = str(first or 0) + text
            first = float(first) if "." in first else int(first)
        else:
            second = str(second or 0) + text
            second = float(second) if "." in second else int(second)
        output["text"] = str(first) if second is None else str(second)
    elif text == "-/+":
        if second is not None:
            second = float("-" + str(second) if str(second)[0] != "-" else str(second)[1:])
            output["text"] = str(second)
        else:
            first = float("-" + str(first) if str(first)[0] != "-" else str(first)[1:])
            output["text"] = str(first)
    elif text == ".":
        if second is not None:
            if "." not in str(second):
                second = str(second) + "."
                output["text"] = str(second)
        else:
            if "." not in str(first):
                first = str(first) + "."
                output["text"] = str(first)
    elif text in ["+", "-", "*", "/"]:
        if second is not None:
            match operator:
                case "+":
                    first += second
                case "-":
                    first -= second
                case "*":
                    first *= second
                case "/":
                    first /= second if second != 0 else "Error"
                case _:
                    first = second
            if first >= 1e9:
                first = "Error"
            output["text"] = str(int(first)) if first == int(first) else str(first)
            if first == "Error":
                first, second, operator = None, None, None
            else:
                second = None
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
        if result >= 1e9:
            result = "Error"
        output["text"] = result if result == "Error" else str(int(result)) if result == int(result) else str(result)
        if result == "Error":
            first, second, operator = None, None, None
        else:
            first, second, operator = result, None, None
        equal = True
    elif text == "%" and first is not None:
        result = first / 100
        output["text"] = str(result)
        first, second, operator = result, None, None
        equal = True
    elif text == "!" and first is not None and first >= 0 and isinstance(first, int):
        result = 1
        for i in range(1, first + 1):
            result *= i
        if result >= 1e9:
            result = "Error"
        output["text"] = str(result)
        first, second, operator = result, None, None
        equal = True
    elif text == "AC":
        first, second, operator = None, None, None
        output["text"] = "0"
        equal = False


output = Label(
    frame,
    text="0",
    font=("Helvetica", 48),
    anchor="e",
    width=13,
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
