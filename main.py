import json




def choices():
    print("\n\n         1. View All Contacts")
    print("         2. Add Contact")
    print("         3. Search Contact")
    print("         4. Update Contact")
    print("         5. Delete Contact")
    print("         6. Exit\n\n")


def read_contacts_from_file():
    try:
        file = open("conbook.json", "r")
        file_converted_to_text = file.read()

        contacts = json.loads(file_converted_to_text)
        file.close()
        return contacts
    except:
        return[]




def write_contacts_to_file(contacts):
    file = open("conbook.json", "w+")

    json_text = json.dumps(contacts, indent=4)

    file.writelines(json_text)

    file.close()




def add():
    newcon = dict()

    newcon['fname'] = input("\nEnter First Name  : ")
    newcon['lname'] = input("Enter Last Name   : ")
    newcon['pnum'] = input("Enter Phone Number: ")
    newcon['email'] = input("Enter Your Email  : ")
    newcon['address'] = input("Enter Your Address: ")

    #json file
    contacts = read_contacts_from_file()
    contacts.append(newcon)
    write_contacts_to_file(contacts)

    print("\nAdded Successfully.")
    return add_look()

def add_look():
    select = int(input("\nDo You Want to Add Again?\n1. Yes\n2. No\n\nSelect any: "))
    if select == 1:
        return add()
    if select == 2:
        return




def all_contacts():
    with open("conbook.json", "r") as a:
        temp = json.load(a)

        for book in temp:
            fname = book["fname"]
            lname = book["lname"]
            pnum = book["pnum"]
            email = book["email"]
            address = book["address"]

            print(f"\nName      : {fname} {lname}")
            print(f"Phone No. : {pnum}")
            print(f"Email     : {email}")
            print(f"Address   : {address}\n\n")





def search():
    query = input("\nWrite First Name Or Last Name: ")
    with open("conbook.json", "r") as a:
        temp = json.load(a)

        check = 0
        for book in temp:
            if book.get("fname") == query or book.get("lname") == query:
                check=1
                print("\nName      : {} {}\nPhone No. : {}\nEmail     : {}\nAddress   : {}\n".format(book.get("fname"), book.get("lname"),book.get("pnum"),book.get("email"),book.get("address")))
                return search_look()

        if check==0:
            print("\nNo contact match. Please try Again!")
            return search_look()
def search_look():
    select = int(input("\nDo You Want to Search Again?\n1. Yes\n2. No\n\nSelect any: "))
    if select==1:
        return search()
    if select==2:
        return






def contacts_delete():
    with open("conbook.json", "r") as a:
        temp = json.load(a)

        i = 1

        for book in temp:
            fname = book["fname"]
            lname = book["lname"]
            pnum = book["pnum"]
            email = book["email"]
            address = book["address"]

            print(f"\nIndex No.= {i}")
            print(f"\nName      : {fname} {lname}")
            print(f"Phone No. : {pnum}")
            print(f"Email     : {email}")
            print(f"Address   : {address}\n\n")
            i+=1




def delete():

    contacts_delete()

    newdata = []

    with open("conbook.json", "r") as a:
        temp = json.load(a)
        length = len(temp)

    while True:
        updatedata = int(input(f"Enter a Index number which you want to delete: "))

        if updatedata < length+1 and updatedata > 0:
            i = 1
            for book in temp:
                if i == int(updatedata):
                    pass
                    i += 1
                else:
                    newdata.append(book)
                    i += 1

                with open("conbook.json", "w") as a:
                    json.dump(newdata, a, indent=4)
            print("\nDelete Successfully!")
            return look_delete()
        else:
            print("\nPlease Enter Right Index!")

def look_delete():
    select = int(input("\nDo You Want to Delete Another Contact?\n1. Yes\n2. No\n\nSelect any: "))
    if select == 1:
        return delete()
    if select == 2:
        return






def update():
    contacts_delete()

    newdata = []

    with open("conbook.json","r") as a:
        temp = json.load(a)
        length = len(temp)


    while True:
        deletedata = int(input(f"\nEnter a Index number which you want to update: "))

        if deletedata < length+1 and deletedata > 0:
            i = 1
            for book in temp:
                if i == int(deletedata):
                    fname = book["fname"]
                    lname = book["lname"]
                    pnum = book["pnum"]
                    email = book["email"]
                    address = book["address"]

                    print(f"\nCurrent Name         : {fname} {lname}")
                    fname = input("Enter New Name(first): ")
                    lname = input("Enter New Name(last) : ")

                    print(f"\nCurrent Phone No.  : {pnum}")
                    pnum = input("Enter New Phone No.: ")

                    print(f"\nCurrent Email     : {email}")
                    email = input("Enter New Email   : ")

                    print(f"\nCurrent Address   : {address}")
                    address = input("Enter New Address : ")

                    newdata.append({"fname": fname,"lname": lname,"pnum": pnum,"email": email,"address": address})
                    i+=1
                else:
                    newdata.append(book)
                    i+=1

                with open ("conbook.json","w") as a:
                    json.dump(newdata,a,indent=4)
            print("\nUpdate Successfully!")
            return look_update()
        else:
            print("\nPlease Enter Right Index!")


def look_update():
    select = int(input("\nDo You Want to Update Another Contact?\n1. Yes\n2. No\n\nSelect any: "))
    if select == 1:
        return update()
    if select == 2:
        return





while True:
    choices()
    choice = int(input("Select Your Choice: "))
    if choice==1:
        all_contacts()
        #print("\nall Successfully.")

    elif choice==2:
        add()
        #print("\nAdded Successfully.")


    elif choice==3:
        search()
        #print("\nSearch Successfully.")


    elif choice==4:
        update()
        #print("\nUpdate Successfully.")


    elif choice==5:
        delete()
        #print("\nDelete Successfully!")

    elif choice==6:
        break

    else:
        print("\nYou press wrong key! Please Enter Carefully.")


