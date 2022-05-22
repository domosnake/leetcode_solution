# Design a service class used by Emergency department of a hospital,
# which will be used to triage patients.
#
# Your task is to design and implement below class and methods.
# You may create additional helper methods or classes as you see fit.
# You have max freedom to use any data type or structure, error handling, code logic as long as it serves the purpose and you can explain the reasoning.
#
# When you design the system, consider Extensibility and Scalability.
from heapq import heappush, heappop, heapify
from datetime import datetime as dt
from re import A
from sys import ps1
from typing import List


class Patient:
    def __init__(self, patient_id: int, severity: int):
        self.patient_id = patient_id
        self.severity = severity


class Severity:
    def __init__(self, severity: int, code: str):
        self.severity = severity
        self.code = code


class ER:
    # Constructor. Parameters:
    # severities - the severity each patient will be assigned to
    # capacity - the max number of patients the ER can serve at any given time
    def __init__(self, capacity: int, severities: List[Severity]):
        if capacity <= 0:
            raise ValueError('Capacity must be positive')
        if len(severities) == 0:
            raise ValueError('At least one severity must be specified')
        self.max_heap = []
        self.codeBlue = []
        self.capacity = capacity
        self.triage_codes = {}
        for s in severities:
            if s.severity in self.triage_codes:
                raise KeyError('Severity must be unique')
            self.triage_codes[s.severity] = s.code

    # Method. Admit and triage a patient into the waiting line based on their severity
    # If capacity is reached, no new patient can be admitted
    # Parameters:
    # patient - data type can be defined by you
    def admit(self, patient: Patient) -> bool:
        if len(self.max_heap) >= self.capacity:
            # failed to admin patient due to capacity reached
            return False
        if patient.severity not in self.triage_codes:
            raise ValueError('Invalid severity')
        # sorting by severity, then by admin datetime
        heappush(self.max_heap, (-patient.severity, dt.now(), patient))
        return True

    # Method. Treat and discharge(remove) the next patient from the waiting line.
    # Calling of the method should automatically find the patient with the highest severity,
    # if there are patients with the same severity, it's on a first-come, first-served basis.
    # If there are patient(s) in Code Blue, all patients in Code Blue
    # should be treated firstly and removed from the waiting line.
    def treat(self) -> List[Patient]:
        if self.codeBlue:
            temp = self.codeBlue[::]
            self.codeBlue.clear()
            return temp
        severity, admin_dt, patient = heappop(self.max_heap)
        severity *= -1
        return patient

    # Method. When a patient is in cardiac or respiratory arrest,
    # a Code Blue is called to assign a special severity to the patient.
    # Parameters:
    # patient - data type can be defined by you
    def codeBlue(self, patient: Patient):
        found = False
        for p in self.max_heap:
            if p.id == patient.id:
                found = True
                break
        if found:
            self.blueCode.append(p)
            self.max_heap.remove(patient)
            heapify(self.max_heap)
        else:
            raise ValueError('Patient not found')


# Example:
er = ER(10, [
    Severity(1, 'White'),
    Severity(2, 'Green'),
    Severity(3, 'Yellow'),
    Severity(4, 'Orange'),
    Severity(5, 'Red')
])  # cap is 3, severity ranges from 1 to 5
p1 = Patient(1, 1)
p2 = Patient(2, 5)
p3 = Patient(3, 4)
p4 = Patient(4, 4)
p5 = Patient(5, 3)

er.admit(p1)  # admit patient 1 with severity 1
er.admit(p2)  # admit patient 2 with severity 5
er.admit(p3)  # admit patient 3 with severity 4
er.admit(p4)  # admit patient 4 with severity 4
# the line should be [1, 1], [3, 4], [2, 5], where [4, 4] can not be admitted due to capacity
er.treat()  # treat and discharge [2, 5]
er.treat()  # treat and discharge [3, 4]
er.admit(p4)  # admit patient 4 with severity 4
er.admit(p5)  # admit patient 5 with severity 3
# the line should be [1, 1], [5, 3], [4, 4]
er.codeBlue(p1)  # code blue called on [1, 1]
er.codeBlue(p5)  # code blue called on [5, 3]
er.treat()  # treat all patients in code blue, the line should be [4, 4]
