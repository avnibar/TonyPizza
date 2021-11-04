from tkinter import *
from tkinter.font import Font
from datetime import datetime, timedelta

root = Tk()
root.title("Tony's Pizza Order Form")
root.config(bg="#ffe599")
root.geometry("640x360")


global regularCost
regularCost = 8.5
global gourmetCost
gourmetCost = 13.5
global deliveryCost
deliveryCost = 3
menuList = ["Cheese", "Pepperoni", "Meat Lovers", "Hawaiian", "BBQ Chicken", "Vegetable", "Mushroom", "Tuna (G)", "Triple Cheese (G)", "Margherita (G)", "Buffalo (G)", "Sausage (G)"] 


global pageFont
pageFont = Font(family = "Georgia")
global titleFont
titleFont = Font(family = "Georgia", size=15)
global underlineFont
underlineFont = Font(family = "Georgia")
underlineFont.configure(underline = True)


mainTitle = Label(root, text="Tony's Pizza Company", font=titleFont, bg="#ffe599")
mainTitle.place(x=0,y=0)

subTitle = Label(root, text="Order Form", font=titleFont, bg="#ffe599")
subTitle.place(x=0,y=25)

menuText = Label(root, text="Menu", font=underlineFont, bg="#ffe599")
menuText.place(x=5, y=140)

quantityText = Label(root, text="Quantity", font=underlineFont, bg="#ffe599")
quantityText.place(x=240,y=140)

cheeseText = Label(root, text="1.          Cheese", font=pageFont, bg="#ffe599")
cheeseText.place(x=18,y=160)

pepperoniText = Label(root, text="2.          Pepperoni", font=pageFont, bg="#ffe599")
pepperoniText.place(x=18,y=190)


#findInvalids()
#calcCost()
#createInvoice()

root.mainloop()