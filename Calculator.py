# A basic calculator in python using customtkinter
import customtkinter
from PIL import ImageTk, Image
import tkinter
app = customtkinter.CTk()
# functions

def click(num):
    n = e.get()
    clear()
    e.insert(0, str(n)+str(num))
    # clear()
# def leave(*arg):
    # clear()
    # e.insert(0,"Enter here!")
    # app.focus()


def clear():
    e.delete(0, tkinter.END)


def calc():
    exp = e.get()
    clear()
    try:
        e.insert(0, eval(exp))
    except:
        e.insert(0, "Invalid expresion!")


# System outlook
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("system")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("green")

# App title
app.title("Calculator")

# App Icon
# ico = Image.open('calc_icon.png')
# photo = ImageTk.PhotoImage(ico)
# app.iconphoto(False, photo)

# app.geometry('400x300')

# Entry field

# row 0
e = customtkinter.CTkEntry(master=app,
                           width=370,
                           height=70,
                           corner_radius=50,
                           font=('monospace', 30),
                           border_color="grey", border_width=5,
                           justify=tkinter.CENTER,
                           fg_color="lightgrey",
                           text_color="blue")
# e.place(relx=0.5,rely=0.5,anchor=tkinter.N)

# place holder text
# e.insert(0,"Enter Here!")
# e.bind("<button-1>",click)
# e.bind("<Leave>",leave)

e.grid(row=0, column=0, columnspan=6)

# buttons

# Number buttons

# row 1
btn_clear = customtkinter.CTkButton(master=app,
                                    text="C",
                                    width=80,
                                    height=80,
                                    corner_radius=50,
                                    border_width=1,
                                    command=clear,
                                    fg_color="purple",
                                    font=('bold', 20))
btn_mod = customtkinter.CTkButton(master=app,
                                  text="%",
                                  width=80,
                                  height=80,
                                  corner_radius=50,
                                  border_width=1,
                                  command=lambda: click("%"),
                                  fg_color="brown",
                                  font=('bold', 20))
btn_div = customtkinter.CTkButton(master=app, text="/",
                                  width=80,
                                  height=80,
                                  corner_radius=50,
                                  border_width=1,
                                  command=lambda: click("/"),
                                  fg_color="brown",
                                  font=('bold', 20))
btn_mul = customtkinter.CTkButton(master=app, text="*",
                                  width=80,
                                  height=80,
                                  corner_radius=50,
                                  border_width=1,
                                  command=lambda: click("*"),
                                  fg_color="brown",
                                  font=('bold', 30))

# row 2
btn9 = customtkinter.CTkButton(master=app,
                               text="9",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("9"),
                               font=('bold', 20))
btn8 = customtkinter.CTkButton(master=app,
                               text="8",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("8"),
                               font=('bold', 20))
btn7 = customtkinter.CTkButton(master=app,
                               text="7",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("7"), 
                               font=('bold', 20))
btn_add = customtkinter.CTkButton(master=app,
                                  text="+",
                                  width=80,
                                  height=80,
                                  corner_radius=50,
                                  border_width=1,
                                  command=lambda: click("+"),
                                  fg_color="brown",
                                  font=('bold', 20))

# row 3
btn4 = customtkinter.CTkButton(master=app,
                               text="4",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("4"),
                               font=('bold', 20))
btn5 = customtkinter.CTkButton(master=app,
                               text="5",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("5"),
                               font=('bold', 20))
btn6 = customtkinter.CTkButton(master=app,
                               text="6",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("6"),
                               font=('bold', 20))
btn_sub = customtkinter.CTkButton(master=app,
                                  text="-",
                                  width=80,
                                  height=80,
                                  corner_radius=50,
                                  border_width=1,
                                  command=lambda: click("-"),
                                  fg_color="brown",
                                  font=('bold', 20))

# row 4
btn1 = customtkinter.CTkButton(master=app,
                               text="1",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("1"),
                               font=('bold', 20))
btn2 = customtkinter.CTkButton(master=app,
                               text="2",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1,
                               command=lambda: click("2"),
                               font=('bold', 20))
btn3 = customtkinter.CTkButton(master=app,
                               text="3",
                               width=80,
                               height=80,
                               corner_radius=50,
                               border_width=1, 
                               command=lambda: click("3"),
                               font=('bold', 20))
btn_pow = customtkinter.CTkButton(master=app,
                                  text="**",
                                  width=80,
                                  height=80,
                                  corner_radius=50,
                                  border_width=1,
                                  command=lambda: click("**"),
                                  fg_color="brown",
                                  font=('bold', 20))

# row 5
btn_dot = customtkinter.CTkButton(master=app,
                                  text=".",
                                  width=80,
                                  height=80,
                                  corner_radius=50,
                                  border_width=1,
                                  command=lambda: click("."),
                                  font=('bold', 20))
btn_zero = customtkinter.CTkButton(master=app,
                                   text="0",
                                   width=80,
                                   height=80,
                                   corner_radius=50,
                                   border_width=1,
                                   command=lambda: click("0"),
                                   font=('bold', 20))
btn_equal = customtkinter.CTkButton(master=app,
                                    text="=",
                                    width=80,
                                    height=80,
                                    corner_radius=50,
                                    border_width=1, command=calc,
                                    fg_color="brown",
                                    font=('bold', 20))
btn_exit = customtkinter.CTkButton(master=app,
                                   text="Exit",
                                   width=70,
                                   height=70,
                                   corner_radius=50,
                                   border_width=1,
                                   command=app.quit,
                                   fg_color="red",
                                   font=('bold', 20))
# placing the buttons on the screen

# row 1
btn_clear.grid(row=1, column=0, padx=0, pady=0)
btn_mod.grid(row=1, column=1, padx=0, pady=0)
btn_div.grid(row=1, column=2, padx=0, pady=0)
btn_mul.grid(row=1, column=3, padx=0, pady=0)

# row 2
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btn_add.grid(row=2, column=3)

# row 3
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn_sub.grid(row=3, column=3)

# row 4
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btn_pow.grid(row=4, column=3)

# row 5
btn_exit.grid(row=5, column=0)
btn_dot.grid(row=5, column=1)
btn_zero.grid(row=5, column=2)
btn_equal.grid(row=5, column=3)
app.mainloop()