import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    #save user data
    accepted = accept_var.get()
    if accepted == "Accepted":  #Condition to ensure that the correct info enttered checkbox is ticked
        firstname=first_name_entry.get()
        lastname=last_name_entry.get()

        if firstname and lastname: #condition to ensure first name and last name are entered
            title=title_combobox.get()
            age=age_spinbox.get()
            ethnicity=ethnicity_combobox.get()

            print("----------------------------------------------------")
            print("First Name:", firstname, "Last Name:", lastname)
            print("Title:", title, "Age:", age, "Ethnicity:", ethnicity)
            print("----------------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="First Name and Last Name not entered")
    else:
        tkinter.messagebox.showwarning(title="Error", message="Correct information checkbox not ticked")

window = tkinter.Tk()
window.title("User Data Entry Form")

frame =tkinter.Frame(window)
frame.pack()

#saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User information")
user_info_frame.grid(row= 0, column=0 )

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0, padx=10,pady=10)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title=tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr","Mrs","Ms","Dr"])
title.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_lable = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=16, to=100)
age_lable.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

ethnicity_label = tkinter.Label(user_info_frame ,text="Ehnicity")
ethnicity_combobox = ttk.Combobox(user_info_frame, values=["African","White","Indian","Colored","Asian"])
ethnicity_label.grid(row=2,column=1)
ethnicity_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Validate info
validate_info=tkinter.LabelFrame(frame, text="Validate information")
validate_info.grid(row=1, column=0, sticky="news", padx=10, pady=10)

accept_var = tkinter.StringVar(value= "Not Accepted" )
validate_check = tkinter.Checkbutton(validate_info, text="Correct Infomation entered",
                                     variable=accept_var, onvalue="Accepted", offvalue="Not accepted")
validate_check.grid(row=0, column=0)

#Button
button = tkinter.Button(frame, text="Enter Data", command= enter_data)
button.grid(row=2, column=0, sticky="news", padx=10, pady=10)

window.mainloop()