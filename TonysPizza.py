from tkinter import *
from tkinter.font import Font
from datetime import datetime, timedelta

root = Tk()
root.title("Tony's Pizza Order Form")
root.config(bg="#ffe599")


global regularCost
regularCost = 8.5
global gourmetCost
gourmetCost = 13.5
global deliveryCost
deliveryCost = 3
menuList = ["Cheese", "Pepperoni", "Meat Lovers", "Hawaiian", "BBQ Chicken", "Vegetable", "Mushroom", "Tuna (G)", "Triple Cheese (G)", "Margherita (G)", "Buffalo (G)", "Sausage (G)"] 
















findInvalids()
calcCost()
createInvoice()

root.mainloop()