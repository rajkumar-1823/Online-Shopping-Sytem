from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import mysql.connector as SQL
from twilio.rest import Client

#Frontpage__window    

m = Tk()  # create CTk window like the Tk window
m.title('Vkart Shopping')
m.geometry("1366x768")
#m.resizable(False,False)

####database###
def database_create():
    try:
        mydb = SQL.connect(host = "localhost",user = "root")
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE shopping")
    except:
        pass
database_create()
        

def table_create():
    try:
        
        account_db = SQL.connect(host = "localhost",user = "root",database="shopping")
        cursor = account_db.cursor()
        cursor.execute('CREATE TABLE account (username varchar(20) PRIMARY KEY,name varchar(25),phone_number BIGINT(10),Address varchar(255),password VARCHAR(120))')
        
        cursor.execute('CREATE TABLE Purchase_details (username varchar(20),item_purchased LONGTEXT,Total_price varchar(100), Dateandtime datetime PRIMARY KEY)')
        
        account_db.commit()
        account_db.close()
    except:
         pass
        
table_create()


###############################Register Page####################################




#Signup_page
def signup_command():
    window=Toplevel()
    window.title("SignUp")
    window.geometry ('925x650')
    window.configure(bg='#fff')
    window.resizable (False, False)

    def signup():
        global username
        global userf
        
        username=user.get()
        password=code.get()
        name=namee.get()
        phone_number=phone.get()
        Address=address.get()
        conform_password=conform_code.get()
        if password==conform_password and len(phone_number)==10:
            stored_db = SQL.connect(host = "localhost",user = "root",database="shopping")
            store = stored_db.cursor()
            
            insert_query = "INSERT INTO `account`(`username`, `name`, `phone_number`, `Address`, `password`) VALUES (%s,%s,%s,%s,%s)"
            vals =(username,name,phone_number,Address,password)
            store.execute(insert_query,vals)
            stored_db.commit()
            
            messagebox.showinfo('Signup', 'Sucessfully sign up')
            
            window.destroy()
        
        else:
            messagebox.showerror('Invalid', "Both Password should match or check your Phone number")

    def sign():
        window.destroy()

    show_image=ImageTk.PhotoImage (file='img\show.png')
    hide_image=ImageTk.PhotoImage (file='img\hide.png')     
    ##Image
    img= PhotoImage(file='img\signup.png')
    Label(window,image=img, border=0, bg='white').place(x=50, y=175)
    #frame
    frame=Frame(window, width=925,height=650, bg='#fff')
    frame.place(x=480, y=50)
    #text
    heading=Label (frame, text='Sign up',fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)
    
#####Username
    def on_enter(e):
        user.delete (0, 'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0, 'Username')
        
    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame (frame, width=295, height=2, bg='black').place(x=25, y=107)
#####name
    def on_enter(e):
        namee.delete (0, 'end')
    def on_leave(e):
        if namee.get()=='':
            namee.insert(0, 'Name')
        
    namee = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
    namee.place(x=30, y=150)
    namee.insert(0, 'Name')
    namee.bind("<FocusIn>", on_enter)
    namee.bind("<FocusOut>", on_leave)

    Frame (frame, width=295, height=2, bg='black').place(x=25, y=177)

#####phone
    def on_enter(e):
        phone.delete (0, 'end')
    def on_leave(e):
        if phone.get()=='':
            phone.insert(0, 'Phone Number')
        
    phone = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
    phone.place(x=30, y=220)
    phone.insert(0, 'Phone Number')
    phone.bind("<FocusIn>", on_enter)
    phone.bind("<FocusOut>", on_leave)

    Frame (frame, width=295, height=2, bg='black').place(x=25, y=247)

#####phone
    def on_enter(e):
        address.delete (0, 'end')
    def on_leave(e):
        if address.get()=='':
            address.insert(0, 'Address')
        
    address = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
    address.place(x=30, y=290)
    address.insert(0, 'Address')
    address.bind("<FocusIn>", on_enter)
    address.bind("<FocusOut>", on_leave)

    Frame (frame, width=295, height=2, bg='black').place(x=25, y=317)

#####password    
    def show():
        hide_button = Button (frame, image=hide_image, command=hide, relief=FLAT, cursor="hand2", activebackground="white", bd=0, bg='white')
        hide_button.place (x=280, y=355)
        code.config(show='')
    
    def hide():
        show_button3 = Button (frame, image=show_image, command=show, relief=FLAT, cursor="hand2", activebackground='white', bd=0, bg='white')
        show_button3.place (x=280, y=355)
        code.config(show='*')


    def on_enter(e):
        code.delete(0, 'end')
        code.config(show="*")
    def on_leave(e):
        if code.get()=='':
                code.insert(0, 'Password')
                code.config(show="")
        
    code = Entry (frame, width=25, fg='black', border=0, bg='white', font= ('Microsoft Yahei UI Light',11))
    code.place(x=30, y=360)
    
    show_button = Button(frame, image=show_image,command=show, cursor="hand2", relief=FLAT, activebackground='white',bd=0, bg='white')
    show_button.place(x=280, y=355)
    
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame (frame, width=295, height=2, bg='black').place(x=25,y=387)

    
####conform password
    def show2():
        hide_button2 = Button (frame, image=hide_image, command=hide2, relief=FLAT, cursor="hand2", activebackground="white", bd=0, bg='white')
        hide_button2.place (x=280, y=425)
        conform_code.config(show='')
    
    def hide2():
        show_button4 = Button (frame, image=show_image, command=show2, relief=FLAT, cursor="hand2", activebackground='white', bd=0, bg='white')
        show_button4.place (x=280, y=425)
        conform_code.config(show='*')
    

    def on_enter(e):
        conform_code.delete(0, 'end')
        conform_code.config(show="*")
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0, 'Conform Password')
            conform_code.config(show="")
        
    conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font= ('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=425)

    show_button2 = Button(frame, image=show_image, cursor="hand2", relief=FLAT, command=show2, activebackground='white',bd=0, bg='white')
    show_button2.place(x=280, y=425)
    
    conform_code.insert(0, 'Conform Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>", on_leave)

    Frame (frame, width=295, height=2, bg='black').place(x=25, y=457)
###########Button
    Button (frame, width=39, pady=7,text='Sign up',bg='#57a1f8',fg='white', border=0,command =signup).place(x=35,y=480)
    label=Label(frame, text='I have an account',fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
    label.place(x=90, y=520)

    signin=Button(frame,width=6, text='Sign in', border=0, bg='white', cursor='hand2',command=sign,fg='#57a1f8')
    signin.place(x=200, y=520)




    window.mainloop()
    
####signin--open--from--sigup--page

def rootdes():
    root.destroy()

def signin_main():
    root=Toplevel()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure (bg="#fff")
    root.resizable (False, False)

    img = ImageTk.PhotoImage(Image.open("img\login.png"))
    Label (root, image=img, bg='white').place(x=50, y=50)
    frame=Frame (root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)    
    
    user=Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')

    Frame (frame, width=295, height=2, bg='black').place(x=25, y=107)

    
    def sign_in():
        global username
        username=user.get()
        password=code.get()

        connection = SQL.connect(host = "localhost",user = "root",database="shopping")
        c = connection.cursor()
        
        select_query = 'SELECT * FROM `account` WHERE `username` = %s AND `password` = %s'
        vals = (username,password,)
        c.execute(select_query,vals)

        global userf
        
        userf = c.fetchone()
        
        if userf is not None:
            messagebox.showinfo('Login', 'You have logged in sucessfully')
            root.destroy()
            sign.destroy()
            sign_name=Label(head, text='Welcome, \n'+str(userf[1]), fg='white', bg='#57a1f8', font=('Microsoft YaHei UI Light', 12, 'bold'))
            sign_name.place(x=1235, y=20)

        elif username=="admin" and password =="admin":
            admin()
        
        else: 
            messagebox.showerror("Invalid", "invalid username and password")
    

    ############Username
    def on_enter(e):
        user.delete (0, 'end')
    def on_leave(e):
        name=user.get()

    mystr = StringVar()
    mystr.set('Username')       
    user=Entry (frame,textvariable=mystr,width=25, fg='black',border=0, bg="white", font=('Microsoft YaHei UI Light',11))
    user.place(x=30, y=80)
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame (frame, width=295, height=2, bg='black').place (x=25, y=107)

############Password
    show_image2=ImageTk.PhotoImage (file='img\show.png')
    hide_image2=ImageTk.PhotoImage (file='img\hide.png')

    def show3():
        hide_button4 = Button (frame, image=hide_image2, command=hide3, relief=FLAT, cursor="hand2", activebackground="white", bd=0, bg='white')
        hide_button4.place (x=280, y=145)
        code.config(show='')
    
    def hide3():
        show_button6 = Button (frame, image=show_image2, command=show3, relief=FLAT, cursor="hand2", activebackground='white', bd=0, bg='white')
        show_button6.place (x=280, y=145)
        code.config(show='*')


    def on_enter(e):
        code.delete(0, 'end')
        code.config(show="*")
    def on_leave (e):
        name=code.get()
        code.config(show="")
        
    mystr = StringVar()
    mystr.set('Password')   
     
    code = Entry (frame,textvariable=mystr,width=25,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
    code.place(x=30, y=150)

    show_button5 = Button(frame, image=show_image2, cursor="hand2", relief=FLAT, command=show3, activebackground='white',bd=0, bg='white')
    show_button5.place(x=280, y=145)
    
    code.config(fg="black")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame (frame, width=295, height=2, bg='black').place(x=25, y=177)

    ###############Button

    Button (frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=1,command=sign_in).place(x=35, y=204)
    label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei U Light',9))
    label.place(x=75,y=270)

    sign_up= Button (frame,width=6, text='Sign up', border=0, bg='white', cursor='hand2',fg='#57a1f8',command = signup_command )
    sign_up.place(x=215, y=270)



    root.mainloop()


#############################Admin#############################################

def purchase_debit():
    global c
    global connection
    
    connection = SQL.connect(host = "localhost",user = "root",database="shopping")
    c = connection.cursor()
        
    select_query = 'SELECT `username`, `item_purchased`, `Total_price`, `Dateandtime` FROM `purchase_details`'
    c.execute(select_query)

    data = c.fetchall()

    for dt in data: 
        order_tabel.insert("", 'end',iid=dt[3], text=dt[0],
                   values =(dt[0],dt[1],dt[2],dt[3]))



def removeRecord():
    selected = order_tabel.selection()
    if selected:
        # a row is selected
        x = selected[0]
        order_tabel.delete(x)
        # delete record from table
        sql = 'DELETE FROM purchase_details WHERE Dateandtime = %s'
        c.execute(sql, (x,))
        # assume mydb is the connection object of MySQL database
        connection.commit()  # make sure to commit the change
            


def admin():
    global order_tabel
    
    ad=Toplevel()
    ad.geometry("1366x768")

    one_frame = Frame(ad,bg="white",height=768,width=1366)

    New_frame = Frame(ad,bg="#1bcc7f",height=100,width=1345)
    New_frame.place(x=10,y=10)

    admin_logo=ImageTk.PhotoImage (file='img\Admin.png')
    lab = Label(New_frame,image=admin_logo,bd=0,bg="#1bcc7f")
    lab.place(x=1155,y=22)

    si_frame = Frame(ad,bg="#0487bf",height=640,width=1345)
    si_frame.place(x=10,y=120)

    btnframe1=Frame(si_frame,bg="white",height=620,width=250,highlightbackground="black",highlightthickness=2)
    btnframe1.place(x=10,y=10)


    lab = Label(New_frame,text = 'Vkart Shopping',bg="#1bcc7f",fg="white",font=('Britannic bold',25))
    lab.place(x=10,y=25)

    lab2=Label(New_frame,text = "ADMIN",bg="#1bcc7f",fg="white",font=('Franklin Gothic Heavy',25))
    lab2.place(x=1200,y=25)

    button1=Button(btnframe1,text="View orders",bg="#0487bf",fg="white",width=25,height=2,font =("Calibri",11),command=purchase_debit,cursor="hand2")
    button1.place(x=17,y=25)

    button2=Button(btnframe1,text="View Login Details",bg="#0487bf",fg="white",width=25,height=2,font=("Calibri",11),cursor="hand2")
    button2.place(x=17,y=100)

    #button3=Button(btnframe1,text="Add Products",bg="#0487bf",fg="white",width=25,height=2,font=("Calibri",11),cursor="hand2")
    #button3.place(x=17,y=175)

    #button4=Button(btnframe1,text="Delete Products",bg="#0487bf",fg="white",width=25,height=2,font=("Calibri",11),cursor="hand2")
    #button4.place(x=17,y=250)

    button5=Button(btnframe1,text="Delete",bg="#b5101b",fg="white",width=25,height=2,font=("Calibri",11),command=removeRecord,cursor="hand2")
    button5.place(x=17,y=550)



    db_frame = Frame(si_frame,highlightbackground="black",highlightthickness=2)
    db_frame.place(x=275,y=10,height=620,width=1060)

    scrollbar_db_x = Scrollbar(db_frame,orient=HORIZONTAL)
    scrollbar_db_y = Scrollbar(db_frame,orient=VERTICAL)

    s=ttk.Style()
    s.theme_use('clam')

    
    order_tabel = ttk.Treeview(db_frame,selectmode ='browse',xscrollcommand=scrollbar_db_x.set,yscrollcommand=scrollbar_db_y.set)

    order_tabel["columns"] = ("1", "2", "3", "4")
    order_tabel['show'] = 'headings'

    # width of columns and alignment 
    order_tabel.column("1", width = 30, anchor ='c')
    order_tabel.column("2", width = 80, anchor ='c')
    order_tabel.column("3", width = 80, anchor ='c')
    order_tabel.column("4", width = 80, anchor ='c')

    # Headings  
    # respective columns
    order_tabel.heading("1", text ="username")
    order_tabel.heading("2", text ="Item Purchased")
    order_tabel.heading("3", text ="Total Price")
    order_tabel.heading("4", text ="Date and Time")  

    scrollbar_db_x.pack(side=BOTTOM,fill=X)
    scrollbar_db_y.pack(side=RIGHT,fill=Y)

    scrollbar_db_x.configure(command=order_tabel.xview)
    scrollbar_db_y.configure(command=order_tabel.yview)

    order_tabel.pack(fill=BOTH,expand=1)

    ad.mainloop()


########################Payment##########################################

def order_placed():
        fr2.destroy()

"""def upi_call():
    Name2_lab=Label(upi_frame, text='Name:'+str(userf[1]), fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=220)
    add2_lab=Label(upi_frame, text='Address:'+str(userf[3]), fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=260)
    pur2_lab=Label(upi_frame, text='Purchased Items:', fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=320)
    entry_upi = Entry(upi_frame,width = 35,bd=0,bg="#fff",font=('Microsoft Yahei UI Light',11)).place(x=500,y=173)
    new=Frame(upi_frame, width=295, height=2, bg='black').place(x=500,y=200)
    pay_btn=Button(upi_frame,text="Pay",cursor="hand2",fg="white",bg="#3b91fe",font=('MathSans 16'),width=22,height=0).place(x = 507,y = 400)"""
    

"""def cash_call():
    Name_lab=Label(csh_frame, text='Name:'+str(userf[1]), fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=180)
    add_lab=Label(csh_frame, text='Address:'+str(userf[3]), fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=220)
    pur_lab=Label(csh_frame, text='Purchased Items:', fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=280)
    place_btn=Button(csh_frame,text="Place Order",cursor="hand2",fg="white",bg="#3b91fe",font=('MathSans 16'),width=22,height=0).place(x = 507,y = 400)"""

def send_msg():
    Getupinumber=entry_upi.get()
    if len(Getupinumber) == 17 and Getupinumber[-4:] == "@ybl" or len(Getupinumber) == 19 and Getupinumber[-6:] == "@paytm":
        print(Getupinumber)
        account_sid = "ACd07c4058dcb666b1de39481c31e6d4ea"
        auth_token = "29286961fceeb4fce9d7eb3d0ed2cb89"

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                 body='Hello '+str(userf[1])+' Your Order has been placed Successfully.. Purchased Items:'+str(userf2[1])+' -Vcart Team',
                 from_ =  "+16205434796",
                 to = "+91"+str(userf[2])
             )
        messagebox.showinfo("Order", "Your Order has been placed successfully")
        pay.destroy()
        mk_pay.destroy()
        last=Label(m, text='Thankyou for Purchasing',fg='#3b91fe', font=('Microsoft YaHei UI Light', 12, 'bold'))
        last.place(x=1110,y=600)
    else:
        messagebox.showerror("Invalid", "wrong")
def payment():
    itemstoredb()
    global userf2,entry_upi,pay
    pay=Tk()
    pay.geometry('925x500+300+200')
    pay.title("Order Conform")
    pay.config(bg="#fff")
    pay.resizable (False, False)

    bill=Label(pay, text='Payment', fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    bill.place(x=600, y=25) 

    ##img_bill = ImageTk.PhotoImage(Image.open("img\pay.jpg"))
    #img_bill_label=Label(pay, image=img_bill, bg='white')
    #img_bill_label.place(x=40, y=100)

    UPI_NO=Label(pay, text='upi number', fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 10, 'bold'))
    UPI_NO.place(x=500, y=350)

    connection2 = SQL.connect(host = "localhost",user = "root",database="shopping")
    c2 = connection2.cursor()
        
    select_query2 = 'SELECT * FROM `purchase_details` WHERE `username` = %s'
    vals2 = (username,)
    c2.execute(select_query2,vals2)

    userf2 = c2.fetchone()



    Name_lab=Label(pay, text='Name:'+str(userf[1]), fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=140)
    add_lab=Label(pay, text='Address:'+str(userf[3]), fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).place(x=500, y=180)
    pur_lab=Label(pay, text='Purchased Items:'+str(userf2[1]), fg='#3b91fe', bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
    pur_lab.place(x=500, y=240)
    entry_upi = Entry(pay,width = 34,bd=0,textvariable="Upi Number",bg="#fff",font=('Microsoft Yahei UI Light',11))
    entry_upi.place(x=500,y=320)
    line = Frame(pay, width=280, height=2, bg='black').place(x=500, y=350)

    pay_btn=Button(pay,text="Pay",cursor="hand2",fg="white",bg="#3b91fe",command=send_msg,font=('MathSans 16'),width=22,height=0).place(x = 507,y = 400)


    pay.mainloop()   


################################################################################

def Hideframe():
    try:
        frame_banner.destroy()
        frame_loc.destroy()
        frame_tre.destroy()
        txt_f.destroy()
    except:
        pass

def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s    


#############################################################women's Fashion#########################################################

women_1_image=ImageTk.PhotoImage(Image.open("img\women_1.jpg"))
women_2_image=ImageTk.PhotoImage(Image.open("img\women_2.jpg"))
women_3_image=ImageTk.PhotoImage(Image.open("img\women_3.jpg"))
women_4_image=ImageTk.PhotoImage(Image.open("img\women_4.jpeg"))
women_5_image=ImageTk.PhotoImage(Image.open("img\women_5.png"))
women_6_image=ImageTk.PhotoImage(Image.open("img\women_6.jpg"))
women_7_image=ImageTk.PhotoImage(Image.open("img\women_7.jpeg"))
women_8_image=ImageTk.PhotoImage(Image.open("img\women_8.jpeg"))
women_9_image=ImageTk.PhotoImage(Image.open("img\women_9.jpeg"))
women_10_image=ImageTk.PhotoImage(Image.open("img\women_10.jpg"))

#women_ variables
women_list=[]

def women_Call():
    Hideframe()
    
    lf_women_1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_1.place(x=5,y=35,width=200,height=280)
    lf_women_2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_2.place(x=210,y=35,width=200,height=280)
    lf_women_3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_3.place(x=415,y=35,width=200,height=280)
    lf_women_4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_4.place(x=620,y=35,width=200,height=280)
    lf_women_5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_5.place(x=825,y=35,width=200,height=280)
    lf_women_6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_6.place(x=5,y=310,width=200,height=280)
    lf_women_7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_7.place(x=210,y=310,width=200,height=280)
    lf_women_8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_8.place(x=415,y=310,width=200,height=280)
    lf_women_9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_9.place(x=620,y=310,width=200,height=280)
    lf_women_10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_women_10.place(x=825,y=310,width=200,height=280)
    label_women_1=Label(lf_women_1,image=women_1_image,bd=2,justify="center").grid(row=0,column=0)
    label_women_2=Label(lf_women_2,image=women_2_image,bd=2,justify="center").grid(row=0,column=0)
    label_women_3=Label(lf_women_3,image=women_3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_women_4=Label(lf_women_4,image=women_4_image,bd=2,justify="center").grid(row=0,column=0)
    label_women_5=Label(lf_women_5,image=women_5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_women_6=Label(lf_women_6,image=women_6_image,bd=2,justify="center").grid(row=0,column=0)
    label_women_7=Label(lf_women_7,image=women_7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_women_8=Label(lf_women_8,image=women_8_image,bd=2,justify="center").grid(row=0,column=0)
    label_women_9=Label(lf_women_9,image=women_9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_women_10=Label(lf_women_10,image=women_10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_women_1=Label(lf_women_1,text="SareeQueen-Red Jacquard Saree",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_2=Label(lf_women_2,text="Fostelo- Tan PU Sling Bag",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_3=Label(lf_women_3,text="Red Printed Unstitched Dress",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_4=Label(lf_women_4,text="Do Bahi Pink Stiletto Heels",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_5=Label(lf_women_5,text="PUJVI - Silver Ear Chain Earrings",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_6=Label(lf_women_6,text="Apnisha pink stiched Lehenga",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_women_7=Label(lf_women_7,text="Apratim Yellow Ethnic Footwear",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_8=Label(lf_women_8,text="Satin de NEXT",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_9=Label(lf_women_9,text="Bhagya Lakshmi-Gold Bangle",font="arial 9",justify="center").grid(row=1,column=0)
    name_women_10=Label(lf_women_10,text="Blue Zippered Sweater",font="arial 9",justify="center").grid(row=1,column=0)
    price_women_1=Label(lf_women_1,text="Price: Rs.649",font="arial 9 bold").grid(row=2,column=0)
    price_women_2=Label(lf_women_2,text="Price: Rs.329",font="arial 9 bold").grid(row=2,column=0)
    price_women_3=Label(lf_women_3,text="Price: Rs.399",font="arial 9 bold").grid(row=3,column=0)
    price_women_4=Label(lf_women_4,text="Price: Rs.675",font="arial 9 bold").grid(row=2,column=0)
    price_women_5=Label(lf_women_5,text="Price: Rs.280",font="arial 9 bold").grid(row=3,column=0)
    price_women_6=Label(lf_women_6,text="Price: Rs.649",font="arial 9 bold").grid(row=2,column=0)
    price_women_7=Label(lf_women_7,text="Price: Rs.239",font="arial 9 bold").grid(row=2,column=0)
    price_women_8=Label(lf_women_8,text="Price: Rs.419",font="arial 9 bold").grid(row=3,column=0)
    price_women_9=Label(lf_women_9,text="Price: Rs.289",font="arial 9 bold").grid(row=2,column=0)
    price_women_10=Label(lf_women_10,text="Price: Rs.469",font="arial 9 bold").grid(row=3,column=0)
    def AddW1():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["SareeQueen-Red Jacquard Saree",649,"649",Spaces(40-len("Grey Shirts"))])
            messagebox.showinfo("Product Status","SareeQueen-Red Jacquard Saree is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","SareeQueen-Red Jacquard Saree is not added to the cart.")
    def AddW2():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Fostelo- Tan PU Sling Bag",329,"329",Spaces(40-len("Johny T-shirts"))])
            messagebox.showinfo("Product Status","Fostelo- Tan PU Sling Bag is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fostelo- Tan PU Sling Bag is not added to the cart.")
    def AddW3():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Red Printed Unstitched Dress",399,"399",Spaces(40-len("Spark Casual shoe"))])
            messagebox.showinfo("Product Status","Red Printed Unstitched Dress is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Red Printed Unstitched Dress is not added to the cart.")
    def AddW4():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Do Bahi Pink Stiletto Heels",675,"675",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","Do Bahi Pink Stiletto Heels is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Do Bahi Pink Stiletto Heels is not added to the cart.")
    def AddW5():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["PUJVI - Silver Ear Chain Earrings",280,"280",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","PUJVI - Silver Ear Chain Earrings is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","PUJVI - Silver Ear Chain Earrings is not added to the cart.")
    def AddW6():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Peter England Jeans Pant",649,"649",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Peter England Jeans Pant is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Peter England Jeans Pant is not added to the cart.")
    def AddW7():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Lee Cooper Lether Belt",239,"239",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Lee Cooper Lether Belt is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Lee Cooper Lether Belt is not added to the cart.")
    def AddW8():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Hidesign Grey jeans belt",419,"419",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Hidesign Grey jeans belt is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Hidesign Grey jeans belt is not added to the cart.")
    def AddW9():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Head Band for women's (Grey",289,"289",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Head Band for women's (Grey is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Head Band for women's (Grey is not added to the cart.")
    def AddW10():
        global women_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            women_list.append(["Bally womens Wallet Brown",469,"469",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Bally womens Wallet Brown is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bally womens Wallet Brown is not added to the cart.")
    add_women_1=Button(lf_women_1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW1).place(x=68,y=245)
    add_women_2=Button(lf_women_2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW2).place(x=68,y=245)
    add_women_3=Button(lf_women_3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW3).place(x=68,y=245)
    add_women_4=Button(lf_women_4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW4).place(x=68,y=245)
    add_women_5=Button(lf_women_5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW5).place(x=68,y=245)
    add_women_6=Button(lf_women_6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW6).place(x=68,y=245)
    add_women_7=Button(lf_women_7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW7).place(x=68,y=245)
    add_women_8=Button(lf_women_8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW8).place(x=68,y=245)
    add_women_9=Button(lf_women_9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW9).place(x=68,y=245)
    add_women_10=Button(lf_women_10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddW10).place(x=68,y=245)

#############################################################Men's Fashion#########################################################

men_1_image=ImageTk.PhotoImage(Image.open("img\men_1.jpg"))
men_2_image=ImageTk.PhotoImage(Image.open("img\men_2.jpg"))
men_3_image=ImageTk.PhotoImage(Image.open("img\men_3.jpg"))
men_4_image=ImageTk.PhotoImage(Image.open("img\men_4.jpg"))
men_5_image=ImageTk.PhotoImage(Image.open("img\men_5.jpg"))
men_6_image=ImageTk.PhotoImage(Image.open("img\men_6.jpg"))
men_7_image=ImageTk.PhotoImage(Image.open("img\men_7.jpg"))
men_8_image=ImageTk.PhotoImage(Image.open("img\men_8.jpg"))
men_9_image=ImageTk.PhotoImage(Image.open("img\men_9.jpeg"))
men_10_image=ImageTk.PhotoImage(Image.open("img\men_10.jpeg"))

#men_ variables
men_list=[]

def men_Call():
    Hideframe()
    
    lf_men_1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_1.place(x=5,y=35,width=200,height=280)
    lf_men_2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_2.place(x=210,y=35,width=200,height=280)
    lf_men_3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_3.place(x=415,y=35,width=200,height=280)
    lf_men_4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_4.place(x=620,y=35,width=200,height=280)
    lf_men_5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_5.place(x=825,y=35,width=200,height=280)
    lf_men_6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_6.place(x=5,y=310,width=200,height=280)
    lf_men_7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_7.place(x=210,y=310,width=200,height=280)
    lf_men_8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_8.place(x=415,y=310,width=200,height=280)
    lf_men_9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_9.place(x=620,y=310,width=200,height=280)
    lf_men_10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_men_10.place(x=825,y=310,width=200,height=280)
    label_men_1=Label(lf_men_1,image=men_1_image,bd=2,justify="center").grid(row=0,column=0)
    label_men_2=Label(lf_men_2,image=men_2_image,bd=2,justify="center").grid(row=0,column=0)
    label_men_3=Label(lf_men_3,image=men_3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_men_4=Label(lf_men_4,image=men_4_image,bd=2,justify="center").grid(row=0,column=0)
    label_men_5=Label(lf_men_5,image=men_5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_men_6=Label(lf_men_6,image=men_6_image,bd=2,justify="center").grid(row=0,column=0)
    label_men_7=Label(lf_men_7,image=men_7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_men_8=Label(lf_men_8,image=men_8_image,bd=2,justify="center").grid(row=0,column=0)
    label_men_9=Label(lf_men_9,image=men_9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_men_10=Label(lf_men_10,image=men_10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_men_1=Label(lf_men_1,text="Grey 100% Cotton Slim Fit \nMen's Casual Shirt",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_2=Label(lf_men_2,text="Johny balck and white T-shirt",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_3=Label(lf_men_3,text="Spark Casual Shoe (pair of 2)",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_4=Label(lf_men_4,text="Canvas Grey Shoes",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_5=Label(lf_men_5,text="Levi's Jeans for men's",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_6=Label(lf_men_6,text="Peter England Jeans Pant",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_men_7=Label(lf_men_7,text="Lee Cooper Lether Belt",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_8=Label(lf_men_8,text="Hidesign Grey jeans belt",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_9=Label(lf_men_9,text="Head Band for men's (Grey)",font="arial 9",justify="center").grid(row=1,column=0)
    name_men_10=Label(lf_men_10,text="Bally Mens Wallet Brown",font="arial 9",justify="center").grid(row=1,column=0)
    price_men_1=Label(lf_men_1,text="Price: Rs.799",font="arial 9 bold").grid(row=2,column=0)
    price_men_2=Label(lf_men_2,text="Price: Rs.499",font="arial 9 bold").grid(row=2,column=0)
    price_men_3=Label(lf_men_3,text="Price: Rs.699",font="arial 9 bold").grid(row=3,column=0)
    price_men_4=Label(lf_men_4,text="Price: Rs.899",font="arial 9 bold").grid(row=2,column=0)
    price_men_5=Label(lf_men_5,text="Price: Rs.1,350",font="arial 9 bold").grid(row=3,column=0)
    price_men_6=Label(lf_men_6,text="Price: Rs.1,999",font="arial 9 bold").grid(row=2,column=0)
    price_men_7=Label(lf_men_7,text="Price: Rs.879",font="arial 9 bold").grid(row=2,column=0)
    price_men_8=Label(lf_men_8,text="Price: Rs.450",font="arial 9 bold").grid(row=3,column=0)
    price_men_9=Label(lf_men_9,text="Price: Rs.279",font="arial 9 bold").grid(row=2,column=0)
    price_men_10=Label(lf_men_10,text="Price: Rs.429",font="arial 9 bold").grid(row=3,column=0)
    def AddM1():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Grey Shirts",799,"799",Spaces(40-len("Grey Shirts"))])
            messagebox.showinfo("Product Status","Grey 100% Cotton Slim Fit Men's Casual Shirt is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Grey 100% Cotton Slim Fit Men's Casual Shirt is not added to the cart.")
    def AddM2():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Johny T-shirt",499,"499",Spaces(40-len("Johny T-shirts"))])
            messagebox.showinfo("Product Status","Johny T-shirt is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Johny T-shirt is not added to the cart.")
    def AddM3():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Spark Casual shoe",699,"699",Spaces(40-len("Spark Casual shoe"))])
            messagebox.showinfo("Product Status","Spark Casual Shoe (pair of 2) is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Spark Casual Shoe (pair of 2) is not added to the cart.")
    def AddM4():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Canvas Grey Shoes",899,"899",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","Canvas Grey Shoes is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Canvas Grey Shoes is not added to the cart.")
    def AddM5():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Levi's Jeans for men's",1350,"1350",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","Levi's Jeans for men's is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Levi's Jeans for men's is not added to the cart.")
    def AddM6():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Peter England Jeans Pant",1999,"1,999",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Peter England Jeans Pant is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Peter England Jeans Pant is not added to the cart.")
    def AddM7():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Lee Cooper Lether Belt",879,"879",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Lee Cooper Lether Belt is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Lee Cooper Lether Belt is not added to the cart.")
    def AddM8():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Hidesign Grey jeans belt",450,"450",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Hidesign Grey jeans belt is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Hidesign Grey jeans belt is not added to the cart.")
    def AddM9():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Head Band for men's (Grey",279,"279",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Head Band for men's (Grey is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Head Band for men's (Grey is not added to the cart.")
    def AddM10():
        global men_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            men_list.append(["Bally Mens Wallet Brown",429,"429",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Bally Mens Wallet Brown is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bally Mens Wallet Brown is not added to the cart.")
    add_men_1=Button(lf_men_1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM1).place(x=68,y=245)
    add_men_2=Button(lf_men_2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM2).place(x=68,y=245)
    add_men_3=Button(lf_men_3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM3).place(x=68,y=245)
    add_men_4=Button(lf_men_4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM4).place(x=68,y=245)
    add_men_5=Button(lf_men_5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM5).place(x=68,y=245)
    add_men_6=Button(lf_men_6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM6).place(x=68,y=245)
    add_men_7=Button(lf_men_7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM7).place(x=68,y=245)
    add_men_8=Button(lf_men_8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM8).place(x=68,y=245)
    add_men_9=Button(lf_men_9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM9).place(x=68,y=245)
    add_men_10=Button(lf_men_10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddM10).place(x=68,y=245)

    
    
    

#################################################################Grocery#############################################################################

global Products_frame
Products_frame=Label(m)
Products_frame.place(x=310,y=90,width=1040,height=620)

grocery1_image=ImageTk.PhotoImage(Image.open("img\Grocery_1.jpg"))
grocery2_image=ImageTk.PhotoImage(Image.open("img\Grocery_2.jpeg"))
grocery3_image=ImageTk.PhotoImage(Image.open("img\Grocery_3.jpeg"))
grocery4_image=ImageTk.PhotoImage(Image.open("img\Grocery_4.jpeg"))
grocery5_image=ImageTk.PhotoImage(Image.open("img\Grocery_5.jpeg"))
grocery6_image=ImageTk.PhotoImage(Image.open("img\Grocery_6.jpeg"))
grocery7_image=ImageTk.PhotoImage(Image.open("img\Grocery_7.jpeg"))
grocery8_image=ImageTk.PhotoImage(Image.open("img\Grocery_8.jpeg"))
grocery9_image=ImageTk.PhotoImage(Image.open("img\Grocery_9.jpeg"))
grocery10_image=ImageTk.PhotoImage(Image.open("img\Grocery_10.jpg"))

#Grocery Variables
clicked_grocery1=StringVar()
clicked_grocery1.set("250g - Rs.93")
clicked_grocery2=StringVar()
clicked_grocery2.set("5kg – Rs.235")
clicked_grocery3=StringVar()
clicked_grocery3.set("1kg – Rs.18")
clicked_grocery4=StringVar()
clicked_grocery4.set("1L – Rs.195")
clicked_grocery5=StringVar()
clicked_grocery5.set("500g – Rs.95")
clicked_grocery6=StringVar()
clicked_grocery6.set("55g – Rs.76")
clicked_grocery7=StringVar()
clicked_grocery7.set("120g – Rs.23")
clicked_grocery8=StringVar()
clicked_grocery8.set("200g – Rs.65")
clicked_grocery9=StringVar()
clicked_grocery9.set("500g – Rs.104")
clicked_grocery10=StringVar()
clicked_grocery10.set("70g – Rs.25")
grocery_list=[]


def GroceryCall():
    Hideframe()
    lf_grocery1=Label(Products_frame,bd=2,relief="groove")
    lf_grocery1.place(x=5,y=35,width=180,height=280)
    lf_grocery2=Label(Products_frame,bd=2,relief="groove")
    lf_grocery2.place(x=210,y=35,width=180,height=280)
    lf_grocery3=Label(Products_frame,bd=2,relief="groove")
    lf_grocery3.place(x=415,y=35,width=180,height=280)
    lf_grocery4=Label(Products_frame,bd=2,relief="groove")
    lf_grocery4.place(x=620,y=35,width=180,height=280)
    lf_grocery5=Label(Products_frame,bd=2,relief="groove")
    lf_grocery5.place(x=825,y=35,width=180,height=280)
    lf_grocery6=Label(Products_frame,bd=2,relief="groove")
    lf_grocery6.place(x=5,y=310,width=180,height=280)
    lf_grocery7=Label(Products_frame,bd=2,relief="groove")
    lf_grocery7.place(x=210,y=310,width=180,height=280)
    lf_grocery8=Label(Products_frame,bd=2,relief="groove")
    lf_grocery8.place(x=415,y=310,width=180,height=280)
    lf_grocery9=Label(Products_frame,bd=2,relief="groove")
    lf_grocery9.place(x=620,y=310,width=180,height=280)
    lf_grocery10=Label(Products_frame,bd=2,relief="groove")
    lf_grocery10.place(x=825,y=310,width=180,height=280)
    label_grocery_1=Label(lf_grocery1,image=grocery1_image,bd=2).grid(row=0,column=0)
    label_grocery_2=Label(lf_grocery2,image=grocery2_image,bd=2).grid(row=0,column=0)
    label_grocery_3=Label(lf_grocery3,image=grocery3_image,bd=2).grid(row=0,column=0,padx=13)
    label_grocery_4=Label(lf_grocery4,image=grocery4_image,bd=2).grid(row=0,column=0)
    label_grocery_5=Label(lf_grocery5,image=grocery5_image,bd=2).grid(row=0,column=0)
    label_grocery_6=Label(lf_grocery6,image=grocery6_image,bd=2).grid(row=0,column=0)
    label_grocery_7=Label(lf_grocery7,image=grocery7_image,bd=2).grid(row=0,column=0)
    label_grocery_8=Label(lf_grocery8,image=grocery8_image,bd=2).grid(row=0,column=0)
    label_grocery_9=Label(lf_grocery9,image=grocery9_image,bd=2).grid(row=0,column=0)
    label_grocery_10=Label(lf_grocery10,image=grocery10_image,bd=2).grid(row=0,column=0)
    name_grocery1=Label(lf_grocery1,text="Kellogg's Corn Flakes Original",font="arial 9").grid(row=1,column=0)
    name_grocery2=Label(lf_grocery2,text="Aashirwaad Superior Atta",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery3=Label(lf_grocery3,text="Tata Iodized Salt",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery4=Label(lf_grocery4,text="Safal Filtered Groundnut Oil",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery5=Label(lf_grocery5,text="24 Mantra Organic Toor Dal",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_grocery6=Label(lf_grocery6,text="Dairy Milk Silk Fruit & Nut",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_grocery7=Label(lf_grocery7,text="Yippee Noodles Magic Masala",font="arial 9",justify="center").grid(row=1,column=0)
    name_grocery8=Label(lf_grocery8,text="Kissan Mixed Fruit Jam",font="arial 9",justify="center").grid(row=1,column=0,padx=20)
    name_grocery9=Label(lf_grocery9,text="Mother's Recipe Mango Pickle",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_grocery10=Label(lf_grocery10,text="Parle's Cream & Onion Wafers",font="arial 9",justify="center").grid(row=1,column=0)
    label_qty_grocery1=Label(lf_grocery1,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery2=Label(lf_grocery2,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery3=Label(lf_grocery3,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery4=Label(lf_grocery4,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery5=Label(lf_grocery5,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery6=Label(lf_grocery6,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery7=Label(lf_grocery7,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery8=Label(lf_grocery8,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery9=Label(lf_grocery9,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_qty_grocery10=Label(lf_grocery10,text="Qty:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_grocery1=["250g – Rs.93","475g – Rs.166"]
    options_grocery2=["5kg – Rs.235","10kg – Rs.394"]
    options_grocery3=["1kg – Rs.18"]
    options_grocery4=["1L – Rs.195"]
    options_grocery5=["500g – Rs.95","1kg – Rs.165"]
    options_grocery6=["55g – Rs.76","137g – Rs.175"]
    options_grocery7=["120g – Rs.23","250g – Rs.48"]
    options_grocery8=["200g – Rs.65","500g – Rs.150","700g – Rs.215"]
    options_grocery9=["500g – Rs.104","1kg – Rs.160"]
    options_grocery10=["70g – Rs.25","150g – Rs.40"]
    global clicked_grocery1,clicked_grocery2,clicked_grocery3,clicked_grocery4,clicked_grocery5,grocery_list
    global clicked_grocery6,clicked_grocery7,clicked_grocery8,clicked_grocery9,clicked_grocery10
    drop_grocery1=OptionMenu(lf_grocery1,clicked_grocery1,*options_grocery1).place(x=30,y=212)
    drop_grocery2=OptionMenu(lf_grocery2,clicked_grocery2,*options_grocery2).place(x=30,y=212)
    drop_grocery3=OptionMenu(lf_grocery3,clicked_grocery3,*options_grocery3).place(x=30,y=212)
    drop_grocery4=OptionMenu(lf_grocery4,clicked_grocery4,*options_grocery4).place(x=30,y=212)
    drop_grocery5=OptionMenu(lf_grocery5,clicked_grocery5,*options_grocery5).place(x=30,y=212)
    drop_grocery6=OptionMenu(lf_grocery6,clicked_grocery6,*options_grocery6).place(x=30,y=212)
    drop_grocery7=OptionMenu(lf_grocery7,clicked_grocery7,*options_grocery7).place(x=30,y=212)
    drop_grocery8=OptionMenu(lf_grocery8,clicked_grocery8,*options_grocery8).place(x=30,y=212)
    drop_grocery9=OptionMenu(lf_grocery9,clicked_grocery9,*options_grocery9).place(x=30,y=212)
    drop_grocery10=OptionMenu(lf_grocery10,clicked_grocery10,*options_grocery10).place(x=30,y=212)

    def GroceryPrice(s):
        s1=""
        for i in range(len(s)-1,0,-1):
            if s[i]!='.':
                s1=s1+s[i]
            else:
                break
        return int(s1[::-1])
    def GroceryQty(s):
        s1=""
        for i in range(len(s)):
            s1=s1+s[i]
            if s[i]=='g' or s[i]=='L':
                break
        return s1
    def AddG1():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Corn Flakes",GroceryPrice(clicked_grocery1.get()),GroceryQty(clicked_grocery1.get()),Spaces(40-len("Corn Flakes"))])
            messagebox.showinfo("Product Status","Kellogg's Corn Flakes Original ("+clicked_grocery1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kellogg's Corn Flakes Original ("+clicked_grocery1.get()+") is not added to the cart.")
    def AddG2():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Aashirwaad Atta",GroceryPrice(clicked_grocery2.get()),GroceryQty(clicked_grocery2.get()),Spaces(40-len("Aashirwaad Atta"))])
            messagebox.showinfo("Product Status","Aashirwaad Superior Atta ("+clicked_grocery2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Aashirwaad Superior Atta ("+clicked_grocery2.get()+") is not added to the cart.")
    def AddG3():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Iodized Salt",GroceryPrice(clicked_grocery3.get()),GroceryQty(clicked_grocery3.get()),Spaces(40-len("Iodized Salt"))])
            messagebox.showinfo("Product Status","Tata Iodized Salt ("+clicked_grocery3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Tata Iodized Salt ("+clicked_grocery3.get()+") is not added to the cart.")
    def AddG4():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Filtered Groundnut Oil",GroceryPrice(clicked_grocery4.get()),GroceryQty(clicked_grocery4.get()),Spaces(40-len("Filtered Groundnut Oil"))])
            messagebox.showinfo("Product Status","Safal Filtered Groundnut Oil ("+clicked_grocery4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Safal Filtered Groundnut Oil ("+clicked_grocery4.get()+") is not added to the cart.")
    def AddG5():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Organic Toor Dal",GroceryPrice(clicked_grocery5.get()),GroceryQty(clicked_grocery5.get()),Spaces(40-len("Organic Toor Dal"))])
            messagebox.showinfo("Product Status","24 Mantra Organic Toor Dal ("+clicked_grocery5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","24 Mantra Organic Toor Dal ("+clicked_grocery5.get()+") is not added to the cart.")
    def AddG6():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Dairy Milk Silk",GroceryPrice(clicked_grocery6.get()),GroceryQty(clicked_grocery6.get()),Spaces(40-len("Dairy Milk Silk"))])
            messagebox.showinfo("Product Status","Dairy Milk Silk Fruit & Nut ("+clicked_grocery6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Dairy Milk Silk Fruit & Nut ("+clicked_grocery6.get()+") is not added to the cart.")
    def AddG7():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Yippee Noodles",GroceryPrice(clicked_grocery7.get()),GroceryQty(clicked_grocery7.get()),Spaces(40-len("Yippee Noodles"))])
            messagebox.showinfo("Product Status","Yippee Noodles Magic Masala ("+clicked_grocery7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Yippee Noodles Magic Masala ("+clicked_grocery7.get()+") is not added to the cart.")
    def AddG8():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Mixed Fruit Jam",GroceryPrice(clicked_grocery8.get()),GroceryQty(clicked_grocery8.get()),Spaces(40-len("Mixed Fruit Jam"))])
            messagebox.showinfo("Product Status","Kissan Mixed Fruit Jam ("+clicked_grocery8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kissan Mixed Fruit Jam ("+clicked_grocery8.get()+") is not added to the cart.")
    def AddG9():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Mango Pickle",GroceryPrice(clicked_grocery9.get()),GroceryQty(clicked_grocery9.get()),Spaces(40-len("Mango Pickle"))])
            messagebox.showinfo("Product Status","Mother's Recipe Mango Pickle ("+clicked_grocery9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Mother's Recipe Mango Pickle ("+clicked_grocery9.get()+") is not added to the cart.")
    def AddG10():
        global grocery_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Parle's Wafers",GroceryPrice(clicked_grocery10.get()),GroceryQty(clicked_grocery10.get()),Spaces(40-len("Parle's Wafers"))])
            messagebox.showinfo("Product Status","Parle's Cream & Onion Wafers ("+clicked_grocery10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Parle's Cream & Onion Wafers ("+clicked_grocery10.get()+") is not added to the cart.")
    add_grocery1=Button(lf_grocery1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1).place(x=60,y=245)
    add_grocery2=Button(lf_grocery2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2).place(x=60,y=245)
    add_grocery3=Button(lf_grocery3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3).place(x=60,y=245)
    add_grocery4=Button(lf_grocery4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4).place(x=60,y=245)
    add_grocery5=Button(lf_grocery5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5).place(x=60,y=245)
    add_grocery6=Button(lf_grocery6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6).place(x=60,y=245)
    add_grocery7=Button(lf_grocery7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7).place(x=60,y=245)
    add_grocery8=Button(lf_grocery8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8).place(x=60,y=245)
    add_grocery9=Button(lf_grocery9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9).place(x=60,y=245)
    add_grocery10=Button(lf_grocery10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10).place(x=60,y=245)

###########################################################Electronics##################################################################

electronics1_image=ImageTk.PhotoImage(Image.open("img\Electronics_1.jpeg"))
electronics2_image=ImageTk.PhotoImage(Image.open("img\Electronics_2.jpeg"))
electronics3_image=ImageTk.PhotoImage(Image.open("img\Electronics_3.jpeg"))
electronics4_image=ImageTk.PhotoImage(Image.open("img\Electronics_4.jpeg"))
electronics5_image=ImageTk.PhotoImage(Image.open("img\Electronics_5.jpeg"))
electronics6_image=ImageTk.PhotoImage(Image.open("img\Electronics_6.jpeg"))
electronics7_image=ImageTk.PhotoImage(Image.open("img\Electronics_7.jpeg"))
electronics8_image=ImageTk.PhotoImage(Image.open("img\Electronics_8.jpeg"))
electronics9_image=ImageTk.PhotoImage(Image.open("img\Electronics_9.jpeg"))
electronics10_image=ImageTk.PhotoImage(Image.open("img\Electronics_10.jpeg"))

#Electronics Variables
clicked_electronics1=StringVar()
clicked_electronics1.set("Aurora Blue")
clicked_electronics2=StringVar()
clicked_electronics2.set("Aquamarine Green")
clicked_electronics3=StringVar()
clicked_electronics3.set("Black")
clicked_electronics4=StringVar()
clicked_electronics4.set("Black")
clicked_electronics5=StringVar()
clicked_electronics5.set("Charcoal Grey")
clicked_electronics6=StringVar()
clicked_electronics6.set("Shadow Black")
clicked_electronics7=StringVar()
clicked_electronics7.set("Black")
clicked_electronics8=StringVar()
clicked_electronics8.set("Black")
clicked_electronics9=StringVar()
clicked_electronics9.set("Jet Black")
clicked_electronics10=StringVar()
clicked_electronics10.set("Blue & White")
electronics_list=[]


def ElectronicsCall():
    Hideframe()
    lf_electronics1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics1.place(x=5,y=35,width=200,height=280)
    lf_electronics2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics2.place(x=210,y=35,width=200,height=280)
    lf_electronics3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics3.place(x=415,y=35,width=200,height=280)
    lf_electronics4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics4.place(x=620,y=35,width=200,height=280)
    lf_electronics5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics5.place(x=825,y=35,width=200,height=280)
    lf_electronics6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics6.place(x=5,y=310,width=200,height=280)
    lf_electronics7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics7.place(x=210,y=310,width=200,height=280)
    lf_electronics8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics8.place(x=415,y=310,width=200,height=280)
    lf_electronics9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics9.place(x=620,y=310,width=200,height=280)
    lf_electronics10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_electronics10.place(x=825,y=310,width=200,height=280)
    label_electronics_1=Label(lf_electronics1,image=electronics1_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_2=Label(lf_electronics2,image=electronics2_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_3=Label(lf_electronics3,image=electronics3_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_4=Label(lf_electronics4,image=electronics4_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_5=Label(lf_electronics5,image=electronics5_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_6=Label(lf_electronics6,image=electronics6_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_7=Label(lf_electronics7,image=electronics7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_electronics_8=Label(lf_electronics8,image=electronics8_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_electronics_9=Label(lf_electronics9,image=electronics9_image,bd=2,justify="center").grid(row=0,column=0)
    label_electronics_10=Label(lf_electronics10,image=electronics10_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    name_electronics1=Label(lf_electronics1,text="Redmi Note 9 Pro(Storage:64GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_electronics2=Label(lf_electronics2,text="OnePlus 8T 5G(Storage:128GB)",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_electronics3=Label(lf_electronics3,text="boAt Bassheads Wired Earphones",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics4=Label(lf_electronics4,text="JBL T460BT On-Ear Headphones",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_electronics5=Label(lf_electronics5,text="Logitech M221 Wireless Mouse",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_electronics6=Label(lf_electronics6,text="HP Pavilion 15.6-inch",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics6=Label(lf_electronics6,text="FHD Gaming Laptop",font="arial 9",justify="center").grid(row=2,column=0)
    name_electronics6=Label(lf_electronics6,text="Storage:1TB HDD + 256GB SSD",font="arial 9",justify="center").grid(row=3,column=0,padx=6)
    price_electronics6=Label(lf_electronics6,text="Price: Rs.67,900",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_electronics7=Label(lf_electronics7,text="Acer Aspire 5 15.6 inch Laptop",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics7=Label(lf_electronics7,text="Intel Core i5 11th Generation",font="arial 9",justify="center").grid(row=2,column=0)
    name_electronics7=Label(lf_electronics7,text="Storage: 512GB SSD",font="arial 9",justify="center").grid(row=3,column=0)
    price_electronics7=Label(lf_electronics7,text="Price: Rs.49,990",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_electronics8=Label(lf_electronics8,text="OnePlus Y Series Full HD",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics8=Label(lf_electronics8,text="LED Smart Android TV 43Y1",font="arial 9",justify="center").grid(row=2,column=0)
    price_electronics8=Label(lf_electronics8,text="Price: Rs.15,499  Inches: 32",font="arial 9 bold",justify="center").grid(row=3,column=0)
    name_electronics9=Label(lf_electronics9,text="Noise Colorfit Pro 2 Smartwatch",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_electronics10=Label(lf_electronics10,text="EPSON L3115 Color A4",font="arial 9",justify="center").grid(row=1,column=0)
    name_electronics10=Label(lf_electronics10,text="All in ONE Printer",font="arial 9",justify="center").grid(row=2,column=0)
    price_electronics10=Label(lf_electronics10,text="Price: Rs.12,250",font="arial 9 bold",justify="center").grid(row=3,column=0)
    label_clr_electronics1=Label(lf_electronics1,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics2=Label(lf_electronics2,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics3=Label(lf_electronics3,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics4=Label(lf_electronics4,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics5=Label(lf_electronics5,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics6=Label(lf_electronics6,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics7=Label(lf_electronics7,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics8=Label(lf_electronics8,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics9=Label(lf_electronics9,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_electronics10=Label(lf_electronics10,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_electronics1=["Aurora Blue","Interstellar Black","Glacier White","Champagne Gold"]
    options_electronics2=["Aquamarine Green","Lunar Silver"]
    options_electronics3=["Black","Forest Green","Molten Orange","Neon Lime"]
    options_electronics4=["Black","Blue","White"]
    options_electronics5=["Charcoal Grey","Red","Blue"]
    options_electronics6=["Shadow Black","Fiery Red"]
    options_electronics7=["Black"]
    options_electronics8=["Black"]
    options_electronics9=["Jet Black","Cherry Red","Mist Grey","Royal Blue"]
    options_electronics10=["Blue & White"]
    global clicked_electronics1,clicked_electronics2,clicked_electronics3,clicked_electronics4,clicked_electronics5,electronics_list
    global clicked_electronics6,clicked_electronics7,clicked_electronics8,clicked_electronics9,clicked_electronics10
    drop_electronics1=OptionMenu(lf_electronics1,clicked_electronics1,*options_electronics1).place(x=48,y=212)
    drop_electronics2=OptionMenu(lf_electronics2,clicked_electronics2,*options_electronics2).place(x=48,y=212)
    drop_electronics3=OptionMenu(lf_electronics3,clicked_electronics3,*options_electronics3).place(x=48,y=212)
    drop_electronics4=OptionMenu(lf_electronics4,clicked_electronics4,*options_electronics4).place(x=48,y=212)
    drop_electronics5=OptionMenu(lf_electronics5,clicked_electronics5,*options_electronics5).place(x=48,y=212)
    drop_electronics6=OptionMenu(lf_electronics6,clicked_electronics6,*options_electronics6).place(x=48,y=212)
    drop_electronics7=OptionMenu(lf_electronics7,clicked_electronics7,*options_electronics7).place(x=48,y=212)
    drop_electronics8=OptionMenu(lf_electronics8,clicked_electronics8,*options_electronics8).place(x=48,y=212)
    drop_electronics9=OptionMenu(lf_electronics9,clicked_electronics9,*options_electronics9).place(x=48,y=212)
    drop_electronics10=OptionMenu(lf_electronics10,clicked_electronics10,*options_electronics10).place(x=48,y=212)
    def AddE1():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Redmi Note 9 Pro",13650,"13,650",clicked_electronics1.get(),Spaces(40-len("Redmi Note 9 Pro"))])
            messagebox.showinfo("Product Status","Redmi Note 9 Pro(Storage:64GB) ("+clicked_electronics1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Redmi Note 9 Pro(Storage:64GB) ("+clicked_electronics1.get()+") is not added to the cart.")
    def AddE2():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["OnePlus 8T 5G",42999,"42,999",clicked_electronics2.get(),Spaces(40-len("OnePlus 8T 5G"))])
            messagebox.showinfo("Product Status","OnePlus 8T 5G(Storage:128GB) ("+clicked_electronics2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus 8T 5G(Storage:128GB) ("+clicked_electronics2.get()+") is not added to the cart.")
    def AddE3():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["boAt Earphones",499,"499",clicked_electronics3.get(),Spaces(40-len("boAt Earphones"))])
            messagebox.showinfo("Product Status","boAt Bassheads Wired Earphones ("+clicked_electronics3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","boAt Bassheads Wired Earphones ("+clicked_electronics3.get()+") is not added to the cart.")
    def AddE4():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["JBL Headphones",2799,"2,799",clicked_electronics4.get(),Spaces(40-len("JBL Headphones"))])
            messagebox.showinfo("Product Status","JBL T460BT On-Ear Headphones ("+clicked_electronics4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","JBL T460BT On-Ear Headphones ("+clicked_electronics4.get()+") is not added to the cart.")
    def AddE5():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Logitech Mouse",699,"699",clicked_electronics5.get(),Spaces(40-len("Logitech Mouse"))])
            messagebox.showinfo("Product Status","Logitech M221 Wireless Mouse ("+clicked_electronics5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Logitech M221 Wireless Mouse ("+clicked_electronics5.get()+") is not added to the cart.")
    def AddE6():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["HP Pavilion Laptop",67900,"67,900",clicked_electronics6.get(),Spaces(40-len("HP Pavilion Laptop"))])
            messagebox.showinfo("Product Status","HP Pavilion 15.6-inch FHD Gaming Laptop Storage:1TB HDD + 256GB SSD ("+clicked_electronics6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","HP Pavilion 15.6-inch FHD Gaming Laptop Storage:1TB HDD + 256GB SSD ("+clicked_electronics6.get()+") is not added to the cart.")
    def AddE7():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Acer Aspire 5 Laptop",49990,"49,990",clicked_electronics7.get(),Spaces(40-len("Acer Aspire 5 Laptop"))])
            messagebox.showinfo("Product Status","Acer Aspire 5 15.6 inch Laptop Intel Core i5 11th Generation Storage: 512GB SSD ("+clicked_electronics7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Acer Aspire 5 15.6 inch Laptop Intel Core i5 11th Generation Storage: 512GB SSD ("+clicked_electronics7.get()+") is not added to the cart.")
    def AddE8():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["OnePlus Android TV",15499,"15,499",clicked_electronics8.get(),Spaces(40-len("OnePlus Android TV"))])
            messagebox.showinfo("Product Status","OnePlus Y Series Full HD LED Smart Android TV 43Y1 ("+clicked_electronics8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus Y Series Full HD LED Smart Android TV 43Y1 ("+clicked_electronics8.get()+") is not added to the cart.")
    def AddE9():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["Noise Colorfit Smartwatch",2999,"2,999",clicked_electronics9.get(),Spaces(40-len("Noise Colorfit Smartwatch"))])
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_electronics9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Noise Colorfit Pro 2 Smartwatch ("+clicked_electronics9.get()+") is not added to the cart.")
    def AddE10():
        global electronics_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            electronics_list.append(["EPSON Color Printer",12250,"12,250",clicked_electronics10.get(),Spaces(40-len("EPSON Color Printer"))])
            messagebox.showinfo("Product Status","EPSON L3115 Color A4 All in ONE Printer ("+clicked_electronics10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","EPSON L3115 Color A4 All in ONE Printer ("+clicked_electronics10.get()+") is not added to the cart.")
    price_electronics1=Label(lf_electronics1,text="Price: Rs.13,650",font="arial 9 bold").place(x=5,y=245)
    price_electronics2=Label(lf_electronics2,text="Price: Rs.42,999",font="arial 9 bold").place(x=5,y=245)
    price_electronics3=Label(lf_electronics3,text="Price: Rs.499",font="arial 9 bold").place(x=5,y=245)
    price_electronics4=Label(lf_electronics4,text="Price: Rs.2,799",font="arial 9 bold").place(x=5,y=245)
    price_electronics5=Label(lf_electronics5,text="Price: Rs.699",font="arial 9 bold").place(x=5,y=245)
    price_electronics9=Label(lf_electronics9,text="Price: Rs.2,999",font="arial 9 bold").place(x=5,y=245)
    add_electronics1=Button(lf_electronics1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE1).place(x=120,y=245)
    add_electronics2=Button(lf_electronics2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE2).place(x=120,y=245)
    add_electronics3=Button(lf_electronics3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE3).place(x=120,y=245)
    add_electronics4=Button(lf_electronics4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE4).place(x=120,y=245)
    add_electronics5=Button(lf_electronics5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE5).place(x=120,y=245)
    add_electronics6=Button(lf_electronics6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE6).place(x=60,y=245)
    add_electronics7=Button(lf_electronics7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE7).place(x=60,y=245)
    add_electronics8=Button(lf_electronics8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE8).place(x=60,y=245)
    add_electronics9=Button(lf_electronics9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE9).place(x=120,y=245)
    add_electronics10=Button(lf_electronics10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddE10).place(x=60,y=245)

#########################################################################Appliances#####################################################################
appliances1_image=ImageTk.PhotoImage(Image.open("img\Appliances_1.jpeg"))
appliances2_image=ImageTk.PhotoImage(Image.open("img\Appliances_2.jpeg"))
appliances3_image=ImageTk.PhotoImage(Image.open("img\Appliances_3.jpeg"))
appliances4_image=ImageTk.PhotoImage(Image.open("img\Appliances_4.jpeg"))
appliances5_image=ImageTk.PhotoImage(Image.open("img\Appliances_5.jpeg"))
appliances6_image=ImageTk.PhotoImage(Image.open("img\Appliances_6.jpeg"))
appliances7_image=ImageTk.PhotoImage(Image.open("img\Appliances_7.jpeg"))
appliances8_image=ImageTk.PhotoImage(Image.open("img\Appliances_8.jpeg"))
appliances9_image=ImageTk.PhotoImage(Image.open("img\Appliances_9.jpeg"))
appliances10_image=ImageTk.PhotoImage(Image.open("img\Appliances_10.jpeg"))

#Appliances variables
appliances_list=[]

def AppliancesCall():
    Hideframe()
    lf_appliances1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances1.place(x=5,y=35,width=200,height=280)
    lf_appliances2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances2.place(x=210,y=35,width=200,height=280)
    lf_appliances3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances3.place(x=415,y=35,width=200,height=280)
    lf_appliances4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances4.place(x=620,y=35,width=200,height=280)
    lf_appliances5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances5.place(x=825,y=35,width=200,height=280)
    lf_appliances6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances6.place(x=5,y=310,width=200,height=280)
    lf_appliances7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances7.place(x=210,y=310,width=200,height=280)
    lf_appliances8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances8.place(x=415,y=310,width=200,height=280)
    lf_appliances9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances9.place(x=620,y=310,width=200,height=280)
    lf_appliances10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_appliances10.place(x=825,y=310,width=200,height=280)
    label_appliances_1=Label(lf_appliances1,image=appliances1_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_2=Label(lf_appliances2,image=appliances2_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_3=Label(lf_appliances3,image=appliances3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_appliances_4=Label(lf_appliances4,image=appliances4_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_5=Label(lf_appliances5,image=appliances5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_appliances_6=Label(lf_appliances6,image=appliances6_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_7=Label(lf_appliances7,image=appliances7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_appliances_8=Label(lf_appliances8,image=appliances8_image,bd=2,justify="center").grid(row=0,column=0)
    label_appliances_9=Label(lf_appliances9,image=appliances9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_appliances_10=Label(lf_appliances10,image=appliances10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_appliances1=Label(lf_appliances1,text="Whirlpool 7kg Automatic Top Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances2=Label(lf_appliances2,text="IFB 6kg Fully Automatic Front Load",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances3=Label(lf_appliances3,text="Samsung 1.5 Ton 5 Star",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances3=Label(lf_appliances3,text="Split Inverter AC",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances4=Label(lf_appliances4,text="LG 260L Double Door Refrigerator",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances5=Label(lf_appliances5,text="IFB 20 L Convection",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances5=Label(lf_appliances5,text="Microwave Oven 20SC2",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances6=Label(lf_appliances6,text="Bajaj GX1 500W Mixer Grinder",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_appliances7=Label(lf_appliances7,text="Balzano OX218 Electric Kettle",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances8=Label(lf_appliances8,text="Elica WDFL 606 HAC MS NERO",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances8=Label(lf_appliances8,text="Auto Clean Wall Mounted Chimney",font="arial 9",justify="center").grid(row=2,column=0)
    name_appliances9=Label(lf_appliances9,text="Kent Ace 8 L Water Purifier",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances10=Label(lf_appliances10,text="Eureka Forbes Quick Clean DX",font="arial 9",justify="center").grid(row=1,column=0)
    name_appliances10=Label(lf_appliances10,text="Dry Vacuum Cleaner",font="arial 9",justify="center").grid(row=2,column=0)
    price_appliances1=Label(lf_appliances1,text="Price: Rs.14,990",font="arial 9 bold").grid(row=2,column=0)
    price_appliances2=Label(lf_appliances2,text="Price: Rs.23,790",font="arial 9 bold").grid(row=2,column=0)
    price_appliances3=Label(lf_appliances3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_appliances4=Label(lf_appliances4,text="Price: Rs.25,290",font="arial 9 bold").grid(row=2,column=0)
    price_appliances5=Label(lf_appliances5,text="Price: Rs.9,690",font="arial 9 bold").grid(row=3,column=0)
    price_appliances6=Label(lf_appliances6,text="Price: Rs.1,999",font="arial 9 bold").grid(row=2,column=0)
    price_appliances7=Label(lf_appliances7,text="Price: Rs.879",font="arial 9 bold").grid(row=2,column=0)
    price_appliances8=Label(lf_appliances8,text="Price: Rs.11,999",font="arial 9 bold").grid(row=3,column=0)
    price_appliances9=Label(lf_appliances9,text="Price: Rs.12,499",font="arial 9 bold").grid(row=2,column=0)
    price_appliances10=Label(lf_appliances10,text="Price: Rs.3,249",font="arial 9 bold").grid(row=3,column=0)
    def AddA1():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Whirlpool Top Load",14990,"14,990",Spaces(40-len("Whirlpool Top Load"))])
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Whirlpool 7kg Automatic Top Load is not added to the cart.")
    def AddA2():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["IFB Front Load",23790,"23,790",Spaces(40-len("IFB Front Load"))])
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 6kg Fully Automatic Front Load is not added to the cart.")
    def AddA3():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Samsung Inverter AC",34999,"34,999",Spaces(40-len("Samsung Inverter AC"))])
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung 1.5 Ton 5 Star Split Inverter AC is not added to the cart.")
    def AddA4():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["LG 260L Refrigerator",25290,"25,290",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","LG 260L Double Door Refrigerator is not added to the cart.")
    def AddA5():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["IFB Microwave Oven",9690,"9,690",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","IFB 20 L Convection Microwave Oven 20SC2 is not added to the cart.")
    def AddA6():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Bajaj Mixer Grinder",1999,"1,999",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bajaj GX1 500W Mixer Grinder is not added to the cart.")
    def AddA7():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Balzano Electric Kettle",879,"879",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Balzano OX218 Electric Kettle is not added to the cart.")
    def AddA8():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Elica Wall Mounted Chimney",11999,"11,999",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Elica WDFL 606 HAC MS NERO Auto Clean Wall Mounted Chimney is not added to the cart.")
    def AddA9():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Kent Ace Water Purifier",12499,"12,499",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kent Ace 8 L Water Purifier is not added to the cart.")
    def AddA10():
        global appliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            appliances_list.append(["Eureka Dry Vacuum Cleaner",3249,"3,249",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Eureka Forbes Quick Clean DX Dry Vacuum Cleaner is not added to the cart.")
    add_appliances1=Button(lf_appliances1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA1).place(x=68,y=245)
    add_appliances2=Button(lf_appliances2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA2).place(x=68,y=245)
    add_appliances3=Button(lf_appliances3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA3).place(x=68,y=245)
    add_appliances4=Button(lf_appliances4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA4).place(x=68,y=245)
    add_appliances5=Button(lf_appliances5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA5).place(x=68,y=245)
    add_appliances6=Button(lf_appliances6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA6).place(x=68,y=245)
    add_appliances7=Button(lf_appliances7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA7).place(x=68,y=245)
    add_appliances8=Button(lf_appliances8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA8).place(x=68,y=245)
    add_appliances9=Button(lf_appliances9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA9).place(x=68,y=245)
    add_appliances10=Button(lf_appliances10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA10).place(x=68,y=245)

###########################################sports#####################################################

sportsgym1_image=ImageTk.PhotoImage(Image.open("img\SportsGym_1.jpg"))
sportsgym2_image=ImageTk.PhotoImage(Image.open("img\SportsGym_2.jpg"))
sportsgym3_image=ImageTk.PhotoImage(Image.open("img\SportsGym_3.jpg"))
sportsgym4_image=ImageTk.PhotoImage(Image.open("img\SportsGym_4.jpg"))
sportsgym5_image=ImageTk.PhotoImage(Image.open("img\SportsGym_5.jpg"))
sportsgym6_image=ImageTk.PhotoImage(Image.open("img\SportsGym_6.jpg"))
sportsgym7_image=ImageTk.PhotoImage(Image.open("img\SportsGym_7.jpg"))
sportsgym8_image=ImageTk.PhotoImage(Image.open("img\SportsGym_8.jpg"))
sportsgym9_image=ImageTk.PhotoImage(Image.open("img\SportsGym_9.jpg"))
sportsgym10_image=ImageTk.PhotoImage(Image.open("img\SportsGym_10.jpg"))

#Sports and Gym variables
sportsgym_list=[]

def SportsGymCall():
    Hideframe()
    lf_sportsgym1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym1.place(x=5,y=35,width=200,height=280)
    lf_sportsgym2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym2.place(x=210,y=35,width=200,height=280)
    lf_sportsgym3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym3.place(x=415,y=35,width=200,height=280)
    lf_sportsgym4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym4.place(x=620,y=35,width=200,height=280)
    lf_sportsgym5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym5.place(x=825,y=35,width=200,height=280)
    lf_sportsgym6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym6.place(x=5,y=310,width=200,height=280)
    lf_sportsgym7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym7.place(x=210,y=310,width=200,height=280)
    lf_sportsgym8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym8.place(x=415,y=310,width=200,height=280)
    lf_sportsgym9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym9.place(x=620,y=310,width=200,height=280)
    lf_sportsgym10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_sportsgym10.place(x=825,y=310,width=200,height=280)
    label_sportsgym_1=Label(lf_sportsgym1,image=sportsgym1_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_2=Label(lf_sportsgym2,image=sportsgym2_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_sportsgym_3=Label(lf_sportsgym3,image=sportsgym3_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_4=Label(lf_sportsgym4,image=sportsgym4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_sportsgym_5=Label(lf_sportsgym5,image=sportsgym5_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_6=Label(lf_sportsgym6,image=sportsgym6_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_sportsgym_7=Label(lf_sportsgym7,image=sportsgym7_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_8=Label(lf_sportsgym8,image=sportsgym8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_sportsgym_9=Label(lf_sportsgym9,image=sportsgym9_image,bd=2,justify="center").grid(row=0,column=0)
    label_sportsgym_10=Label(lf_sportsgym10,image=sportsgym10_image,bd=2,justify="center").grid(row=0,column=0)
    name_sportsgym1=Label(lf_sportsgym1,text="GM Purist KW 202 Cricket Bat",font="arial 9",justify="center").grid(row=1,column=0,padx=13)
    name_sportsgym2=Label(lf_sportsgym2,text="GTS Dezir Cricket Leather Ball",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym3=Label(lf_sportsgym3,text="Yonex GR 303 Badminton Racquet",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym4=Label(lf_sportsgym4,text="Strauss Maxis Pro Shuttlecock",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym5=Label(lf_sportsgym5,text="Stag 4 Star Table Tennis Kit",font="arial 9",justify="center").grid(row=1,column=0,padx=14)
    name_sportsgym6=Label(lf_sportsgym6,text="Cockatoo CTM14A 2.5HP",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym6=Label(lf_sportsgym6,text="Treadmill with Auto-Incline",font="arial 9",justify="center").grid(row=2,column=0)
    name_sportsgym7=Label(lf_sportsgym7,text="Aurion HEX Rubber Coated Cast",font="arial 9",justify="center").grid(row=1,column=0,padx=4)
    name_sportsgym7=Label(lf_sportsgym7,text="Iron Hexagonal Dumbbells for",font="arial 9",justify="center").grid(row=2,column=0)
    name_sportsgym7=Label(lf_sportsgym7,text="Professional Exercise",font="arial 9",justify="center").grid(row=3,column=0)
    name_sportsgym8=Label(lf_sportsgym8,text="SPORTAL Foldable Multi Bench",font="arial 9",justify="center").grid(row=1,column=0)
    name_sportsgym8=Label(lf_sportsgym8,text="Press Workout Machine",font="arial 9",justify="center").grid(row=2,column=0)
    name_sportsgym9=Label(lf_sportsgym9,text="Reach Air Bike Exercise Cycle",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_sportsgym10=Label(lf_sportsgym10,text="RMOUR Filled Heavy Punch Bag",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    price_sportsgym1=Label(lf_sportsgym1,text="Price: Rs.1,970",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym2=Label(lf_sportsgym2,text="Price: Rs.160",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym3=Label(lf_sportsgym3,text="Price: Rs.550",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym4=Label(lf_sportsgym4,text="Price: Rs.350",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym5=Label(lf_sportsgym5,text="Price: Rs.980",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym6=Label(lf_sportsgym6,text="Price: Rs.28,990",font="arial 9 bold").grid(row=3,column=0)
    price_sportsgym7=Label(lf_sportsgym7,text="Price: Rs.949",font="arial 9 bold").grid(row=4,column=0)
    price_sportsgym8=Label(lf_sportsgym8,text="Price: Rs.6,799",font="arial 9 bold").grid(row=3,column=0)
    price_sportsgym9=Label(lf_sportsgym9,text="Price: Rs.6,999",font="arial 9 bold").grid(row=2,column=0)
    price_sportsgym10=Label(lf_sportsgym10,text="Price: Rs.2,999",font="arial 9 bold").grid(row=2,column=0)
    def AddS1():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["GM Cricket Bat",1970,"1,970",Spaces(40-len("GM Cricket Bat"))])
            messagebox.showinfo("Product Status","GM Purist KW 202 Cricket Bat is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GM Purist KW 202 Cricket Bat is not added to the cart.")
    def AddS2():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["GTS Leather Ball",160,"160",Spaces(40-len("GTS Leather Ball"))])
            messagebox.showinfo("Product Status","GTS Dezir Cricket Leather Ball is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GTS Dezir Cricket Leather Ball is not added to the cart.")
    def AddS3():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Yonex Badminton Racquet",550,"550",Spaces(40-len("Yonex Badminton Racquet"))])
            messagebox.showinfo("Product Status","Yonex GR 303 Badminton Racquet is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Yonex GR 303 Badminton Racquet is not added to the cart.")
    def AddS4():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Strauss Shuttlecock",350,"350",Spaces(40-len("Strauss Shuttlecock"))])
            messagebox.showinfo("Product Status","Strauss Maxis Pro Shuttlecock is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Strauss Maxis Pro Shuttlecock is not added to the cart.")
    def AddS5():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Table Tennis Kit",980,"980",Spaces(40-len("Table Tennis Kit"))])
            messagebox.showinfo("Product Status","Stag 4 Star Table Tennis Kit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Stag 4 Star Table Tennis Kit is not added to the cart.")
    def AddS6():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Cockatoo Treadmill",28990,"28,990",Spaces(40-len("Cockatoo Treadmill"))])
            messagebox.showinfo("Product Status","Cockatoo CTM14A 2.5HP Treadmill with Auto-Incline is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cockatoo CTM14A 2.5HP Treadmill with Auto-Incline is not added to the cart.")
    def AddS7():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Aurion Dumbbells",949,"949",Spaces(40-len("Aurion Dumbbells"))])
            messagebox.showinfo("Product Status","Aurion HEX Rubber Coated Cast Iron Hexagonal Dumbbells for Professional Exercise is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Aurion HEX Rubber Coated Cast Iron Hexagonal Dumbbells for Professional Exercise is not added to the cart.")
    def AddS8():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Bench Press Machine",6799,"6,799",Spaces(40-len("Bench Press Machine"))])
            messagebox.showinfo("Product Status","SPORTAL Foldable Multi Bench Press Workout Machine is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","SPORTAL Foldable Multi Bench Press Workout Machine is not added to the cart.")
    def AddS9():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Reach Exercise Cycle",6999,"6,999",Spaces(40-len("Reach Exercise Cycle"))])
            messagebox.showinfo("Product Status","Reach Air Bike Exercise Cycle is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Reach Air Bike Exercise Cycle is not added to the cart.")
    def AddS10():
        global sportsgym_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["RMOUR Punch Bag",2999,"2,999",Spaces(40-len("RMOUR Punch Bag"))])
            messagebox.showinfo("Product Status","RMOUR Filled Heavy Punch Bag is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","RMOUR Filled Heavy Punch Bag is not added to the cart.")
    add_sportsgym1=Button(lf_sportsgym1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS1).place(x=68,y=245)
    add_sportsgym2=Button(lf_sportsgym2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS2).place(x=68,y=245)
    add_sportsgym3=Button(lf_sportsgym3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS3).place(x=68,y=245)
    add_sportsgym4=Button(lf_sportsgym4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS4).place(x=68,y=245)
    add_sportsgym5=Button(lf_sportsgym5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS5).place(x=68,y=245)
    add_sportsgym6=Button(lf_sportsgym6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS6).place(x=68,y=245)
    add_sportsgym7=Button(lf_sportsgym7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS7).place(x=68,y=245)
    add_sportsgym8=Button(lf_sportsgym8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS8).place(x=68,y=245)
    add_sportsgym9=Button(lf_sportsgym9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS9).place(x=68,y=245)
    add_sportsgym10=Button(lf_sportsgym10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddS10).place(x=68,y=245)

######################################################Furniture##################################################################

furniture1_image=ImageTk.PhotoImage(Image.open("img\Furniture_1.jpeg"))
furniture2_image=ImageTk.PhotoImage(Image.open("img\Furniture_2.jpeg"))
furniture3_image=ImageTk.PhotoImage(Image.open("img\Furniture_3.jpeg"))
furniture4_image=ImageTk.PhotoImage(Image.open("img\Furniture_4.jpeg"))
furniture5_image=ImageTk.PhotoImage(Image.open("img\Furniture_5.jpeg"))
furniture6_image=ImageTk.PhotoImage(Image.open("img\Furniture_6.jpeg"))
furniture7_image=ImageTk.PhotoImage(Image.open("img\Furniture_7.jpeg"))
furniture8_image=ImageTk.PhotoImage(Image.open("img\Furniture_8.jpeg"))
furniture9_image=ImageTk.PhotoImage(Image.open("img\Furniture_9.jpeg"))
furniture10_image=ImageTk.PhotoImage(Image.open("img\Furniture_10.jpeg"))

#Furniture variables
furniture_list=[]


def FurnitureCall():
    Hideframe()
    lf_furniture1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture1.place(x=5,y=35,width=200,height=280)
    lf_furniture2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture2.place(x=210,y=35,width=200,height=280)
    lf_furniture3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture3.place(x=415,y=35,width=200,height=280)
    lf_furniture4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture4.place(x=620,y=35,width=200,height=280)
    lf_furniture5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture5.place(x=825,y=35,width=200,height=280)
    lf_furniture6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture6.place(x=5,y=310,width=200,height=280)
    lf_furniture7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture7.place(x=210,y=310,width=200,height=280)
    lf_furniture8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture8.place(x=415,y=310,width=200,height=280)
    lf_furniture9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture9.place(x=620,y=310,width=200,height=280)
    lf_furniture10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_furniture10.place(x=825,y=310,width=200,height=280)
    label_furniture_1=Label(lf_furniture1,image=furniture1_image,bd=2,justify="center").grid(row=0,column=0)
    label_furniture_2=Label(lf_furniture2,image=furniture2_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_3=Label(lf_furniture3,image=furniture3_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_4=Label(lf_furniture4,image=furniture4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_5=Label(lf_furniture5,image=furniture5_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_6=Label(lf_furniture6,image=furniture6_image,bd=2,justify="center").grid(row=0,column=0)
    label_furniture_7=Label(lf_furniture7,image=furniture7_image,bd=2,justify="center").grid(row=0,column=0)
    label_furniture_8=Label(lf_furniture8,image=furniture8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_9=Label(lf_furniture9,image=furniture9_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_furniture_10=Label(lf_furniture10,image=furniture10_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    name_furniture1=Label(lf_furniture1,text="Julian Wood 2 Door Wardrobe",font="arial 9",justify="center").grid(row=1,column=0,padx=10)
    name_furniture2=Label(lf_furniture2,text="Zuari Niko Engineered Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture2=Label(lf_furniture2,text="3 Door Wardrobe",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture3=Label(lf_furniture3,text="TADesign Vinicio Engineered",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture3=Label(lf_furniture3,text="Wood 3 Door Wardrobe",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture4=Label(lf_furniture4,text="Flipkart Perfect Homes Opus",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture4=Label(lf_furniture4,text="Engineered Wood",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture4=Label(lf_furniture4,text="Queen Box Bed",font="arial 9",justify="center").grid(row=3,column=0)
    name_furniture5=Label(lf_furniture5,text="Forzza Jasper Engineered",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture5=Label(lf_furniture5,text="Wood King Box Bed",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture6=Label(lf_furniture6,text="Zuari Wood TV Entertainwoment Unit",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_furniture7=Label(lf_furniture7,text="Forzza Belfast Engineered Wood",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    name_furniture7=Label(lf_furniture7,text="TV Entertainwoment Unit",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture8=Label(lf_furniture8,text="Kurlon Crescent Leatherette",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture8=Label(lf_furniture8,text="3 + 1 + 1 Black Sofa Set",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture9=Label(lf_furniture9,text="Suncrown Furniture Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture9=Label(lf_furniture9,text="Fabric 6 Seater Sofa",font="arial 9",justify="center").grid(row=2,column=0)
    name_furniture9=Label(lf_furniture9,text="3 + 2 + 1 Vanilla Cream Sofa Set",font="arial 9",justify="center").grid(row=3,column=0)
    name_furniture10=Label(lf_furniture10,text="Allie Wood Solid Wood",font="arial 9",justify="center").grid(row=1,column=0)
    name_furniture10=Label(lf_furniture10,text="6 Seater Dining Set",font="arial 9",justify="center").grid(row=2,column=0)
    price_furniture1=Label(lf_furniture1,text="Price: Rs.6,990",font="arial 9 bold").grid(row=2,column=0)
    price_furniture2=Label(lf_furniture2,text="Price: Rs.17,390",font="arial 9 bold").grid(row=3,column=0)
    price_furniture3=Label(lf_furniture3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_furniture4=Label(lf_furniture4,text="Price: Rs.12,290",font="arial 9 bold").grid(row=4,column=0)
    price_furniture5=Label(lf_furniture5,text="Price: Rs.13,640",font="arial 9 bold").grid(row=3,column=0)
    price_furniture6=Label(lf_furniture6,text="Price: Rs.6,590",font="arial 9 bold").grid(row=2,column=0)
    price_furniture7=Label(lf_furniture7,text="Price: Rs.14,999",font="arial 9 bold").grid(row=3,column=0)
    price_furniture8=Label(lf_furniture8,text="Price: Rs.24,490",font="arial 9 bold").grid(row=3,column=0)
    price_furniture9=Label(lf_furniture9,text="Price: Rs.36,854",font="arial 9 bold").grid(row=4,column=0)
    price_furniture10=Label(lf_furniture10,text="Price: Rs.26,999",font="arial 9 bold").grid(row=3,column=0)
    def AddF1():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Julian 2 Door Wardrobe",6990,"6,990",Spaces(40-len("Julian 2 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Julian Wood 2 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Julian Wood 2 Door Wardrobe is not added to the cart.")
    def AddF2():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Zuari 3 Door Wardrobe",17390,"17,390",Spaces(40-len("Zuari 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Zuari Niko Engineered Wood 3 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Zuari Niko Engineered Wood 3 Door Wardrobe is not added to the cart.")
    def AddF3():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["TADesign 3 Door Wardrobe",34999,"34,999",Spaces(40-len("TADesign 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","TADesign Vinicio Engineered Wood 3 Door Wardrobe is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","TADesign Vinicio Engineered Wood 3 Door Wardrobe is not added to the cart.")
    def AddF4():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Opus Queen Box Bed",12290,"12,290",Spaces(40-len("Opus Queen Box Bed"))])
            messagebox.showinfo("Product Status","Flipkart Perfect Homes Opus Engineered Wood Queen Box Bed is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Flipkart Perfect Homes Opus Engineered Wood Queen Box Bed is not added to the cart.")
    def AddF5():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Jasper King Box Bed",13640,"13,640",Spaces(40-len("Jasper King Box Bed"))])
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Jasper Engineered Wood King Box Bed is not added to the cart.")
    def AddF6():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Zuari TV Unit",6590,"6,590",Spaces(40-len("Zuari TV Unit"))])
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainwoment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Zuari Wood TV Entertainwoment Unit is not added to the cart.")
    def AddF7():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Forzza TV Unit",14999,"14,999",Spaces(40-len("Forzza TV Unit"))])
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainwoment Unit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Forzza Belfast Engineered Wood TV Entertainwoment Unit is not added to the cart.")
    def AddF8():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Kurlon Black Sofa Set",24490,"24,490",Spaces(40-len("Kurlon Black Sofa Set"))])
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kurlon Crescent Leatherette 3 + 1 + 1 Black Sofa Set is not added to the cart.")
    def AddF9():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Suncrown Cream Sofa Set",36854,"36,854",Spaces(40-len("Suncrown Cream Sofa Set"))])
            messagebox.showinfo("Product Status","Suncrown Furniture Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Suncrown Furniture Solid Wood Fabric 6 Seater Sofa 3 + 2 + 1 Vanilla Cream Sofa Set is not added to the cart.")
    def AddF10():
        global furniture_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            furniture_list.append(["Allie 6 Seater Dining Set",26999,"26,999",Spaces(40-len("Allie 6 Seater Dining Set"))])
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Allie Wood Solid Wood 6 Seater Dining Set is not added to the cart.")
    add_furniture1=Button(lf_furniture1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF1).place(x=68,y=245)
    add_furniture2=Button(lf_furniture2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF2).place(x=68,y=245)
    add_furniture3=Button(lf_furniture3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF3).place(x=68,y=245)
    add_furniture4=Button(lf_furniture4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF4).place(x=68,y=245)
    add_furniture5=Button(lf_furniture5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF5).place(x=68,y=245)
    add_furniture6=Button(lf_furniture6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF6).place(x=68,y=245)
    add_furniture7=Button(lf_furniture7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF7).place(x=68,y=245)
    add_furniture8=Button(lf_furniture8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF8).place(x=68,y=245)
    add_furniture9=Button(lf_furniture9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF9).place(x=68,y=245)
    add_furniture10=Button(lf_furniture10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddF10).place(x=68,y=245)

    
########################################################Computer and gaming#######################################################################

cg_1_image=ImageTk.PhotoImage(Image.open("img\cg_1.jpg"))
cg_2_image=ImageTk.PhotoImage(Image.open("img\cg_2.jpg"))
cg_3_image=ImageTk.PhotoImage(Image.open("img\cg_3.jpg"))
cg_4_image=ImageTk.PhotoImage(Image.open("img\cg_4.jpg"))
cg_5_image=ImageTk.PhotoImage(Image.open("img\cg_5.jpg"))
cg_6_image=ImageTk.PhotoImage(Image.open("img\cg_6.jpg"))
cg_7_image=ImageTk.PhotoImage(Image.open("img\cg_7.jpg"))
cg_8_image=ImageTk.PhotoImage(Image.open("img\cg_8.jpg"))
cg_9_image=ImageTk.PhotoImage(Image.open("img\cg_9.jpg"))
cg_10_image=ImageTk.PhotoImage(Image.open("img\cg_10.jpg"))

#cg_ variables
cg_list=[]

def cg_Call():
    Hideframe()
    
    lf_cg_1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_1.place(x=5,y=35,width=200,height=280)
    lf_cg_2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_2.place(x=210,y=35,width=200,height=280)
    lf_cg_3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_3.place(x=415,y=35,width=200,height=280)
    lf_cg_4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_4.place(x=620,y=35,width=200,height=280)
    lf_cg_5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_5.place(x=825,y=35,width=200,height=280)
    lf_cg_6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_6.place(x=5,y=310,width=200,height=280)
    lf_cg_7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_7.place(x=210,y=310,width=200,height=280)
    lf_cg_8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_8.place(x=415,y=310,width=200,height=280)
    lf_cg_9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_9.place(x=620,y=310,width=200,height=280)
    lf_cg_10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_cg_10.place(x=825,y=310,width=200,height=280)
    label_cg_1=Label(lf_cg_1,image=cg_1_image,bd=2,justify="center").grid(row=0,column=0)
    label_cg_2=Label(lf_cg_2,image=cg_2_image,bd=2,justify="center").grid(row=0,column=0)
    label_cg_3=Label(lf_cg_3,image=cg_3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_cg_4=Label(lf_cg_4,image=cg_4_image,bd=2,justify="center").grid(row=0,column=0)
    label_cg_5=Label(lf_cg_5,image=cg_5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_cg_6=Label(lf_cg_6,image=cg_6_image,bd=2,justify="center").grid(row=0,column=0)
    label_cg_7=Label(lf_cg_7,image=cg_7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_cg_8=Label(lf_cg_8,image=cg_8_image,bd=2,justify="center").grid(row=0,column=0)
    label_cg_9=Label(lf_cg_9,image=cg_9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_cg_10=Label(lf_cg_10,image=cg_10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_cg_1=Label(lf_cg_1,text="Acer Nitro Vg270 S 27 Inch \nLCD 1920 x 1080 Pixels Monitor \nLED IPS Gaming \n0.5 Ms Response Time \n165Hz Refresh Rate I HDR 10 I \nAMD Radeon Free Sync I (Black)",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_2=Label(lf_cg_2,text="Samsung 980 PRO 2TB \nUp to 7,000 MB/s \nPCIe 4.0 NVMe M.2 SSD",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_3=Label(lf_cg_3,text="Redgear MT02 Keyboard \nwith LED Modes",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_4=Label(lf_cg_4,text="Redgear A-10 Wired Gaming Mouse \nwith RGB LED",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_5=Label(lf_cg_5,text="Corsair 16 GB Vengeance \nLPX DDR4 3000MHz",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_6=Label(lf_cg_6,text="Green Soul Monster Ultimate \nGaming Chair",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_cg_7=Label(lf_cg_7,text="TP-Link Archer AC1200 Archer C6 \nWi-Fi Speed Up to 867 Mbps",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_8=Label(lf_cg_8,text="MSI GeForce RTX 3050 Ventus \n2X 8G OC 8GB GDDR6 128-bit",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_9=Label(lf_cg_9,text="Amd Ryzen 9 5950X Processor \n16 Cores 32 Threads",font="arial 9",justify="center").grid(row=1,column=0)
    name_cg_10=Label(lf_cg_10,text="HP v236w USB 2.0 \n64GB Pen Drive, Metal",font="arial 9",justify="center").grid(row=1,column=0)
    price_cg_1=Label(lf_cg_1,text="Price: Rs.15,899",font="arial 9 bold").grid(row=2,column=0)
    price_cg_2=Label(lf_cg_2,text="Price: Rs.4,999",font="arial 9 bold").grid(row=2,column=0)
    price_cg_3=Label(lf_cg_3,text="Price: Rs.998",font="arial 9 bold").grid(row=3,column=0)
    price_cg_4=Label(lf_cg_4,text="Price: Rs.299",font="arial 9 bold").grid(row=2,column=0)
    price_cg_5=Label(lf_cg_5,text="Price: Rs.4,495",font="arial 9 bold").grid(row=3,column=0)
    price_cg_6=Label(lf_cg_6,text="Price: Rs.18,700",font="arial 9 bold").grid(row=2,column=0)
    price_cg_7=Label(lf_cg_7,text="Price: Rs.2,549",font="arial 9 bold").grid(row=2,column=0)
    price_cg_8=Label(lf_cg_8,text="Price: Rs.28,189",font="arial 9 bold").grid(row=3,column=0)
    price_cg_9=Label(lf_cg_9,text="Price: Rs.53,999",font="arial 9 bold").grid(row=2,column=0)
    price_cg_10=Label(lf_cg_10,text="Price: Rs.429",font="arial 9 bold").grid(row=3,column=0)
    def AddG1():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["Acer Nitro Vg270 S 27 Inch Monitor",15,899,"15,899",Spaces(40-len("Grey Shirts"))])
            messagebox.showinfo("Product Status","Acer Nitro Vg270 S 27 Inch Monitor is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Acer Nitro Vg270 S 27 Inch Monitor is not added to the cart.")
    def AddG2():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["Samsung 980 PRO 2TB \nUp to 7,000 MB/s \nPCIe 4.0 NVMe M.2 SSD",4,999,"4,999",Spaces(40-len("Johny T-shirts"))])
            messagebox.showinfo("Product Status","Samsung 980 PRO 2TB \nUp to 7,000 MB/s \nPCIe 4.0 NVMe M.2 SSD is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung 980 PRO 2TB \nUp to 7,000 MB/s \nPCIe 4.0 NVMe M.2 SSD is not added to the cart.")
    def AddG3():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["Redgear MT02 Keyboard \nwith LED Modes",998,"998",Spaces(40-len("Spark Casual shoe"))])
            messagebox.showinfo("Product Status","Redgear MT02 Keyboard \nwith LED Modes) is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Redgear MT02 Keyboard \nwith LED Modes) is not added to the cart.")
    def AddG4():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["Redgear A-10 Wired Gaming Mouse \nwith RGB LED",299,"299",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","Redgear A-10 Wired Gaming Mouse \nwith RGB LED is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Redgear A-10 Wired Gaming Mouse \nwith RGB LEDs is not added to the cart.")
    def AddG5():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["Corsair 16 GB Vengeance \nLPX DDR4 3000MHz",4,495,"4,495",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","Corsair 16 GB Vengeance \nLPX DDR4 3000MHz is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Corsair 16 GB Vengeance \nLPX DDR4 3000MHz is not added to the cart.")
    def AddG6():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["Green Soul Monster Ultimate \nGaming Chair",18,700,"18,700",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Green Soul Monster Ultimate \nGaming Chair is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Green Soul Monster Ultimate \nGaming Chair is not added to the cart.")
    def AddG7():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["TP-Link Archer AC1200 Archer C6 \nWi-Fi Speed Up to 867 Mbps",2,549,"2,549",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","TP-Link Archer AC1200 Archer C6 \nWi-Fi Speed Up to 867 Mbps is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","TP-Link Archer AC1200 Archer C6 \nWi-Fi Speed Up to 867 Mbps is not added to the cart.")
    def AddG8():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["MSI GeForce RTX 3050 Ventus \n2X 8G OC 8GB GDDR6 128-bit",28,189,"28,189",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","MSI GeForce RTX 3050 Ventus \n2X 8G OC 8GB GDDR6 128-bit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","MSI GeForce RTX 3050 Ventus \n2X 8G OC 8GB GDDR6 128-bit is not added to the cart.")
    def AddG9():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["Amd Ryzen 9 5950X Processor \n16 Cores 32 Threads",53,999,"53,999",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Amd Ryzen 9 5950X Processor \n16 Cores 32 Threads is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Amd Ryzen 9 5950X Processor \n16 Cores 32 Threads is not added to the cart.")
    def AddG10():
        global cg_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            cg_list.append(["HP v236w USB 2.0 \n64GB Pen Drive, Metal",429,"429",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","HP v236w USB 2.0 \n64GB Pen Drive, Metal is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","HP v236w USB 2.0 \n64GB Pen Drive, Metal is not added to the cart.")
    add_cg_1=Button(lf_cg_1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1).place(x=68,y=245)
    add_cg_2=Button(lf_cg_2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2).place(x=68,y=245)
    add_cg_3=Button(lf_cg_3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3).place(x=68,y=245)
    add_cg_4=Button(lf_cg_4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4).place(x=68,y=245)
    add_cg_5=Button(lf_cg_5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5).place(x=68,y=245)
    add_cg_6=Button(lf_cg_6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6).place(x=68,y=245)
    add_cg_7=Button(lf_cg_7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7).place(x=68,y=245)
    add_cg_8=Button(lf_cg_8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8).place(x=68,y=245)
    add_cg_9=Button(lf_cg_9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9).place(x=68,y=245)
    add_cg_10=Button(lf_cg_10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10).place(x=68,y=245)

#############################################################auto's#########################################################

auto_1_image=ImageTk.PhotoImage(Image.open("img\muto_1.jpeg"))
auto_2_image=ImageTk.PhotoImage(Image.open("img\muto_2.jpg"))
auto_3_image=ImageTk.PhotoImage(Image.open("img\muto_3.jpg"))
auto_4_image=ImageTk.PhotoImage(Image.open("img\muto_4.jpg"))
auto_5_image=ImageTk.PhotoImage(Image.open("img\muto_5.jpg"))
auto_6_image=ImageTk.PhotoImage(Image.open("img\muto_6.jpg"))
auto_7_image=ImageTk.PhotoImage(Image.open("img\muto_7.jpg"))
auto_8_image=ImageTk.PhotoImage(Image.open("img\muto_8.jpg"))
auto_9_image=ImageTk.PhotoImage(Image.open("img\muto_9.jpg"))
auto_10_image=ImageTk.PhotoImage(Image.open("img\muto_10.jpg"))

#auto_ variables
auto_list=[]

def auto_Call():
    Hideframe()
    
    lf_auto_1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_1.place(x=5,y=35,width=200,height=280)
    lf_auto_2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_2.place(x=210,y=35,width=200,height=280)
    lf_auto_3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_3.place(x=415,y=35,width=200,height=280)
    lf_auto_4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_4.place(x=620,y=35,width=200,height=280)
    lf_auto_5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_5.place(x=825,y=35,width=200,height=280)
    lf_auto_6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_6.place(x=5,y=310,width=200,height=280)
    lf_auto_7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_7.place(x=210,y=310,width=200,height=280)
    lf_auto_8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_8.place(x=415,y=310,width=200,height=280)
    lf_auto_9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_9.place(x=620,y=310,width=200,height=280)
    lf_auto_10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_auto_10.place(x=825,y=310,width=200,height=280)
    label_auto_1=Label(lf_auto_1,image=auto_1_image,bd=2,justify="center").grid(row=0,column=0)
    label_auto_2=Label(lf_auto_2,image=auto_2_image,bd=2,justify="center").grid(row=0,column=0)
    label_auto_3=Label(lf_auto_3,image=auto_3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_auto_4=Label(lf_auto_4,image=auto_4_image,bd=2,justify="center").grid(row=0,column=0)
    label_auto_5=Label(lf_auto_5,image=auto_5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_auto_6=Label(lf_auto_6,image=auto_6_image,bd=2,justify="center").grid(row=0,column=0)
    label_auto_7=Label(lf_auto_7,image=auto_7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_auto_8=Label(lf_auto_8,image=auto_8_image,bd=2,justify="center").grid(row=0,column=0)
    label_auto_9=Label(lf_auto_9,image=auto_9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_auto_10=Label(lf_auto_10,image=auto_10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_auto_1=Label(lf_auto_1,text="Bentag Multicolour Helmet Lock",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_2=Label(lf_auto_2,text="SHOPEE Tubeless Puncture Kit",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_3=Label(lf_auto_3,text="Bike Cover For Yamaha FZ-S",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_4=Label(lf_auto_4,text="Coaxial Car Speakers",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_5=Label(lf_auto_5,text="NBOX - Car Mobile Holder",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_6=Label(lf_auto_6,text="Sterio Sound Amplifier \nUSB,AUX,MIC,BLUTHOOTH,AV",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_auto_7=Label(lf_auto_7,text="AutoPowerz Light For All Bike",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_8=Label(lf_auto_8,text="CARIZO Handle Grip Side Mirror \nfor Bajaj Pulsar 150 Type 1",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_9=Label(lf_auto_9,text="Castrol MAGNATEC \nEngine Oil for Petrol Cars 3L",font="arial 9",justify="center").grid(row=1,column=0)
    name_auto_10=Label(lf_auto_10,text="CARIZO Steering Wheel Cover \nNappa Leather (Dark Brown)",font="arial 9",justify="center").grid(row=1,column=0)
    price_auto_1=Label(lf_auto_1,text="Price: Rs.407",font="arial 9 bold").grid(row=2,column=0)
    price_auto_2=Label(lf_auto_2,text="Price: Rs.549",font="arial 9 bold").grid(row=2,column=0)
    price_auto_3=Label(lf_auto_3,text="Price: Rs.799",font="arial 9 bold").grid(row=3,column=0)
    price_auto_4=Label(lf_auto_4,text="Price: Rs.399",font="arial 9 bold").grid(row=2,column=0)
    price_auto_5=Label(lf_auto_5,text="Price: Rs.350",font="arial 9 bold").grid(row=3,column=0)
    price_auto_6=Label(lf_auto_6,text="Price: Rs.3,599",font="arial 9 bold").grid(row=2,column=0)
    price_auto_7=Label(lf_auto_7,text="Price: Rs.579",font="arial 9 bold").grid(row=2,column=0)
    price_auto_8=Label(lf_auto_8,text="Price: Rs.450",font="arial 9 bold").grid(row=3,column=0)
    price_auto_9=Label(lf_auto_9,text="Price: Rs.2,979",font="arial 9 bold").grid(row=2,column=0)
    price_auto_10=Label(lf_auto_10,text="Price: Rs.429",font="arial 9 bold").grid(row=3,column=0)
    def AddA1():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["Bentag Multicolour Helmet Lock",407,"407",Spaces(40-len("Grey Shirts"))])
            messagebox.showinfo("Product Status","Bentag Multicolour Helmet Lock is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bentag Multicolour Helmet Lock is not added to the cart.")
    def AddA2():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["SHOPEE Tubeless Puncture Kit",549,"549",Spaces(40-len("Johny T-shirts"))])
            messagebox.showinfo("Product Status","SHOPEE Tubeless Puncture Kit is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","SHOPEE Tubeless Puncture Kit is not added to the cart.")
    def AddA3():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["Bike Cover For Yamaha FZ-S",799,"799",Spaces(40-len("Spark Casual shoe"))])
            messagebox.showinfo("Product Status","Bike Cover For Yamaha FZ-S is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bike Cover For Yamaha FZ-S is not added to the cart.")
    def AddA4():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["Coaxial Car Speakers",399,"399",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","Coaxial Car Speakers is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Coaxial Car Speakers is not added to the cart.")
    def AddA5():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["NBOX - Car Mobile Holder",350,"350",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","NBOX - Car Mobile Holder is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","NBOX - Car Mobile Holder is not added to the cart.")
    def AddA6():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["Sterio Sound Amplifier",3,599,"3,599",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Sterio Sound Amplifier \nUSB,AUX,MIC,BLUTHOOTH,AV is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Sterio Sound Amplifier \nUSB,AUX,MIC,BLUTHOOTH,AV is not added to the cart.")
    def AddA7():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["AutoPowerz Light For All Bike",579,"579",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","AutoPowerz Light For All Bike is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","AutoPowerz Light For All Bike is not added to the cart.")
    def AddA8():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["CARIZO Handle Grip Side Mirror for Bike",450,"450",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","CARIZO Handle Grip Side Mirror for Bajaj Pulsar 150 Type 1 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","CARIZO Handle Grip Side Mirror for Bajaj Pulsar 150 Type 1 is not added to the cart.")
    def AddA9():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["Castrol MAGNATEC \nEngine Oil for Petrol Cars 3L",2,979,"2,979",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Castrol MAGNATEC \nEngine Oil for Petrol Cars 3L is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Castrol MAGNATEC \nEngine Oil for Petrol Cars 3L is not added to the cart.")
    def AddA10():
        global auto_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            auto_list.append(["CARIZO Steering Wheel Cover \nNappa Leather (Dark Brown)",429,"429",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","CARIZO Steering Wheel Cover \nNappa Leather (Dark Brown) is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bally autos Wallet Brown is not added to the cart.")
    add_auto_1=Button(lf_auto_1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA1).place(x=68,y=245)
    add_auto_2=Button(lf_auto_2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA2).place(x=68,y=245)
    add_auto_3=Button(lf_auto_3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA3).place(x=68,y=245)
    add_auto_4=Button(lf_auto_4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA4).place(x=68,y=245)
    add_auto_5=Button(lf_auto_5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA5).place(x=68,y=245)
    add_auto_6=Button(lf_auto_6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA6).place(x=68,y=245)
    add_auto_7=Button(lf_auto_7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA7).place(x=68,y=245)
    add_auto_8=Button(lf_auto_8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA8).place(x=68,y=245)
    add_auto_9=Button(lf_auto_9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA9).place(x=68,y=245)
    add_auto_10=Button(lf_auto_10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddA10).place(x=68,y=245)

#############################################################Home and Kitchen#########################################################

hk_1_image=ImageTk.PhotoImage(Image.open("img\hk_1.jpg"))
hk_2_image=ImageTk.PhotoImage(Image.open("img\hk_2.jpg"))
hk_3_image=ImageTk.PhotoImage(Image.open("img\hk_3.jpg"))
hk_4_image=ImageTk.PhotoImage(Image.open("img\hk_4.jpg"))
hk_5_image=ImageTk.PhotoImage(Image.open("img\hk_5.jpg"))
hk_6_image=ImageTk.PhotoImage(Image.open("img\hk_6.jpg"))
hk_7_image=ImageTk.PhotoImage(Image.open("img\hk_7.jpg"))
hk_8_image=ImageTk.PhotoImage(Image.open("img\hk_8.jpg"))
hk_9_image=ImageTk.PhotoImage(Image.open("img\hk_9.jpeg"))
hk_10_image=ImageTk.PhotoImage(Image.open("img\hk_10.jpg"))

#hk_ variables
hk_list=[]

def hk_Call():
    Hideframe()
    
    lf_hk_1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_1.place(x=5,y=35,width=200,height=280)
    lf_hk_2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_2.place(x=210,y=35,width=200,height=280)
    lf_hk_3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_3.place(x=415,y=35,width=200,height=280)
    lf_hk_4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_4.place(x=620,y=35,width=200,height=280)
    lf_hk_5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_5.place(x=825,y=35,width=200,height=280)
    lf_hk_6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_6.place(x=5,y=310,width=200,height=280)
    lf_hk_7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_7.place(x=210,y=310,width=200,height=280)
    lf_hk_8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_8.place(x=415,y=310,width=200,height=280)
    lf_hk_9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_9.place(x=620,y=310,width=200,height=280)
    lf_hk_10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hk_10.place(x=825,y=310,width=200,height=280)
    label_hk_1=Label(lf_hk_1,image=hk_1_image,bd=2,justify="center").grid(row=0,column=0)
    label_hk_2=Label(lf_hk_2,image=hk_2_image,bd=2,justify="center").grid(row=0,column=0)
    label_hk_3=Label(lf_hk_3,image=hk_3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_hk_4=Label(lf_hk_4,image=hk_4_image,bd=2,justify="center").grid(row=0,column=0)
    label_hk_5=Label(lf_hk_5,image=hk_5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_hk_6=Label(lf_hk_6,image=hk_6_image,bd=2,justify="center").grid(row=0,column=0)
    label_hk_7=Label(lf_hk_7,image=hk_7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_hk_8=Label(lf_hk_8,image=hk_8_image,bd=2,justify="center").grid(row=0,column=0)
    label_hk_9=Label(lf_hk_9,image=hk_9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_hk_10=Label(lf_hk_10,image=hk_10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_hk_1=Label(lf_hk_1,text="ZunVolt - 500W Mixer Grinder",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_2=Label(lf_hk_2,text="Aqua Grand Plus 12 Water Purifier",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_3=Label(lf_hk_3,text="Lifelong Gas Stove Manual Ignition",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_4=Label(lf_hk_4,text="Lifelong 750 Wat Sandwich Griller",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_5=Label(lf_hk_5,text="Master Perfect 5 L \nPressure Cooker Gas Stovetop",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_6=Label(lf_hk_6,text="Spotzero Elegant Spin Mop",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_hk_7=Label(lf_hk_7,text="Unikkus Heavy Padlock for home",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_8=Label(lf_hk_8,text="Brightflame bove3 Ltr Air Fryer",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_9=Label(lf_hk_9,text="HOMETALES Water Bottle",font="arial 9",justify="center").grid(row=1,column=0)
    name_hk_10=Label(lf_hk_10,text="Zovesty Plastic 3 Compartment",font="arial 9",justify="center").grid(row=1,column=0)
    price_hk_1=Label(lf_hk_1,text="Price: Rs.1,290",font="arial 9 bold").grid(row=2,column=0)
    price_hk_2=Label(lf_hk_2,text="Price: Rs.5,324",font="arial 9 bold").grid(row=2,column=0)
    price_hk_3=Label(lf_hk_3,text="Price: Rs.2,499",font="arial 9 bold").grid(row=3,column=0)
    price_hk_4=Label(lf_hk_4,text="Price: Rs.903",font="arial 9 bold").grid(row=2,column=0)
    price_hk_5=Label(lf_hk_5,text="Price: Rs.825",font="arial 9 bold").grid(row=3,column=0)
    price_hk_6=Label(lf_hk_6,text="Price: Rs.1,199",font="arial 9 bold").grid(row=2,column=0)
    price_hk_7=Label(lf_hk_7,text="Price: Rs.299",font="arial 9 bold").grid(row=2,column=0)
    price_hk_8=Label(lf_hk_8,text="Price: Rs.6,399",font="arial 9 bold").grid(row=3,column=0)
    price_hk_9=Label(lf_hk_9,text="Price: Rs.2,299",font="arial 9 bold").grid(row=2,column=0)
    price_hk_10=Label(lf_hk_10,text="Price: Rs.339",font="arial 9 bold").grid(row=3,column=0)
    def AddH1():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["Bentag Multicolour Cable Type Helmet Lock",1,290,"1,290",Spaces(40-len("Grey Shirts"))])
            messagebox.showinfo("Product Status","Bentag Multicolour Cable Type Helmet Lock is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bentag Multicolour Cable Type Helmet Lock is not added to the cart.")
    def AddH2():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["SHOPEE Tubeless Tyre Puncture Repair Kit 5 - 10 Strips",5,324,"5,324",Spaces(40-len("Johny T-shirts"))])
            messagebox.showinfo("Product Status","SHOPEE Tubeless Tyre Puncture Repair Kit 5 - 10 Strips is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","SHOPEE Tubeless Tyre Puncture Repair Kit 5 - 10 Strips is not added to the cart.")
    def AddH3():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["HOMETALES Dustproof Bike Cover For Yamaha FZ-S with Mirror Pocket - Red & Blue",2,499,"2,499",Spaces(40-len("Spark Casual shoe"))])
            messagebox.showinfo("Product Status","HOMETALES Dustproof Bike Cover For Yamaha FZ-S with Mirror Pocket - Red & Blue is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","HOMETALES Dustproof Bike Cover For Yamaha FZ-S with Mirror Pocket - Red & Blue is not added to the cart.")
    def AddH4():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["GoMechanic Coaxial Car Speakers",903,"903",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","GoMechanic Coaxial Car Speakers is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GoMechanic Coaxial Car Speakers is not added to the cart.")
    def AddH5():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["NBOX - Black Horizontal Clip Car Mobile Holder",825,"825",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","NBOX - Black Horizontal Clip Car Mobile Holder is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","NBOX - Black Horizontal Clip Car Mobile Holder is not added to the cart.")
    def AddH6():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["Tech-lobby® Sterio Sound Amplifier with USB,AUX,MIC,BLUTHOOTH,AV",1,199,"1,199",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Tech-lobby® Sterio Sound Amplifier with USB,AUX,MIC,BLUTHOOTH,AV is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Tech-lobby® Sterio Sound Amplifier with USB,AUX,MIC,BLUTHOOTH,AV is not added to the cart.")
    def AddH7():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["hkPowerz - Front Left & Right Fog Light For All Car and Bike",299,"299",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","hkPowerz - Front Left & Right Fog Light For All Car and Bike is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","hkPowerz - Front Left & Right Fog Light For All Car and Bike is not added to the cart.")
    def AddH8():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["CARIZO Handle Grip Side Mirror for Bajaj Pulsar 150 Type 1",6,399,"6,399",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","CARIZO Handle Grip Side Mirror for Bajaj Pulsar 150 Type 1 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","CARIZO Handle Grip Side Mirror for Bajaj Pulsar 150 Type 1 is not added to the cart.")
    def AddH9():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["Castrol MAGNATEC STOP-START 0W-20 Full Synthetic Engine Oil for Petrol Cars 3L",2,299,"2,299",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Castrol MAGNATEC STOP-START 0W-20 Full Synthetic Engine Oil for Petrol Cars 3L is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Castrol MAGNATEC STOP-START 0W-20 Full Synthetic Engine Oil for Petrol Cars 3L is not added to the cart.")
    def AddH10():
        global hk_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hk_list.append(["CARIZO Steering Wheel Cover Nappa Leather Grips (Dark Brown)",339,"339",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","CARIZO Steering Wheel Cover Nappa Leather Grips (Dark Brown) is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bally hks Wallet Brown is not added to the cart.")
    add_hk_1=Button(lf_hk_1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH1).place(x=68,y=245)
    add_hk_2=Button(lf_hk_2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH2).place(x=68,y=245)
    add_hk_3=Button(lf_hk_3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH3).place(x=68,y=245)
    add_hk_4=Button(lf_hk_4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH4).place(x=68,y=245)
    add_hk_5=Button(lf_hk_5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH5).place(x=68,y=245)
    add_hk_6=Button(lf_hk_6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH6).place(x=68,y=245)
    add_hk_7=Button(lf_hk_7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH7).place(x=68,y=245)
    add_hk_8=Button(lf_hk_8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH8).place(x=68,y=245)
    add_hk_9=Button(lf_hk_9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH9).place(x=68,y=245)
    add_hk_10=Button(lf_hk_10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddH10).place(x=68,y=245)

#############################################################Books and Media#########################################################

bm_1_image=ImageTk.PhotoImage(Image.open("img\mm_1.jpg"))
bm_2_image=ImageTk.PhotoImage(Image.open("img\mm_2.png"))
bm_3_image=ImageTk.PhotoImage(Image.open("img\mm_3.jpg"))
bm_4_image=ImageTk.PhotoImage(Image.open("img\mm_4.jpg"))
bm_5_image=ImageTk.PhotoImage(Image.open("img\mm_5.jpg"))
bm_6_image=ImageTk.PhotoImage(Image.open("img\mm_6.jpg"))
bm_7_image=ImageTk.PhotoImage(Image.open("img\mm_7.jpg"))
bm_8_image=ImageTk.PhotoImage(Image.open("img\mm_8.jpg"))
bm_9_image=ImageTk.PhotoImage(Image.open("img\mm_9.jpg"))
bm_10_image=ImageTk.PhotoImage(Image.open("img\mm_10.jpg"))

#bm_ variables
bm_list=[]

def bm_Call():
    Hideframe()
    
    lf_bm_1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_1.place(x=5,y=35,width=200,height=280)
    lf_bm_2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_2.place(x=210,y=35,width=200,height=280)
    lf_bm_3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_3.place(x=415,y=35,width=200,height=280)
    lf_bm_4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_4.place(x=620,y=35,width=200,height=280)
    lf_bm_5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_5.place(x=825,y=35,width=200,height=280)
    lf_bm_6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_6.place(x=5,y=310,width=200,height=280)
    lf_bm_7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_7.place(x=210,y=310,width=200,height=280)
    lf_bm_8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_8.place(x=415,y=310,width=200,height=280)
    lf_bm_9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_9.place(x=620,y=310,width=200,height=280)
    lf_bm_10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_bm_10.place(x=825,y=310,width=200,height=280)
    label_bm_1=Label(lf_bm_1,image=bm_1_image,bd=2,justify="center").grid(row=0,column=0)
    label_bm_2=Label(lf_bm_2,image=bm_2_image,bd=2,justify="center").grid(row=0,column=0)
    label_bm_3=Label(lf_bm_3,image=bm_3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_bm_4=Label(lf_bm_4,image=bm_4_image,bd=2,justify="center").grid(row=0,column=0)
    label_bm_5=Label(lf_bm_5,image=bm_5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_bm_6=Label(lf_bm_6,image=bm_6_image,bd=2,justify="center").grid(row=0,column=0)
    label_bm_7=Label(lf_bm_7,image=bm_7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_bm_8=Label(lf_bm_8,image=bm_8_image,bd=2,justify="center").grid(row=0,column=0)
    label_bm_9=Label(lf_bm_9,image=bm_9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_bm_10=Label(lf_bm_10,image=bm_10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_bm_1=Label(lf_bm_1,text="Crash Course for NEET Physics",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_2=Label(lf_bm_2,text="Brief history Modern india",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_3=Label(lf_bm_3,text="Kadence Frontier guitar",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_4=Label(lf_bm_4,text="Yamaha PSR-I400 61-Key \nPortable Keyboard",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_5=Label(lf_bm_5,text="Ram Lakhan Musical Instruments \nProfessional Acoustic Violin",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_6=Label(lf_bm_6,text="Titanic Blu-ray 3D & Blu-ray",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_bm_7=Label(lf_bm_7,text="Fast & Furious 3: Tokyo Drift",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_8=Label(lf_bm_8,text="MakeMyTrip E-Gift Card 3000",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_9=Label(lf_bm_9,text="MakeMyTrip Holiday E-Gift Card",font="arial 9",justify="center").grid(row=1,column=0)
    name_bm_10=Label(lf_bm_10,text="Google Play E-Gift Card \nRedeemable on Play Store",font="arial 9",justify="center").grid(row=1,column=0)
    price_bm_1=Label(lf_bm_1,text="Price: Rs.342",font="arial 9 bold").grid(row=2,column=0)
    price_bm_2=Label(lf_bm_2,text="Price: Rs.289",font="arial 9 bold").grid(row=2,column=0)
    price_bm_3=Label(lf_bm_3,text="Price: Rs.4,949",font="arial 9 bold").grid(row=3,column=0)
    price_bm_4=Label(lf_bm_4,text="Price: Rs.17,300",font="arial 9 bold").grid(row=2,column=0)
    price_bm_5=Label(lf_bm_5,text="Price: Rs.8,000",font="arial 9 bold").grid(row=3,column=0)
    price_bm_6=Label(lf_bm_6,text="Price: Rs.2,499",font="arial 9 bold").grid(row=2,column=0)
    price_bm_7=Label(lf_bm_7,text="Price: Rs.750",font="arial 9 bold").grid(row=2,column=0)
    price_bm_8=Label(lf_bm_8,text="Price: Rs.2,910",font="arial 9 bold").grid(row=3,column=0)
    price_bm_9=Label(lf_bm_9,text="Price: Rs.40,000",font="arial 9 bold").grid(row=2,column=0)
    price_bm_10=Label(lf_bm_10,text="Price: Rs.100",font="arial 9 bold").grid(row=3,column=0)
    def AddBM1():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["40 Days Crash Course for NEET Physics",342,"342",Spaces(40-len("Grey Shirts"))])
            messagebox.showinfo("Product Status","B40 Days Crash Course for NEET Physics is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","40 Days Crash Course for NEET Physics is not added to the cart.")
    def AddBM2():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["BRIEF HISTORY OF MODERN INDIA(LATEST 2022)",289,"289",Spaces(40-len("Johny T-shirts"))])
            messagebox.showinfo("Product Status","SHOPEE Tubeless Tyre Puncture Repair Kit 5 - 10 Strips is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","BRIEF HISTORY OF MODERN INDIA(LATEST 2022) is not added to the cart.")
    def AddBM3():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["Kadence Frontier guitar",4,949,"4,949",Spaces(40-len("Spark Casual shoe"))])
            messagebox.showinfo("Product Status","Kadence Frontier guitar is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Kadence Frontier guitar not added to the cart.")
    def AddBM4():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["Yamaha PSR-I400 61-Key Portable Keyboard",17,300,"17,300",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","Yamaha PSR-I400 61-Key Portable Keyboardis successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Yamaha PSR-I400 61-Key Portable Keyboard is not added to the cart.")
    def AddBM5():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["Ram Lakhan Musical Instruments \nProfessional Acoustic Violin",8,000,"8,000",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","Ram Lakhan Musical Instruments \nProfessional Acoustic Violin is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Ram Lakhan Musical Instruments \nProfessional Acoustic Violin is not added to the cart.")
    def AddBM6():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["Titanic Blu-ray 3D & Blu-ray",2,499,"2,499",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Titanic Blu-ray 3D & Blu-ray is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Titanic Blu-ray 3D & Blu-ray is not added to the cart.")
    def AddBM7():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["Fast & Furious 3: Tokyo Drift",750,"750",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Fast & Furious 3: Tokyo Drift is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Fast & Furious 3: Tokyo Drift is not added to the cart.")
    def AddBM8():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["MakeMyTrip E-Gift Card 3000",2,910,"2,910",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","MakeMyTrip E-Gift Card 3000 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","MakeMyTrip E-Gift Card 3000 is not added to the cart.")
    def AddBM9():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["MakeMyTrip Holiday E-Gift Card",40,000,"40,000",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","MakeMyTrip Holiday E-Gift Card is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","MakeMyTrip Holiday E-Gift Card is not added to the cart.")
    def AddBM10():
        global bm_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            bm_list.append(["Google Play E-Gift Card \nRedeemable on Play Store",100,"100",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Google Play E-Gift Card \nRedeemable on Play Store is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Google Play E-Gift Card \nRedeemable on Play Store is not added to the cart.")
    add_bm_1=Button(lf_bm_1,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM1).place(x=68,y=245)
    add_bm_2=Button(lf_bm_2,text="Add Item",bg="#ff9f00",fg="white",font="times 9 bold",command=AddBM2).place(x=68,y=245)
    add_bm_3=Button(lf_bm_3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM3).place(x=68,y=245)
    add_bm_4=Button(lf_bm_4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM4).place(x=68,y=245)
    add_bm_5=Button(lf_bm_5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM5).place(x=68,y=245)
    add_bm_6=Button(lf_bm_6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM6).place(x=68,y=245)
    add_bm_7=Button(lf_bm_7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM7).place(x=68,y=245)
    add_bm_8=Button(lf_bm_8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM8).place(x=68,y=245)
    add_bm_9=Button(lf_bm_9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM9).place(x=68,y=245)
    add_bm_10=Button(lf_bm_10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddBM10).place(x=68,y=245)

#############################################################Beauty and Health#########################################################

hlt_1_image=ImageTk.PhotoImage(Image.open("img\hlt_1.jpg"))
hlt_2_image=ImageTk.PhotoImage(Image.open("img\hlt_2.jpg"))
hlt_3_image=ImageTk.PhotoImage(Image.open("img\hlt_3.jpg"))
hlt_4_image=ImageTk.PhotoImage(Image.open("img\hlt_4.jpg"))
hlt_5_image=ImageTk.PhotoImage(Image.open("img\hlt_5.jpg"))
hlt_6_image=ImageTk.PhotoImage(Image.open("img\hlt_6.jpg"))
hlt_7_image=ImageTk.PhotoImage(Image.open("img\hlt_7.jpg"))
hlt_8_image=ImageTk.PhotoImage(Image.open("img\hlt_8.jpeg"))
hlt_9_image=ImageTk.PhotoImage(Image.open("img\hlt_9.jpg"))
hlt_10_image=ImageTk.PhotoImage(Image.open("img\hlt_10.jpg"))

#hlt_ variables
hlt_list=[]

def hlt_Call():
    Hideframe()
    
    lf_hlt_1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_1.place(x=5,y=35,width=200,height=280)
    lf_hlt_2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_2.place(x=210,y=35,width=200,height=280)
    lf_hlt_3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_3.place(x=415,y=35,width=200,height=280)
    lf_hlt_4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_4.place(x=620,y=35,width=200,height=280)
    lf_hlt_5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_5.place(x=825,y=35,width=200,height=280)
    lf_hlt_6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_6.place(x=5,y=310,width=200,height=280)
    lf_hlt_7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_7.place(x=210,y=310,width=200,height=280)
    lf_hlt_8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_8.place(x=415,y=310,width=200,height=280)
    lf_hlt_9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_9.place(x=620,y=310,width=200,height=280)
    lf_hlt_10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_hlt_10.place(x=825,y=310,width=200,height=280)
    label_hlt_1=Label(lf_hlt_1,image=hlt_1_image,bd=2,justify="center").grid(row=0,column=0)
    label_hlt_2=Label(lf_hlt_2,image=hlt_2_image,bd=2,justify="center").grid(row=0,column=0)
    label_hlt_3=Label(lf_hlt_3,image=hlt_3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_hlt_4=Label(lf_hlt_4,image=hlt_4_image,bd=2,justify="center").grid(row=0,column=0)
    label_hlt_5=Label(lf_hlt_5,image=hlt_5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_hlt_6=Label(lf_hlt_6,image=hlt_6_image,bd=2,justify="center").grid(row=0,column=0)
    label_hlt_7=Label(lf_hlt_7,image=hlt_7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_hlt_8=Label(lf_hlt_8,image=hlt_8_image,bd=2,justify="center").grid(row=0,column=0)
    label_hlt_9=Label(lf_hlt_9,image=hlt_9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_hlt_10=Label(lf_hlt_10,image=hlt_10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_hlt_1=Label(lf_hlt_1,text="Miyuki Black Kajal 54 g Pencil",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_2=Label(lf_hlt_2,text="VVQVV Onlion black Shampoo",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_3=Label(lf_hlt_3,text="Indo challenge 30mL Beard Oil",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_4=Label(lf_hlt_4,text="OZiva Superfood Plant Protein",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_5=Label(lf_hlt_5,text="Omron HEM 7124 Fully Automatic \nDigital Blood Pressure Monitor",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_6=Label(lf_hlt_6,text="Venus Weighing Scales",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_hlt_7=Label(lf_hlt_7,text="Alainne - Room Freshener Spray",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_8=Label(lf_hlt_8,text="Natural Glow Facial Kit",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_9=Label(lf_hlt_9,text="PaxClean All Purpose Cleaner",font="arial 9",justify="center").grid(row=1,column=0)
    name_hlt_10=Label(lf_hlt_10,text="NIINE - S Diaper Pants",font="arial 9",justify="center").grid(row=1,column=0)
    price_hlt_1=Label(lf_hlt_1,text="Price: Rs.209",font="arial 9 bold").grid(row=2,column=0)
    price_hlt_2=Label(lf_hlt_2,text="Price: Rs.179",font="arial 9 bold").grid(row=2,column=0)
    price_hlt_3=Label(lf_hlt_3,text="Price: Rs.130",font="arial 9 bold").grid(row=3,column=0)
    price_hlt_4=Label(lf_hlt_4,text="Price: Rs.1,104",font="arial 9 bold").grid(row=2,column=0)
    price_hlt_5=Label(lf_hlt_5,text="Price: Rs.1,599",font="arial 9 bold").grid(row=3,column=0)
    price_hlt_6=Label(lf_hlt_6,text="Price: Rs.675",font="arial 9 bold").grid(row=2,column=0)
    price_hlt_7=Label(lf_hlt_7,text="Price: Rs.179",font="arial 9 bold").grid(row=2,column=0)
    price_hlt_8=Label(lf_hlt_8,text="Price: Rs.269",font="arial 9 bold").grid(row=3,column=0)
    price_hlt_9=Label(lf_hlt_9,text="Price: Rs.725",font="arial 9 bold").grid(row=2,column=0)
    price_hlt_10=Label(lf_hlt_10,text="Price: Rs.349",font="arial 9 bold").grid(row=3,column=0)
    def Addhlt1():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["Miyuki - Black Matte Kajal 54 g Pencil",342,"342",Spaces(40-len("Grey Shirts"))])
            messagebox.showinfo("Product Status","Miyuki - Black Matte Kajal 54 g Pencil is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Miyuki - Black Matte Kajal 54 g Pencil is not added to the cart.")
    def Addhlt2():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["VVQVV ONION BLACK SEED Shampoo 300 mL",289,"289",Spaces(40-len("Johny T-shirts"))])
            messagebox.showinfo("Product Status","VVQVV ONION BLACK SEED Shampoo 300 mL is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","VVQVV ONION BLACK SEED Shampoo 300 mL) is not added to the cart.")
    def Addhlt3():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["INDO CHALLENGE - 30mL Anti Dandruff Beard Oil",130,"130",Spaces(40-len("Spark Casual shoe"))])
            messagebox.showinfo("Product Status","INDO CHALLENGE - 30mL Anti Dandruff Beard Oil is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","INDO CHALLENGE - 30mL Anti Dandruff Beard Oil not added to the cart.")
    def Addhlt4():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["OZiva Superfood Plant Protein",1,104,"1,104",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","OZiva Superfood Plant Protein is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OZiva Superfood Plant Protein is not added to the cart.")
    def Addhlt5():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["Omron HEM 7124 Fully Automatic Digital Blood Pressure Monitor",1,599,"1,599",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","Omron HEM 7124 Fully Automatic Digital Blood Pressure Monitor is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Omron HEM 7124 Fully Automatic Digital Blood Pressure Monitor is not added to the cart.")
    def Addhlt6():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["Venus Electronic Digital LCD Body Weighing Scales",675,"675",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Venus Electronic Digital LCD Body Weighing Scales is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Venus Electronic Digital LCD Body Weighing Scales is not added to the cart.")
    def Addhlt7():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["Alainne - Room Freshener Spray",179,"179",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Alainne - Room Freshener Spray is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Alainne - Room Freshener Spray is not added to the cart.")
    def Addhlt8():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["Professional - Natural Glow Facial Kit For All Skin Type",269,"269",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Professional - Natural Glow Facial Kit For All Skin Type is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Professional - Natural Glow Facial Kit For All Skin Type is not added to the cart.")
    def Addhlt9():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["PaxClean All Purpose Cleaner",725,"725",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","PaxClean All Purpose Cleaner is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","PaxClean All Purpose Cleaner is not added to the cart.")
    def Addhlt10():
        global hlt_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            hlt_list.append(["NIINE - S Diaper Pants",349,"349",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","NIINE - S Diaper Pants is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","NIINE - S Diaper Pants is not added to the cart.")
    add_hlt_1=Button(lf_hlt_1,text="Add Item",bg="#ff9f00",fg="white",font="times 9 bold",command=Addhlt1).place(x=68,y=245)
    add_hlt_2=Button(lf_hlt_2,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt2).place(x=68,y=245)
    add_hlt_3=Button(lf_hlt_3,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt3).place(x=68,y=245)
    add_hlt_4=Button(lf_hlt_4,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt4).place(x=68,y=245)
    add_hlt_5=Button(lf_hlt_5,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt5).place(x=68,y=245)
    add_hlt_6=Button(lf_hlt_6,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt6).place(x=68,y=245)
    add_hlt_7=Button(lf_hlt_7,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt7).place(x=68,y=245)
    add_hlt_8=Button(lf_hlt_8,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt8).place(x=68,y=245)
    add_hlt_9=Button(lf_hlt_9,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt9).place(x=68,y=245)
    add_hlt_10=Button(lf_hlt_10,text="Add Item",bg="green",fg="white",font="times 9 bold",command=Addhlt10).place(x=68,y=245)

 
    
########################################################billig#######################################################################

def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        global i,j,k,l,f,n,o,p,q,r,s,t
        global total_price,mk_pay,bill_txt_area
        Products_frame.destroy()
        Hideframe()
        frame4.destroy()
        head.destroy()
        auto_price=0
        hk_price=0
        bm_price=0
        cg_price=0
        men_price=0
        women_price=0
        hlt_price=0
        grocery_price=0
        electronics_price=0
        sportsgym_price=0
        furniture_price=0
        appliances_price=0
        for r in range(len(cg_list)):
            cg_price+=cg_list[r][1]
        for i in range(len(men_list)):
            men_price+=men_list[i][1]
        for k in range(len(women_list)):
            women_price+=women_list[k][1]
        for l in range(len(grocery_list)):
            grocery_price+=grocery_list[l][1]
        for j in range(len(bm_list)):
            bm_price+=bm_list[j][1]
        for f in range(len(hlt_list)):
            hlt_price+=hlt_list[f][1]   
        for s in range(len(hk_list)):
            hk_price+=hk_list[s][1]    
        for n in range(len(electronics_list)):
            electronics_price+=electronics_list[n][1]
        for o in range(len(sportsgym_list)):
            sportsgym_price+=sportsgym_list[o][1]
        for p in range(len(furniture_list)):
            furniture_price+=furniture_list[p][1]
        for q in range(len(auto_list)):
            auto_price+=auto_list[q][1]    
        for t in range(len(appliances_list)):
            appliances_price+=appliances_list[t][1]
        total_price=auto_price+hk_price+hlt_price+bm_price+cg_price+men_price+women_price+grocery_price+electronics_price+sportsgym_price+furniture_price+appliances_price

        bill_area=LabelFrame(m,bd=2,relief="groove")
        bill_area.place(x=305,y=80,width=750,height=600)
        bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
        scroll_y=Scrollbar(bill_area,orient=VERTICAL)
        bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=bill_txt_area.yview)
        bill_txt_area.pack(fill=BOTH,expand=1)
        bill_txt_area.insert(END,Spaces(40)+"Vkart shopping\n"+Spaces(90,'*')+"\n")
        if len(men_list)>0:
            bill_txt_area.insert(END,"Men's Fasion \n\nProduct Name"+Spaces(28)+"Price\n")
            for i in men_list:
                bill_txt_area.insert(END,str(i[0])+str(i[3])+"Rs."+str(i[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Mens's Fasion : Rs."+str(men_price)+"\n"+Spaces(90,'*'))
        if len(bm_list)>0:
            bill_txt_area.insert(END,"Home and Kitchen \n\nProduct Name"+Spaces(28)+"Price\n")
            for j in bm_list:
                bill_txt_area.insert(END,str(j[0])+str(j[3])+"Rs."+str(j[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Books,Music Price : Rs."+str(bm_price)+"\n"+Spaces(90,'*'))    
        if len(women_list)>0:
            bill_txt_area.insert(END,"Women's Fasion \n\nProduct Name"+Spaces(28)+"Price\n")
            for k in women_list:
                bill_txt_area.insert(END,str(k[0])+str(k[3])+"Rs."+str(k[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Womens's Fasion : Rs."+str(women_price)+"\n"+Spaces(90,'*'))
        if len(grocery_list)>0:
            bill_txt_area.insert(END,"Grocery Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
            for l in grocery_list:
                bill_txt_area.insert(END,str(l[0])+str(l[3])+"Rs."+str(l[1])+Spaces(27-len(str(l[1])))+l[2]+"\n")
            bill_txt_area.insert(END,"\nTotal Grocery Price : Rs."+str(grocery_price)+"\n"+Spaces(90,'*')+"\n")
        if len(hlt_list)>0:
            bill_txt_area.insert(END,"Beauty and Health \n\nProduct Name"+Spaces(28)+"Price\n")
            for f in hlt_list:
                bill_txt_area.insert(END,str(f[0])+str(f[3])+"Rs."+str(f[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Beauty and Health Price : Rs."+str(hlt_price)+"\n"+Spaces(90,'*'))    
        if len(electronics_list)>0:
            bill_txt_area.insert(END,"Electronics Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
            for n in electronics_list:
                bill_txt_area.insert(END,str(n[0])+str(n[3])+"Rs."+str(n[2])+Spaces(27-len(n[2]))+n[3]+"\n")
            bill_txt_area.insert(END,"\nTotal Electronics Price : Rs."+str(electronics_price)+"\n"+Spaces(90,'*')+"\n")
        if len(sportsgym_list)>0:
            bill_txt_area.insert(END,"Sports and Gym Equipwoment(s)\n\nProduct Name"+Spaces(28)+"Price\n")
            for o in sportsgym_list:
                bill_txt_area.insert(END,str(o[0])+str(o[3])+"Rs."+str(o[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Sports and Gym Equipwoment Price : Rs."+str(sportsgym_price)+"\n"+Spaces(90,'*')+"\n")
        if len(furniture_list)>0:
            bill_txt_area.insert(END,"Furniture Product(s)\n\nProduct Name"+Spaces(28)+"Price\n")
            for p in furniture_list:
                bill_txt_area.insert(END,str(p[0])+str(p[3])+"Rs."+str(p[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Furniture Price : Rs."+str(furniture_price)+"\n"+Spaces(90,'*')+"\n")
        if len(auto_list)>0:
            bill_txt_area.insert(END,"Automotive \n\nProduct Name"+Spaces(28)+"Price\n")
            for q in auto_list:
                bill_txt_area.insert(END,str(q[0])+str(q[3])+"Rs."+str(q[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Automotive Price : Rs."+str(auto_price)+"\n"+Spaces(90,'*'))
        if len(cg_list)>0:
            bill_txt_area.insert(END,"Computer and Gaming \n\nProduct Name"+Spaces(28)+"Price\n")
            for r in cg_list:
                bill_txt_area.insert(END,str(r[0])+str(r[3])+"Rs."+str(r[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Computer and Gaming price : Rs."+str(cg_price)+"\n"+Spaces(90,'*'))
        if len(hk_list)>0:
            bill_txt_area.insert(END,"Home and Kitchen \n\nProduct Name"+Spaces(28)+"Price\n")
            for s in hk_list:
                bill_txt_area.insert(END,str(s[0])+str(s[3])+"Rs."+str(s[2])+"\n")
            bill_txt_area.insert(END,"\nTotal Home and Kitchen : Rs."+str(hk_price)+"\n"+Spaces(90,'*'))    
        if len(appliances_list)>0:
            bill_txt_area.insert(END,"Appliance(s)\n\nProduct Name"+Spaces(28)+"Price\n")
            for t in appliances_list:
                bill_txt_area.insert(END,str(t[0])+str(t[3])+"Rs."+t[2]+"\n")
            bill_txt_area.insert(END,"\nTotal Appliances Price : Rs."+str(appliances_price)+"\n"+Spaces(90,'*'))
        bill_txt_area.insert(END,"\nTotal Price = Rs."+str(total_price))


            
        mk_pay=Button(m,text="Make Payment",font="times 20 bold",bd=6,bg="skyblue",width=12,cursor="hand2",command=payment,fg="white")
        mk_pay.place(x=1110,y=600)
        
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
        
        
   

def itemstoredb():
    a = i[0]
    c = p[0]
    
    item_store = SQL.connect(host = "localhost",user = "root",database="shopping")
    item = item_store.cursor()
    
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    values_str = ','.join([str(a), str(c)])
    
    insert_query = "INSERT INTO `purchase_details`(`username`,`item_purchased` ,`Total_price`,`Dateandtime`) VALUES (%s,%s,%s,%s)"
    vals =(userf[0],values_str,total_price,formatted_date,)
    item.execute(insert_query,vals)
    item_store.commit()

def help_center():
    messagebox.showinfo("Help Centre","Call 1800-050-6111 For Support")

def app():
    messagebox.showinfo("Download App","Our app is under development we I'll notify you once it came back")

def gift():
    messagebox.showinfo("Giftcards","Currently no gift Cards are available")
    

#Frame
#main_frame = Frame(m,height = 1080,width = 1920,bg = "#eeeee4")
bfhead = Frame(m,height = 28,width = 1920,bg = "#4988d1")
head = Frame(m,height = 88,width = 1920,bg = "#57a1f8")



logo = ImageTk.PhotoImage(Image.open("img\logo.png"))
label_logo = Label(head, image = logo,bd=0).place(x = 35,y = -12)
log = Label(head, text = "shopping",font="MathSans 18",bg="#57a1f8",fg="white").place(x = 120,y = 28)
slogan = Label(bfhead, text = "Shop till you drop",font="Times 12",bg="#4988d1",fg="white").place(x = 45,y = 1)
#button login
sign = Button(head,text = "SignIn👨",relief = FLAT,width = 7,height = 1,cursor="hand2",command=signin_main,font= ('MathSans'),bg = "#57a1f8",fg = "#ffffff",activebackground="#57a1f8")

cart = Button(head,text = "Cart🛒",relief = FLAT,width = 7,height = 1,cursor="hand2",command=Bill, font= ('MathSans'), bg = "#57a1f8",fg = "#ffffff",activebackground="#57a1f8").place(x=1150,y=25)

#button title
dwnl = Button(m,text = "📱Download App",relief = FLAT,width = 12,cursor="hand2",height = 1,command=app, bg = "#4988d1",fg = "#ffffff").place(x=1200,y=1)
helpc = Button(m,text = "HelpCentre",relief = FLAT,width = 8,cursor="hand2",height = 1,command=help_center, bg = "#4988d1",fg = "#ffffff").place(x=1100,y=1)
gift = Button(m,text = "GiftCards",relief = FLAT,width = 7,cursor="hand2",height = 1,command=gift, bg = "#4988d1",fg = "#ffffff").place(x=1000,y=1)

#search
ser = Button(head,text = "🔍Search",relief = FLAT,width = 10,height = 1,cursor="hand2",font= ('MathSans'), bg = "#000000",fg = "#ffffff").place(x=850,y=25)
e3 = Entry(head,width = 42,font=('MathSans 18')).place(x = 300, y = 25)

#categories
frame4 = Frame(m,height = 550,width = 200,bg = "#ffffff",borderwidth=1)
frame4.place(x=10,y=130)
cat = Label(frame4, text = "TOP CATEGORIES",font="times 12 bold",bg="white",fg="#b5b4b1").place(x = 25,y = 15)
mens = Button(frame4,text = "Men's Fasion",relief = FLAT,width = 12,height = 1,cursor="hand2",command=men_Call, font= ('MathSans'), bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=38,y=50)
women = Button(frame4,text = "Women's Fasion",relief = FLAT,width = 13,height = 0,cursor="hand2",command=women_Call, font= ('MathSans'), bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=32,y=90)
home = Button(frame4,text = "Home and Kitchen",relief = FLAT,width = 14,height = 0,cursor="hand2", font= ('MathSans'),command=hk_Call, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=27,y=130)
groce = Button(frame4,text = "Grocery",relief = FLAT,width = 14,height = 0,cursor="hand2",command=GroceryCall, font= ('MathSans'), bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=24,y=170)
beauty = Button(frame4,text = "Beauty and Health",relief = FLAT,width = 14,height = 0,cursor="hand2", font= ('MathSans'),command=hlt_Call, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=24,y=210)

#morecategories
mrcat = Label(frame4, text = "MORE CATEGORIES",font="times 12 bold",bg="white",fg="#b5b4b1").place(x = 16,y = 260)
auto = Button(frame4,text = "Automotive",relief = FLAT,width = 12,height = 1,cursor="hand2", font= ('MathSans'),command=auto_Call, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=38,y=300)
fur = Button(frame4,text = "Furniture",relief = FLAT,width = 18,height = 0,cursor="hand2", font= ('MathSans'),command=FurnitureCall, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=13,y=340)
ele = Button(frame4,text = "Electronics",relief = FLAT,width = 14,height = 0,cursor="hand2", font= ('MathSans'),command=ElectronicsCall, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=25,y=380)
sports = Button(frame4,text = "Sports and Fitness",relief = FLAT,width = 14,height = 0,cursor="hand2", font= ('MathSans'),command=SportsGymCall, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=27,y=420)
books = Button(frame4,text = "Books,Media and Music",relief = FLAT,width = 18,height = 0,cursor="hand2", font= ('MathSans'),command=bm_Call, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=12,y=460)
com = Button(frame4,text = "Computer and Gaming",relief = FLAT,width = 18,height = 0,cursor="hand2", font= ('MathSans'),command=cg_Call, bg = "#ffffff",fg = "#6b6a68",activebackground="white").place(x=10,y=500)

#Slider
frame_banner = Frame(m,height = 278,width = 810)
frame_banner.place(x=250,y=132)

img = ImageTk.PhotoImage(Image.open("img\dv1.png"))
img2 = ImageTk.PhotoImage(Image.open("img\dv2.png"))
img3 = ImageTk.PhotoImage(Image.open("img\dv3.png"))
img4 = ImageTk.PhotoImage(Image.open("img\dv4.png"))
img5 = ImageTk.PhotoImage(Image.open("img\dv5.png"))
img6 = ImageTk.PhotoImage(Image.open("img\dv6.png"))
img7 = ImageTk.PhotoImage(Image.open("img\dv7.png"))
img8 = ImageTk.PhotoImage(Image.open("img\dv8.png"))

banner=Label(frame_banner)


x = 1

def move():
    global x
    if x == 9:
        x = 1
    if x == 1:
        banner.config(image=img)
    elif x == 2:
        banner.config(image=img2)
    elif x == 3:
        banner.config(image=img3)
    elif x == 4:
        banner.config(image=img4)
    elif x == 5:
        banner.config(image=img5)
    elif x == 6:
        banner.config(image=img6)
    elif x == 7:
        banner.config(image=img7)
    elif x == 8:
        banner.config(image=img8)    
    x = x+1
    m.after(4000, move)
  
# calling the function
move()

#location
frame_loc = Frame(m,height = 279,width = 223,bg = "#ffffff")
frame_loc.place(x=1100,y=132)

loc = ImageTk.PhotoImage(Image.open("img\loc.png"))
label = Label(frame_loc, image = loc,bd=0).place(x = 60,y = 25)
txt = Label(frame_loc, text = "Enter your pincode to check availability \nand fater delivery options",font="MathSans 8",bg="white",fg="#b5b4b1").place(x = 10,y = 150)
e4 = Entry(frame_loc,width = 18,border=1,bg="#ebe8e6",font=('Microsoft Yahei UI Light',15)).place(x=10,y=200)

sub = Button(frame_loc,text = "SUBMIT",relief = FLAT,width = 12,height = 1,cursor="hand2",font= ('MathSans 10'),bg = "#000000",fg = "#ffffff").place(x=60,y=238)

#Trending_Products
frame_tre = Frame(m,height = 230,width = 1080,bg = "#ffffff")
frame_tre.place(x=245,y=450)

txt_f = Frame(m,height = 35,width = 200)
txt_f.place(x=235,y=412)

tre_txt = Label(txt_f, text = "TRENDING PRODUCTS",font="times 12 bold",fg="#6b6a68").place(x = 10,y = 6)
mob = ImageTk.PhotoImage(Image.open("img\mobile.png"))
label_mob = Label(frame_tre, image = mob,bd=0).place(x = 40,y = 10)
jel = ImageTk.PhotoImage(Image.open("img\jewels.jpg"))
label_jel = Label(frame_tre, image = jel,bd=0).place(x = 200,y = 10)
mon = ImageTk.PhotoImage(Image.open("img\monitors.jpg"))
label_mon = Label(frame_tre, image = mon,bd=0).place(x = 450,y = 20)
shirt = ImageTk.PhotoImage(Image.open("img\shirt.png"))
label_shirt = Label(frame_tre, image = shirt,bd=0).place(x = 730,y = 10)
headp = ImageTk.PhotoImage(Image.open("img\headphone.jpg"))
label_head = Label(frame_tre, image = headp,bd=0).place(x = 930,y = 30)

mb_txt = Label(frame_tre, text = "MOBILES",font="times 12 bold",fg="#6b6a68",bg="white").place(x = 40,y = 170)
jew_txt = Label(frame_tre, text = "JEWELS",font="times 12 bold",fg="#6b6a68",bg="white").place(x = 245,y = 170)
mon_txt = Label(frame_tre, text = "MONITORS",font="times 12 bold",fg="#6b6a68",bg="white").place(x = 480,y = 170)
head_txt = Label(frame_tre, text = "HEADPHONES",font="times 12 bold",fg="#6b6a68",bg="white").place(x = 930,y = 170)
shirt_txt = Label(frame_tre, text = "SHIRTS",font="times 12 bold",fg="#6b6a68",bg="white").place(x = 750,y = 170)

ofer = Label(frame_tre, text = "\nupto 15% off",font="times 10",fg="green",bg="white").place(x = 40,y = 190)
ofer2 = Label(frame_tre, text = "\nupto 5% off",font="times 10",fg="green",bg="white").place(x = 245,y = 190)
ofer3 = Label(frame_tre, text = "From ₹8,999",font="times 10",fg="green",bg="white").place(x = 490,y = 205)
ofer4 = Label(frame_tre, text = "From ₹999",font="times 10",fg="green",bg="white").place(x = 955,y = 205)
ofer5 = Label(frame_tre, text = "\nupto 25% off",font="times 10",fg="green",bg="white").place(x = 745,y = 190)

#pack
bfhead.pack()
head.pack()
banner.pack()
sign.grid(row=5,column=9,padx=1250,pady=25)
#main_frame.pack()


m.mainloop()  



