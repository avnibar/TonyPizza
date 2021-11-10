from tkinter import *
from tkinter.font import Font
from datetime import datetime, timedelta
import os
os.chdir('//internal.glendowie-college.school.nz/users/Home/Students/18222/Documents/prg python/12 PRG Avni')

root = Tk()
root.title("Tony's Pizza Order Form")
root.config(bg="#ffe599")
root.geometry("660x555")


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


shippingText = Label(root, text="Order Type:", font=pageFont, bg="#ffe599")
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

logoFile = PhotoImage(file="pizzaLogo.png")
logoInput = Label(root, image=logoFile, bg="#ffe599")
logoInput.place(x=460,y=20)

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
    nameEntry.delete(0, END)
    orderType.set("")
    addressEntry.delete(0, END)
    addressEntry.insert(0, "")
    phoneEntry.delete(0, END)
    phoneEntry.insert(0, "")
    return

def close():
    root.quit()
    return

def createInvoice():
    root2=Toplevel(root)
    root2.title("Tony's Pizza Customer Order")
    root2.configure(bg="#ffe599")
    root2.geometry("590x530")

    mainTitle = Label(root2, text="Tony's Pizza Company", font=titleFont, bg="#ffe599")
    mainTitle.place(x=72,y=0)
    subTitle = Label(root2, text="Processed Customer Order", font=titleFont, bg="#ffe599")
    subTitle.place(x=45,y=35)
    logoInput = Label(root2, image=logoFile, bg="#ffe599")
    logoInput.place(x=390,y=0)

    dateText = Label(root2, text="Date:",font=pageFont,bg="#ffe599")
    dateText.place(x=30,y=100)
    invDate = datetime.now()
    date = Label(root2, text=invDate.strftime("%d/%m/%y"), font=pageFont, bg="#ffe599")
    date.place(x=185,y=100)
    customerNameText = Label(root2, text="Customer Name:",font=pageFont,bg="#ffe599")
    customerNameText.place(x=30,y=130)
    customerName = Label(root2, text=nameEntry.get(), font=pageFont, bg="#ffe599")
    customerName.place(x=185,y=130)
    shippingText = Label(root2, text="Order Type:",font=pageFont,bg="#ffe599")
    shippingText.place(x=30,y=160)
    orderTypeText = Label(root2, text=orderType.get(),font=pageFont,bg="#ffe599")
    orderTypeText.place(x=185,y=160)
    if orderType.get() == "Delivery":
        addressText = Label(root2, text="Address:",font=pageFont,bg="#ffe599")
        addressText.place(x=30,y=190)
        customerAddress = Label(root2,text=addressEntry.get(),font=pageFont,bg="#ffe599")
        customerAddress.place(x=185,y=190)
        phoneText = Label(root2,text="Phone Number:",font=pageFont,bg="#ffe599")
        phoneText.place(x=30,y=220)
        customerPhoneNo = Label(root2,text=phoneEntry.get(),font=pageFont,bg="#ffe599")
        customerPhoneNo.place(x=185,y=220)
    embellishment = Label(root2, text="_____________________________________________________________________________________________________________________",bg="#ffe599")
    embellishment.place(x=0,y=245)
    itemHeader = Label(root2, text="Item",font=underlineFont,bg="#ffe599")
    itemHeader.place(x=40,y=275)
    qtyHeader = Label(root2, text="Qty",font=underlineFont,bg="#ffe599")
    qtyHeader.place(x=330,y=275)
    priceHeader = Label(root2, text="Price Per",font=underlineFont,bg="#ffe599")
    priceHeader.place(x=460,y=275)

    linecount = 1
    if int(entry1.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[0],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry1.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(REGULAR_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry2.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[1],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry2.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(REGULAR_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry3.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[2],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry3.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(REGULAR_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry4.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[3],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry4.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(REGULAR_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry5.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[4],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry5.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(REGULAR_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry6.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[5],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry6.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(REGULAR_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry7.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[6],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry7.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(REGULAR_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry8.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[7],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry8.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(GOURMET_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry9.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[8],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry9.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(GOURMET_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry10.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[9],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry10.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(GOURMET_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry11.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[10],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry11.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(GOURMET_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if int(entry12.get()) > 0:
        pizzaOutput = Label(root2,text=menuList[11],font=pageFont,bg="#ffe599")
        pizzaOutput.place(x=20,y=(275+(30*linecount)))
        qtyOutput = Label(root2,text=int(entry12.get()),font=pageFont,bg="#ffe599")
        qtyOutput.place(x=340,y=(275+(30*linecount)))
        priceOutput = Label(root2,text="$"+str(GOURMET_COST)+"0",font=pageFont,bg="#ffe599")
        priceOutput.place(x=470,y=(275+(30*linecount)))
        linecount+= 1
    if orderType.get() == "Delivery":
        deliveryText = Label(root2,text="Delivery Fee",font=pageFont,bg="#ffe599")
        deliveryText.place(x=20,y=(275+(30*linecount)))
        
    return


def calcCost():
    regularAmount = int(entry1.get()) + int(entry2.get()) + int(entry3.get()) + int(entry4.get()) + int(entry5.get()) + int(entry6.get()) + int(entry7.get())
    gourmetAmount = int(entry8.get()) + int(entry9.get()) + int(entry10.get()) + int(entry11.get()) + int(entry12.get())
    
    global totalCost
    totalCost = (regularAmount * REGULAR_COST) + (gourmetAmount * GOURMET_COST)
    if orderType.get() == "Delivery":
        totalCost += DELIVERY_COST

    createInvoice()
    return

def findInvalids():
    
    entry1Var = entry1.get()
    entry2Var = entry2.get()
    entry3Var = entry3.get()
    entry4Var = entry4.get()
    entry5Var = entry5.get()
    entry6Var = entry6.get()
    entry7Var = entry7.get()
    entry8Var = entry8.get()
    entry9Var = entry9.get()
    entry10Var = entry10.get()
    entry11Var = entry11.get()
    entry12Var = entry12.get()
    invalid = 0
    try:
        entry1Var = int(entry1Var)
        if (int(entry1Var) < 0) or (int(entry1Var) > 5):
            entry1.delete(0, END)
            entry1.insert(0, "Invalid")
            invalid = 1
    except:
        entry1.delete(0, END)
        entry1.insert(0, "Invalid")
        invalid = 1
    try:
        entry2Var = int(entry2Var)
        if (int(entry2Var) < 0) or (int(entry2Var) > 5):
            entry2.delete(0, END)
            entry2.insert(0, "Invalid")
            invalid = 1
    except:
        entry2.delete(0, END)
        entry2.insert(0, "Invalid")
        invalid = 1
    try:
        entry3Var = int(entry3Var)
        if (int(entry3Var) < 0) or (int(entry3Var) > 5):
            entry3.delete(0, END)
            entry3.insert(0, "Invalid")
            invalid = 1
    except:
        entry3.delete(0, END)
        entry3.insert(0, "Invalid")
        invalid = 1
    try:
        entry4Var = int(entry4Var)
        if (int(entry4Var) < 0) or (int(entry4Var) > 5):
            entry4.delete(0, END)
            entry4.insert(0, "Invalid")
            invalid = 1
    except:
        entry4.delete(0, END)
        entry4.insert(0, "Invalid")
        invalid = 1
    try:
        entry5Var = int(entry5Var)
        if (int(entry5Var) < 0) or (int(entry5Var) > 5):
            entry5.delete(0, END)
            entry5.insert(0, "Invalid")
            invalid = 1
    except:
        entry5.delete(0, END)
        entry5.insert(0, "Invalid")
        invalid = 1
    try:
        entry6Var = int(entry6Var)
        if (int(entry6Var) < 0) or (int(entry6Var) > 5):
            entry6.delete(0, END)
            entry6.insert(0, "Invalid")
            invalid = 1
    except:
        entry6.delete(0, END)
        entry6.insert(0, "Invalid")
        invalid = 1
    try:
        entry7Var = int(entry7Var)
        if (int(entry7Var) < 0) or (int(entry7Var) > 5):
            entry7.delete(0, END)
            entry7.insert(0, "Invalid")
            invalid = 1
    except:
        entry7.delete(0, END)
        entry7.insert(0, "Invalid")
        invalid = 1
    try:
        entry8Var = int(entry8Var)
        if (int(entry8Var) < 0) or (int(entry8Var) > 5):
            entry8.delete(0, END)
            entry8.insert(0, "Invalid")
            invalid = 1
    except:
        entry8.delete(0, END)
        entry8.insert(0, "Invalid")
        invalid = 1
    try:
        entry9Var = int(entry9Var)
        if (int(entry9Var) < 0) or (int(entry9Var) > 5):
            entry9.delete(0, END)
            entry9.insert(0, "Invalid")
            invalid = 1
    except:
        entry9.delete(0, END)
        entry9.insert(0, "Invalid")
        invalid = 1
    try:
        entry10Var = int(entry10Var)
        if (int(entry10Var) < 0) or (int(entry10Var) > 5):
            entry10.delete(0, END)
            entry10.insert(0, "Invalid")
            invalid = 1
    except:
        entry10.delete(0, END)
        entry10.insert(0, "Invalid")
        invalid = 1
    try:
        entry11Var = int(entry11Var)
        if (int(entry11Var) < 0) or (int(entry11Var) > 5):
            entry11.delete(0, END)
            entry11.insert(0, "Invalid")
            invalid = 1
    except:
        entry11.delete(0, END)
        entry11.insert(0, "Invalid")
        invalid = 1
    try:
        entry12Var = int(entry12Var)
        if (int(entry12Var) < 0) or (int(entry12Var) > 5):
            entry12.delete(0, END)
            entry12.insert(0, "Invalid")
            invalid = 1
    except:
        entry12.delete(0, END)
        entry12.insert(0, "Invalid")
        invalid = 1

    global pizzaAmount
    pizzaAmount = int(entry1.get()) + int(entry2.get()) + int(entry3.get()) + int(entry4.get()) + int(entry5.get()) + int(entry6.get()) + int(entry7.get()) + int(entry8.get()) + int(entry9.get()) + int(entry10.get()) + int(entry11.get()) + int(entry12.get())
    
    if (pizzaAmount > 5) or (pizzaAmount < 1):
        invalid = 1
        errorText = Label(root, text="Invalid Pizza Amount.", bg="#ffe599", font=pageFont, fg="#ff0000")
        errorText.place(x=410,y=500)

    if (nameEntry.get() == "") or (nameEntry.get() == "Please Enter Name"):
        nameEntry.delete(0, END)
        nameEntry.insert(0, "Please Enter Name")
        invalid = 1

    if orderType.get() == "Delivery":
        if phoneEntry.get() == "":
            phoneEntry.insert(0, "Invalid Phone Number")
            invalid = 1
        if addressEntry.get() == "":
            addressEntry.insert(0, "Invalid Shipping Address")
            invalid = 1
    elif orderType.get() == "":
        errorText2 = Label(root, text="Please Select Order Type.", bg="#ffe599", font=pageFont, fg="#ff0000")
        errorText2.place(x=390,y=530)

    if invalid != 1:
        calcCost()
        return

clearButton = Button(root, text="Clear", font=pageFont, bg="#e69138", fg="#ffffff", padx=18, pady=2, command=clearFields)
clearButton.place(x=340,y=450)

orderButton = Button(root, text="Order", font=pageFont, bg="#e69138", fg="#ffffff", padx=18, pady=2, command=findInvalids)
orderButton.place(x=442,y=450)

quitButton = Button(root, text="Quit", font=pageFont, bg="#e69138", fg="#ffffff", padx=18, pady=2, command=close)
quitButton.place(x=550,y=450)

root.mainloop()