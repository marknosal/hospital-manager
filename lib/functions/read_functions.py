from .delete_functions import delete_func_1
from ..db.models import Doctor, Patient, Appointment
from ..cli import main
from ..db.database import session

def print_table(table):
    [print(row) for row in table]
    return [row for row in table]

def read_func_1():
    print()
    print('What records would you like to see?')
    print()
    choice = 0
    while choice != 5:
        print('1) Doctors')
        print('2) Patients')
        print('3) Appointments')
        print('4) Return to previous menu')
        print('5) Quit')
        print()
        print('-' * 30)
        choice = int(input('Enter choice number: '))
        print()
        results = list()
        if choice == 1:
            print_table(Doctor)
        elif choice == 2:
            print_table(Patient)
        elif choice == 3:
            print_table(Appointment)
        elif choice == 4:
            main()
        else:
            print('Closing application...')
    
