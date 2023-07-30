from ..db.database import session
from ..db.models import Doctor, Patient, Appointment

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
            [print(dr) for dr in session.query(Doctor).all()]
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            main()
        else:
            print('Closing application...')
    
