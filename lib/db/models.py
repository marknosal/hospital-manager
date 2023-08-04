from sqlalchemy import  func
from sqlalchemy import Column, Table, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime



convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    appointments = relationship('Appointment', back_populates='doctor', cascade='all, delete-orphan')
    patients = association_proxy('appointments', 'patient', creator=lambda pt: Appointment(patient=pt))

    def __repr__(self):
        return f'Doctor # {self.id} named {self.name}.'

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())

    appointments = relationship('Appointment', back_populates='patient', cascade='all, delete-orphan')
    doctors = association_proxy('appointments', 'doctor', creator=lambda dr: Appointment(doctor=dr))

    def __repr__(self):
        return f'Patient # {self.id} named {self.name} age {self.age}.'

class Appointment(Base):
    __tablename__ = 'appointments'
    

    id = Column(Integer(), primary_key=True)
    created_at = Column(DateTime(), server_default=func.now())
    date_of_appt = Column(DateTime())
    doctor_id = Column(ForeignKey('doctors.id'))
    patient_id = Column(ForeignKey('patients.id'))

    doctor = relationship('Doctor', back_populates='appointments')
    patient = relationship('Patient', back_populates='appointments')

    def __repr__(self):
        return f'Appointment # {self.id} between doctor #{self.doctor.id} ({self.doctor.name}) and patient #{self.patient.id} ({self.patient.name}).  The appointment is at: {self.date_of_appt}'
    
class Dict_Object():
    def __init__(self, name='rando'):
        self.name = name
        self.my_dict = {'my_key': 'my_value'}

    def __repr__(self):
        return f'Dictionary Object named {self.name} that has a key: {list(self.my_dict.keys())[0]} and a value: {self.my_dict["my_key"]}'