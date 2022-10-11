from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data


def main():
    print("List of company employees")


def input_data():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    posit = input("Enter position: ")
    salary = input("Enter salary amount: ")
    return [last_name, first_name, posit, salary]


def choice_separator():
    sep = input("Specify separator: ")
    if sep == "":
        sep = None
    return sep


def select_action():
    print("Select an action:\n\
    1 - import;\n\
    2 - export;\n\
    3 - search by parameters.")
    sel = input("Enter the number of the action: ")
    if sel == '1':
        sep = choice_separator()
        import_data(input_data(), sep)
    elif sel == '2':
        data = export_data()
        print_data(data)
    else:
        lettering = input("Enter the searh data: ")
        data = export_data()
        elem = search_data(lettering, data)
        if elem != None:
            print("Last name".center(20), "First name".center(20),
                  "Position".center(15), "Salary amount".center(30))
            print("-"*85)
            print(elem[0].center(20), elem[1].center(20),
                  elem[2].center(15), elem[3].center(30))
        else:
            print("The data does not correspond to the list")
