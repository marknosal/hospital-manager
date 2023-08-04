from sys import exit
from lib.db.database import session
from lib.db.models import Doctor, Patient, Appointment

from datetime import datetime, date
import calendar


def save(row):
    session.add(row)
    session.commit()

def buffer(some_string):
    print('-' * 30)
    print('-' * 30)
    print(some_string)
    print('-' * 30)

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
    print('-' * 30)
    buffer('New Doctor saved!')

# add patient
def add_func_3():
    name = input('Enter name name of patient: ')

    while True:
        age = input('Enter patient\'s age: ')
        try:
            if 0 <= int(age) <= 130:
                break
            print('Please enter a valid age in whole/positive digits (less than 135)')
        except ValueError:
            print('Invalid input.  Please enter numeric age in whole numbers')
    
    new_patient = Patient(name=name, age=age)
    save(new_patient)
    buffer('New patient saved!')

# add appointment
def add_func_4():

    while True:
        # enter new appt date/time
        appt_date = enter_new_appt()
        # check if available drs for new appt date/time
        avail_drs = avail_drs_on_date(appt_date)

        if avail_drs:
            print('Here are a list of doctors available on that day: ')
            [print(dr) for dr in avail_drs]
            break
        print('Sorry, there are no available doctors for that date. Please try another time.\n')

    appt_dr_id = input('Please enter the number of the doctor you would like to see: ')
    pat_name = input('Please enter your first and last name: ')
    pat_age = input('Please enter your age: ')
    # if patient exists, but with a new age.  A new patient with same name but new age will be created
    appt_pat_id = generate_pat_id(pat_name, pat_age)
    
    new_appt = Appointment(date_of_appt=appt_date, created_at=datetime.now(), doctor_id=appt_dr_id, patient_id=appt_pat_id)
    save(new_appt)
    buffer(f'New appointment scheduled!  To confirm it is at {new_appt.date_of_appt.hour}:{new_appt.date_of_appt.minute} on day {new_appt.date_of_appt.day} of {calendar.month_name[new_appt.date_of_appt.month]}, {new_appt.date_of_appt.year}')

def enter_new_appt():
    # check year
    while True:
        year = input('Enter year of appointment (YYYY): ')
        year = int(year)
        if 2023 <= year:
            break
        print('Please enter valid year, 2023 or beyond.\n')
    
    # check month
    while True:
        month = input('Enter month of appointment (MM): ')
        if month.isdigit() and 1 <= int(month) <= 12:
            month = int(month)
            break
        print('Please enter a valid month (1 to 12 ) in the format \'MM\'\n')

    # check day
    while True:
        day = input('Enter day of appointment (DD): ')
        day = int(day)
        _, max_day = calendar.monthrange(year, month)
        if 1 <= day <= max_day:
            break
        print(f'Please enter a valid day (1 to {max_day}) in the format "DD".\n')

    # check hour
    while True:
        hour = input('Enter hour (9am-17pm): ') 
        try:
            if int(hour) in range(9, 18):
                hour = int(hour)
                break
            print('Invalid hour. Please enter an hour between 9am and 17pm.\n')
        except ValueError:
            print('Invalid input. Please enter a numeric hour.\n')

    # check minute
    while True:
        minute = input('Enter minute (00, 15, 30, 45): ')
        if minute in {'0', '00', '15', '30', '45'}:
            minute = int(minute)
            break
        print('Invalid minute value. Please enter 00, 15, 30, or 45.\n')

    return datetime(year, month, day, hour, minute)

def generate_pat_id(name, age):
    result = session.query(Patient).filter_by(name=name, age=age).first()
    if result:
        return result.id
    else:
        new_pat = Patient(name=name, age=age)
        session.add(new_pat)
        session.commit()
        return new_pat.id

def avail_drs_on_date(date):
    doctors = session.query(Doctor).filter().all()
    available_drs = []
    for dr in doctors:
        has_appt = False
        for appt in dr.appointments:
            if appt.date_of_appt.month == date.month and appt.date_of_appt.day == date.day and appt.date_of_appt.year == date.year:
                has_appt = True
                break
        if not has_appt:
            available_drs.append(dr)
    
    return available_drs

        
