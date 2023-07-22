#WONG JIAN WEI
#TP068349

##################################################################################################################

# this function is to allow new customer to sign up, data entered will be stored in a list in list
def upload_customer_detail():
    customer_txt = []
    for i in range(1):
        customer_txt_file = []

        customer_enter_details_name = input("\nName: ")
        customer_txt_file.append(customer_enter_details_name)

        customer_enter_details_address = input("\nAddress: ")
        customer_txt_file.append(customer_enter_details_address)

        customer_enter_details_email_id = input("\nEmail ID: ")
        customer_txt_file.append(customer_enter_details_email_id)

        customer_enter_details_contact_number = input("\nContact Number: ")
        customer_txt_file.append(customer_enter_details_contact_number)

        customer_enter_details_gender = input("\nGender (Male/Female/Others): ")
        customer_txt_file.append(customer_enter_details_gender)

        customer_enter_details_date_of_birth = input("\nDate Of Birth (dd/mm/yy): ")
        customer_txt_file.append(customer_enter_details_date_of_birth)

        customer_enter_details_user_id = input("\nUser ID: ")
        customer_txt_file.append(customer_enter_details_user_id)

        customer_enter_details_password = input("\nEnter Password: ")
        customer_txt_file.append(customer_enter_details_password)

        while True:
            customer_enter_details_confirm_password = input("\nConfirm Password: ")
            if customer_enter_details_confirm_password == customer_enter_details_password:
                break
            else:
                print("Please confirm your password")

        customer_txt.append(customer_txt_file)

    return customer_txt


##################################################################################################################################

# this function is to check if the customer's login username and password is already registered or not, then decide whether to allow the user to login
def registered_customer_login_checker():
    registered_customer_login_details_username = input("Username: ")
    registered_customer_login_details_password = input("Password: ")

    try:
        registered_customer_check_login = open(f'{registered_customer_login_details_username}_info.txt', 'r')
        print("Login successful!")
    except FileNotFoundError:
        print("User not found")
        exit()

    registered_customer_check_login.close()


##################################################################################################################################
##################################################################################################################################

# this function is to allow admin to upload medicine information into the database
def input_Admin_number1():
    admin_open_file = open('medicine.txt', 'a')
    print("""\nUpload medicine detail in system in such format:
            Medicine name, Expiration date(dd/mm/yy), Price(RM), Quantity (per pack/per bottle), Package forms  (Blister packs/Prescription bottle)
            \nFor example:
            Paracetamol, 11/06/23, RM7, 10 caplets per pack, Blister packs
                 """)

    medicine_enter_details = input("\nEnter details: ")

    admin_open_file.write(medicine_enter_details)

    admin_open_file.write("\n")

    admin_open_file.close()

    print("\nMedicine details uploaded in system")
    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow admin to view all uploaded medicine and its information
def input_Admin_number2():
    try:
        admin_open_file = open('medicine.txt', 'r')
    except:
        print('File cannot be opened:')
        exit()

    print("\nAll uploaded medicines:\n")

    print("""Medicine Name, Expiration Date, Price, Quantity, Package Forms
---------------------------------------------------------------------------------------""")

    for line in admin_open_file:
        line = line.rstrip()
        print(line)
    input("\nPress <Enter> to continue\n")
    admin_open_file.close()


################################################################################################################################

# this function is to allow admin to modify the medicine information by locating the line that will be edited, then enter the new medicine information
def input_Admin_number3():
    print("")
    print("""Medicine Name, Expiration Date, Price, Quantity, Package Forms
---------------------------------------------------------------------------------------""")
    admin_modify_file = open('medicine.txt', 'r')
    print(admin_modify_file.read())
    admin_modify_file.close()
    admin_modify_file = open('medicine.txt', 'r')
    admin_string_list = admin_modify_file.readlines()      # this is to get file's content as a list
    admin_modify_file.close()

    medicine_modify_line = int(input("\nEnter the medicine line number that will be modified <starting at 1>: "))
    medicine_modify_line_number = medicine_modify_line - 1
    print("""\nUpdate/modify medicine information in system in such format:
                    Medicine name, Expiration date(dd/mm/yy), Price(RM), Quantity, Package forms
                    \nFor example:
                    Paracetamol, 11/06/23, RM7, 10 caplets per pack, Blister packs
                         """)
    medicine_modify_details = input("\nEnter new details: ")

    medicine_modify_details2 = medicine_modify_details + '\n'
    admin_string_list[medicine_modify_line_number] = medicine_modify_details2

    try:
        admin_modify_file = open('medicine.txt', 'w')
        new_medicine_modify_details = "".join(admin_string_list)       # takes all items in the list and joins them into one string
        admin_modify_file.write(new_medicine_modify_details)

        admin_modify_file.close()

    except IndexError:
        print("There's no line number.")
        

    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow admin to delete the medicine information by locating the line that will be deleted
def input_Admin_number4():
    print("")
    try:
        admin_modify_file = open('medicine.txt', 'r')
    except:
        print('File cannot be opened')
        exit()
        
    print("""Medicine Name, Expiration Date, Price, Quantity, Package Forms
---------------------------------------------------------------------------------------""")
    admin_modify_file = open('medicine.txt', 'r')
    print(admin_modify_file.read())
    admin_modify_file.close()
    admin_modify_file = open('medicine.txt', 'r')
    admin_string_list = admin_modify_file.readlines()  # this is to get file's content as a list
    admin_modify_file.close()

    medicine_modify_line = int(input("\nEnter the medicine line number that will be deleted <starting at 1>: "))
    medicine_modify_line_number = medicine_modify_line - 1

    medicine_modify_details2 = ""
    admin_string_list[medicine_modify_line_number] = medicine_modify_details2

    admin_modify_file = open('medicine.txt', 'w')
    new_medicine_modify_details = "".join(admin_string_list)  # takes all items in the list and joins them into one string
    admin_modify_file.write(new_medicine_modify_details)

    admin_modify_file.close()

    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow admin to search for a specific medicine by searching the medicine file line by line for line(s) containing the keyword
def input_Admin_number5():
    print("")
    try:
        search_medicine_file = open('medicine.txt', 'r')
    except:
        print('File cannot be opened')
        exit()

    admin_search_medicine = input("Type what medicine details you want to search: ")

    print("""Medicine Name, Expiration Date, Price, Quantity, Package Forms
---------------------------------------------------------------------------------------""")

    search_medicine_file = open('medicine.txt', 'r')
    for line in search_medicine_file:
        line = line.rstrip()
        if admin_search_medicine.lower() in line.lower():
            print(line)

        else:
            continue

    search_medicine_file.close()
    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow admin to view all medicine orders made by customers
def input_Admin_number6():
    admin_read_order_file = open('order.txt', 'r')
    print("")
    print("Below is the information of order(s):")
    print("""Medicine name          Quantity (packs/bottles) 
------------------------------------------------------------ """)
    print(admin_read_order_file.read())
    admin_read_order_file.close()
    input("\nPress <Enter> to continue\n")


################################################################################################################################
    
# this function is to allow admin to view a specific medicine order made by a customer, it is done by locating and read the order file containing the customer's username
def input_Admin_number7():
    print("")
    registered_customer_login_details_username_in_admin = input("Customer Username: ")

    try:
        registered_customer_order_in_admin = open(f'{registered_customer_login_details_username_in_admin}_medicine_order.txt', 'r')

    except FileNotFoundError:
        print("User not found")
        exit()

    print("Below is the information of order(s):")
    print("""Medicine name          Quantity (packs/bottles) 
------------------------------------------------------------ """)

    print(registered_customer_order_in_admin.read())
    registered_customer_order_in_admin.close()


    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow admin to exit the program
def input_Admin_number8():

    admin_exit = input("\nAre you sure you want to exit? ('y' for Yes, any other key for No): ")
 
    if admin_exit == "y":
        exit()


################################################################################################################################
################################################################################################################################
################################################################################################################################

# this function is to let new customer to view all uploaded medicine and its information uploaded by the admin
def input_new_customer_number1():
    
    new_customer_read_file = open('medicine.txt', 'r')
    print("\nBelow are the details of the medicines:")
    print("""Medicine Name, Expiration Date, Price, Quantity, Package Forms
---------------------------------------------------------------------------------------""")
    print(new_customer_read_file.read())
    new_customer_read_file.close()
    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow new customer to sign up, the data entered will be stored using list in list, in a file using their username as a part of the file name 
def input_new_customer_number2():
    customer_txt = []
    for i in range(1):
        customer_txt_file = []

        customer_enter_details_name = input("\nName: ")
        customer_txt_file.append(customer_enter_details_name)

        customer_enter_details_address = input("\nAddress: ")
        customer_txt_file.append(customer_enter_details_address)

        customer_enter_details_email_id = input("\nEmail ID: ")
        customer_txt_file.append(customer_enter_details_email_id)

        customer_enter_details_contact_number = input("\nContact Number: ")
        customer_txt_file.append(customer_enter_details_contact_number)

        customer_enter_details_gender = input("\nGender (Male/Female/Others): ")
        customer_txt_file.append(customer_enter_details_gender)

        customer_enter_details_date_of_birth = input("\nDate Of Birth (dd/mm/yy): ")
        customer_txt_file.append(customer_enter_details_date_of_birth)

        customer_enter_details_user_id = input("\nUsername: ")
        customer_txt_file.append(customer_enter_details_user_id)

        customer_enter_details_password = input("\nEnter Password: ")
        customer_txt_file.append(customer_enter_details_password)

        while True:
            customer_enter_details_confirm_password = input("\nConfirm Password: ")
            if customer_enter_details_confirm_password == customer_enter_details_password:
                break
            else:
                print("Please confirm your password")

        customer_txt.append(customer_txt_file)

    customer_enter_details_user_string = customer_enter_details_user_id + '_info.txt'

    new_customer_registration = open(f'{customer_enter_details_user_string}', "a")

    for customer_txt_file in customer_txt:
        for lines in customer_txt_file:
            new_customer_registration.write(lines)
            spacing_customer_txt_file_calculation = int(30) - len(lines)
            spacing_customer_txt_file = spacing_customer_txt_file_calculation * " "
            new_customer_registration.write(spacing_customer_txt_file)

        new_customer_registration.write("\n")

    new_customer_registration.close()
    print("\nYou have successfully created an account!")
    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow new customer to exit the program
def input_new_customer_number3():
    new_customer_exit = input("\nAre you sure you want to exit? ('y' for Yes, any other key for No): ")

    if new_customer_exit == "y":
            exit()
  
################################################################################################################################
################################################################################################################################
################################################################################################################################

# this function is to let registered customer to view all uploaded medicine and its information uploaded by the admin
def input_registered_customer_number1():
    registered_customer_read_file = open('medicine.txt', 'r')
    print("")
    print("\nBelow are the details of the medicines:")
    print("")
    print("""Medicine Name, Expiration Date, Price, Quantity, Package Forms
---------------------------------------------------------------------------------------""")
    print(registered_customer_read_file.read())
    registered_customer_read_file.close()
    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to let registered customer to order medicine by entering the name and quantity, then proceed to online payment method
# the medicine orders will be placed in an order file that can be viewed by the admin and in an order file that can be viewed by the customer
def input_registered_customer_number2():
    reconfirm_username_place_orders = input("Please enter your username again for security purposes: ")

    registered_customer_read_file = open('medicine.txt', 'r')
    print("")
    print("Below is the information of the medicines:")
    print("""Medicine Name, Expiration Date, Price, Quantity, Package Forms
---------------------------------------------------------------------------------------""")
    print(registered_customer_read_file.read())
    registered_customer_read_file.close()
    input("\nPress <Enter> to proceed to order\n")

    registered_customer_order_medicine_medicine_name = input("\nEnter medicine name: ")
    registered_customer_order_medicine_quantity = input("\nEnter quantity (packs/bottles): ")

    print("Proceed to payment?")
    input("Press <Enter> to continue\n")

    print("\nEnter credit/debit card details: ")
    input("Enter card number: ")
    input("Enter expiry date (mm/yy): ")
    input("Enter CVV: ")
    registered_customer_payment = input("Confirm payment? ('y' for Yes, any other key for No)")
    if registered_customer_payment == "y":
        print("Order and payment successful")

        registered_customer_order_medicine = []
        for i in range(1):
            registered_customer_order_medicine_lines = []
            registered_customer_order_medicine_lines.append(registered_customer_order_medicine_medicine_name)
            registered_customer_order_medicine_lines.append(registered_customer_order_medicine_quantity)
            registered_customer_order_medicine.append(registered_customer_order_medicine_lines)

        customer_place_order = reconfirm_username_place_orders + '_medicine_order.txt'
        registered_customer_order_medicine_file = open(f'{customer_place_order}', 'a')

        for registered_customer_order_medicine_lines in registered_customer_order_medicine:
            for lines in registered_customer_order_medicine_lines:
                registered_customer_order_medicine_file.write(lines)
                spacing_order_txt_file_calculation = int(30) - len(lines)
                spacing_order_txt_file = spacing_order_txt_file_calculation * " "
                registered_customer_order_medicine_file.write(spacing_order_txt_file)

            registered_customer_order_medicine_file.write("\n")

        registered_customer_order_medicine_file.close()

        registered_customer_order_medicine_in_order = []
        for i in range(1):
            registered_customer_order_medicine_in_order_lines = []
            registered_customer_order_medicine_in_order_lines.append(registered_customer_order_medicine_medicine_name)
            registered_customer_order_medicine_in_order_lines.append(registered_customer_order_medicine_quantity)
            registered_customer_order_medicine_in_order.append(registered_customer_order_medicine_in_order_lines)

        registered_customer_order_medicine_file_in_order = open('order.txt', 'a')

        for registered_customer_order_medicine_in_order_lines in registered_customer_order_medicine_in_order:
            for lines in registered_customer_order_medicine_in_order_lines:
                registered_customer_order_medicine_file_in_order.write(lines)
                spacing_order_txt_file_calculation = int(30) - len(lines)
                spacing_order_txt_file = spacing_order_txt_file_calculation * " "
                registered_customer_order_medicine_file_in_order.write(spacing_order_txt_file)

            registered_customer_order_medicine_file_in_order.write("\n")

        registered_customer_order_medicine_file_in_order.close()

    else:
        print("Payment failed")
    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to let registered customer to view medicine orders
# if orders were done, the order information will be shown
# if no orders were done, message prompt of 'Currently no orders.' will be shown 
def input_registered_customer_number3():
    reconfirm_username_show_personal_orders = input("Please enter your username again for security purposes: ")
    try:
        customer_personal_order_details = reconfirm_username_show_personal_orders + '_medicine_order.txt'
        registered_customer_read_order_file = open(f'{customer_personal_order_details}', 'r')
        print("")
        print("Below is the information of your order:")
        print("""Medicine name          Quantity (packs/bottles) 
--------------------------------------------------------- """)
        print(registered_customer_read_order_file.read())

        registered_customer_read_order_file.close()
        input("\nPress <Enter> to continue\n")

    except FileNotFoundError:
        print("\nCurrently no orders.")
        input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow registered customer to view own personal information by accessing a file using their username as a part of the file name
def input_registered_customer_number4():
    reconfirm_username_show_personal_details = input("Please enter your username again for security purposes: ")

    print("""Name                                Address                        Email ID                                Contact Number               Gender                     Date Of Birth               Username              Password
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

    customer_enter_details_user_string = reconfirm_username_show_personal_details + '_info.txt'
    registered_customer_view_personal_information = open(f'{customer_enter_details_user_string}', 'r')
    print(registered_customer_view_personal_information.read())
    registered_customer_view_personal_information.close()
    input("\nPress <Enter> to continue\n")


################################################################################################################################

# this function is to allow registered customer to exit the program
def input_registered_customer_number5():
    registered_customer_exit = input("\nAre you sure you want to exit? ('y' for Yes, any other key for No): ")
    
    if registered_customer_exit == "y":
            exit()

################################################################################################################################

# this function is to let admin to login using designated username and password, then input a number to choose the desired function to run
def admin_login():
    while True:
        Admin_login_details_username = input("Username: ")
        Admin_login_details_password = input("Password: ")
        if Admin_login_details_username == "admin" and Admin_login_details_password == "admin":
            break
        else:
            print("\nPlease try again\n")

    while True:
        print("""\nDo you want to:
    \t1. Upload medicine details in system
    \t2. View all uploaded medicines
    \t3. Update/modify medicine information
    \t4. Delete medicine information
    \t5. Search specific medicine detail
    \t6. View all orders of customers
    \t7. Search order of specific customer
    \t8. Exit
          """)

        input_Admin_number = int(input("Please enter the chosen number: "))

        if input_Admin_number <= 0 or input_Admin_number >= 9:
            print('Invalid input')

        else:
            if input_Admin_number == 1:
                input_Admin_number1()

            if input_Admin_number == 2:
                input_Admin_number2()

            if input_Admin_number == 3:
                input_Admin_number3()

            if input_Admin_number == 4:
                input_Admin_number4()

            if input_Admin_number == 5:
                input_Admin_number5()

            if input_Admin_number == 6:
                input_Admin_number6()

            if input_Admin_number == 7:
                input_Admin_number7()

            if input_Admin_number == 8:
                input_Admin_number8()


########################################################################################################################

# this function is to let new customer to input a number to choose the desired function to run
def new_customer_login():
    while True:
        print("""\nDo you want to:
        \t1. View medicine details
        \t2. Register an account
        \t3. Exit
              """)

        input_new_customer_number = int(input("Please enter the chosen number: "))

        if input_new_customer_number <= 0 or input_new_customer_number >= 4:
            print('Invalid input')

        else:
            if input_new_customer_number == 1:
                input_new_customer_number1()

            if input_new_customer_number == 2:
                input_new_customer_number2()

            if input_new_customer_number == 3:
                input_new_customer_number3()


########################################################################################################################

# this function is to let registered customer to login using designated username and password, then input a number to choose the desired function to run
def registered_customer_login():
    registered_customer_login_checker()

    while True:
        print("""\nDo you want to:
    \t1. View all medicines details
    \t2. Place order of medicines and make payment
    \t3. View own order
    \t4. View personal information
    \t5. Exit
                          """)
        input_registered_customer_number = int(input("Please enter the chosen number: "))

        if input_registered_customer_number <= 0 or input_registered_customer_number >= 6:
            print('Invalid input')

        else:
            if input_registered_customer_number == 1:
                 input_registered_customer_number1()

            if input_registered_customer_number == 2:
                input_registered_customer_number2()

            if input_registered_customer_number == 3:
                input_registered_customer_number3()

            if input_registered_customer_number == 4:
                input_registered_customer_number4()

            if input_registered_customer_number == 5:
                input_registered_customer_number5()


########################################################################################################################

# this function is a menu, allowing the user to run the program either as an admin, a new customer or a registered customer
def menu():
    while True:
        print("""\nWelcome! Are you a(n):
    \t1. Admin
    \t2. New Customer
    \t3. Registered Customer
    """)

        input_user_number = int(input("Please enter the chosen number: "))

        if input_user_number <= 0 or input_user_number >= 4:
            print('Invalid input\n')

        else:
            if input_user_number == 1:
                admin_login()

            if input_user_number == 2:
                new_customer_login()

            if input_user_number == 3:
                registered_customer_login()

    


##############################################################################################################
# this function is called to run the whole program
menu()
