

from db.database import session
from db.models import Doctor, Patient, Appointment

from functions.read_functions import read_func_1 as read
from functions.add_functions import add_func_1 as add
from functions.update_functions import update_func_1 as update
from functions.delete_functions import delete_func_1 as delete

def main():
    choice = 0
    while choice != 5:
        print('*** Hospital Manager ***')
        print('1) Look up records')
        print('2) Add  add records')
        print('3) Update records')
        print('4) Delete records')
        print('5) Quit')
        print()
        print('-' * 30)
        choice = int(input("Ener choice number: "))

        if choice == 1:
            read()
        elif choice == 2:
            add()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            print('Closing application...')

    

if __name__ == '__main__':
    print()
    print('Welcome to Phase 3 Project!!') 
    print()
    print('-' * 30)
    print()
    main()