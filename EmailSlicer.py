from tkinter import *



'''Initializing Window'''
root = Tk()
root.geometry('600x600')
root.title('Email Slicer')
root.resizable(0,0)


username = StringVar()
domain = StringVar()

'''Defining Functions'''
def result():
    mail = email.get()
    up_mail = mail.strip()
    try:
        username1 = up_mail[0:up_mail.index('@')]
        domain1 = up_mail[up_mail.index('@')+1:]
        username.set(username1)
        domain.set(domain1)
    except:
        print("Something went Wrong")
        print(mail)
        print(up_mail)
    
    print(f"Your username is {username1} & domain is {domain1}")
        
        
def reset():
    usernamebox.delete(0, END)
    domainbox.delete(0, END)
    email.delete(0, END)
        


headingframe = Frame(root, bg= '#FFBB00', bd= 5)
headingframe.place(relx= 0.2, rely= 0.1, relwidth= 0.6, relheight= 0.16)
headinglbl = Label(headingframe, text= 'Email Slicer', bg= 'black', fg= 'white', font= 'Courier 15 bold')
headinglbl.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)


displayframe = Frame(root, bg= 'black')
displayframe.place(relx= 0.1, rely= 0.4, relwidth= 0.8, relheight= 0.4)

#Email input
emaillbl = Label(displayframe, text= 'Email:- ', bg= 'black', fg= 'white')
emaillbl.place(relx= 0.05, rely= 0.2, relheight= 0.08)
email = Entry(displayframe)
email.place(relx= 0.3, rely= 0.2, relwidth= 0.62, relheight= 0.08)

#username
usernamelbl = Label(displayframe, text= 'Username', bg= 'black', fg= 'white')
usernamelbl.place(relx= 0.05, rely= 0.35, relheight= 0.08)
usernamebox = Entry(displayframe, textvariable= username)
usernamebox.place(relx= 0.3, rely= 0.35, relwidth= 0.62, relheight= 0.08)

#domain
domainlbl = Label(displayframe, text= 'Domain', bg= 'black', fg= 'white')
domainlbl.place(relx= 0.05, rely= 0.5, relheight= 0.08)
domainbox = Entry(displayframe, textvariable= domain)
domainbox.place(relx= 0.3, rely= 0.5, relwidth= 0.62, relheight= 0.08)


'''Button'''
executebtn= Button(root, text= 'Click to Slice', bg= 'black', fg= 'white', command= result)
executebtn.place(relx= 0.1, rely= 0.85, relwidth= 0.2, relheight= 0.07)
exitbtn= Button(root, text= 'Reset', bg= 'black', fg= 'white', command= reset)
exitbtn.place(relx= 0.4, rely= 0.85, relwidth= 0.2, relheight= 0.07)
exitbtn= Button(root, text= 'Exit', bg= 'black', fg= 'white', command= root.destroy)
exitbtn.place(relx= 0.7, rely= 0.85, relwidth= 0.2, relheight= 0.07)


root.mainloop()




