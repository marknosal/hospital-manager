from lib.db.database import session, engine
from lib.db.models import metadata, Doctor, Patient, Appointment


def delete_func_1():
    while True:
        print('Please select delete option: ')
        print('----------------------------')
        print('1) Clear table/class')
        print('2) Delete by row/instance')
        print('3) Return to previous menu')
        print('4) Quit application')
        print('----------------------------')
        
        print()
        try:
            choice = int(input('Enter your selection: '))
            if choice == 1:
                delete_tables()
                

            elif choice == 2:
                delete_instance()

            elif choice == 3:
                print('Previous Menu')
                break
            elif choice == 4:
                exit()
            else:
                print('Invalid selection, please try again\n')
        except ValueError:
            print('Enter integer type')

def delete_tables():
    while True:
        metadata.reflect(engine)
        table_names = metadata.tables.keys()
        [print(name) for name in table_names]
        print('----------------------------')
        choice = input('Enter name of table you wish to clear or enter "all" to clear all tables: ')
        if choice == 'all':
            confirm = input('Are you sure? This cannot be undone, Yes to confirm: ')
            if confirm.lower() == 'yes':
                for table in metadata.sorted_tables:
                    session.query(table).delete()
                session.commit()
                print('All tables are cleared!!!')
            break
        elif choice in table_names:
            confirm = input('Are you sure? This cannot be undone, Yes to confirm: ')
            if confirm.lower() == 'yes':
                table = metadata.tables[choice]
                session.query(table).delete()
                session.commit()
                print('----------------------------')
                print(f'table "{choice}" has been cleared')
                print('----------------------------')
            break
        else:
            print('Enter valid table name or "all"')
            print('----------------------------')
                
def delete_instance():
    while True:
        metadata.reflect(engine)
        table_names = metadata.tables.keys()
        [print(name) for name in table_names]
        print('----------------------------')
        selection = input('Enter name of table you want to clear from: ')
        print('----------------------------')

        if selection == 'doctors':
            delete_from_doctors()
            break
        elif selection == 'patients':
            delete_from_patients()
            break
        elif selection == 'appointments':
            delete_from_appointments()
            break
        else:
            print('Select from valid table names')
            print('----------------------------') 

def delete_from_doctors():
    doctors = session.query(Doctor).all()
    [print(dr) for dr in doctors]
    print('----------------------------')
    delete_specific_table(Doctor, doctors)



def delete_from_patients():
    patients = session.query(Patient).all()
    [print(pat) for pat in patients]
    print('----------------------------')
    delete_specific_table(Patient, patients)


def delete_from_appointments():
    appointments = session.query(Appointment).all()
    for i, appt in enumerate(appointments, 1):
        print(appt)
        if i % 100 == 0:
            input("Press Enter to continue...")
    print('----------------------------')
    print('Now that you have seen the multitude of appointments')
    delete_specific_table(Appointment, appointments)

def delete_specific_table(model_name, all_rows):

    while True:
        selection = input(f'Input ID of {model_name.__name__} you wish to delete: ')
        try:
            selection = int(selection)
            if selection in [row.id for row in all_rows]:
                confirm = input(f'This will clear {model_name.__name__} record. Proceed?  : ')
                if confirm.lower() == 'yes':
                    deleted_row = session.query(model_name).get(selection)
                    session.delete(deleted_row)
                    session.commit()
                    print(f'{model_name.__name__} cleared!')
                else:
                    print('----------------------------')
                    print('----------------------------')
                    print(f'{model_name.__name__} data clearing...ABORTED')
                    print('----------------------------')
                    print('----------------------------')
                break
            else:
                print('Invalid ID entered.  Please enter valid ID from provided list.')
        except ValueError:
            print('Invalid input.  Need valid ID as whole number')