from tkinter import *
from tkinter import ttk
from settings import *
import pydoodle


def main():
    Code1 = Code_1_Text.get("1.0", END)

    inpt = Input_Text.get("1.0", END)
    inpt = inpt.replace("\n", "||")

    output = Output_Text.get("1.0", END)
    Code_1_Result = c.execute(script=Code1, language=Code_1_Language.get().lower(), stdIn=inpt)
    if Code_1_Result.output[0] == output:
        Code_1_Result_Label.config(text="Passed", fg="Green")
    else:
        Code_1_Result_Label.config(text="Failed", fg="Red")
    Code2 = Code_2_Text.get("1.0", END)

    inpt = Input_Text.get("1.0", END)
    inpt = inpt.replace("\n", "||")

    output = Output_Text.get("1.0", END)

    Code_2_Result = c.execute(script=Code2, language=Code_2_Language.get().lower(), stdIn=inpt)
    if Code_2_Result.output[0] == output:
        Code_2_Result_Label.config(text="Passed", fg="Green")
    else:
        Code_2_Result_Label.config(text="Failed", fg="Red")

    t1 = Code_1_Result.cpuTime
    t2 = Code_2_Result.cpuTime
    if float(t1) > float(t2):
        Time_1.config(text=f"{t1} s", fg="Red")
        Time_2.config(text=f"{t2} s", fg="Green")
    elif float(t1) < float(t2):
        Time_1.config(text=f"{t1} s", fg="Green")
        Time_2.config(text=f"{t2} s", fg="Red")
    else:
        Time_1.config(text=f"{t1} s", fg="Yellow")
        Time_2.config(text=f"{t2} s", fg="Yellow")

    m1 = eval(Code_1_Result.memory)[0]
    m2 = eval(Code_2_Result.memory)[0]
    if float(m1) > float(m2):
        Space_1.config(text=f"{m1} Kb", fg="Red")
        Space_2.config(text=f"{m2} Kb", fg="Green")
    elif float(m1) < float(m2):
        Space_1.config(text=f"{m1} Kb", fg="Green")
        Space_2.config(text=f"{m2} Kb", fg="Red")
    else:
        Space_1.config(text=f"{m1} Kb", fg="Yellow")
        Space_2.config(text=f"{m2} Kb", fg="Yellow")

    root.title(f"PyCHEF ({(200-c.usage())//2} left)")


c = pydoodle.Compiler(clientId=client_id,clientSecret=client_secret)

root = Tk()
root.title(f"PyCHEF ({(200-c.usage())//2} left)")
root.geometry("1600x950")
root.minsize(1600 ,950)
root.maxsize(1600 ,950)
languages = [
    "Python3",
    "JAVA",
    "Cpp",
    "Cpp17",
    "C",
    "Kotlin",
    ]
Code_1_Frame = LabelFrame(
    root, text="Code 1", borderwidth=6, padx=290, pady=640)
Code_1_Frame.pack(side=LEFT, padx=20, pady=10)
Label(Code_1_Frame, text="").grid(row=0, column=0)
Code_1_Text = Text(root, width=65, height=50, bg="#ffffcc")
Code_1_Text.place(x=50, y=60)
Code_1_Result_Label = Label(root, text="")
Code_1_Result_Label.place(x=50, y=35)


Code_1_Language = ttk.Combobox(root, values=languages)
Code_1_Language.current(0)
Code_1_Language['state'] = 'readonly'
Code_1_Language.bind("<<ComboboxSelected>>")
Code_1_Language.pack(fill='none', expand='False')
Code_1_Language.place(x=200, y=35, height=20, width=118)


Code_2_Frame = LabelFrame(
    root, text="Code 2", borderwidth=6, padx=290, pady=640)
Code_2_Frame.pack(side=RIGHT, padx=20, pady=10)
Label(Code_2_Frame, text="").grid(row=0, column=0)
Code_2_Text = Text(root, width=65, height=50, bg="#ffffcc")
Code_2_Text.place(x=1018, y=60)
Code_2_Result_Label = Label(root, text="")
Code_2_Result_Label.place(x=1018, y=35)

Code_2_Language = ttk.Combobox(root, values=languages)
Code_2_Language.current(0)
Code_2_Language['state'] = 'readonly'
Code_2_Language.bind("<<ComboboxSelected>>")
Code_2_Language.pack(fill='none', expand='False')
Code_2_Language.place(x=1168, y=35, height=20, width=118)


Input_Frame = LabelFrame(root, text="Custom Input",
                        borderwidth=4, padx=150, pady=150)
Input_Frame.pack(pady=20)
Label(Input_Frame, text="").grid(row=0, column=0)
Input_Text = Text(root, width=34, height=17, bg="#ffffcc")
Input_Text.place(x=660, y=50)

Output_Frame = LabelFrame(root, text="Expected Output",
                        borderwidth=4, padx=150, pady=150)
Output_Frame.pack()
Label(Output_Frame, text="").grid(row=0, column=0)
Output_Text = Text(root, width=34, height=17, bg="#ffffcc")
Output_Text.place(x=660, y=420)


Go_Button = Button(root, text="GO", bg="#ff751a",
                activebackground="#ff751a", height=1, width=5, command=main)
Go_Button.place(x=750, y=750)

Time_1 = Label(root, text="", font=("Arial", 20))
Time_1.place(x=630, y=830)
Time_2 = Label(root, text="", font=("Arial", 20))
Time_2.place(x=860, y=830)

Space_1 = Label(root, text="", font=("Arial", 20))
Space_1.place(x=630, y=880)
Space_2 = Label(root, text="", font=("Arial", 20))
Space_2.place(x=860, y=880)

mainloop()
