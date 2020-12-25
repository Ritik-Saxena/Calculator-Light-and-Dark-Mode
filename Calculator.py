from tkinter import *
import parser
import os


# Path for respective directories
BASE_DIR = os.path.join(os.getcwd(), "Media")

buttondir_path_light_mode = os.path.join(BASE_DIR, "Buttons", "Light Mode")
buttondir_path_dark_mode = os.path.join(BASE_DIR, "Buttons", "Dark Mode")



root = Tk()

window_icon = PhotoImage(file = os.path.join(BASE_DIR, "Icon", "Calculator icon.png"))
root.iconphoto(False, window_icon)
root.title("Calculator")
root.resizable(height=0, width=0)


mode = 0            # Default mode : Light Mode
class Calculator:
    def screen(self):
        self.display = Entry(root, justify=RIGHT, font="Verdana, 18", relief = FLAT)
        self.display.grid(columnspan=4, ipady=30)

    def numeric_buttons(self):
        self.button_1 = Button(root, text="1", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(1))
        self.button_1.grid(row=2, column=0, ipadx=18, ipady=10, sticky="nsew")

        self.button_2 = Button(root, text="2", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(2))
        self.button_2.grid(row=2, column=1, ipadx=18, ipady=10, sticky="nsew")

        self.button_3 = Button(root, text="3", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(3))
        self.button_3.grid(row=2, column=2, ipadx=18, ipady=10, sticky="nsew")

        self.button_4 = Button(root, text="4", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(4))
        self.button_4.grid(row=3, column=0, ipadx=18, ipady=10, sticky="nsew")

        self.button_5 = Button(root, text="5", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(5))
        self.button_5.grid(row=3, column=1, ipadx=18, ipady=10, sticky="nsew")

        self.button_6 = Button(root, text="6", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(6))
        self.button_6.grid(row=3, column=2, ipadx=18, ipady=10, sticky="nsew")

        self.button_7 = Button(root, text="7", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(7))
        self.button_7.grid(row=4, column=0, ipadx=18, ipady=10, sticky="nsew")

        self. button_8 = Button(root, text="8", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(8))
        self.button_8.grid(row=4, column=1, ipadx=18, ipady=10, sticky="nsew")

        self.button_9 = Button(root, text="9", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(9))
        self.button_9.grid(row=4, column=2, ipadx=18, ipady=10, sticky="nsew")

        self.button_0 = Button(root, text="0", font="Verdana, 15", bg="White", bd=0, command = lambda : self.get_numeric(0))
        self.button_0.grid(row=5, columnspan = 2, ipadx=18, ipady=10, sticky="nsew")



    def operator_buttons(self):
        self.button_all_clear = Button(root, text="AC", font="Verdana, 15", bg="White", fg="#ff5c35", bd=0,
                                       command = lambda : self.all_clear(), activeforeground = "#ff5c33")
        self.button_all_clear.grid(row=1, column=0, ipadx=5, ipady=5, sticky="nsew")


        self.open_brace_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "braces.png"))
        self.inverting_brace = self.open_brace_img.subsample(-1, -1)        # inverting image
        self.open_brace_img = self.inverting_brace.subsample(6, 6)          # resizing image
        self.button_open_brace = Button(root,  bg="White", bd=0, image = self.open_brace_img,
                                        command = lambda : self.get_operator("("))
        self.button_open_brace.grid(row=1, column=1, ipadx=4, ipady=5, sticky="nsew")


        self.close_brace_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "braces.png"))
        self.close_brace_img = self.close_brace_img.subsample(6, 6)
        self.button_close_brace = Button(root, bg="White", bd=0, image=self.close_brace_img,
                                         command = lambda : self.get_operator(")"))
        self.button_close_brace.grid(row=1, column=2, ipadx=5, ipady=5, sticky="nsew")


        self.backspace = PhotoImage(file=os.path.join(buttondir_path_light_mode, "backspace.png"))
        self.backspace = self.backspace.subsample(3, 3)
        self.button_backspace = Button(root, bg="White", bd=0, image=self.backspace,
                                       command = lambda : self.back_space())
        self.button_backspace.grid(row=1, column=3, ipadx=5, ipady=5, sticky="nsew")


        self.plus_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "plus.png"))
        self.plus_img = self.plus_img.subsample(4, 4)
        self.button_plus = Button(root, bg = "white", bd=0, image = self.plus_img,
                                         command = lambda : self.get_operator("+"))
        self.button_plus.grid(row=2, column=3, ipadx = 5, sticky="nsew")


        self.minus_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "minus.png"))
        self.minus_img = self.minus_img.subsample(4, 4)
        self.button_minus = Button(root, bg="White", bd=0, image = self.minus_img,
                                         command = lambda : self.get_operator("-"))
        self.button_minus.grid(row=3, column=3, ipadx = 5, sticky="nsew")


        self.mul_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "multiply.png"))
        self.mul_img = self.mul_img.subsample(4, 4)
        self.button_mul = Button(root, bg="White", bd=0, image = self.mul_img,
                                         command = lambda : self.get_operator("*"))
        self.button_mul.grid(row=4, column=3, ipadx = 5, sticky="nsew")


        self.div_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "divide.png"))
        self.div_img = self.div_img.subsample(4, 4)
        self.button_div = Button(root, bg="White", bd = 0, image=self.div_img,
                                         command = lambda : self.get_operator("/"))
        self.button_div.grid(row=5, column=3, ipadx=20, ipady=10, sticky="nsew")


        self.pow_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "caret.png"))
        self.pow_img = self.pow_img.subsample(4, 4)
        self.button_pow = Button(root, bg="White", bd=0, image=self.pow_img,
                                         command = lambda : self.get_operator("**"))
        self.button_pow.grid(row=6, column=1, ipadx=20, ipady=18, sticky="nsew")


        self.fact_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "factorial.png"))
        self.fact_img = self.fact_img.subsample(3, 3)
        self.button_fact = Button(root, bg="White", bd=0, image=self.fact_img,
                                  command = lambda : self.factorial())
        self.button_fact.grid(row=6, column=2, ipadx=20, ipady=0, sticky="nsew")


        self.swap_mode_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "dark mode.png"))
        self.swap_mode_img = self.swap_mode_img.subsample(3, 3)
        self.button_swap_mode = Button(root, bg="White", bd=0, image=self.swap_mode_img,
                                       command=lambda : self.swap_mode())
        self.button_swap_mode.grid(row=6, column=0, sticky="nsew")


        self.equal_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "equal.png"))
        self.equal_img = self.equal_img.subsample(2, 2)
        self.button_equal = Button(root, bg="White", bd=0, image=self.equal_img,
                                   command = lambda : self.result())
        self.button_equal.grid(row=6, column=3, sticky="nsew")


        self.button_dot = Button(root, text=".", font="Verdana, 15", bg="White", bd=0,
                                 command = lambda : self.get_operator('.'))
        self.button_dot.grid(row=5, column=2, ipadx=18, ipady=10, sticky="nsew")


    def light_mode(self):
        # display
        self.display.config(bg = "White", fg = "Black")

        # numeric buttons
        self.button_1.config(bg="White", fg="Black")
        self.button_2.config(bg="White", fg="Black")
        self.button_3.config(bg="White", fg="Black")
        self.button_4.config(bg="White", fg="Black")
        self.button_5.config(bg="White", fg="Black")
        self.button_6.config(bg="White", fg="Black")
        self.button_7.config(bg="White", fg="Black")
        self.button_8.config(bg="White", fg="Black")
        self.button_9.config(bg="White", fg="Black")
        self.button_0.config(bg="White", fg="Black")
        self.button_dot.config(bg="White", fg="Black")

        # operator buttons
        self.button_all_clear.config(bg="White", fg="#ff5c33", activeforeground = "#ff5c33")

        self.open_brace_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "braces.png"))
        self.inverting_brace = self.open_brace_img.subsample(-1, -1)  # inverting image
        self.open_brace_img = self.inverting_brace.subsample(6, 6)  # resizing image
        self.button_open_brace.config(bg="White", image=self.open_brace_img)

        self.close_brace_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "braces.png"))
        self.close_brace_img = self.close_brace_img.subsample(6, 6)
        self.button_close_brace.config(bg="White", image=self.close_brace_img)

        self.backspace = PhotoImage(file=os.path.join(buttondir_path_light_mode, "backspace.png"))
        self.backspace = self.backspace.subsample(3, 3)
        self.button_backspace.config(bg="White", image=self.backspace)

        self.plus_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "plus.png"))
        self.plus_img = self.plus_img.subsample(4, 4)
        self.button_plus.config(bg="White", image=self.plus_img)

        self.minus_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "minus.png"))
        self.minus_img = self.minus_img.subsample(4, 4)
        self.button_minus.config(bg="White", image=self.minus_img)

        self.mul_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "multiply.png"))
        self.mul_img = self.mul_img.subsample(4, 4)
        self.button_mul.config(bg="White", image=self.mul_img)

        self.div_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "divide.png"))
        self.div_img = self.div_img.subsample(4, 4)
        self.button_div.config(bg="White", image=self.div_img)

        self.pow_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "caret.png"))
        self.pow_img = self.pow_img.subsample(4, 4)
        self.button_pow.config(bg="White", image=self.pow_img)

        self.fact_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "factorial.png"))
        self.fact_img = self.fact_img.subsample(3, 3)
        self.button_fact.config(bg="White", image=self.fact_img)

        self.swap_mode_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "dark mode.png"))
        self.swap_mode_img = self.swap_mode_img.subsample(3, 3)
        self.button_swap_mode.config(bg="White", image=self.swap_mode_img)

        self.equal_img = PhotoImage(file=os.path.join(buttondir_path_light_mode, "equal.png"))
        self.equal_img = self.equal_img.subsample(2, 2)
        self.button_equal.config(bg="White", image=self.equal_img)


    def dark_mode(self):
        # display
        self.display.config(bg = "#2D3134", fg = "#93979B")

        # numeric buttons
        self.button_1.config(bg="Black", fg="White")
        self.button_2.config(bg="Black", fg="White")
        self.button_3.config(bg="Black", fg="White")
        self.button_4.config(bg="Black", fg="White")
        self.button_5.config(bg="Black", fg="White")
        self.button_6.config(bg="Black", fg="White")
        self.button_7.config(bg="Black", fg="White")
        self.button_8.config(bg="Black", fg="White")
        self.button_9.config(bg="Black", fg="White")
        self.button_0.config(bg="Black", fg="White")
        self.button_dot.config(bg="Black", fg="White")

        # operator buttons
        self.button_all_clear.config(bg="Black", fg="#7293C6", activeforeground = "#7293C6")

        self.open_brace_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "braces dark.png"))
        self.inverting_brace = self.open_brace_img.subsample(-1, -1)  # inverting image
        self.open_brace_img = self.inverting_brace.subsample(6, 6)  # resizing image
        self.button_open_brace.config(bg="Black", image=self.open_brace_img)

        self.close_brace_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "braces dark.png"))
        self.close_brace_img = self.close_brace_img.subsample(6, 6)
        self.button_close_brace.config(bg="Black", image=self.close_brace_img)

        self.backspace = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "backspace dark.png"))
        self.backspace = self.backspace.subsample(3, 3)
        self.button_backspace.config(bg="Black", image=self.backspace)

        self.plus_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "plus dark.png"))
        self.plus_img = self.plus_img.subsample(4, 4)
        self.button_plus.config(bg="Black", image=self.plus_img)

        self.minus_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "minus dark.png"))
        self.minus_img = self.minus_img.subsample(4, 4)
        self.button_minus.config(bg="Black", image=self.minus_img)

        self.mul_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "multiply dark.png"))
        self.mul_img = self.mul_img.subsample(4, 4)
        self.button_mul.config(bg="Black", image=self.mul_img)

        self.div_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "divide dark.png"))
        self.div_img = self.div_img.subsample(4, 4)
        self.button_div.config(bg="Black", image=self.div_img)

        self.pow_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "caret dark.png"))
        self.pow_img = self.pow_img.subsample(4, 4)
        self.button_pow.config(bg="Black", image=self.pow_img)

        self.fact_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "factorial dark.png"))
        self.fact_img = self.fact_img.subsample(3, 3)
        self.button_fact.config(bg="Black", image=self.fact_img)

        self.swap_mode_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "light mode.png"))
        self.swap_mode_img = self.swap_mode_img.subsample(3, 3)
        self.button_swap_mode.config(bg="Black", image=self.swap_mode_img)

        self.equal_img = PhotoImage(file=os.path.join(buttondir_path_dark_mode, "equal dark.png"))
        self.equal_img = self.equal_img.subsample(2, 2)
        self.button_equal.config(bg="Black", image=self.equal_img)



    # Logic for swapping between Light Mode and Dark Mode
    def swap_mode(self):
        global mode
        if (mode == 1):
            mode = 0
        elif (mode == 0):
            mode = 1


        if (mode == 0):
            self.light_mode()
        else:
            self.dark_mode()


    # adding functionality to numeric buttons
    index = 0
    def get_numeric(self, num):
        self.display.insert(Calculator.index, num)
        Calculator.index += 1

    # adding functionality to operator button
    def get_operator(self, op):
        string = self.display.get()
        if (len(string) == 0 and op != '(' and op != ')'):
            Calculator.index = 0
            self.display.insert(Calculator.index, '0')
            Calculator.index += 1
            self.display.insert(Calculator.index, op)
            Calculator.index += len(op)
        else:
            self.display.insert(Calculator.index, op)
            Calculator.index += len(op)

    # AC functionality
    def all_clear(self):
        self.display.delete(0, END)

    # backspace functionality
    def back_space(self):
        self.string = self.display.get()
        self.new_string = self.string[:-1]
        self.all_clear()
        self.display.insert(0, self.new_string)

    def result(self):
        try:
            self.string = self.display.get()
            self.new_string = parser.expr(self.string).compile()
            self.result_string = eval(self.new_string)
            self.all_clear()
            self.display.insert(0, self.result_string)

        except ZeroDivisionError:
            self.all_clear()
            self.display.insert(0, "Can't divide by Zero")
        except Exception:
            self.all_clear()
            self.display.insert(0, "Error!")


    def factorial(self):
        try:
            self.num = int(self.display.get())
            fact = 1
            for x in range(self.num, 1, -1):
                fact *= x

            self.all_clear()
            self.display.insert(0, fact)

        except Exception:
            self.display.insert(0, "Error!")



cal_obj = Calculator()
cal_obj.screen()
cal_obj.numeric_buttons()
cal_obj.operator_buttons()

root.mainloop()


#   light mode operator color: ff5c33
#   dark mode operator color: 7293C6
