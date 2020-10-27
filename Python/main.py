import tkinter as tk
from tkinter import font

import config


class Application(tk.Tk): # Application Class Object
    def __init__(self):
        super().__init__() # Superclass (tk.Tk)
        
        self.title(f"{config.PROGRAM_NAME} | {config.BUILD_VERSION} | By {config.AUTHOR}") # Window Title
        self.geometry("400x600") # Window Size (Template)
        self.resizable(0, 0) # not Resizable
        
        # Fonts
        self.hel15b = font.Font(family="Helvetica", size=15, weight="bold") # Font (Helvetica, 15, Bold)
        self.hel30b = font.Font(family="Helvetica", size=30, weight="bold") # Font (Helvetica, 30, Bold)
        self.sys20bu = font.Font(family="system", size=20, weight="bold", underline=1) # Font (system, 20, Bold, Underline)

    def __repr__(self):
        __name = self.__class__
        __type = type(self)
        __module = type.__module__
        __qualname = type.__qualname__

        return f"""\
        Class Name: {__name}
        Class Details: {config.PROGRAM_NAME}

        Build Version: {config.BUILD_VERSION}
        Author: {config.AUTHOR}
        
        Class Type: {__type}
        Class Module: {__module}
        Class Qualname: {__qualname}
        """


class Main(Application): # Main Window
    def __init__(self):
        super().__init__() # Superclass (Application)

        # Window Contents
            # Result Box
        self.result_box = tk.Text(self, bg="gray75", width=35, height=4, borderwidth=3, relief="raised", font=self.hel15b, state="disabled")
        self.result_box.place(x=5, y=5, anchor="nw")

            # Number Buttons
        self.button_0 = tk.Button(self, text="0", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_0)
        self.button_0.place(x=5, y=480)

        self.button_1 = tk.Button(self, text="1", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_1)
        self.button_1.place(x=5, y=360)

        self.button_2 = tk.Button(self, text="2", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_2)
        self.button_2.place(x=95, y=360)

        self.button_3 = tk.Button(self, text="3", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_3)
        self.button_3.place(x=185, y=360)

        self.button_4 = tk.Button(self, text="4", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_4)
        self.button_4.place(x=5, y=240)

        self.button_5 = tk.Button(self, text="5", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_5)
        self.button_5.place(x=95, y=240)

        self.button_6 = tk.Button(self, text="6", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_6)
        self.button_6.place(x=185, y=240)

        self.button_7 = tk.Button(self, text="7", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_7)
        self.button_7.place(x=5, y=120)

        self.button_8 = tk.Button(self, text="8", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_8)
        self.button_8.place(x=95, y=120)

        self.button_9 = tk.Button(self, text="9", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_9)
        self.button_9.place(x=185, y=120)

            # Other Buttons
        self.button_point = tk.Button(self, text=".", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_point)
        self.button_point.place(x=95, y=480)

            # Action Buttons
        self.button_equals = tk.Button(self, text="=", width=6, height=4, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_calculate)
        self.button_equals.place(x=185, y=480)
        
        self.button_plus = tk.Button(self, text="+", width=9, height=2, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_add)
        self.button_plus.place(x=275, y=527)

        self.button_minus = tk.Button(self, text="-", width=9, height=2, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_subtract)
        self.button_minus.place(x=275, y=455)
        
        self.button_times = tk.Button(self, text="×", width=9, height=2, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_multiply)
        self.button_times.place(x=275, y=383)

        self.button_divide = tk.Button(self, text="÷", width=9, height=2, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_divide)
        self.button_divide.place(x=275, y=311)

        self.button_del = tk.Button(self, text="DEL", width=9, height=2, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_delete)
        self.button_del.place(x=275, y=239)

        self.button_ac = tk.Button(self, text="AC", width=9, height=2, borderwidth=2, relief="raised", font=self.hel15b, bg="gray85", command=self.action_ac)
        self.button_ac.place(x=275, y=167)
        
        self.theme_slider = tk.Scale(self, from_=0, to=1, width=10, length=112, orient="horizontal", bg="gray85", borderwidth=2, relief="raised", command=self.update_theme)
        self.theme_slider.place(x=275, y=120)
        
            # Keys Pressed
        self.bind("<Key>", self.key_pressed) # Check for Keys
        self.bind("<Return>", self.enter_pressed) # Check for Return/Enter Key

        self.bind("<Delete>", self.delete_pressed) # Check for Delete Key
        self.bind("<Shift-BackSpace>", self.delete_pressed) ## Check for Shift+BackSpace Keys

        self.bind("<BackSpace>", self.backspace_pressed) # Check for BackSpace Key

    def move_window(self, event): # Moves Window
        self.geometry("+{0}+{1}".format(event.x_root, event.y_root))

    def update_theme(self, new_value): # Updates theme based on slider values TODO
        if new_value == "0": # Light Theme
            self.configure(bg="white")
            self.result_box.configure(bg="gray75", fg="black")

            self.button_0.configure(bg="gray85", fg="black")
            self.button_1.configure(bg="gray85", fg="black")
            self.button_2.configure(bg="gray85", fg="black")
            self.button_3.configure(bg="gray85", fg="black")
            self.button_4.configure(bg="gray85", fg="black")
            self.button_5.configure(bg="gray85", fg="black")
            self.button_6.configure(bg="gray85", fg="black")
            self.button_7.configure(bg="gray85", fg="black")
            self.button_8.configure(bg="gray85", fg="black")
            self.button_9.configure(bg="gray85", fg="black")
            self.button_point.configure(bg="gray85", fg="black")
            self.button_equals.configure(bg="gray85", fg="black")
            self.button_plus.configure(bg="gray85", fg="black")
            self.button_minus.configure(bg="gray85", fg="black")
            self.button_times.configure(bg="gray85", fg="black")
            self.button_divide.configure(bg="gray85", fg="black")
            self.button_del.configure(bg="gray85", fg="black")
            self.button_ac.configure(bg="gray85", fg="black")
            self.theme_slider.configure(bg="gray85", fg="black")
        elif new_value == "1": # Dark Theme
            self.configure(bg="gray15")
            self.result_box.configure(bg="gray15", fg="white")

            self.button_0.configure(bg="gray25", fg="white")
            self.button_1.configure(bg="gray25", fg="white")
            self.button_2.configure(bg="gray25", fg="white")
            self.button_3.configure(bg="gray25", fg="white")
            self.button_4.configure(bg="gray25", fg="white")
            self.button_5.configure(bg="gray25", fg="white")
            self.button_6.configure(bg="gray25", fg="white")
            self.button_7.configure(bg="gray25", fg="white")
            self.button_8.configure(bg="gray25", fg="white")
            self.button_9.configure(bg="gray25", fg="white")
            self.button_point.configure(bg="gray25", fg="white")
            self.button_equals.configure(bg="gray25", fg="white")
            self.button_plus.configure(bg="gray25", fg="white")
            self.button_minus.configure(bg="gray25", fg="white")
            self.button_times.configure(bg="gray25", fg="white")
            self.button_divide.configure(bg="gray25", fg="white")
            self.button_del.configure(bg="gray25", fg="white")
            self.button_ac.configure(bg="gray25", fg="white")
            self.theme_slider.configure(bg="gray25", fg="white")

    def key_pressed(self, event): # Execute action for each key pressed on keyboard
        if event.char == "0":
            self.action_0()
        elif event.char == "1":
            self.action_1()
        elif event.char == "2":
            self.action_2()
        elif event.char == "3":
            self.action_3()
        elif event.char == "4":
            self.action_4()
        elif event.char == "5":
            self.action_5()
        elif event.char == "6":
            self.action_6()
        elif event.char == "7":
            self.action_7()
        elif event.char == "8":
            self.action_8()
        elif event.char == "9":
            self.action_9()
        elif event.char == ".":
            self.action_point()
        elif event.char == "=":
            self.action_calculate()
        elif event.char == "+":
            self.action_add()
        elif event.char == "-":
            self.action_subtract()
        elif event.char == "*" or event.char == "×":
            self.action_multiply()
        elif event.char == "/" or event.char == "÷":
            self.action_divide()

    def enter_pressed(self, event): # Execute action for ENTER key
        self.action_calculate()

    def backspace_pressed(self, event): # Execute action for BACKSPACE key
        self.action_delete()

    def delete_pressed(self, event): # Execute action for DELETE key
        self.action_ac()

    def get_last_value(self): # Return last value
        list_of_values = list(self.result_box.get("1.0", "end"))
        try:
            return list_of_values[-2]
        except IndexError:
            return None

    def action_delete(self): # Delete last value
        try:
            self.items = self.result_box.get("1.0", "end")
            self.items = self.items.rstrip("\n")
            self.items = list(self.items)
            self.items.pop()
            self.items = "".join(self.items)
        
            self.result_box.configure(state="normal")
            self.result_box.delete("1.0", "end")
            self.result_box.insert("1.0", self.items)
            self.result_box.configure(state="disabled")
        except:
            pass

    def action_calculate(self):
        try:
            self.to_calculate = self.result_box.get("1.0", "end")

            self.to_calculate = self.to_calculate.replace(" ", "") 
            self.to_calculate = self.to_calculate.replace("×", "*")
            self.to_calculate = self.to_calculate.replace("÷", "/")
            self.to_calculate = self.to_calculate.rstrip("\n")
            
            # print(list(self.to_calculate))

            if self.to_calculate != "":
                self.result = eval(self.to_calculate)
            
                self.action_ac()
                self.result_box.configure(state="normal")
                self.result_box.insert("1.0", self.result)
                self.result_box.configure(state="disabled")
        except Exception as e:
            # print(f"Syntax ERROR: {e}")
            self.action_ac()
            self.result_box.configure(state="normal")
            self.result_box.insert("1.0", "Syntax ERROR | [AC]: Cancel")
            self.result_box.configure(state="disabled")

    def action_ac(self):
        self.result_box.configure(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.configure(state="disabled")

    def action_0(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "0")
        self.result_box.configure(state="disabled")

    def action_1(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "1")
        self.result_box.configure(state="disabled")

    def action_2(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "2")
        self.result_box.configure(state="disabled")

    def action_3(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "3")
        self.result_box.configure(state="disabled")

    def action_4(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "4")
        self.result_box.configure(state="disabled")

    def action_5(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "5")
        self.result_box.configure(state="disabled")

    def action_6(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "6")
        self.result_box.configure(state="disabled")

    def action_7(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "7")
        self.result_box.configure(state="disabled")

    def action_8(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "8")
        self.result_box.configure(state="disabled")

    def action_9(self):
        self.result_box.configure(state="normal")
        self.result_box.insert("end", "9")
        self.result_box.configure(state="disabled")

    def action_point(self):
        if self.get_last_value() != ".":
            self.result_box.configure(state="normal")
            self.result_box.insert("end", ".")
            self.result_box.configure(state="disabled")

    def action_add(self):
        if self.get_last_value() != "×" and self.get_last_value() != "÷":
            self.result_box.configure(state="normal")
            self.result_box.insert("end", "+")
            self.result_box.configure(state="disabled")

    def action_subtract(self):
        if self.get_last_value() != "×" and self.get_last_value() != "÷":
            self.result_box.configure(state="normal")
            self.result_box.insert("end", "-")
            self.result_box.configure(state="disabled")
    
    def action_multiply(self):
        if self.get_last_value() != "×" and self.get_last_value() != "÷" and self.get_last_value() != "+" and self.get_last_value() != "-":
            self.result_box.configure(state="normal")
            self.result_box.insert("end", "×")
            self.result_box.configure(state="disabled")

    def action_divide(self):
        if self.get_last_value() != "÷" and self.get_last_value() != "×" and self.get_last_value() != "+" and self.get_last_value() != "-":
            self.result_box.configure(state="normal")
            self.result_box.insert("end", "÷")
            self.result_box.configure(state="disabled")

          
def setup(): # Main Menu Setup
    main = Main() # Main Menu Window (init)
    main.mainloop() # Window Loop


if __name__ == "__main__": # If Program is run directly...
    setup() # App Setup