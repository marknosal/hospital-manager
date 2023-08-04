from lib.db.database import session, engine
from lib.db.models import metadata, Doctor, Patient, Appointment


def delete_func_1():
    while True:
        print('Please select delete option: ')
        print('----------------------------')
        print('1) Clear table/class')
        print('2) Delete by attribute/column')
        print('3) Quit application')
        print('----------------------------')
        
        print()
        try:
            choice = int(input('Enter your selection: '))
            if choice == 1:
                delete_tables()
                # break
            elif choice == 2:
                delete_attributes()
                # break
            elif choice == 3:
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
                
def delete_attributes():
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

def delete_from_doctors():
    doctors = session.query(Doctor).all()
    [print(dr) for dr in doctors]
    print('----------------------------')

    while True:
        selection = input('Input ID of doctor you wish to remove from database: ')
        try:
            selection = int(selection)
            if selection in [dr.id for dr in doctors]:
                confirm = input('This will clear doctor record and any appointments they have/had. Proceed?  : ')
                if confirm.lower() == 'yes':
                    deleted_doctor = session.query(Doctor).get(selection)
                    session.delete(deleted_doctor)
                    session.commit()
                    print('Doctor and all their associated apppointments have been cleared!')
                else:
                    print('Doctor data clearing...ABORTED')
                break
            else:
                print('Invalid ID entered.  Please enter valid ID from provided list.')
        except ValueError:
            print('Invalid input.  Need valid ID as whole number')



def delete_from_patients():
    patients = session.query(Patient).all()
    [print(pat) for pat in patients]
    print('----------------------------')

    while True:
        selection = input('Input ID of patient you wish to remove from database: ')
        try:
            selection = int(selection)
            if selection in [pat.id for pat in patients]:
                confirm = input('This will clear patient record and any appointments they had/will have. Proceed?  : ')
                if confirm.lower() == 'yes':
                    deleted_patient = session.query(Patient).get(selection)
                    session.delete(deleted_patient)
                    session.commit()
                    print('Patient and all their associated apppointments have been cleared!')
                else:
                    print('Patient data clearing...ABORTED')
                break
            else:
                print('Invalid ID entered.  Please enter valid ID from provided list.')
        except ValueError:
            print('Invalid input.  Need valid ID as whole number')

def delete_from_appointments():
    pass