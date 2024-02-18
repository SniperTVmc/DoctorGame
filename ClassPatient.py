from random import choice, randint


defaultNames = ["Léo", "Juliette", "Maël", "Jules", "Victor", "Gaspard", "Mathis", "Martin", "Laurence", "Paul", "Ambre", "Gaston"]
defaultSymptoms = ["Unexplained Pain", "Respiratory Problems", "Digestive Problems", "Bleedings", "Physical Changes"]

class Patient:
    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms

    def getName(self):
        """Return the name of the patient"""
        return self.name

    def getAge(self):
        """Return the age of the patient"""
        return self.age

    def getSymptoms(self):
        """Return the symptoms of the patient"""
        return self.symptoms


def generatePatients(n):
    """Generate a list of n random patient.

    :param int n: number of patients to generate
    return list: return [patients]
    """

    patients = []
    for _ in range(n):
        randomName = choice(defaultNames)
        randomAge = randint(10, 80)
        randomSymptom = choice(defaultSymptoms)
        patients.append(Patient(randomName, randomAge, randomSymptom))
    return patients
