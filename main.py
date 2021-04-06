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


def all_contacts():
    with open("conbook.json", "r") as a:
        temp = json.load(a)

        for book in temp:
            fname = book["fname"]
            lname = book["lname"]
            pnum = book["pnum"]
            email = book["email"]


            print(f"\nName      : {fname} {lname}")
            print(f"Phone No. : {pnum}")
            print(f"Email     : {email}\n\n")



def add():
    newcon = dict()
    newcon['fname'] = input("Enter First Name: ")
    newcon['lname'] = input("Enter Last Name: ")
    newcon['pnum'] = input("Enter Phone Number: ")
    newcon['email'] = input("Enter Your Email: ")

    #json file
    contacts = read_contacts_from_file()

    contacts.append(newcon)

    write_contacts_to_file(contacts)




def search():
    query = input("\nWrite First Name Or Last Name: ")

    contacts = read_contacts_from_file()



    check=0
    for contact in contacts:
        if contact.get("fname") == query or contact.get("lname") == query:
            check=1
            print("\nName      : {} {}".format(contact.get("fname"), contact.get("lname")))
            print("Phone No. : {}".format(contact.get("pnum")))
            print("Email     : {}\n".format(contact.get("email")))




    if check == 0:
        print("\nNo contact match. Please try Again!")


def contacts_delete():
    with open("conbook.json", "r") as a:
        temp = json.load(a)

        i = 1

        for book in temp:
            fname = book["fname"]
            lname = book["lname"]
            pnum = book["pnum"]
            email = book["email"]

            print(f"\nIndex No.= {i}")
            print(f"\nName      : {fname} {lname}")
            print(f"Phone No. : {pnum}")
            print(f"Email     : {email}\n\n")
            i+=1



def delete():

    contacts_delete()

    newdata = []

    with open("conbook.json", "r") as a:
        temp = json.load(a)
        length = len(temp)

    while True:
        updatedata = int(input(f"Enter a Index number which you want to delete: "))

        if updatedata >= length and updatedata <= length:
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
            break
        else:
            print("\nPlease Enter Right Index!")



def update():
    contacts_delete()

    newdata = []

    with open("conbook.json","r") as a:
        temp = json.load(a)
        length = len(temp)


    while True:
        deletedata = int(input(f"\nEnter a Index number which you want to update: "))

        if deletedata>=length and deletedata<=length:
            i = 1
            for book in temp:
                if i== int(deletedata):
                    fname = book["fname"]
                    lname = book["lname"]
                    pnum = book["pnum"]
                    email = book["email"]

                    print(f"\nCurrent Name      : {fname} {lname}")
                    fname = input("Enter New Name(first): ")
                    lname = input("Enter New Name(last): ")

                    print(f"Current Phone No. : {pnum}")
                    pnum = input("Enter New Phone No.: ")

                    print(f"Current Email     : {email}\n\n")
                    email = input("Enter New email: ")

                    newdata.append({"fname": fname,"lname": lname,"pnum": pnum,"email": email})
                    i+=1
                else:
                    newdata.append(book)
                    i+=1

                with open ("conbook.json","w") as a:
                    json.dump(newdata,a,indent=4)
            print("\nUpdate Successfully!")
            break
        else:
            print("\nPlease Enter Right Index!")





while True:
    choices()
    choice = int(input("Select One: "))
    if choice == 1:
        all_contacts()
        #print("\nall Successfully.")

    elif choice == 2:
        add()
        print("\nAdded Successfully.")


    elif choice == 3:
        search()
        #print("\nSearch Successfully.")


    elif choice == 4:
        update()
        #print("\nUpdate Successfully.")


    elif choice == 5:
        delete()
        #print("\nDelete Successfully!")

    elif choice == 6:
        break

    else:
        print("\nYou press wrong key! Please Enter Carefully.")

