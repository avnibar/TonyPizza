from tkinter import *
from tkinter.font import Font
from datetime import datetime, timedelta

root = Tk()
root.title("Tony's Pizza Order Form")
root.config(bg="#ffe599")
root.geometry("660x550")


global REGULAR_COST
REGULAR_COST = 8.5
global GOURMET_COST
GOURMET_COST = 13.5
global DELIVERY_COST
DELIVERY_COST = 3
menuList = ["Cheese", "Pepperoni", "Meat Lovers", "Hawaiian", "BBQ Chicken", "Vegetable", "Mushroom", "Tuna (G)", "Triple Cheese (G)", "Margherita (G)", "Buffalo (G)", "Sausage (G)"] 

global orderType
orderType = StringVar()

global pageFont
pageFont = Font(family = "Georgia")
global titleFont
titleFont = Font(family = "Georgia", size=20)
global underlineFont
underlineFont = Font(family = "Georgia")
underlineFont.configure(underline = True)


mainTitle = Label(root, text="Tony's Pizza Company", font=titleFont, bg="#ffe599")
mainTitle.place(x=0,y=0)

subTitle = Label(root, text="Order Form", font=titleFont, bg="#ffe599")
subTitle.place(x=0,y=35)

menuText = Label(root, text="Menu", font=underlineFont, bg="#ffe599")
menuText.place(x=5, y=130)

quantityText = Label(root, text="Quantity", font=underlineFont, bg="#ffe599")
quantityText.place(x=240,y=130)

for loop in range(0,12):
    pizzaVar = menuList[loop]
    if loop < 9:
        pizzaText = Label(root, text=str(loop+1)+".          "+pizzaVar, font=pageFont, bg="#ffe599")
    else:
        pizzaText = Label(root, text=str(loop+1)+".        "+pizzaVar, font=pageFont, bg="#ffe599")
    pizzaText.place(x=18, y=(loop*30 + 160))


shippingText = Label(root, text="Shipping Method:", font=pageFont, bg="#ffe599")
shippingText.place(x=340,y=200)

cInfoText = Label(root, text="Customer Info:", font=pageFont, bg="#ffe599")
cInfoText.place(x=430, y=240)

nameText = Label(root, text="Name:", font=pageFont, bg="#ffe599")
nameText.place(x=340,y=290)

addressText = Label(root, text="Address:", font=pageFont, bg="#ffe599")
addressText.place(x=340,y=340)

phoneText = Label(root, text="Phone Number:", font=pageFont, bg="#ffe599")
phoneText.place(x=340,y=390)

entry1 = Entry(root, borderwidth=3, width = 12, justify="center")
entry1.place(x=235,y=160)
entry1.insert(0, 0)
entry2 = Entry(root, borderwidth=3, width = 12, justify="center")
entry2.place(x=235,y=190)
entry2.insert(0, 0)
entry3 = Entry(root, borderwidth=3, width = 12, justify="center")
entry3.place(x=235,y=220)
entry3.insert(0, 0)
entry4 = Entry(root, borderwidth=3, width = 12, justify="center")
entry4.place(x=235,y=250)
entry4.insert(0, 0)
entry5 = Entry(root, borderwidth=3, width = 12, justify="center")
entry5.place(x=235,y=280)
entry5.insert(0, 0)
entry6 = Entry(root, borderwidth=3, width = 12, justify="center")
entry6.place(x=235,y=310)
entry6.insert(0, 0)
entry7 = Entry(root, borderwidth=3, width = 12, justify="center")
entry7.place(x=235,y=340)
entry7.insert(0, 0)
entry8 = Entry(root, borderwidth=3, width = 12, justify="center")
entry8.place(x=235,y=370)
entry8.insert(0, 0)
entry9 = Entry(root, borderwidth=3, width = 12, justify="center")
entry9.place(x=235,y=400)
entry9.insert(0, 0)
entry10 = Entry(root, borderwidth=3, width = 12, justify="center")
entry10.place(x=235,y=430)
entry10.insert(0, 0)
entry11 = Entry(root, borderwidth=3, width = 12, justify="center")
entry11.place(x=235,y=460)
entry11.insert(0, 0)
entry12 = Entry(root, borderwidth=3, width = 12, justify="center")
entry12.place(x=235,y=490)
entry12.insert(0, 0)

shippingOption = OptionMenu(root, orderType, "Delivery", "Pickup")
shippingOption.place(x=500,y=195)
shippingOption.config(font=pageFont, width=10)

nameEntry = Entry(root, borderwidth=3, width=23)
nameEntry.place(x=500,y=290)

addressEntry = Entry(root, borderwidth=3, width=23)
addressEntry.place(x=500,y=340)

phoneEntry = Entry(root, borderwidth=3, width=23)
phoneEntry.place(x=500,y=390)

def clearFields():
    entry1.delete(0, END)
    entry1.insert(0, 0)
    entry2.delete(0, END)
    entry2.insert(0, 0)
    entry3.delete(0, END)
    entry3.insert(0, 0)
    entry4.delete(0, END)
    entry4.insert(0, 0)
    entry5.delete(0, END)
    entry5.insert(0, 0)
    entry6.delete(0, END)
    entry6.insert(0, 0)
    entry7.delete(0, END)
    entry7.insert(0, 0)
    entry8.delete(0, END)
    entry8.insert(0, 0)
    entry9.delete(0, END)
    entry9.insert(0, 0)
    entry10.delete(0, END)
    entry10.insert(0, 0)
    entry11.delete(0, END)
    entry11.insert(0, 0)
    entry12.delete(0, END)
    entry12.insert(0, 0)
    return

def close():
    root.quit()
    return

def findInvalids():

    return

clearButton = Button(root, text="Clear", font=pageFont, bg="#e69138", fg="#ffffff", padx=18, pady=2, command=clearFields)
clearButton.place(x=340,y=450)

orderButton = Button(root, text="Order", font=pageFont, bg="#e69138", fg="#ffffff", padx=18, pady=2, command=findInvalids)
orderButton.place(x=442,y=450)

quitButton = Button(root, text="Quit", font=pageFont, bg="#e69138", fg="#ffffff", padx=18, pady=2, command=close)
quitButton.place(x=550,y=450)

root.mainloop()