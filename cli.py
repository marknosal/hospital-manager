from sys import exit

from lib.db.database import session

from lib.db.functions.read_functions import read_func_1 as read
from lib.db.functions.add_functions import add_func_1 as add
from lib.db.functions.update_functions import update_func_1 as update
from lib.db.functions.delete_functions import delete_func_1 as delete

def main():
    choice = 0
    while choice != 5:
        print('*** Hospital Manager ***')
        print('1) Look up records')
        print('2) Add record')
        print('3) Update records')
        print('4) Clear records')
        print('5) Quit')
        print()
        print('-' * 30)
        try:
            choice = int(input("Enter choice number: "))
            if choice == 1:
                read()
            elif choice == 2:
                add()
            elif choice == 3:
                update()
            elif choice == 4:
                delete()
            elif choice == 5:
                print('Closing application...')
                exit()
            else:
                print('Please enter valid choice (integers 1 through 5)')
        except ValueError:
            print('Try again')

    

if __name__ == '__main__':
    print()
    print('Welcome to Phase 3 Project!!') 
    print()
    print('-' * 30)
    print()
    main()
    session.close()