from sqlalchemy import create_engine, func
from sqlalchemy import Column, Table, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


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
        return f'A doctor named {self.name}.'

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())

    appointments = relationship('Appointment', back_populates='patient', cascade='all, delete-orphan')
    doctors = association_proxy('appointments', 'doctor', creator=lambda dr: Appointment(doctor=dr))

    def __repr__(self):
        return f'A patient named {self.name}.'

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
        return f'An appointment between doctor: {self.doctor} and patient: {self.patient}.  The appointment is at: {self.date_of_appt}'
