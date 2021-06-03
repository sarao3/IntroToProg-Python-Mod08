# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# SaraONeal,6.1.2021,Created started script
# SaraONeal,6.1.2021,Added pseudo-code to start assignment 8
# SaraONeal,6.2.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: string type with product name
        product_price: float type with price of product
    methods:
    changelog: (When,Who,What)
        SaraONeal,6.1.2021,Created Class
        SaraONeal,6.2.2021,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class
    # Constructor
    def __init__(self, product_name, product_price):
        # Attributes
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error creating initial values for object")

    # Properties
    # Product Name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names can only include characters")

    # Product Price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric() == False:
            self.__product_price = float(value)
        else:
            raise Exception("Prices must be numbers")

    # Methods
    # def to_string(self):  # explicit definition; friendly version of def __str__(self)
    #    return self.__str__()

    def __str__(self):  # implicit definition
        return self.product_name + "," + str(self.product_price)

    def __doc__(self):
        return 'This class holds product information'

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        SaraONeal,6.1.2021,Created Class
        SaraONeal,6.2.2021,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Write data to a file from a list of product rows

        :param file_name: string type with name of file
        :param list_of_product_objects: list of product objects data saved to file
        """
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_objects, 'Success'

    # TODO: Add Code to process data to a file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of product rows

        :param file_name: string type with name of file
        :return: list of product rows
        """
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows, 'Success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ A class for performing input and output

    methods:
        print_menu_tasks():

        print_current_list_tasks(list_of_rows):

        input_product_data():

        changelog:  (When,Who,What)
            SaraONeal,6.1.2021,Created Class:
        """
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_tasks():
        """ Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save data to file
        4) Exit the program
        ''')
        print()

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_list_tasks(list_of_rows):
        """ Show the current tasks in the list of rows

        :param: list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("****** The current products are: ******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("****************************************")
        print()

    # TODO: Add code to get product data from user
    @staticmethod
    def input_product_data():
        """ Gets data for a product object

        :return: Input product data
        """
        try:
            name = str(input("What is the product name? - ").strip())
            price = float(input("What is the price? - ").strip())
            print()
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return p

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
try:
    listOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        # Show user a menu of options
        IO.print_menu_tasks()

        # Get user's menu option choice
        strChoice = IO.input_menu_choice()

        if strChoice.strip() == '1':

            # Show user current data in the list of product objects
            IO.print_current_list_tasks(lstOfProductObjects)
            continue

        elif strChoice.strip() == '2':

            # Let user add data to the list of product objects
            lstOfProductObjects.append(IO.input_product_data())
            continue

        elif strChoice.strip() == '3':

            # Let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue

        elif strChoice.strip() == '4':
            print("Goodbye!")
            break # and exit

except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')

# Main Body of Script  ---------------------------------------------------- #