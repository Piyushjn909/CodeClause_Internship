import tkinter as tk
from tkinter.font import Font

# some constants
ADD = "+"
SUBTRACT = "-"
MULTIPLY = "*"
DIVIDE = "/"
CLEAR = "Clear"
EQUAL = "="
ERROR_INPUT = False
btn_click = False

# colors
text_prev_calc = "#3f823c"
bg_prev_calc = '#cefa75'

previous_calculations = []

root = tk.Tk()

root.resizable(False, False)
root.title("AP San Calculator")
#root.iconbitmap(r"F:\ADARSH\WorkSpace\Pyth\gui\favicon.ico")
root.iconbitmap(r"favicon.ico")

prev_calc_frame = ''


def only_numbers(char):
    global btn_click
    if isinstance(prev_calc_frame, tk.Frame):
        prev_calc_frame.destroy()
    bool = char.isdigit() or char == ADD or char == SUBTRACT or char == MULTIPLY or char == DIVIDE or btn_click
    btn_click = False
    return bool


frame1 = tk.Frame(root)
frame1.grid(row=0, sticky='nsew')

validation = frame1.register(only_numbers)

entryText = tk.StringVar()

last_command_equal = False

entry = tk.Entry(frame1, width=30, validate="key", validatecommand=(validation, '%S'),
                 font="Calibri 20", justify="right", textvariable=entryText)

entry.grid(padx=8, pady=8, ipadx=8, ipady=8, columnspan=4)
entry.focus()

myFont = Font(family='Helvetica', size=15)


def prev_calc_edit(i, labels):
    global last_command_equal
    entryText.set(labels[i]['text'][labels[i]['text'].rfind('=') + 1:])
    last_command_equal = False
    entry.icursor("end")


def btn_prev_calc():
    global prev_calc_frame
    if prev_calc_frame == '' or prev_calc_frame.winfo_exists() == 0 :
        prev_calc_frame = tk.Frame(root, bg='#cefa75')
        prev_calc_frame.grid(row=0, sticky='nsw', column=0)
        l1 = tk.Label(prev_calc_frame, text="Your previous calculations", font="Calibri 12")
        l1.grid(row=0)
        prev_calc_frame.tkraise()

        labels = {}
        for i in range(len(previous_calculations)):
            calculation = previous_calculations[i]
            labels[i] = tk.Label(prev_calc_frame, text=calculation,
                                 font="Helvetica 8", bg=bg_prev_calc, fg=text_prev_calc,
                                 )
            labels[i].bind("<Button-1>", lambda e, i=i: prev_calc_edit(i, labels))
            labels[i].grid(row=i + 1, pady=5, sticky='ew', columnspan=2)
        global photo
        #photo = tk.PhotoImage(file=r"F:\ADARSH\WorkSpace\Pyth\gui\newimage.png")
        photo = tk.PhotoImage(file=r"newimage.png")
        closepanel = tk.Button(prev_calc_frame, image=photo, command=lambda: prev_calc_frame.destroy())
        closepanel.grid(row=0, column=1)


def btn_numb_click(clicked_no):
    global last_command_equal
    global btn_click
    btn_click = True
    if not last_command_equal:
        entryText1 = entryText.get() + str(clicked_no)
        entryText.set(entryText1)
    else:
        entryText.set("")
        last_command_equal = False
        entryText1 = entryText.get() + str(clicked_no)
        entryText.set(entryText1)
    entry.icursor("end")


def btn_symb_click(symbol):
    global last_command_equal
    global btn_click
    btn_click = True
    if symbol == ADD or symbol == SUBTRACT or symbol == MULTIPLY or symbol == DIVIDE:
        last_command_equal = False
        btn_numb_click(" " + symbol + " ")
    elif symbol == CLEAR:
        entryText.set("")
    elif symbol == EQUAL:
        try:
            result = eval(entryText.get())
            last_command_equal = True
            entry.config(highlightthickness=0)
            if not isinstance(result, int):
                result = "%.4f" % result
            expression = entryText.get()
            if str(result) != str(expression):
                previous_calculations.append(str(entryText.get()) + " = " + str(result))
            if len(previous_calculations) >= 9:
                del previous_calculations[0]
            entryText.set(result)
        except SyntaxError:
            entry.config(highlightbackground="red", highlightthickness=2, highlightcolor="red")
    entry.icursor("end")


button_previous = tk.Button(frame1, text="See Previous Calculations", font="Calibri 8",
                            command=btn_prev_calc)

button_previous.grid(row=1, column=3, padx=20, sticky='e')

button_1 = tk.Button(frame1, text="1", font=myFont, command=lambda: btn_numb_click(1))
button_2 = tk.Button(frame1, text="2", font=myFont, command=lambda: btn_numb_click(2))
button_3 = tk.Button(frame1, text="3", font=myFont, command=lambda: btn_numb_click(3))
button_4 = tk.Button(frame1, text="4", font=myFont, command=lambda: btn_numb_click(4))
button_5 = tk.Button(frame1, text="5", font=myFont, command=lambda: btn_numb_click(5))
button_6 = tk.Button(frame1, text="6", font=myFont, command=lambda: btn_numb_click(6))
button_7 = tk.Button(frame1, text="7", font=myFont, command=lambda: btn_numb_click(7))
button_8 = tk.Button(frame1, text="8", font=myFont, command=lambda: btn_numb_click(8))
button_9 = tk.Button(frame1, text="9", font=myFont, command=lambda: btn_numb_click(9))
button_0 = tk.Button(frame1, text="0", font=myFont, command=lambda: btn_numb_click(0))

button_divide = tk.Button(frame1, text="/", font=myFont, command=lambda: btn_symb_click(DIVIDE))
button_add = tk.Button(frame1, text="+", font=myFont, command=lambda: btn_symb_click(ADD))
button_subt = tk.Button(frame1, text="-", font=myFont, command=lambda: btn_symb_click(SUBTRACT))
button_multiply = tk.Button(frame1, text="x", font=myFont, command=lambda: btn_symb_click(MULTIPLY))
button_equals = tk.Button(frame1, text="=", font=myFont, command=lambda: btn_symb_click(EQUAL))
button_clear = tk.Button(frame1, text="CLR", font=myFont, command=lambda: btn_symb_click(CLEAR))

button_clear.grid(row=5, column=0, sticky="nesw", padx=5, pady=5)
button_0.grid(row=5, column=1, sticky="nesw", padx=5, pady=5)
button_equals.grid(row=5, column=2, sticky="nesw", padx=5, pady=5)
button_add.grid(row=5, column=3, sticky="nesw", padx=5, pady=5)

button_1.grid(row=4, column=0, sticky="nesw", padx=5, pady=5)
button_2.grid(row=4, column=1, sticky="nesw", padx=5, pady=5)
button_3.grid(row=4, column=2, sticky="nesw", padx=5, pady=5)
button_subt.grid(row=4, column=3, sticky="nesw", padx=5, pady=5)

button_4.grid(row=3, column=0, sticky="nesw", padx=5, pady=5)
button_5.grid(row=3, column=1, sticky="nesw", padx=5, pady=5)
button_6.grid(row=3, column=2, sticky="nesw", padx=5, pady=5)
button_multiply.grid(row=3, column=3, sticky="nesw", padx=5, pady=5)

button_7.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)
button_8.grid(row=2, column=1, sticky="nesw", padx=5, pady=5)
button_9.grid(row=2, column=2, sticky="nesw", padx=5, pady=5)
button_divide.grid(row=2, column=3, sticky="nesw", padx=5, pady=5)

root.mainloop()