# # WK1
# In this week we'll be building out the foundation of your app, in particular, the UI aspect.
# This will make use of your ability to print to the screen, clear the screen, accept user input, and create a basic `list` data structure.
# Try to make good use of functions for repetitive tasks.
# ## Goals
# As a user I want to:
# - create a Courier and add it to a list
# - view all products
# - _STRETCH_ update or delete a Courier
# ## Spec
# A `Courier` should just be a `string` containing its name, i.e: `"Coke Zero"`
# A list of `products` should be a list of `strings`, i.e: `["Coke Zero"]`
# ## Pseudo Code
# - START APP
# LOAD COURIERS AND PRODUCTS FROM TXT 
# FILESHOW LIST OF OPTIONS TO USER AND ACCEPT NUMERICAL INPUT
# IF USER ENTERS 0 THEN SAVE APP STATE TO TXT FILES AND EXIT APP
# - SHOW LIST OF OPTIONS TO USER AND ACCEPT NUMERICAL INPUT
# - IF USER ENTERS `0` THEN EXIT APP
# - IF USER ENTERS `1` THEN SHOW `PRODUCT` MENU - list
#   - IF USER ENTERS `0` RETURN TO MAIN MENU
#   - IF USER ENTERS `1` PRINT OUT `PRODUCTS` TO SCREEN - print list
#   - IF USER ENTER `2` CREATE NEW `PRODUCT`
#     - ASK USER FOR THE `NAME` OF THE `PRODUCT`
#     - APPEND THIS TO THE LIST OF `PRODUCTS` - append
#   - _STRETCH_ IF USER ENTERS `3` UPDATE `PRODUCT`
#     - ASK USER TO SELECT A `PRODUCT` TO UPDATE
#     - ASK USER FOR NEW `NAME` OF `PRODUCT`
#     - REPLACE `PRODUCT` AT SELECTED `IDX` WITH NEW `NAME`
#   - _STRETCH_ IF USER ENTERS `4` DELETE `PRODUCT`
#     - ASK USER TO SELECT A `PRODUCT` TO DELETE
#     - REMOVE THIS ITEM FROM THE `PRODUCT` LIST
# IF USER ENTERS `2` THEN SHOW `COURIER` MENU
#   - IF USER ENTERS `0` RETURN TO MAIN MENU
#   - IF USER ENTERS `1` PRINT OUT `COURIERS` TO SCREEN
#   - IF USER ENTER `2` CREATE NEW `COURIER`
#     - ASK USER FOR THE `NAME` OF THE `COURIER`
#     - APPEND THIS TO THE LIST OF `COURIERS`
#   - _STRETCH_ IF USER ENTERS `3` UPDATE `COURIER`
#     - ASK USER TO SELECT A `COURIER` TO UPDATE OR `0` TO CANCEL
#     - ASK USER FOR NEW `NAME` OF `COURIER`
#     - REPLACE `COURIER` AT SELECTED `IDX` WITH NEW `NAME`
#   - _STRETCH_ IF USER ENTERS `4` DELETE `COURIER`
#     - ASK USER TO SELECT A `COURIER` TO DELETE OR `0` TO CANCEL
#     - REMOVE THIS ITEM FROM THE `COURIER` LIST
# IF USER ENTERS 3 THEN SHOW ORDER MENU
# IF USER ENTERS 0 RETURN TO MAIN MENU
# IF USER ENTERS 1 PRINT OUT ORDERS TO SCREEN
# IF USER ENTER 2 CREATE NEW ORDER
# ASK USER FOR THE NAME OF THE CUSTOMER
# ASK USER FOR THE ADDRESS OF THE CUSTOMER
# ASK USER FOR THE PHONE OF THE CUSTOMER
# AKS THE USER TO SELECT A COURIER FROM THE LIST
# SET THE DEFAULT ORDER STATUS TO BE PREPARING
# APPEND THE NEW ORDER TO THE LIST OF ORDERS
# IF USER ENTERS 3 UPDATE ORDER STATUS
# ASK USER TO SELECT AND ORDER TO UPDATE OR 0 TO CANCEL
# ASK USER TO SELECT A NEW STATUS
# UPDATE THE ORDER
# STRETCH IF USER ENTERS 4 UPDATE ORDER
# ASK USER TO SELECT AN ORDER TO UPDATE OR 0 TO CANCEL
# FOR EACH ORDER PROPERTY
# ASK USER FOR UPDATED DATA OR LEAVE BLANK TO SKIP
# UPDATE THE ORDER PROPERTY IF NOT BLANK
# STRETCH IF USER ENTERS 5 DELETE ORDER
# ASK USER TO SELECT AN ORDER TO DELETE OR 0 TO CANCEL
# REMOVE THIS ITEM FROM THE ORDERS LIST

import os
import csv
# import pymysql
# import os
# from dotenv import load_dotenv



# # ------------------------------------------------------------------------------------------------ SQL-----------------------------------------------------------------------------------------------------------------------------------          
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection

def open_connection(host = host,  user = user, password = password, database=database):
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    return connection

# cursor = connection.cursor()

# cursor.execute("CREATE DATABASE products")

# connection.commit()
# cursor.close()
# connection.close()

# def product_dct():
    
#     p_d = 
# def Network():
    
#     dict = {}


#     #len(dict)
#     return (dict)


# def load_product_db():
#     product_lst.clear()
#     product_lst_2 = []
#     connection = pymysql.connect(host, user, password, database)
#     cursor = connection.cursor()
#     cursor.execute("SELECT product_id, product_name, product_price FROM products")
#     rows = cursor.fetchall()
#     for row in rows:
#         prod = {'ID': row[0], 'Product Name': row[1], 'Price': row[2]}
#         # print(f'ID: {row[0]} Product: {str(row[1])}, Price: {row[2]}')
#         print(prod)
#         return prod
#         product_lst_2.append(prod)
    # print(product_lst_2)
    # cursor.close()
    # connection.close()
    # print(prod)

# def load_courier_db():
#     product_lst_2 = []
#     connection = pymysql.connect(host, user, password, database)
#     cursor = connection.cursor()
#     cursor.execute("SELECT courier_id, courier_name, courier_number FROM courier")
#     rows = cursor.fetchall()
#     for row in rows:
#         cour = {'ID': row[0], 'Courier Name': row[1], 'Phone Number': row[2]}

# variable = Network()
# load_product_db()
# cursor.close()
# connection.close()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------



def clear():
    os.system('cls')

products_available = []
courier_available = []

order_1 = {'Name': 'Sweeny Todd', 
                  'Address': 'Unit 45, 2 Hogwarts Street, LONDON, BR6 3LQ', 
                  'Contact No': '07940479678', 
                  'Courier': 2, 
                  'Status': 'Preparing', 'Items': [2, 4, 5]}

order_2 = {'Name': 'Michael Jackson', 
                  'Address': '20, Neverland, New York, NH1 3TR', 
                  'Contact No': '07940479689', 
                  'Courier': 1, 
                  'Status': 'Preparing', 'Items': [1, 2, 3]}
orders = []
orders_dict = {}
items = []
l_o_o = len(orders)

ord_num_rows = 0

for row in open('C:/Users/chesney/Documents/Python Programme/Mini-project/Order_lst.csv'):
    ord_num_rows += 1

ord_num = ord_num_rows -1

# products
fanta_dct = {'Product Name': 'Fanta', 'Price': 0.8}
coke_dct = {'Product Name': 'Coke', 'Price': 0.75}
sprite_dct = {'Product Name': 'Sprite', 'Price': 0.8}
tango_dct = {'Product Name': 'Tango', 'Price': 0.8}
apple_dct = {'Product Name': 'Apple Juice', 'Price': 1.2}
pineapple_dct = {'Product Name': 'Pineapple Juice', 'Price': 1.2}
product_lst = []
product_id = []
product_dct = {}
l_o_p = len(product_lst)

prod_num_rows = 0

for row in open('C:/Users/chesney/Documents/Python Programme/Mini-project/Product_lst.csv'):
    prod_num_rows += 1

prod_num = prod_num_rows -1


# couriers
courier_1 = {'Courier Name': 'Matthew', 'Phone Number': '07956322433'}
courier_2 = {'Courier Name': 'Mark', 'Phone Number': '07956322435'}
courier_3 = {'Courier Name': 'Luke', 'Phone Number': '07956322436'}
courier_4 = {'Courier Name': 'John', 'Phone Number': '07956322437'}
courier_5 = {'Couier Name': 'James', 'Phone Number': '07956322483'}
courier_6 = {'Courier Name': 'Hector', 'Phone Number': '07956322933'}
courier_lst = []
courier_dct = {}
l_o_c = len(courier_lst)

cour_num_rows = 0

for row in open('C:/Users/chesney/Documents/Python Programme/Mini-project/Courier_lst.csv'):
    cour_num_rows += 1

cour_num = cour_num_rows -1


courier_num_options = "\nPlease select:\n\n[0] Exit to Main Menu\n[1] Courier List\n[2] Add Courier\n[3] Replace Courier\n[4] Delete Courier\n"
product_num_options = "\nPlease select:\n\n[0] Exit to Main Menu\n[1] Product List\n[2] Add Product\n[3] Replace Product\n[4] Delete Product\n"
order_num_options = "\nPlease select:\n\n[0] Exit to Main Menu\n[1] Order List\n[2] Create New Order\n[3] Update Order Status\n[4] Update Order\n[5] Delete Order\n"
main_menu_num = "\nWelcome to the Main Menu\n\nPlease select:\n[0] Exit App\n[1] Product Options\n[2] Courier Options\n[3] Order Option\n"
start_app_num = "\nHello, Welcome Gen Convenience\n\nPlease select:\n[0] Exit App\n[1] Main Menu\n"
select_status = [['[1] Preparing', 'Preparing'], ['[2] Out for Devlivery', 'Out for Delivery'], ['[3] Delivered', 'Delivered']]
c_uos = '\nPlease Select:\n\n[0] CANCEL\n[1] Update Order Status\n'
c_uod = '\nPlease Select:\n\n[0] CANCEL\n[1] Update Customer Order Details\n'
c_dod = '\nPlease Select:\n\n[0] CANCEL\n[1] Delete Customer Order Details\n'
c_upd = '\nPlease Select:\n\n[0] CANCEL\n[1] Update Product Details\n'
c_dpd = '\nPlease Select:\n\n[0] CANCEL\n[1] Delete Product Details\n'

c = 'No Changes Made'
ce = 'Updating...'

def print_n():
    print('\n')

def user_input_1():
    user_input_1 = input()
    return user_input_1.title()

def user_input_2():
    user_input_2 = input()
    return user_input_2

product_file_csv = 'C:/Users/chesney/Documents/Python Programme/Mini-project/Product_lst.csv'
courier_file_csv = 'C:/Users/chesney/Documents/Python Programme/Mini-project/Courier_lst.csv'
orders_file_csv = 'C:/Users/chesney/Documents/Python Programme/Mini-project/Order_lst.csv'
# ----------------------------------------------------------------------------------------------SELECT PRODUCT ------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------SELECT PRODUCT ID ----------------------------------------------------------------

# -------------------------------------------------------------------------------------------- PRODUCTS --------------------------------------------------------------------------------------------------------------------------------------------------------------
# view product list
def print_product_list():
    print('\nProduct List:\n')
    for value in product_lst:
        print(f'{value}')
# print_product_list()

# ------------------------------------------------------------------------------------------ CREATE PRODUCT --------------------------------------------------------------------------------------------------------------------------------------------------------
def create_product_name():
    print('Product Name: ')
    p_u_i = user_input_1()
    return p_u_i
# create_product_name()

def create_product_price():
    print('Product Price:')
    pr_u_i = user_input_2()
    while pr_u_i.replace(".", "", 1).isdigit() == False:
        print('Invalid input')
        print('Product Price:')
        pr_u_i = user_input_2()
        pr_u_i
    f_pr_u_i = float(pr_u_i)
    return f_pr_u_i
# create_product_price()

# create new prodct db
def create_new_product_db():
    connection = open_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            print('Enter Product Details')
            print_n()
            product_name = create_product_name()
            print_n()
            product_price = create_product_price()
            print_n()
            print('Adding Product...')
            print(product_name, product_price)
            
            sql = "INSERT INTO products (product_name, product_price) VALUES (%s, %s)"
            val = (product_name, product_price)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            connection.close()
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    except Exception as e:
        print('An error occured: ' + str(e))
    load_product_db()
# create_new_product_db()

# ---------------------------------------------------------------------------------------------SELECT PRODUCT-------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------- UPDATE PRODUCT -----------------------------------------------------------------------------------------------------------------------------------------------------
def update_product_name(create_product_name, sel_prod_id):
    connection = open_connection()
    prod_nam_in = create_product_name()
    if prod_nam_in == "":
        print(c)
    else:
        print(ce)
        s_p_id = sel_prod_id['ID']
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "UPDATE products SET product_name = %s WHERE product_id = %s"
            val = (prod_nam_in, s_p_id)
            cursor.execute(sql, val)
            connection.commit()
            # connection.close()
# update_product_name(create_product_name)

def update_product_price(user_input_2, sel_prod_id):
    connection = open_connection()
    empty_string = ""
    print('Enter Product Price:')
    prod_price_in = user_input_2()
    while prod_price_in.replace(".", "", 1).isdigit() == False and prod_price_in != empty_string:
        print('Invalid input')
        print('Enter Product Price:')
        prod_price_in = user_input_2()
    if prod_price_in == "":
        print(c)
    else:
        fl_prod_price_in = float(prod_price_in)
        print(ce)
        s_p_id = sel_prod_id['ID']
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "UPDATE products SET product_price = %s WHERE product_id = %s"
            val = (fl_prod_price_in, s_p_id)
            cursor.execute(sql, val)
            connection.commit()
        # connection.close()
# update_product_price()


# Update details
def update_product(sel_prod_id):
    print_n()
    update_product_name(create_product_name, sel_prod_id)
    print_n()
    update_product_price(user_input_2, sel_prod_id)
    print_n()
    load_product_db()
# update_product()

# --------------------------------------------------------------------------------------------DELETE PRODUCT ---------------------------------------------------------------------------------------------------------------------------------------------------
def del_sel_prod(sel_prod_id):
    connection = open_connection()
    print('Deleting...')
    s_p_id = sel_prod_id['ID']
    print(sel_prod_id)
    
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "DELETE FROM products WHERE product_id = %s"
        val = (s_p_id)
        cursor.execute(sql, val)
        connection.commit()
# del_sel_prod(sel_prod_dict)

def delete_product(sel_prod_id):
    print_n()
    del_sel_prod(sel_prod_id)
    load_product_db()
# delete_product(sel_prod_dict)

# ----------------------------------------------------------------------------------------- WRITE & READ -----------------------------------------------------------------------------------------------------------------------------------------------------
def load_product_db():
    product_lst.clear()
    connection = pymysql.connect(host, user, password, database)
    cursor = connection.cursor()
    cursor.execute("SELECT product_id, product_name, product_price FROM products")
    rows = cursor.fetchall()
    for row in rows:
        prod = {'ID': row[0], 'Product Name': row[1], 'Price': row[2]}
        # print(f'ID: {row[0]} Product: {str(row[1])}, Price: {row[2]}')
        # print(prod)
        product_lst.append(prod)
    cursor.close()
    connection.close()
# load_product_db()


def sel_product_id():
    print_product_list()
    print_n()
    print('Select Product ID or 0 to Cancel:')
    up_can = user_input_2()
    while up_can.isdigit() == False:
        print('Invalid input')
        print('Select Product ID or 0 to Cancel:')
        up_can = user_input_2()
    if up_can == "0":
        print('Exiting...')
        product_options()
    elif up_can != "0":
        int_up_can = int(up_can)

    
        temp_lst = []
        for product in product_lst:
            temp_lst.append(product['ID'])
            
        while int_up_can not in temp_lst:
            print('Invalid')
            up_can = user_input_2()
            int_up_can = int(up_can)

        for product in product_lst:    
            if int_up_can == product['ID']:
                selected_product = product
                print(selected_product)
                break
    return selected_product
# sel_product_id()


# -------------------------------------------------------------------------------------------- PRODUCT OPTIONS ----------------------------------------------------------------------------------------------------------------------------------------------------
# Courier options
def product_options():
    clear()
    print(product_num_options)
    prod_num_sel = user_input_2()
    
    while prod_num_sel.isdigit() == False:
        print('Invalid input')
        print('Select from the following:\n',product_num_options)
        prod_num_sel = user_input_2()
    int_prod_num_sel = int(prod_num_sel)
    
    while int_prod_num_sel not in [0, 1, 2, 3, 4]:
        print('Invalid input')
        print('Select from the following options:')
        print(product_num_options) 
        prod_num_sel = user_input_2()
        int_prod_num_sel = int(prod_num_sel)
    
    while int_prod_num_sel in [0, 1, 2, 3, 4]:
        if int_prod_num_sel == 1:
            print_product_list()
            print(product_num_options)
            prod_num_sel = user_input_2()
            int_prod_num_sel = int(prod_num_sel)
        
        elif int_prod_num_sel == 2:
            create_new_product_db()
            print(product_num_options)
            prod_num_sel = user_input_2()
            int_prod_num_sel = int(prod_num_sel)
        
        elif int_prod_num_sel == 3:
            sel_prod_id = sel_product_id()
            update_product(sel_prod_id)
            print(product_num_options)
            prod_num_sel = user_input_2()
            int_prod_num_sel = int(prod_num_sel)
        
        elif int_prod_num_sel == 4:
            sel_prod_id = sel_product_id()
            delete_product(sel_prod_id)
            print(product_num_options)
            prod_num_sel = user_input_2()
            int_prod_num_sel = int(prod_num_sel)
        
        elif int_prod_num_sel == 0:
            main_menu()
        while int_prod_num_sel not in [0, 1, 2, 3, 4]:
            print("Invalid input")
            print('Select from the following options:')
            print(product_num_options)
            prod_num_sel = user_input_2()
            int_prod_num_sel = int(prod_num_sel)
# product_options()








# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------- COURIER -------------------------------------------------------------------------------------------------------------------------------------------------------------

# print courier list
def print_courier_list():
    print('\nCourier List:\n')
    for value in courier_lst:
        print(f'{value}')
# print_courier_list()

# ------------------------------------------------------------------------------------------CREATE COURIER--------------------------------------------------------------------------------------------------------------------------------------------------------

def create_courier_name():
    print('Courier Name:')
    cour_name = user_input_1()
    return cour_name

def create_courier_num():
    print('Courier Contact No:')
    cour_con_num = user_input_2()
    while cour_con_num.isdigit() == False or len(cour_con_num) != 11:
        print('Invalid input')
        print('Courier Contact No:')
        cour_con_num = user_input_2()
    return cour_con_num


def create_new_courier_db():
    connection = open_connection()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            print('Enter Courier Details')
            print_n()
            courier_name = create_courier_name()
            print_n()
            courier_num = create_courier_num()
            print_n()
            print('Adding Courier...')
            print(courier_name, courier_num)
            
            sql = "INSERT INTO courier (courier_name, courier_num) VALUES (%s, %s)"
            val = (courier_name, courier_num)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            connection.close()
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    except Exception as e:
        print('An error occured: ' + str(e))
    load_courier_db()
# create_new_courier_db()

# ----------------------------------------------------------------------------------------SELECT COURIER ID ------------------------------------------------------------------------------------------------------------------------------------------------------

def sel_courier_id():
    print_courier_list()
    print_n()
    print('Select Courier ID or 0 to Cancel:')
    up_can = user_input_2()
    while up_can.isdigit() == False:
        print('Invalid input')
        print('Select Courier ID or 0 to Cancel:')
        up_can = user_input_2()
    if up_can == "0":
        print('Exiting...')
        product_options()
    elif up_can != "0":
        int_up_can = int(up_can)
    
        temp_lst = []
        for courier in courier_lst:
            temp_lst.append(courier['ID'])
        # print(temp_lst)
            
        while int_up_can not in temp_lst:
            print('Invalid input')
            print('Select Courier ID or 0 to Cancel:')
            up_can = user_input_2()
            int_up_can = int(up_can)
        for courier in courier_lst:    
            if int_up_can == courier['ID']:
                selected_courier = courier
                print(selected_courier)
                break

    return selected_courier
# sel_courier_id()

# ----------------------------------------------------------------------------------------UPDATE COURIER----------------------------------------------------------------------------------------------------------------------------------------------------------

# Update details
def update_courier_name(create_courier_name, sel_cour_id):
    connection = open_connection()
    cour_nam_in = create_courier_name()
    if cour_nam_in == "":
        print(c)
    else:
        print(ce)
        s_c_id = sel_cour_id['ID']
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "UPDATE courier SET courier_name = %s WHERE courier_id = %s"
            val = (cour_nam_in, s_c_id)
            cursor.execute(sql, val)
            connection.commit()
# update_courier_name(create_courier_name, sel_cour_dict)

def update_courier_num(user_input_2, sel_cour_id):
    connection = open_connection()
    empty_string = ""
    print('Enter Courier Contact Number:')
    cour_con_in = user_input_2()
    while cour_con_in.isdigit == False and cour_con_in != empty_string:
        print('Invalid input')
        print('Enter Courier Contact Number:')
        cour_con_in = user_input_2()
    if cour_con_in == "":
        print(c)
    else:
        print(ce)
        s_c_id = sel_cour_id['ID']
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "UPDATE courier SET courier_name = %s WHERE courier_id = %s"
            val = (cour_con_in, s_c_id)
            cursor.execute(sql, val)
            connection.commit()
# update_courier_num(user_input_2, sel_cour_id)

def update_courier(sel_cour_id):
    print_n()
    update_courier_name(create_courier_name, sel_cour_id)
    print_n()
    update_courier_num(user_input_2, sel_cour_id)
    print_n()
    load_courier_db()
# update_courier()


# --------------------------------------------------------------------------------------DELETE COURIER -----------------------------------------------------------------------------------------------------------------------------------------------------------
def del_sel_cour(sel_cour_id):
    connection = open_connection()
    print('Deleting...')
    s_c_id = sel_cour_id['ID']
    print(sel_cour_id)
    
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "DELETE FROM courier WHERE courier_id = %s"
        val = (s_c_id)
        cursor.execute(sql, val)
        connection.commit()
        # print_courier_list()
# del_sel_cour(sel_cour_dict)

def delete_courier(sel_cour_id):
    print_n()
    del_sel_cour(sel_cour_id)
    load_courier_db()
# delete_courier(sel_cour_dict)


# ---------------------------------------------------------------------------------------LOAD SQL DB-------------------------------------------------------------------------------------------------------------------------------------------------------------

def load_courier_db():
    courier_lst.clear()
    connection = pymysql.connect(host, user, password, database)
    cursor = connection.cursor()
    cursor.execute("SELECT courier_id, courier_name, courier_number FROM courier")
    rows = cursor.fetchall()
    for row in rows:
        cour = {'ID': row[0], 'Courier Name': row[1], 'Number': row[2]}
        # print(f'ID: {row[0]} Product: {str(row[1])}, Price: {row[2]}')
        # print(prod)
        courier_lst.append(cour)
    cursor.close()
    connection.close()
# load_courier_db()

# --------------------------------------------------------------------------------------COURIER OPTIONS---------------------------------------------------------------------------------------------------------------------------------------------------------

# Courier option
def courier_options():
    clear()
    print(courier_num_options)
    cour_num_sel = user_input_2()
   
    while cour_num_sel.isdigit() == False:
        print('Invalid input')
        print('Select from the follwoing:\n',courier_num_options)
        cour_num_sel = user_input_2()
    int_cour_num_sel = int(cour_num_sel)
    
    while int_cour_num_sel not in [0, 1, 2, 3, 4]:
        print('Invalid input')
        print('Select from the follwoing:')
        print(courier_num_options)
        cour_num_sel = user_input_2()
        int_cour_num_sel = int(cour_num_sel)
    
    while int_cour_num_sel in [0, 1, 2, 3, 4]:
        if int_cour_num_sel == 1:
            print_courier_list()
            print(courier_num_options)
            cour_num_sel = user_input_2()
            int_cour_num_sel = int(cour_num_sel)
        
        elif int_cour_num_sel == 2:
            create_new_courier_db()
            print(courier_num_options)
            cour_num_sel = user_input_2()
            int_cour_num_sel = int(cour_num_sel)
        
        elif int_cour_num_sel == 3:
            sel_cour_id = sel_courier_id()
            update_courier(sel_cour_id)
            print(courier_num_options)
            cour_num_sel = user_input_2()
            int_cour_num_sel = int(cour_num_sel)
        
        elif int_cour_num_sel == 4:
            sel_cour_id = sel_courier_id()
            delete_courier(sel_cour_id)
            print(courier_num_options)
            cour_num_sel = user_input_2()
            int_cour_num_sel = int(cour_num_sel)
        
        elif int_cour_num_sel == 0:
            main_menu()
        while int_cour_num_sel not in [0, 1, 2, 3, 4]:
            print('Invalid input')
            print('Select from the follwoing options:')
            print(courier_num_options)
            cour_num_sel = user_input_2()
            int_cour_num_sel = int(cour_num_sel)    
# courier_options()



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------ORDERS -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Print order list
def print_order_list():
    print('\nOrder List:\n')
    for value in orders:
        print(f'{value}')
# print_order_list()

# ----------------------------------------------------------------------------------------CREATE ORDER------------------------------------------------------------------------------------------------------------------------------------------------------
def create_order_name():
    print('Customer Name:')
    o_u_i = user_input_1()
    return o_u_i

def create_order_add():
    print('Customer Address:')
    add_u_i = user_input_2()
    return add_u_i


# add_items
def add_items(user_input):
    if user_input == "0":
        print('Exiting...')
        order_options()
    else:
        while user_input.isdigit() == False:
            print('Invalid input')
            user_input = input('Select item: ')
        u_i = int(user_input)
        while u_i > prod_num:
            print(f'Only {prod_num} items available, chose from the following')
            user_input = input('Select item: ')
            u_i = int(user_input)
        items.append(u_i)
        print(items,'\n')  

# add courier indx
def add_courier_indx(user_input):
    if user_input == "0":
        print('Exiting...')
        order_options()
    else:
        while user_input.isdigit() == False:
            print('Invalid input')
            user_input = input('Select Courier: ')
        u_i = int(user_input)
        while u_i > cour_num:
            print(f'Only {cour_num} couriers available, choose from the following:')
            user_input = input('Select Courier: ')
            u_i = int(user_input)
        # orders_dict['Courier'] = courier_lst[(u_i)-1]
        orders_dict['Courier'] = u_i
        print('Adding Courier...')
        print(courier_lst[(u_i)-1])
        while user_input.isdigit() == False:
            print('Invalid input')
            user_input = input('Select item: ')
        u_i = int(user_input)
# user_input = input()
# add_courier_indx(user_input)

# add contact no
def add_contact_no(user_input):
    if user_input == "00":
        print('Exiting...')
        order_options()
    else:
        while user_input.isdigit() == False or len(user_input) != 11:
            print('Invalid input')
            user_input = input('Enter Contact No or 00 to Cancel: ')
        orders_dict['Contact No'] = user_input
        print('Adding Contact Number...')
# user_input = input('Enter Contact No: ')
# add_contact_no(user_input)

# add status
def add_status(user_input):
    if user_input == "0":
        print('Exiting...')
        order_options()
    elif user_input != "0":
        while user_input.isdigit() == False:
            print('Invalid input\n')
            print('Choose from the folloing: ')
            print(select_status[0][0])
            print(select_status[1][0])
            print(select_status[2][0])
            user_input = input('Select status: ')
        u_i = int(user_input)    
        while u_i not in [1, 2, 3]:
                print('\nSelect Status')
                print('Invalid selection\n')
                print('Choose from the folloing: ')
                print(select_status[0][0])
                print(select_status[1][0])
                print(select_status[2][0])
                print('\n')
                user_input = input('Select status: ')
                u_i = int(user_input)
        orders_dict['Status'] = select_status[int(u_i) -1][1]
        print('Status set to:')
        print(orders_dict['Status'])
# user_input = input('Select status: ')
# add_status(user_input)

# add name
def add_name(user_input):
    if user_input == "0":
        print('Exiting...')
        order_options()
    else:
        orders_dict['Name'] = user_input
        print('Adding Name...')
        # print(orders_dict['Name'])
# user_input = input('Enter name or 0 to canel: ').title()
# add_name(user_input)

# add address
def add_address(user_input):
    if user_input == "0":
        print('Exiting...')
        order_options()
    else:
        orders_dict['Address'] = user_input
        print('Adding Address...')
        # print(orders_dict['Address'])
# user_input = input('Enter address or 0 to canel: ').title()
# add_address(user_input)

# create new order
def create_new_order():
    clear()
    print('Create Order\n\nPlease Enter Customer Details:')
    
    print('Enter Name or 0 to Cancel:')
    nam_u_i = user_input_1()
    add_name(nam_u_i)
    print_n()
    
    print('Enter Address or 0 to Cancel:')
    add_u_i = user_input_2()
    add_address(add_u_i)
    print_n()
    
    print('Enter Contact No or 00 to Cancel:')
    con_u_i = user_input_2()
    add_contact_no(con_u_i)
    print_n()
    
    print_courier_list()
    print_n()
    print('Select Courier or 0 to Cancel:')
    cour_u_i = user_input_2()
    add_courier_indx(cour_u_i)
    print_n()
    
    print('\nSelect Status:')
    print(select_status[0][0])
    print(select_status[1][0])
    print(select_status[2][0])
    print_n()
    sel_stat_u_i = user_input_2()
    add_status(sel_stat_u_i)
    print_n()

    print_product_list()
    print_n()
    new_list = []
    print('Select Item:')
    add_i_u_i = user_input_2()
    add_items(add_i_u_i)
    
    print('Would you like to add more items?\nY/N:')
    ask_again = user_input_1()
    
    while ask_again != "Y" and ask_again != "N":
        print('Invalid input')
        print('Would you like to add more items?\nY/N:')
        ask_again = user_input_1()
    while ask_again == "YES" or ask_again == "Yes" or ask_again == "Y" or ask_again == "yes" or ask_again == "y":
        print('Select Item:')
        add_i_u_i = user_input_2()
        add_items(add_i_u_i)
        print('Add more items?\nY/N:')
        ask_again = user_input_1()
        

    if ask_again == "NO" or ask_again == "No" or ask_again == "N" or ask_again == "no" or ask_again == "n":
        print(items)
    
    for i in items:
        i -= 1
        new_list.append(product_lst[i])
    orders_dict['Items'] = items
    # print(orders_dict['Items'])
    print('\nAdding Proucts...')
    print(new_list)
    print_n()
    
    dct_copy = orders_dict.copy()
    orders.append(dct_copy)
    print('Adding New Order...')
    print(dct_copy)
    print_order_list()
# create_new_order()



# -----------------------------------------------------------------------------------------  SELECTED ORDER -----------------------------------------------------------------------------------------------------------------------------------------------
def select_order():
    print_order_list()
    print_n()
    print('Select Order or 0 to Cancel:')
    uo_can = user_input_2()
    while uo_can.isdigit() == False:
        print('Invalid input')
        print('Select Product or 0 to Cancel:')
        uo_can = user_input_2()
    if uo_can == "0":
        print('Exiting...')
        order_options()
    else:
        int_uo_can = int(uo_can)
        while int_uo_can > ord_num:
            print(f'Only {ord_num} orders available, choose from the following:')
            print_order_list()
            print_n()
            print('Select or 0 to Cancel:')
            uo_can = user_input_2()
            int_uo_can = int(uo_can)
        sel_ord = orders[int_uo_can -1]
        print('\nOrder Selected:\n',sel_ord)
    return sel_ord
# sel_ord_dict = select_order()

# -------------------------------------------------------------------------------------------UPDATE STATUS -----------------------------------------------------------------------------------------------------------------------------------------------


def status(user_input):
    while user_input.isdigit() == False:
        print('Invalid input')
        print('Choose from the following:\n')
        print(select_status[0][0])
        print(select_status[1][0])
        print(select_status[2][0])
        user_input = input('Select Status: ')
    u_i_1 = int(user_input)
    while u_i_1 not in [1, 2, 3]:
        print('Invalid selection')
        print('Choose from the following:\n')
        print(select_status[0][0])
        print(select_status[1][0])
        print(select_status[2][0])
        print('\n')
        user_input = input('Select Staus: ')
        u_i_1 = int(user_input)
    return u_i_1
# user_input = input('Select Status: ')
# status(user_input)

# Update order status
def update_order_status(user_input_2, sel_ord_dict):
    print('\nSelect Status:')
    print_n()
    print(select_status[0][0])
    print(select_status[1][0])
    print(select_status[2][0])
    print_n()
    u_o_s = user_input_2()
    s_s = status(u_o_s)
    sel_ord_dict['Status'] = select_status[s_s -1][1]
    print(ce)
    print(sel_ord_dict)
    
    # clear()

        # print_n()
        # print(select_status[0][0])
        # print(select_status[1][0])
        # print(select_status[2][0])
        # print('\n')
        
        # user_input = input('Select Status: ')
        # s_s = status(user_input)
        # s_o['Status'] = select_status[s_s-1][1]
        # print('Changed to:',s_o['Status'])
        # print(s_o)
# user_input = input('Select an Order or 0 to Cancel: ')
# update_order_status(user_input_2, sel_ord_dict)

def update_status(sel_ord_dict):
    update_order_status(user_input_2, sel_ord_dict)
# update_status(sel_ord_dict)

# ----------------------------------------------------------------------------------------UPDATE ORDER DETAILS ------------------------------------------------------------------------------------------------------------------------------------------
# update order name
def update_order_name(create_order_name, sel_ord_dict):
    ord_nam_in = create_order_name()
    if ord_nam_in == "":
        print(c)
    else:
        print(ce)
        sel_ord_dict['Name'] = ord_nam_in
# update_order_name(create_order_name, sel_ord_dict)

# update order address
def update_order_address(create_order_address, sel_ord_dict):
    ord_add_in = create_order_add()
    if ord_add_in == "":
        print(c)
    else:
        print(ce)
        sel_ord_dict['Address'] = ord_add_in
# update_order_address(create_order_name, sel_ord_dict)

def update_order_num(user_input_2, sel_ord_dict):  
    empty_string = ""
    print('Customer Contact Number:')
    ord_con_in = user_input_2()
    while ord_con_in.isdigit == False and ord_con_in != empty_string:
        print('Invalid input')
        print('Customer Contact Number:')
        ord_con_in = user_input_2()
    if ord_con_in == "":
        print(c)
    else:
        print(ce)
        sel_ord_dict['Contact No'] = ord_con_in
# update_order_num(user_input_2, sel_ord_dict)

def update_order_cour(user_input_2, sel_ord_dict):
    empty_string = ""
    print('Select Courier')
    cour_ui = user_input_2()
    while cour_ui.isdigit() == False and cour_ui != empty_string:
        print('Invalid input')
        print_n()
        print_courier_list()
        print_n()
        print('Select Courier:')
        cour_ui = user_input_2()    
    if cour_ui == "":
        print(c)
        print(sel_ord_dict['Courier'], '\n')
    else:
        int_cour_ui = int(cour_ui)
        while int_cour_ui > l_o_c:
            print(f'Only {l_o_c} orders avaiable, choose from the following:')
            print_n()
            print_courier_list()
            cour_ui = user_input_2()
            int_cour_ui = int(cour_ui)
        sel_ord_dict['Courier'] = courier_lst[int_cour_ui -1]
        print(ce)
        print(sel_ord_dict['Courier'], '\n')
# update_order_cour(user_input_2, sel_ord_dict)

def update_items(user_input_2):
    up_it = user_input_2()
    while up_it.isdigit() == False:
        print('Invalid input')
        print('Select item:')
        up_it = user_input_2()
    int_up_it = int(up_it)
    while int_up_it > l_o_p:
        print(f'Only {l_o_p} items available, chose from the following')
        up_it = user_input_2()
        int_up_it = int(up_it)
    # items.append(int_up_it)
    # print(items,'\n')
    return int_up_it
# update_items(user_input_2)

def update_order_items(user_input_2, sel_ord_dict):
    new_list = []
    print('Select Items')
    retr_item = update_items(user_input_2)
    items.append(retr_item)
    print(items)
    
    print('Would you like to add more items?\nY/N:')
    # ask_again = user_input_1()
    ask_again = user_input_1()
    while ask_again != "Y" and ask_again != "N":
        print('Invalid input')
        print('Would you like to add more items?\nY/N:')
        ask_again = user_input_1()
    
    while ask_again == "YES" or ask_again == "Yes" or ask_again == "Y" or ask_again == "yes" or ask_again == "y":
        print('Select Item:')
        add_i_u_i = user_input_2()
        add_items(add_i_u_i)
        print('Add more items?\nY/N:')
        ask_again = user_input_1()
        

    if ask_again == "NO" or ask_again == "No" or ask_again == "N" or ask_again == "no" or ask_again == "n":
        print(items)
    
    for x in items:
        x -=1
        new_list.append(product_lst[x])
        sel_ord_dict['Items'] = items
    print('\nUpdating Items...')
    print(new_list)
    
# update_order_items(user_input_2, sel_ord_dict)

# Update details
def update_details(sel_ord_dict):
    print_n()
    update_order_name(create_order_name, sel_ord_dict)
    print_n()
    update_order_address(create_order_add, sel_ord_dict)
    print_n()
    update_order_num(user_input_2, sel_ord_dict)
    print_n()
    print_courier_list()
    update_order_cour(user_input_2, sel_ord_dict)
    print_n()
    print_product_list()
    update_order_items(user_input_2, sel_ord_dict)
    print_n()
    print(sel_ord_dict)
    # print('Select Order or 0 to Cancel:')
    # up_det_ui = user_input_2()
    # if up_det_ui == "0":
    #     print('Exiting...')
    #     order_options()
    # else:
    #     while up_det_ui.isdigit() == False:
    #         print('Invalid input')
    #         print('Select Order or 0 to Cancel:')
    #         up_det_ui = user_input_2()
    #         int_up_det_ui = int(up_det_ui)
            
    #     while int_up_det_ui > l_o_o:
    #         print(f'Only {l_o_o} orders available, please choose from the following:')
    #         print_order_list()
    #         print_n()
    #         print('Select Order or 0 to Cancel:')
    #         up_det_ui = user_input_2()
    #         int_up_det_ui = int(up_det_ui)
    
    #     sel_ord = orders[int_up_det_ui -1]
    #     print(sel_ord)
        
    #     print('Enter Name:')
    #     nam_ui = user_input_1()
    #     if nam_ui == "":
    #         print(c)
    #         print(sel_ord['Name'],'\n')
    #     else:
    #         sel_ord['Name'] = nam_ui
    #         print(ce)
    #         print(sel_ord['Name'], '\n')
        
    #     print('Enter Address:')
    #     add_ui = user_input_2()
    #     if add_ui == "":
    #         print(c)
    #         print(sel_ord['Address'], '\n')
    #     else:
    #         sel_ord['Address'] = add_ui
    #         print(ce)
    #         print(sel_ord['Address'], '\n')
    
    # empty_string = ""
    # print('Enter Contact Number:')
    # num_ui = user_input_2()
    # while num_ui.isdigit() == False and num_ui != empty_string or len(num_ui) != 11:
    #     print('Invalid input')
    #     print('Enter Contact Number:')
    #     num_ui = user_input_2()
    #     if num_ui == "":
    #         print(c)
    #         print(sel_ord['Contact No'], '\n')
    #     else:
    #         print(ce)
    #         sel_ord['Contact No'] = num_ui
    #         print(sel_ord['Contact No'],'\n')    
    
    # print_courier_list()
    # print_n()
    # print('Select Courier')
    # cour_ui = user_input_2()
    # while cour_ui.isidgit == False and cour_ui != empty_string:
    #     print('Invalid input')
    #     print_n()
    #     print_courier_list()
    #     print_n()
    #     print('Select Courier:')
    #     cour_ui = user_input_2()    
    # if cour_ui == "":
    #     print(c)
    #     print(sel_ord['Courier'], '\n')
    # else:
    #     int_cour_ui = int(cour_ui)
    #     while int_cour_ui > l_o_o:
    #         print(f'Only {l_o_o} orders avaiable, choose from the following:')
    #         print_n()
    #         print_courier_list()
    #         cour_ui = user_input_2()
    #     int_cour_ui = int(cour_ui)
    #     sel_ord['Courier'] = courier_lst[int_cour_ui -1]
    #     print(ce)
    #     print(sel_ord['Courier'], '\n')
    # print_order_list
# update_details(sel_ord_dict)
# ------------------------------------------------------------------------------------------- DELETE------------------------------------------------------------------------------------------------------------------------------------------------------

# delete selected order
def del_sel_ord(sel_ord_dict):
    print('Deleting...')
    print(sel_ord_dict)
    orders.remove(sel_ord_dict)
    print_order_list()

# Del order
def del_order(sel_ord_dict):
    print_n()
    del_sel_ord(sel_ord_dict)
# del_order(sel_ord_dict)

# -----------------------------------------------------------------------------------------READ & WRITE--------------------------------------------------------------------------------------------------------------------------------------------------
# Load order from csv
def load_order():
    try:
        with open('C:/Users/chesney/Documents/Python Programme/Mini-project/Order_lst.csv') as order_options:
            reader = csv.DictReader(order_options)
            for row in reader:
                orders.append(row)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    except Exception as e:
        print('An error occured: ' + str(e)) 
# load_order()

# save courier updates
def save_order_updates():
    try:
        keys = orders[0].keys()
        with open('C:/Users/chesney/Documents/Python Programme/Mini-project/Order_lst.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(orders)
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    except Exception as e:
        print('An error occured: ' + str(e))        

# save_order_updates()


# -------------------------------------------------------------------------------------------------------- ORDER OPTIONS
# order options
def order_options():
    clear()
    print(order_num_options)
    ord_num_sel = user_input_2()
    
    while ord_num_sel.isdigit() == False:
        print('Invalid input')
        print('Select from the following:\n',order_num_options)
        ord_num_sel = user_input_2()
    int_ord_num_sel = int(ord_num_sel)

    
    while int_ord_num_sel not in [0, 1, 2, 3, 4, 5]:
        print("Input invalid")
        print('Select from the following:')
        print(order_num_options) 
        ord_num_sel = user_input_2()
        int_ord_num_sel = int(ord_num_sel)
    
    while int_ord_num_sel in [0, 1, 2, 3, 4, 5]:
        if int_ord_num_sel == 1:
            print_order_list()
            print(order_num_options)
            ord_num_sel = user_input_2()
            int_ord_num_sel = int(ord_num_sel)
        
        elif int_ord_num_sel == 2:
            create_new_order()
            print(order_num_options)
            ord_num_sel = user_input_2()
            int_ord_num_sel = int(ord_num_sel)
        
        elif int_ord_num_sel == 3:
            sel_ord_dict = select_order()
            update_status(sel_ord_dict)
            print(order_num_options)
            ord_num_sel = user_input_2()
            int_ord_num_sel = int(ord_num_sel)
        
        elif int_ord_num_sel == 4:
            sel_ord_dict = select_order()
            update_details(sel_ord_dict)
            print(order_num_options)
            ord_num_sel = user_input_2()
            int_ord_num_sel = int(ord_num_sel)
        
        elif int_ord_num_sel == 5:
            sel_ord_dict = select_order()
            del_order(sel_ord_dict)
            print(order_num_options)
            ord_num_sel = user_input_2()
            int_ord_num_sel = int(ord_num_sel)            
        
        elif int_ord_num_sel == 0:
            main_menu()
        while int_ord_num_sel not in [0, 1, 2, 3, 4, 5]:
            print("Input invalid")
            print('Select from the following:')
            print(order_num_options) 
            ord_num_sel = user_input_2()
            int_ord_num_sel = int(ord_num_sel)
# order_options()

# -------------------------------------------------------------------------------------------- MAIN MENU -----------------------------------------------------------------------------------------------------------
# Main Menu
def main_menu():
    clear()
    main_menu =int(input(main_menu_num))
    while main_menu not in [0, 1, 2, 3]:
        print("Input invalid")
        main_menu =int(input(main_menu_num))
    if main_menu == 1:
        product_options()
    elif main_menu == 2:
        courier_options()
    elif main_menu == 3:
        order_options()
    elif main_menu == 0:
        save_order_updates()
        exit("Thank You !")
    return
# main_menu()

# Start app
def start_app():
    load_courier_db()
    load_product_db()
    load_order()
    start_app = int(input(start_app_num))
    while start_app not in [0, 1]:
        print("Input invalid")
        start_app = int(input(start_app_num))
    if start_app == 0:
        save_order_updates()
        exit()
    elif start_app == 1:
        main_menu()
start_app()