from sys import exit
from lib.db.database import session
from lib.db.models import Doctor, Patient, Appointment
from random import choice as rc
from datetime import datetime, date


def save(row):
    session.add(row)
    session.commit()

def add_func_1():
    print()
    print('Which record would you like to add?')
    print()
    choice = 0
    while choice != 5:
        print('1) Doctor')
        print('2) Patient')
        print('3) Appointment')
        print('4) Return to previous menu')
        print('5) Quit')
        print()
        print('-' * 30)
        try:
            choice = int(input('Enter choice number: '))
            print()
            results = list()
            if choice == 1:
                add_func_2()
            elif choice == 2:
                add_func_3()
            elif choice == 3:
                add_func_4()
            elif choice == 4:
                print('Previous menu...')
                break
            elif choice == 5:
                print('Closing application...')
                exit()
            elif not 1 <= choice <= 5:
                print('Please enter valid choice (integers 1 through 5)')
        except ValueError:
            print('Please enter a valid integer choice (1 through 5)')

# add doctor
def add_func_2():
    name = input('Please enter Doctor\'s name: ')
    new_dr = Doctor(name=name)
    save(new_dr)

# add patient
def add_func_3():
    name = input('Enter name name of patient: ')
    age = input('Enter patient\'s age: ')
    new_patient = Patient(name=name, age=age)
    save(new_patient)

# add appointment
def add_func_4():
    year = input('Enter year of appointment (YYYY): ')
    month = input('Enter month of appointment (MM): ')
    day = input('Enter day of appointment (DD): ')
    hour = input('Enter hour (9am-17pm): ')
    minute = input('Enter minute (00, 15, 30, 45): ')
    appt_date = datetime(int(year), int(month), int(day), int(hour), int(minute))
    # import ipdb; ipdb.set_trace()

    print('Here are a list of doctors available on that day: ')
    [print(dr) for dr in has_appt_on_date(appt_date)]

    new_appt = Appointment(date_of_appt=appt_date, created_at=datetime.now())
    save(new_appt)

def has_appt_on_date(date):
    doctors = session.query(Doctor).filter().all()
    available_drs = list()
    for dr in doctors:
        if dr.appointments.month != date.month and dr.appointments.day != date.day:
            available_drs.append(dr)
    print(available_drs)
        
