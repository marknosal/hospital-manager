from db.database import session
from db.models import Doctor, Patient, Appointment

def main():
    print('testing!')
    id = session.query(Doctor).filter_by(id=1).first()
    print(id)
    

if __name__ == '__main__':
    main()