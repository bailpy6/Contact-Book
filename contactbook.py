import PySimpleGUI as sg
import sqlite3
import sys

#Add Contact to DB
def newcontact(name, phone, email):
    cursor.execute('''INSERT INTO contacts(name, phone, email) VALUES(?,?,?)''',(name,phone,email))
    print("Contact: " + name + " has been added to the database")
    db.commit()

#Remove Contact from DB
def removecontact(name):    
    cursor.execute('''DELETE FROM contacts WHERE name = ?''', (name,))
    print("Contact: " + name + " has been removed from the database")
    db.commit()

#Pull Contact Info
def pullcontact(name):
    cursor.execute('''SELECT name, email, phone FROM contacts WHERE name=?''', (name,))
    contactdetails = cursor.fetchone()
    db.commit()
    print(contactdetails)
    
    
#GUI to Add Contacts    
def addinggui():
    #GUI Layout
    addinglayout = [ [sg.Text("Enter Contact Details:")],
                                [sg.Text("Name: ", size=(10,1)), sg.InputText(key="name")],
                                [sg.Text("Phone: ", size=(10,1)), sg.InputText(key="phone")],
                                [sg.Text("Email: ", size=(10,1)), sg.InputText(key="email")],
                                [sg.Button("Submit"), sg.Button("Close")]]
    
    addingwindow = sg.Window("Contact Book: Add Contact")
    event, values = addingwindow.Layout(addinglayout).Read()
    
    #add to DB
    if event == "Submit":
        n = values["name"]
        p = values["phone"]
        e = values["email"]
        newcontact(n,p,e)
    if event == "Close":
        sys.exit
        
#GUI To View Contacts    
def viewinggui():
    pullcontact(name)
 
 #GUI to Remove Contacts
def removinggui():   
    removecontact(name)
    
#Main GUI   
def maingui():
    #main gui layout
    mainlayout = [ [sg.Text("Please Select an Option")],
                                [sg.Button("Add Contact")],
                                [sg.Button("View Contact")],
                                [sg.Button("Remove Contact")],
                                [sg.Button("Close")]]
    
    mainwindow = sg.Window("Contact Book")
    event, values = mainwindow.Layout(mainlayout).Read()
    return event, values

def main():
    button, values = maingui()
    if button == "Close":
        sys.exit()
    if button == "Add Contact":
        addinggui()
        #do stuff for add contact
    if button == "View Contact":
        sys.exit
        #pullinggui()
        #do stuff for view contact
    if button == "Remove Contact":
        sys.exit
        #removinggui()
        #do stuff for remove contact
    else:
        sys.exit()

if __name__ == '__main__':
    #create DB If doesn't exist
    db = sqlite3.connect("C:\\Users\\Bailey\\Documents\\Python\\contactdb")
    cursor = db.cursor()
    #create the table in the db if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)''')
    db.commit()
    
    #Main Function to Launch GUI's
    main()
    
    
    #Testing Functions
    #newcontact("bailey","01268444444","bailey@google.com")
    #newcontact("fred","01268555555","fred@google.com")
    #pullcontact("fred")
    #removecontact("bailey")
    
    
    
