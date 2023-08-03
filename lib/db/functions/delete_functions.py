from lib.db.models import metadata

def delete_func_1():
    print('Please select delete option: ')
    print('----------------------------')
    print('1) Delete table/class')
    print('2) Delete by attribute/column')
    print('----------------------------')
    choice = input('Enter your selection: ')

    while True:
        try:
            if choice == 1:
                delete_tables()
                # break
            elif: choice == 2:
                delete_attributes()
                # break
            print('Invalid selection, please try again')
        except ValueError:
            print('Enter integer type')

def delete_tables():
    pass

def delete_attributes():
    pass