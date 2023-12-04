# Write: Student name
# Write: Student TP

import os
from datetime import datetime

current_user = []

def Admin_Menu():
    adminMenu = 0
    while adminMenu<9:
        print('\n******************************* ADMIN MAIN MENU PAGE *********************************')
        print("\t\t[1] Add Car Details \n\t\t[2] Display and Manipulate Records")
        print("\t\t[3] Search Specific Record\n\t\t[4] Return a Rented Car")
        print("\t\t[5] Exit\n")

        adminMenu = int(input('Select Your Optional to enjoy the feature: '))

        if adminMenu == 1:
            print('\n********************************** ADD CAR **************************************')
            add_car()
            break
        elif adminMenu == 2:
            option = 0
            while option<4:
                print("\t\t[1] Display All Available Cars \n\t\t[2] Display Customer For a Specific Time Duration")
                print("\t\t[3] Main Menu\n")
                display = int(input('Select Your Optional: '))
                if display == 1:
                    print('\n********************************* DISPLAY ALL CARS ************************************')
                    display_available_cars()
                    print("\nSelect An Option From the Given Features to Enjoy")
                    option = 0
                    while option<3:
                        print(
                            "\t\t[1] Update Car \n\t\t[2] Main Menu")
                        opt = int(input('Select Your Optional: '))
                        if opt == 1:
                            print('\n********************************* MODIFY CAR ************************************')
                            modify_car()
                            break
                        elif opt == 2:
                            Admin_Menu()
                            break
                        else:
                            print("Invalid Input!\nPlease Enter Option Again!\n")
                    break
                elif display == 2:
                    print('\n****************** DISPLAY CUSTOMER PAYMENTS FOR SPECIFIC DURATION *********************')
                    display_cus_payment_specificTime()
                    break
                elif display == 3:
                    Admin_Menu()
                    break
                else:
                    print("Invalid Input!\nPlease Enter Option Again!\n")
            break
        elif adminMenu == 3:
            option = 0
            while option<4:
                print("\t\t[1] Search Specific Car Booking \n\t\t[2] Search Specific Customer Payment")
                print("\t\t[3] Main Menu\n")
                search = int(input('Select Your Optional: '))
                if search == 1:
                    file = open("AllBookings.txt","r")
                    booking = file.readlines()
                    count = 0
                    for booking_record in booking:
                        print("[",(count+1),"]","Booking ID: "+booking_record.split(",")[1])
                        count += 1
                    file.close()
                    id_ = input("Enter Booking ID to Search: ")
                    print()
                    search_booking(id_)
                    break
                elif search == 2:
                    file = open("AllCustomers.txt","r")
                    customer = file.readlines()
                    count = 0
                    print("\nAll Registered Customer Details:")
                    for customer_record in customer:
                        print("[",(count+1),"]"+customer_record.split(",")[0])
                        count += 1
                    file.close()
                    name_ = input("\nEnter Customer Name to Search Payment Details: ")
                    print()
                    search_payment(name_)
                    break
                elif search == 3:
                    Admin_Menu()
                    break
                else:
                    print("Invalid Input!\nPlease Enter Option Again!\n")
            break
        elif adminMenu == 4:
            print('\n********************************* RETURN RENTED CAR ************************************')
            return_car()
            break
        elif adminMenu == 5:
            print("Thanks for using our System! Bye! ")
            main()
        else:
            print("Invalid User Input")
        restart = str(input("Do You Wish to Continue(Y/N): ").lower())
        if restart == 'y':
            Admin_Menu()
        else:
            print("Thank You For Using The System")
            main()


def Registered_Customer_Main():
    regCustomerMenu = 0
    while regCustomerMenu<5:
        print('\n******************************* REGISTERED CUSTOMER MAIN PAGE *********************************')
        print("\t\t[1] View Personal Rental History  \n\t\t[2] View All Cars")
        print("\t\t[3] Rent a Car\n\t\t[4] Exit")

        regCustomerMenu = int(input('Select Your Optional to enjoy the feature: '))

        if regCustomerMenu == 1:
            view_personal_transactions(current_user[0])
            while True:
                try:
                    restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
                    if restart == 'y':
                        Registered_Customer_Main()
                        break
                    print("Invalid Value entered")
                except Exception as e:
                    print(e)
            break
        elif regCustomerMenu == 2:
            display_available_cars()
            while True:
                try:
                    restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
                    if restart == 'y':
                        Registered_Customer_Main()
                        break
                    print("Invalid Value entered")
                except Exception as e:
                    print(e)
            break
        elif regCustomerMenu == 3:
            display_available_cars()
            rent_car(current_user[0])
            break
        elif regCustomerMenu == 4:
            print("Thank you for using the system!")
            main()
        else:
            print("Invalid User Input")
        restart = str(input("Do You Wish to Continue(Y/N): ").lower())
        if restart == 'Y':
            regCustomerMenu()
        else:
            print("Thank You For Using The System")
            main()


def Non_Registered_Customer_Main():
    nonRegCustomerMenu = 0
    while nonRegCustomerMenu<4:
        print('\n******************************* NON REGISTERED CUSTOMER MAIN PAGE *********************************')
        print("\t\t[1] View All Cars \n\t\t[2] Register")
        print("\t\t[3] Exit\n")

        nonRegCustomerMenu = int(input('Select Your Optional to enjoy the feature: '))
        if nonRegCustomerMenu == 1:
            display_available_cars()
            while True:
                try:
                    restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
                    if restart == 'y':
                        Non_Registered_Customer_Main()
                        break
                    print("Invalid Value entered")
                except Exception as e:
                    print(e)
            break
        elif nonRegCustomerMenu == 2:
            customer_registration()
            break
        elif nonRegCustomerMenu == 3:
            print("Thank You For Using The System")
            main()
        else:
            print("Invalid User Input")
        restart = str(input("Do You Wish to Continue(Y/N): ").lower())
        if restart == 'y':
            nonRegCustomerMenu()
        else:
            print("Thank You For Using The System")
            main()


def fileIsEmpty(file):
    file_path = file
    if os.stat(file_path).st_size == 0:  # check if size of file is 0
        return True


def Admin_Login(username,password):
    flag = 0
    for line in open("adminLogin.txt","r").readlines():
        login_info = line.split(";")
        if username == login_info[0] and password == login_info[1]:
            print("Welcome")
            flag = 1
            return flag
        elif username == login_info[0] or password == login_info[1]:
            print("Invalid Username or Password Input!")
            return flag
        else:
            print("Username and Password Does Not Exist!")
            return flag


def add_car():
    id = input("Car ID: ")
    car = input("Car Name: ")
    year = int(input("Year of Car Manufacture: "))
    price = float(input("Price Per Hour: "))
    print("Car Successfully Added!")
    f = open("AvailableCars.txt","a")
    f.write("\n"+id+","+car+","+str(year)+","+str(price))
    f.close()

    while True:
        try:
            restart = str(input("Do You Want to Continue (Y/N): ").lower())
            if restart == 'y':
                add_car()
                break
            elif restart == 'n':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def return_car():
    id = input("Car ID: ")
    car = input("Car Name: ")
    year = int(input("Year of Car Manufacture: "))
    price = float(input("Price Per Hour: "))
    print("Car Successfully Returned!")

    f = open("AvailableCars.txt","a")
    f.write("\n"+id+","+car+","+str(year)+","+str(price))
    f.close()

    while True:
        try:
            restart = str(input("Do You Want to Continue (Y/N): ").lower())
            if restart == 'y':
                return_car()
                break
            elif restart == 'n':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def display_available_cars():
    if not fileIsEmpty("AvailableCars.txt"):
        car_file = open("AvailableCars.txt","r")
        car_records = car_file.readlines()  #return all lines in the file, as a list
        record = 0
        for car_record in car_records:
            print("[",(record+1),"]",
                  "Car ID: "+car_record.split(",")[0]+" ,Name: "+car_record.split(",")[
                      1]+" ,Year: "+car_record.split(",")[2]+" ,Price Per Hour: "+car_record.split(",")[3].strip())
            record += 1
        car_file.close()
    else:
        print("No Vehicles are available!")


def modify_car():
    car_file = open("AvailableCars.txt","r")
    car_records = car_file.readlines()

    record = 0
    for car_record in car_records:
        print("[",(record+1),"]",
              "Car ID: "+car_record.split(",")[0]+" ,Name: "+car_record.split(",")[
                  1]+" ,Year: "+car_record.split(",")[2]+" ,Price Per Hour: "+car_record.split(",")[3].strip())
        record += 1

    record_num = int(input("\nEnter record number you wanted to edit: "))
    print()
    car_details = car_records[record_num-1].split(",")

    element = 0
    for record_element in car_details:
        print("[",(element+1),"]",record_element)
        element += 1

    element_number = int(input("Enter element number you wanted to edit: "))
    print("\nCurrent element value:",car_details[element_number-1])
    new_element_value = input("Enter new element value: ")
    new_line = ""
    if element_number == 3 and record != record_num:
        new_line = "\n"

    car_details[element_number-1] = new_element_value+new_line  #assigning new value into selected element
    updated_record = ','.join(car_details)  #takes all items in a list and joins them into one string
    car_records[record_num-1] = updated_record  #now selected line has updated value

    with open("AvailableCars.txt","w") as file:
        file.writelines(car_records)  #writing the updated student records into text file
    car_file.close()
    print("\nRecord updated!")

    while True:
        try:
            restart = str(input("Do You Want To Modify Another Car (Y/N): ").lower())
            if restart == 'y':
                modify_car()
                break
            elif restart == 'n':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def customer_registration():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    contact = input("Contact: ")
    print("Thank You For Registering with our system!")
    print("Your Login username will be the provided Email")

    f = open("AllCustomers.txt","a")
    f.write(name+","+email+","+password+","+contact+"\n")
    f.close()
    print("\nSelect An Option From the Given Features to Enjoy")
    option = 0
    while option<3:
        print("\t\t[1] Login \n\t\t[2] Main Menu")
        opt = int(input('Select Your Optional: '))
        if opt == 1:
            while True:
                try:
                    username = input("Please enter your username: ")
                    password = input("Please enter your password: ")
                    value = customer_Login(username,password)
                    if value:
                        print('Hello !',value[1]," you have logged in successfully.")
                        current_user.append(value[1])
                        Registered_Customer_Main()
                        break
                    print("Invalid Credentials, Please Try Again!")
                except Exception as e:
                    print(e)
                break
        elif opt == 2:
            Non_Registered_Customer_Main()
            break
        else:
            print("Invalid Input!\nPlease Enter Option Again!\n")


def customer_Login(username,password):
    fileRead = open('AllCustomers.txt','r')
    while True:
        line = fileRead.readline()
        lineLength = len(line)
        if lineLength == 0:
            break
        lineItem = line.split(",")
        if username == lineItem[1] and password == lineItem[2]:
            return True, lineItem[0]
            break


def price(days,price_per_day):
    if days<7:
        return (days*price_per_day)-15
    elif days>7:
        return (days*price_per_day)-40


def rent_car(name):
    record_num = int(input("\nEnter record number you wanted to rent: "))
    car_file = open("AvailableCars.txt","r")
    car_records = car_file.readlines()
    car_details = car_records[record_num-1].split(",")

    id = (car_details[0])
    price_per_day = float(car_details[3])  #price of car
    my_string = str(input('Enter Date, You Want To Rent(yyyy-mm-dd): '))
    s_day = datetime.strptime(my_string,"%Y-%m-%d")
    my_string = str(input('Enter Date, You Want To Return(yyyy-mm-dd): '))
    e_day = datetime.strptime(my_string,"%Y-%m-%d")
    d = e_day-s_day
    days = d.days
    today = datetime.today()

    print("Total Amount (RM): "+str(float(price(days,price_per_day))))

    while True:
        try:
            cash = float(input("Confirm Amount of Cash Provided to Deposit: "))
            if cash == int(price(days,price_per_day)):
                print("Thank You For Your Payment!, \nYour Booking is Confirmed")
                break
            print("Your Due Amount is: "+str(int(price(days,price_per_day))))
            print("Please Enter Again!")
        except Exception as e:
            print(e)

    #count number of line to auto generate bookings id
    file = open("AllBookings.txt","r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    booking_id = line_count+1
    booking_File = open("AllBookings.txt","a")
    booking_File.write(
        "\n"+name+","+str(booking_id)+","+str(id)+","+str(s_day.date())+","+str(e_day.date())+","+str(cash)+","+str(
            today.date()))
    booking_File.close()
    car_file.close()
    update_car_rented(id)

    while True:
        try:
            restart = str(input("Do You Want To Rent Another Car (Y/N): ").lower())
            if restart == 'y':
                rent_car(name)
                break
            elif restart == 'n':
                Registered_Customer_Main()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def update_car_rented(id_):
    #remove rented car from file
    fh_r = open("AvailableCars.txt","r")
    fh_w = open("temp.txt","w")

    s = ' '
    while (s):
        s = fh_r.readline()
        L = s.split(",")
        if len(s)>0:
            if L[0] != id_:
                fh_w.write(s)

    fh_w.close()
    fh_r.close()
    os.remove("AvailableCars.txt")
    os.rename("temp.txt","AvailableCars.txt")


def view_personal_transactions(name):
    file = open("AllBookings.txt", "r")
    count = 0
    flag = 0
    transactions = file.readlines()

    for t_record in transactions:
        line = t_record.split(",")
        if name in line:
            flag = 1
            print("[",(count+1),"]","Booking ID: "+t_record.split(",")[1]+" ,Car ID: "+t_record.split(",")[2]
                  +" ,Start Date: "+t_record.split(",")[3]+" ,Return Date: "+t_record.split(",")[4]
                  +" ,Payment: "+t_record.split(",")[5]+" ,Payment Date: "+t_record.split(",")[6])
        count = +1
    if flag == 0:
        print("No Record Found!")


def search_booking(id_):
    file = open("AllBookings.txt","r")
    booking = file.readlines()
    flag = 0

    for b_record in booking:
        line = b_record.split(",")
        if id_ in line:
            flag = 1
            print("\n[1] Booking ID: "+b_record.split(",")[1]+" ,Car ID: "+b_record.split(",")[2]
                  +" ,Start Date: "+b_record.split(",")[3]+" ,Return Date: "+b_record.split(",")[4]
                  +" ,Payment: "+b_record.split(",")[5]+" ,Payment Date: "+b_record.split(",")[6])
    if flag == 0:
        print("No Record Found!")

    while True:
        try:
            restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
            if restart == 'y':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def search_payment(name_):
    file = open("AllBookings.txt","r")
    payment = file.readlines()
    count = 0
    flag = 0

    for p_record in payment:
        line = p_record.split(",")
        if name_ in line:
            flag = 1
            print("[",(count+1),"]","Booking ID: "+p_record.split(",")[1]+" ,Payment: "+p_record.split(",")[5]
                  +" ,Payment Date: "+p_record.split(",")[6])
        count = +1
    if flag == 0:
        print("No Record Found!")

    while True:
        try:
            restart = str(input("Enter 'Y' to go Back to Menu: ").lower())
            if restart == 'y':
                Admin_Menu()
                break
            print("Invalid Value entered")
        except Exception as e:
            print(e)


def display_cus_payment_specificTime():
    p_day = str(input('Enter Payment Date (yyyy-mm-dd): '))

    file = open("AllBookings.txt","r")
    pay_time = file.readlines()
    flag = 0

    for st_record in pay_time:
        line = st_record.split(",")
        if p_day in line:
            flag = 1
            print("[",(count+1),"]","Customer Name: "+st_record.split(",")[0]+
                  " ,Booking ID: "+st_record.split(",")[1]
                  +" ,Payment: "+st_record.split(",")[5])
        count = +1
    if flag == 0:
        print("No Record Found!")

    file.close()


def main():
    menu = 0
    while menu<5:
        print(" ")

        print("""\t\t\t\t  $$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                 "$                                                                           $"
                 "$		            SUPER CAR RENTAL SERVICES 	                              $"
                 "$                                                                           $"
                 "$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                 """)
        print('\t\t\t\t\t\t  [1] Admin \n\t\t\t\t\t\t'
              '  [2] Registered Customer \n\t\t\t\t\t\t'
              '  [3] Non-Registered Customer \n\t\t\t\t\t\t'
              '  [4] Quit \n ')

        menu = int(input('\tSelect User Type: '))
        print('----------------------------------------------------------------------------------------------------')

        if menu == 1:
            print('\n******************************* ADMIN LOGIN PAGE *********************************')
            print("\nPlease enter your Log in Credentials")
            while True:
                try:
                    username = input("Please enter your username: ")
                    password = input("Please enter your password: ")
                    value = Admin_Login(username,password)
                    if value:
                        Admin_Menu()
                        break
                except Exception as e:
                    print(e)
            break
        elif menu == 2:
            print(
                '\n********************************* REGISTERED CUSTOMER LOGIN PAGE ***********************************')
            while True:
                try:
                    username = input("Please enter your username: ")
                    password = input("Please enter your password: ")
                    value = customer_Login(username,password)
                    if value:
                        print('Hello !',value[1]," you have logged in successfully.")
                        current_user.append(value[1])
                        Registered_Customer_Main()
                        break
                    print("Invalid Credentials, Please Try Again!")
                except Exception as e:
                    print(e)
            break
        elif menu == 3:
            Non_Registered_Customer_Main()
            break
        elif menu == 4:
            print("Thank You For Using The System")
            exit()
            break
        else:
            print("Invalid User Input")

        restart = input("Do You Wish to Continue(Y/N): ").lower()
        if restart == 'y':
            main()
        else:
            print("Thank You For Using The System")
            exit()


#system start
main()
