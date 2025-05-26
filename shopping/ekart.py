from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk,Image
import datetime as dt
from tkinter import filedialog
today = dt.datetime.now()

shop = Tk()
shop.geometry("1000x1000")
shop.title("Ekart")
shop.config(bg="Aqua")


# function to print receipt
def checkout(delivery_address,method):
    amount=0
    # messagebox to ask user to continue or quit shopping
    end=messagebox.askyesno("Receipt", "order receipt saved as \"orderbills\" \n Continue Shopping")
    # creating and writing Invoice
    f = open("orderbills.txt", "w")
    # entering predetermined format
    f.write( f"""                          \t\t\tEcart-Invoice
    To: {delivery_address}   
    date:{today:%A, %B %d, %Y}
    orderNO:89463hhf
    payment mode:{method}\n
products\t\tprice\t\tquantity\t\tamount\n """)
    # set pricing and total amount for the products in cart list
    for product,quantity in cart:

        if product == 'apple':
            amt = 200*int(quantity)
            price = 200
        if product == 'orange':
            amt = 140*int(quantity)
            price = 140
        if product == 'tomato':
            amt = 25*int(quantity)
            price = 25
        if product == 'potato':
            amt = 50*int(quantity)
            price = 50
        if product == 'rice':
            amt = 40*int(quantity)
            price = 40
        # total amount
        amount += amt
        f.write(f"{product}\t\t{price}\t\t{quantity}\t\t{amt}\n ")
    f.write(f"\n\t\t\t\ttotal\t\t{amount}")
    # continue or quit shopping based on user choice
    if end==True:
        # destroy previous frame(page)
        payment.pack_forget()
        # calling main page to shop again
        main()
    else:
        # closing window
        shop.quit()


# function for selecting payment method
def payments(deliver):
    global payment
    place=deliver
    d=StringVar()
    # destroy previous page to set new page
    setaddress.pack_forget()
    # set default radio button value to 'none'
    d.set("none")
    # creating new frame (page)
    payment=Frame(shop)
    payment.pack(fill="both",expand=1)
    Label(payment,text="Select payment method",font=("Times New Roman",15,'bold')).pack(anchor="nw",pady=5)
    # labelframe for payment method 1
    gpay=LabelFrame(payment,pady=20)
    gpay.pack(anchor=W,fill=X,pady=5)
    # Radiobutton to select payment 1
    Radiobutton(gpay,variable=d,value="Gpay",text="Gpay-   select to pay using Gpay").pack(anchor=S,expand=1,pady=10)
    # labelframe for payment method 2
    paytm=LabelFrame(payment,pady=20)
    paytm.pack(anchor=W,fill=X,pady=5)
    # Radiobutton to select payment 2
    Radiobutton(paytm,variable=d,value="Paytm", text="Paytm-   select to pay using Paytm").pack(side=LEFT,expand=1,pady=10)
    # labelframe for payment method 3
    card=LabelFrame(payment,pady=20)
    card.pack(anchor=W,fill=X,pady=5)
    # Radiobutton to select payment 3
    Radiobutton(card,variable=d,value="Card",text="Debit/Credit card-select to pay").pack(side=LEFT,expand=1,pady=10)
    # labelframe for payment method 4
    cashondelivery=LabelFrame(payment,pady=20)
    cashondelivery.pack(anchor=W,fill=X,pady=5)
    # Radiobutton to select payment 4
    Radiobutton(cashondelivery,variable=d,value="COD",text="Cash on delivery").pack(side=LEFT,expand=1,pady=10)
    # Button to finish purchase
    Button(payment, text="Place order",font=("Times New Roman", 12, 'bold'), bg="yellow",padx=5,pady=5, fg="red", command=lambda toplace=place:checkout(toplace,d.get())).pack(anchor=SE, pady=5, padx=10)


# function to set delivery address for shipping
def newaddress(temp,choose):
    # global variable to store shipping address to print in order receipt
    # global deliver
    # temp=  selected address,choose= radio button value
    def setdeliver():
        # get and store values from the textbox
        new_address = textbox.get(1.0, END)
        new_address = new_address.replace('\n',',').strip(",")

        # button to send stored new address as delivery address
        process.config(bg="yellow",command=lambda delivery= new_address: payments(delivery))

    # check whether 3rd radio button is clicked
    if choose == 3:
        # creating textbox to store new address
        textbox=Text(new,height=10,width=30)
        textbox.pack(side=LEFT,anchor="w",expand=1)
        # Button to get and store textbox values using setdeliver function
        Button(textbox,text="Set",command=setdeliver,padx=3,bg="green").place(x=210,y=130)
    else:
        # set deliver address if first two radio button got clicked
        deliver = temp.replace('\n','')
        # calling payments function for next page
        process.config(bg="yellow",command=lambda delivery=deliver: payments(delivery))


# function to select shipping address
def address():
    # globally declaring the variables to be used in other functions
    global r
    global new
    global setaddress
    global process
    # declaring integer variable to store Radiobutton values
    r = IntVar()
    # destroy previous frame(page)
    bag.pack_forget()
    # creating new frame(page) for selecting address
    setaddress=Frame(shop)
    setaddress.pack(fill="both",expand=1)
    Label(setaddress,text="Select a delivery address:",font=("Times New Roman",15,'bold')).pack(anchor="nw")
    # create labelframe for home address
    homead=LabelFrame(setaddress,text="Home address",pady=10)
    homead.pack(anchor=W,fill=X,pady=20)
    # initially setting default Radiobutton value to 0
    r.set(0)
    # variable to store home address
    homdeliver="""41/1, 41/1, Karunasagar Industrial EsNaroda Road,\nGujarat,\n380025"""
    # set delivery address by calling newaddress function when clicked
    Radiobutton(homead,text=homdeliver,variable=r,value=1,font=("Times New Roman",12,'bold'),command=lambda temp=homdeliver: newaddress(temp,1)).pack(side=LEFT,fill="x",expand=1)
    # label frame for office/work address
    officead = LabelFrame(setaddress, text="office address",pady=10)
    officead.pack(anchor=W,fill=X,pady=20)
    # variable to store office address
    offdeliver = """Sufi Chambers, Road No 1,\n Banjara Hills, \nHyderabad-\n500034"""
    # set delivery address by calling newaddress function when clicked
    Radiobutton(officead, text=offdeliver,variable=r, value=2, font=("Times New Roman", 12, 'bold'),command=lambda temp=offdeliver: newaddress(temp,2)).pack(side=LEFT,fill="x", expand=1)
    # label frame for user to add new address
    new=LabelFrame(setaddress,pady=10)
    new.pack(anchor=W,fill=X,pady=20)
    # calling new address to allow user to enter new address
    Radiobutton(new,text="Add new address:",variable=r,value=3,font=("Times New Roman", 12, 'bold'),command=lambda temp="none": newaddress(temp,3)).pack(side=LEFT, expand=1)
    # button to proceed next step in ordering product
    # inactive until any of the radiobutton got selected
    process=Button(setaddress,text="Next",bg="grey",fg="red",font=("Times New Roman", 12, 'bold'),padx=5,pady=5)
    process.pack(anchor=SE,pady=5,padx=5)

# function for cart page to show customer selected product
def checkcart():
    global bag
    global appleimg
    global orangeimg
    global tomatoimg
    global potatoimg
    global riceimg
    # destroy the previous Frame(page)
    main_frame.pack_forget()
    # create new frame(page) bag displaying user selected products
    bag = Frame(shop)
    bag.pack(fill="both",expand=1)
    # labeling fields  in grid format
    Label(bag,text="",fg="red",font=("Times New Roman",25,'bold')).grid(row=1,column=0,padx=30,pady=10)
    Label(bag,text="product",fg="red",font=("Times New Roman",25,'bold')).grid(row=1,column=1,padx=30,pady=10)
    Label(bag, text="quantity",fg="blue", font=("Times New Roman", 25, 'bold')).grid(row=1, column=2,padx=30,pady=10)
    Label(bag, text="Price",fg="green", font=("Times New Roman", 25, 'bold')).grid(row=1, column=3,padx=30,pady=10)
    Label(bag, text="amount",fg="orange", font=("Times New Roman", 25, 'bold')).grid(row=1, column=4,padx=30,pady=10)
    # variable to point out next row
    next=2
    # variable to store total amount
    amount=0
    nxt=0
    # getting product and quantity details from cart List
    for prod, quantity in cart:
        # assign product price,image,amount for each product if available in the cart
        if prod == 'apple':
            # resizing product image
            locate="download.png"
            temp = Image.open(locate)
            resize = temp.resize((50, 50))
            appleimg = ImageTk.PhotoImage(resize)
            price = 200
            # amount for the selected product
            amt = price * int(quantity)
            Label(bag, image=appleimg).grid(row=next, column=0, padx=10, pady=20)
        # repeat the above process for all products available
        if prod == 'orange':
            locate="orange3.jpg"
            temp1 = Image.open(locate)
            resize = temp1.resize((50, 50))
            orangeimg = ImageTk.PhotoImage(resize)
            price = 140
            amt = price * int(quantity)
            Label(bag, image=orangeimg).grid(row=next, column=0, padx=10, pady=20)

        if prod == 'tomato':
            locate = "tomato.jpg"
            temp2 = Image.open(locate)
            resize = temp2.resize((50, 50))
            tomatoimg = ImageTk.PhotoImage(resize)
            price = 25
            amt = price * int(quantity)
            Label(bag, image=tomatoimg).grid(row=next, column=0, padx=10, pady=20)

        if prod == 'potato':
            locate = "potato.jpg"
            temp3 = Image.open(locate)
            resize = temp3.resize((50, 50))
            potatoimg = ImageTk.PhotoImage(resize)
            price = 50
            amt = price * int(quantity)
            Label(bag, image=potatoimg).grid(row=next, column=0, padx=10, pady=20)

        if prod == 'rice':
            locate = "rice.jpg"
            temp4 = Image.open(locate)
            resize = temp4.resize((50, 50))
            riceimg = ImageTk.PhotoImage(resize)
            price = 40
            amt = 40 * int(quantity)
            Label(bag, image=riceimg).grid(row=next, column=0, padx=10, pady=20)
        # display every product available in the cart
        # place the product details in the format of product,quantity,price,amount
        Label(bag, text=prod, font=("Times New Roman", 12, 'bold')).grid(row=next, column=1, padx=10,pady=20)
        Label(bag, text=quantity, font=("Times New Roman", 12, 'bold')).grid(row=next, column=2, padx=30,pady=20)
        Label(bag, text=price, font=("Times New Roman", 12, 'bold')).grid(row=next, column=3, padx=30,pady=20)
        Label(bag, text=amt, font=("Times New Roman", 12, 'bold')).grid(row=next, column=4, padx=30,pady=20)
        # variable to place products in the new line
        next+=1
        # total amount - by adding all the amount(price*quantity) of products
        amount+=amt
    # placing  total amount and 'Next' button in new rows
    nxt = next + 1
    Label(bag, bg="aqua",text="click next -->", font=("Times New Roman", 15, 'bold')).grid(row=nxt, column=0, padx=10,)
    Label(bag,text="Total",bg="yellow",fg="green",font=("Times New Roman", 15, 'bold')).grid(row=next, column=3, padx=30)
    Label(bag,text=amount, bg="yellow",fg="red",font=("Times New Roman", 15, 'bold')).grid(row=next, column=4, padx=30)
    # button to proceed next step in ordering the products
    # calling address function to select shipping address
    Button(bag, text="Next", font=("ariel",15), bg="aqua",fg="red",command= address).grid(row=nxt,column=4,padx=30,pady=30)


# function to add product,quantity into cart list
def addcart(item,quantity):
    # adding products into cart list
    cart .append((item,quantity))
    # disable 'add' button for product after it clicked
    if item == 'apple':
        # change button text into 'Added' after product added into cart
        added.config(text="Added",bg="Lightgreen",state=DISABLED)
        display1.config(state=DISABLED)
    elif item == "orange":
        added1.config(text="Added", bg="Lightgreen", state=DISABLED)
        display2.config(state=DISABLED)
    elif item == "tomato":
        added2.config(text="Added", bg="Lightgreen", state=DISABLED)
        display3.config(state=DISABLED)
    elif item == "potato":
        added3.config(text="Added", bg="Lightgreen", state=DISABLED)
        display4.config(state=DISABLED)
    elif item == "rice":
        added4.config(text="Added", bg="Lightgreen", state=DISABLED)
        display5.config(state=DISABLED)
    # enable checkout button atleast one product get added
    if len(cart)>0:
        check.config(state=NORMAL,bg="yellow")
        # indicate number of product in the cart
        items.config(text=len(cart),bg="yellow")


# function to update product  quantity in the display
def adding(prod,count):
    # check which product quantity get updated
    # display1- product 1 display to show quantity
    if prod == "display1":
        # get and store previous values in display
        co = int(display1.get())
        # adding previous values and current value
        co = co+count
        # restrict value update in display if negative value is entered
        if co > -1:
            display1.delete(0,END)
            display1.insert(END, co)
            # get and send product and its quantity to cart using addcart function
            added.config(command=lambda qt=display1.get(): addcart('apple', qt))
    # continue previous process for all products  available
    if prod == "display2":
        co = int(display2.get())
        co = co + count
        if co > -1:
            display2.delete(0, END)
            display2.insert(END, co)
            added1.config(command=lambda qt=display2.get(): addcart('orange', qt))
    if prod == "display3":
        co = int(display3.get())
        co = co + count
        if co > -1:
            display3.delete(0, END)
            display3.insert(END, co)
            added2.config(command=lambda qt=display3.get(): addcart('tomato', qt))
    if prod == "display4":
        co = int(display4.get())
        co = co + count
        if co > -1:
            display4.delete(0, END)
            display4.insert(END, co)
            added3.config(command=lambda qt=display4.get(): addcart('potato', qt))
    if prod == "display5":
        co = int(display5.get())
        co = co + count
        if co > -1:
            display5.delete(0, END)
            display5.insert(END, co)
            added4.config(command=lambda qt=display5.get(): addcart('rice', qt))


# function to display the searched products
# And to add the product into the  cart
def product(page,slide):
    # globally declaring the variables to be used in other functions
    global appleimg
    global OrangeImage
    global TomatoImage
    global PotatoImage
    global riceImage
    global display1
    global display2
    global added1
    global added
    global display3
    global tomato
    global display4
    global potato
    global added2
    global added3
    global rice
    global apple
    global orange
    global added4
    global display5
    global check
    global items
    # variables to store quantity of the product (initially 0)
    a='0'
    o='0'
    p='0'
    t='0'
    c='0'
    # check if the product  is already placed in the cart
    # if yes,then set the quantity from the cart list
    for prod, quantity in cart:
        ''' set the quantity of the product if its already 
         present in the cart list '''
        if prod == "apple":
            a = quantity

        if prod == "orange":
            o = quantity

        if prod == "potato":
            p = quantity

        if prod == "tomato":
            t = quantity

        if prod == "rice":
            c = quantity
    # keyword to display apple product
    applekey = ["apple", "fruits", "fruit", "all"]
    # check if the searched product is in applekey
    if page in applekey:

        if slide=="home":
            # create a label frame for the product in home page
            apple = LabelFrame(available,bd=0)
        elif slide =="home2":
            # create a label frame for the product  in search result page
            apple = LabelFrame(home2, bd=0)
        # pack the label frame
        apple.pack(fill="x",expand=1)
        # resize the image of the product
        appletemp = Image.open("download.png")
        resize = appletemp.resize((150, 150))
        appleimg = ImageTk.PhotoImage(resize)
        # display the resized image in the label
        Label(apple, image=appleimg).pack(side=LEFT,padx=30)
        # label the pricing and extra details of the product
        Label(apple, text="₹200", bg="aqua", font=('Times New Roman', 20, 'bold')).place(x=280,y=110)
        Label(apple, text="Apple|20% off on fruit items", font=('Ariel', 15),padx=10).pack(side=LEFT,padx=10)
        # Button to Add the product and quantity into the card list
        added = Button(apple, text="Add", pady=5, padx=25)
        added.pack(side=RIGHT,padx=10)
        # Button to decrease the product quantity by 1 using a function 'adding'
        Button(apple, text="-", command=lambda count=-1: adding("display1", count),padx=10).pack(side=RIGHT,padx=10)
        # display to show quantity
        display1 = Entry(apple, width=5, font=('Arial', 15),justify='center')
        display1.pack(side=RIGHT,padx=10)
        # insert the quantity 0 if product is not in the cart list
        # or insert  the quantity as the cart list
        display1.insert(END,a)
        # button to increase the product quantity by 1 using a function 'adding'
        Button(apple,text="+",command=lambda count=1: adding("display1",count),padx=10).pack(side=RIGHT,padx=10)
        # check the product quantity of the is not 0 after the add button clicked
        if a != '0':
            # disable the quantity display if 'add' button is clicked
            # change button text 'add' to 'added'
            added.config(text="Added",bg="Lightgreen",state=DISABLED)
            display1.config(state=DISABLED)
    # repeat the process of previous product to create required number of products
    # product 2 - orange
    orangekey = ["orange", "fruits", "fruit", "all"]
    if page in orangekey:

        if slide == "home":
            orange = LabelFrame(available, bd=0)
        elif slide == "home2":
            orange = LabelFrame(home2, bd=0)
        orange.pack(anchor=W,fill="x",expand=1)
        orangetemp = Image.open("orange3.jpg")
        resize = orangetemp.resize((150, 150))
        OrangeImage = ImageTk.PhotoImage(resize)
        Label(orange,image=OrangeImage).pack(side=LEFT,padx=30)
        Label(orange, text="₹140", bg="orange", font=('Times New Roman', 20, 'bold')).place(x=280,y=110)

        Label(orange, text="orange|20% off on fruit items", font=('Ariel', 15)).pack(side=LEFT,padx=10)
        added1 = Button(orange, text="Add", pady=5, padx=25)
        added1.pack(side=RIGHT,padx=10)
        Button(orange, text="-", command=lambda count=-1: adding("display2", count),padx=10).pack(side=RIGHT,padx=10)

        display2 = Entry(orange, width=5, font=('Arial', 15), justify='center')
        display2.pack(side=RIGHT,padx=10)
        display2.insert(END, o)
        Button(orange, text="+", command=lambda count=1: adding("display2", count),padx=10).pack(side=RIGHT,padx=10)
        # check the product quantity of the is not 0 after the add button clicked
        if o != '0':
            added1.config(text="Added",bg="LightGreen",state=DISABLED)
            display2.config(state=DISABLED)

    # product 3- tomato
    tomatokey=['tomato','vegetable','vegetables','all']
    if page in tomatokey:

        if slide == "home":
            tomato = LabelFrame(available, bd=0)
        elif slide == "home2":

            tomato = LabelFrame(home2, bd=0)
        tomato.pack(anchor=W, fill="x",expand=1)
        tomatotemp = Image.open("tomato.jpg")
        resize = tomatotemp.resize((150, 150))
        TomatoImage = ImageTk.PhotoImage(resize)
        Label(tomato, image=TomatoImage).pack(side=LEFT,padx=30)
        Label(tomato, text="₹25", bg="maroon", font=('Times New Roman', 20, 'bold')).place(x=280,y=110)
        Label(tomato, text="tomato|30% off on vegetable items", font=('Ariel', 15)).pack(side=LEFT,padx=10)
        added2 = Button(tomato, text="Add", pady=5, padx=25)
        added2.pack(side=RIGHT,padx=10)
        Button(tomato, text="-", command=lambda count=-1: adding("display3", count),padx=10).pack(side=RIGHT,padx=10)
        display3 = Entry(tomato, width=5, font=('Arial', 15), justify='center')
        display3.pack(side=RIGHT,padx=10)
        display3.insert(END, t)
        Button(tomato, text="+", command=lambda count=1: adding("display3", count),padx=10).pack(side=RIGHT,padx=10)
        if t != '0':
            added2.config(text="Added",bg="Lightgreen",state=DISABLED)
            display3.config(state=DISABLED)

    # product 4- potato
    potatokey=['potato','vegetable','vegetables','all']
    if page in potatokey:

        if slide == "home":
            potato = LabelFrame(available, bd=0)
        elif slide == "home2":

            potato = LabelFrame(home2, bd=0)
        potato.pack(anchor=W, fill="x",expand=1)
        potatotemp = Image.open("potato.jpg")
        resize = potatotemp.resize((150, 150))
        PotatoImage = ImageTk.PhotoImage(resize)
        Label(potato, image=PotatoImage).pack(side=LEFT,padx=30)
        Label(potato, text="₹50", bg="brown", font=('Times New Roman', 20, 'bold')).place(x=280,y=110)
        Label(potato, text="potato|30% off on all vegetable items", font=('Ariel', 15),padx=10).pack(side=LEFT,padx=10)
        added3 = Button(potato, text="Add", pady=5, padx=25)
        added3.pack(side=RIGHT,padx=10)
        Button(potato, text="-", command=lambda count=-1: adding("display4", count),padx=10).pack(side=RIGHT,padx=10)

        display4 = Entry(potato, width=5, font=('Arial', 15), justify='center')
        display4.pack(side=RIGHT,padx=10)
        display4.insert(END, p)

        Button(potato, text="+", command=lambda count=1: adding("display4", count)).pack(side=RIGHT,padx=10)
        if p != '0':
            added3.config(text="Added",bg="Lightgreen",state=DISABLED)
            display4.config(state=DISABLED)

        # product 5- rice
    if page == 'rice' or page == "grocery" or page == 'all':

        if slide == "home":
            rice = LabelFrame(available, bd=0)
        elif slide == "home2":
            rice = LabelFrame(home2, bd=0)
        rice.pack(anchor=W, fill="x",expand=1)
        ricetemp = Image.open("rice.jpg")
        resize = ricetemp.resize((150, 150))
        riceImage = ImageTk.PhotoImage(resize)
        Label(rice, image=riceImage).pack(side=LEFT,padx=30)
        Label(rice, text="₹40", bg="blue", font=('Times New Roman', 20, 'bold')).place(x=280,y=110)
        Label(rice, text="rice| 10 % off on all groceries ", font=('Ariel', 15)).pack(side=LEFT,padx=10)
        added4 = Button(rice, text="Add", pady=5, padx=25)
        added4.pack(side=RIGHT,padx=10)
        Button(rice, text="-", command=lambda count=-1: adding("display5", count),padx=10).pack(side=RIGHT,padx=10)
        display5 = Entry(rice, width=5, font=('Arial', 15), justify='center')
        display5.pack(side=RIGHT,padx=10)
        display5.insert(END, c)
        Button(rice, text="+", command=lambda count=1: adding("display5", count),padx=10).pack(side=RIGHT,padx=10)
        if c != '0':
            added4.config(text="Added",bg="Lightgreen",state=DISABLED)
            display5.config(state=DISABLED)
    # button to show the items in the cart by calling checkcart function
    # inactive if no product is added to the cart list
    check = Button(main_frame,text="Checkout  ", bg="grey", state=DISABLED,width=8,fg="red",pady=10,padx=10, command=checkcart)
    check.place(x=850,y=60)
    # shows the number product in the cart
    items = Label(main_frame, text=len(cart),bg="grey")
    items.place(x=920, y=72)
    #  activate the checkout button if more than 1 product added to the cart list
    if len(cart) > 0:
        check.config(state=NORMAL,bg="yellow")
        # display number of product in the cart
        items.config(text=len(cart),bg="yellow")


def homepage():
    # get and store the searched product
    page=search.get()
    # check whether searched keyword is valid
    if page in products:
        global home2
        # destroy the main page to show the search result in the new page
        available.destroy()
        # ignore error if there is no previous result page
        try:
            # destroy the previous page to show the search result in the new page
            home2.destroy()
        except:
            # do nothing if throws error
            pass
        # setup home2 frame(page) to display result page
        home2 = Frame(sidespace)
        # set up scroll bar  to the frame
        sidespace.create_window((0, 0), window=home2, anchor="nw")
        # function to call home 2 frame(page)
        product(page,"home2")
    # if no product is searched
    elif page == '':
        """show error message if search button clicked when no product 
            is entered in the search bar"""
        messagebox.showerror("warning","enter product in search box before search")
    # if the searched keyword is not valid
    else:
        messagebox.showerror("ItemNotFound", "entered product not found")


# function to select and upload user Product list
def uploads():
    # user instruction to upload their Product list
    messagebox.showinfo("instructions","List should be in the format of \n Product1-Quantity\n Product2-Quantity\n...")
    # "filename" stores the address of the selected file
    filename = filedialog.askopenfilename(initialdir="/vishnupython/", title="select",
                                               filetypes=(("txt", "*txt"), ("allfile", "*.*")))
    # read (get) the products from the list
    with open(filename, 'r') as file:

        for line in file:
            # convert the 'product-quantity' string into a list items
            details = line.strip().split('-')
            item,quantity= details
            # store the list items into the cart list
            cart.append((item,quantity))
        # enable the checkout and numbers of items
        check.config(state=NORMAL,bg="yellow")
        items.config(text=len(cart),bg="yellow")
        # opens the cart page after added the products in the list
        checkcart()
def main():
    global cart
    global search
    global SearchImage
    global sidespace
    global upload
    global main_frame
    global available
    global products

    # List to store selected product
    cart = []
    # Home page Frame
    main_frame = Frame(shop, width=1000, height=1000)
    main_frame.pack(fill=BOTH, expand=1)
    # Header of the page
    Label(main_frame, text="Ekart", bg="yellow", fg="red", font=('Times New Roman', 30, 'bold')).pack(fill=X)
    # Button to call upload function
    upload=Button(main_frame,bg="green",text="upload your List", font=('Arial', 10),pady=8)
    upload.place(x=80,y=60)
    upload.config(command=uploads)
    # search bar to search product
    search = Entry(main_frame, justify='left', bd=1, insertwidth=1, width=30, font=('Arial', 20))
    search.pack(pady=10)
    # resize image for search button
    searchtemp = Image.open("searching.png")
    resize = searchtemp.resize((32, 33))
    SearchImage = ImageTk.PhotoImage(resize)
    # search button to display products entered in search bar
    button = Button(search, image=SearchImage, bd=0)
    button.place(x=419)

    button.config(command=homepage)
    # A space that move along with scrollbar
    sidespace = Canvas(main_frame)
    sidespace.pack(side=LEFT, fill=BOTH, expand=1)
    # creating a  scroll bar
    scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=sidespace.yview)
    scroll.pack(side=RIGHT, fill=Y)
    sidespace.config(yscrollcommand=scroll.set)
    sidespace.bind('<Configure>', lambda e: sidespace.configure(scrollregion=sidespace.bbox("all")))
    # main page to show all product available
    available = Frame(sidespace)
    sidespace.create_window((0, 0), window=available, anchor="nw")
    # function to show all products available
    product('all', "home")
    # list of keywords for search bar to show products
    products = ['all', "fruit", "fruits", "apple", "orange", "vegetables", "vegetable", "tomato",
              "potato", "grocery", "rice"]


main()
shop.mainloop()

