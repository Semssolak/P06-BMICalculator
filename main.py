from tkinter import *

my_window = Tk()
my_window.title("BMI Calculator")
my_window.minsize(width=200,height=200)
my_window.config(background="black")

my_weight = Label(text="Enter Your Weight(kg)")
my_weight.grid(row=0, column=3, padx=30, pady=5)
my_weight.config(background="black",foreground="white")


my_entry = Entry(width=15)
my_entry.grid(row=2,column=3,padx=30,pady=5)


my_height = Label(text="Enter Your Height(cm)")
my_height.grid(row=4, column=3, padx=30, pady=5)
my_height.config(background="black",foreground="white")


my_entry_2 = Entry(width=15)
my_entry_2.grid(row=6,column=3,padx=30,pady=5)

def calculator():
    weight_str = my_entry.get()
    height_str = my_entry_2.get()
    if not weight_str or not height_str:  #kullanıcı değer girmesse
        # veya buraya if weight_Str == "" or height_str == "" da yapabilirdik
        message = "Please enter both weight and height."
    elif not weight_str.isnumeric() or not height_str.isnumeric(): # kullanıcı sayısal değer girmese
        # bu kısım yerine kullanılabilecek şey ise else içinde try except kullanıp except kısmına bu mesajı yazarız
        message = "Please enter valid numeric values for weight and height."
    else:
        weight = float(weight_str)
        height = float(height_str)
        BMIndex = round(weight / ((height / 100) ** 2),2) #sadece virgülden sonra 2 basamak kalacak şekilde yuvarla
        if BMIndex < 16.0:
            message = f"Your BMI is {BMIndex}.You are Severely Underweight"
        elif BMIndex < 18.4:
            message = f"Your BMI is {BMIndex}.You are Underweight"
        elif BMIndex < 24.9:
            message = f"Your BMI is {BMIndex}.You are Normal"
        elif BMIndex < 29.9:
            message = f"Your BMI is {BMIndex}.You are Overweight"
        elif BMIndex < 34.9:
            message = f"Your BMI is {BMIndex}.You are Moderately Obese"
        elif BMIndex < 39.9:
            message = f"Your BMI is {BMIndex}.You are Severaly Obese"
        elif BMIndex >= 40.0:
            message = f"Your BMI is {BMIndex}.You are Morbidly Obese"
    my_label.config(text=message)

my_button = Button(text="Calculate",command=calculator)
my_button.grid(row=8,column=3,padx=30,pady=5)
my_button.config(background="gray",foreground="black")

my_label = Label(text="")
my_label.grid(row=10,column=3,padx=30,pady=5)
my_label.config(background="black",foreground="white")


my_window.mainloop()