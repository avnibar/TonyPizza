from tkinter import *
from tkinter.font import Font
from datetime import datetime, timedelta

root = Tk()
root.title("Tony's Pizza Order Form")
root.config(bg="#ffe599")
root.geometry("800x550")


global regularCost
regularCost = 8.5
global gourmetCost
gourmetCost = 13.5
global deliveryCost
deliveryCost = 3
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
    pizzaText = Label(root, text=str(loop+1)+".          "+pizzaVar, font=pageFont, bg="#ffe599")
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

entry1 = Entry(root, borderwidth=3, width = 12)
entry1.place(x=235,y=160)
entry2 = Entry(root, borderwidth=3, width = 12)
entry2.place(x=235,y=190)
entry3 = Entry(root, borderwidth=3, width = 12)
entry3.place(x=235,y=220)
entry4 = Entry(root, borderwidth=3, width = 12)
entry4.place(x=235,y=250)
entry5 = Entry(root, borderwidth=3, width = 12)
entry5.place(x=235,y=280)
entry6 = Entry(root, borderwidth=3, width = 12)
entry6.place(x=235,y=310)
entry7 = Entry(root, borderwidth=3, width = 12)
entry7.place(x=235,y=340)
entry8 = Entry(root, borderwidth=3, width = 12)
entry8.place(x=235,y=370)
entry9 = Entry(root, borderwidth=3, width = 12)
entry9.place(x=235,y=400)
entry10 = Entry(root, borderwidth=3, width = 12)
entry10.place(x=235,y=430)
entry11 = Entry(root, borderwidth=3, width = 12)
entry11.place(x=235,y=460)
entry12 = Entry(root, borderwidth=3, width = 12)
entry12.place(x=235,y=490)

shippingOption = OptionMenu(root, orderType, "Delivery", "Pickup")
shippingOption.place(x=380,y=200)
shippingOption.config(font=pageFont, width=20)

#findInvalids()
#calcCost()
#createInvoice()

root.mainloop()