from sys import exit
from lib.db.database import session
from lib.db.models import Doctor, Patient, Appointment
from sqlalchemy import desc
from lib.db.functions.add_functions import enter_new_appt, avail_drs_on_date, generate_pat_id
from lib.db.functions.add_functions import buffer

def update_func_1():
    print()
    print('Which record would you like to update?')
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
                update_func_2()
            elif choice == 2:
                update_func_3()
            elif choice == 3:
                update_func_4()
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

def validate_selected_id(selected_class, class_name):
    all_rows = session.query(selected_class).all()
    [print(row) for row in all_rows]

    while True:
        selected_id = input(f'Please enter the ID of the {class_name} you would like to update: ')
        try:
            if int(selected_id) in [row.id for row in all_rows]:
                return selected_id
            else:
                print(f'Please enter a valid ID from the list of {class_name}s')
        except ValueError:
            print('Enter a valid ID. Whole Number.')

# update Doctor
def update_func_2():
    selected_dr_id = validate_selected_id(Doctor, 'Doctor')
    new_dr_name = input('Please enter their correct name: ')
    selected_dr = session.query(Doctor).get(selected_dr_id)
    if selected_dr:
        selected_dr.name = new_dr_name
        session.commit()
        buffer('Doctor\'s record updated successfully!')

# update Patient
def update_func_3():
    selected_pat_id = validate_selected_id(Patient, 'Patient')
    new_pat_name = input('Please enter their correct name: ')
    new_pat_age = input('Please enter correct age: ')
    selected_pat = session.query(Patient).get(selected_pat_id)
    if selected_pat:
        selected_pat.name = new_pat_name
        selected_pat.age = new_pat_age
        session.commit()
        buffer('Patient\s record updated successfully!')


# update Appointment

def update_func_4():
    buffer('There are quite a bit of appointment records...\n')
    update_func_6()


# search by patient
def update_func_6():
    while True:
        pat_name = input('Please enter patient name. Format: Firstname Lastname: ')
        selected_pat = session.query(Patient).filter_by(name=pat_name).first()
        if selected_pat:
            break
        print('Please enter valid patient name from this list:\n')
        [print(p.name)for p in session.query(Patient).all()]
    matching_appts = session.query(Appointment).filter_by(patient_id=selected_pat.id).all()
    [print(appt) for appt in matching_appts]
    selected_appt_id = input('Please enter the ID of the appointment you whish to update: ')
    selected_appt = session.query(Appointment).filter_by(id=selected_appt_id).first()
    buffer('Here is the appointment you selected to update:')
    buffer(selected_appt)
    choice = 0
    while choice != 4:
        print('Would you like to change your Doctor or reschedule?')
        print('-' * 30)
        print('1) Doctor')
        print('2) Reschedule')
        print('3) Return to previous menu')
        print('4) Quit')
        print()
        print('-' * 30)

        try:
            choice = int(input('Enter choice number: '))
            print()
            if choice == 1:
                while True:
                    try:
                        print('Available doctors on that date')
                        avail_drs = avail_drs_on_date(selected_appt.date_of_appt)
                        [print(dr) for dr in avail_drs]
                        new_dr_id = int(input('Enter doctor\'s ID you would like to see: '))
                        
                        if int(new_dr_id) in [dr.id for dr in avail_drs]:
                            break
                        print('Invalid Dr ID.  Enter ID from available doctors')
                    except ValueError:
                        print('Enter type: Integer')
                selected_appt.doctor_id = int(new_dr_id)
                session.commit()
                buffer('Reschedule Complete')

            elif choice == 2:
                selected_appt.date_of_appt = enter_new_appt()
                session.commit()
                buffer('Reschedule Complete')

            elif choice == 3:
                print('Previous menu...')
                break
            elif choice == 4:
                exit()
            elif not 1 <= choice <= 5:
                print('Please enter valid choice (integers 1 through 5)')
        except ValueError:
            print('Please enter integer type')
