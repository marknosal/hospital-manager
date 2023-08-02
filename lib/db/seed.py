from faker import Faker
import random
from datetime import datetime, timedelta

from database import session

from models import Doctor, Patient, Appointment



def save_batch(objects):
    session.add_all(objects)
    session.commit()

def random_appointment():
    current_time = datetime.now()
    random_days = random.randint(-210, 60)
    appointment_date = current_time + timedelta(days=random_days)
    appointment_hour = random.randint(9, 17)
    appointment_minute = random.randint(0,3) * 15
    appointment_time = appointment_date.replace(hour=appointment_hour, minute=appointment_minute, second=0, microsecond=0)
    return appointment_time

def create_doctors(count):
    fake = Faker()
    doctors = []
    for i in range(count):
        doctor = Doctor(
            name = fake.unique.name()
        )
        doctors.append(doctor)
    return doctors

def create_patients(count):
    fake = Faker()
    patients = []
    for i in range(count):
        patient = Patient(
            name = fake.unique.name(),
            age = fake.random_int(min=5, max=80)
        )
        patients.append(patient)
    return patients

def create_appointments(count, doctors, patients):
    appointments = []
    for i in range(count):
        appointment = Appointment(
            date_of_appt = random_appointment(),
            doctor = random.choice(doctors),
            patient = random.choice(patients),
        )
        appointments.append(appointment)
    return appointments



if __name__ == '__main__':

    session.query(Doctor).delete()
    session.query(Patient).delete()
    session.query(Appointment).delete()

    doctors = create_doctors(1)
    patients = create_patients(50)
    appointments = create_appointments(1500, doctors, patients)

    save_batch(doctors)
    save_batch(patients)
    save_batch(appointments)
    