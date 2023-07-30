from ..db.database import session
from datetime import datetime

def add_func_1():
    def read_func_1():
    print()
    print('Schedule Appointment: ')
    print()
    choice = 0
    while choice != 5:
        print('Please enter date/time for appointment and with optional doctor')
        print()
        print('-' * 30)
        choice = int(input('Enter choice number: '))
        print()