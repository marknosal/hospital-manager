from faker import Faker
import random
from datetime import datetime, timedelta

from database import session

from models import Doctor, Patient, Appointment



if __name__ == '__main__':
    # engine = create_engine('sqlite:///phase3_database.db')
    # Session = sessionmaker(bind = engine)
    # session = Session()

    fake = Faker()

    session.query(Doctor).delete()
    session.query(Patient).delete()
    session.query(Appointment).delete()

    doctors = []
    for i in range(20):
        doctor = Doctor(
            name = fake.unique.name()
        )

        session.add(doctor)
        session.commit()
        doctors.append(doctor)

    patients = []
    for i in range(500):
        patient = Patient(
            name = fake.unique.name(),
            age = fake.random_int(min=5, max=80)
        )
        session.add(patient)
        session.commit()
        patients.append(patient)


    def random_appointment():
        current_time = datetime.now()
        random_days = random.randint(-210, 60)
        appointment_date = current_time + timedelta(days=random_days)
        appointment_hour = random.randint(9, 17)
        appointment_minute = random.randint(0,3) * 15
        appointment_time = appointment_date.replace(hour=appointment_hour, minute=appointment_minute, second=0, microsecond=0)

        # Keep the data type as a datetime object without seconds and microseconds
        return appointment_time
    
    appointments = []
    for i in range(1500):
        appointment = Appointment(
            date_of_appt = random_appointment(),
            doctor_id = random.choice(doctors).id,
            patient_id = random.choice(patients).id,
        )
        session.add(appointment)
        session.commit()
        appointments.append(appointment)
