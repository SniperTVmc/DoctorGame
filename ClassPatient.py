from random import choice, randint


defaultNames = ["Léo", "Juliette", "Maël", "Jules", "Victor", "Gaspard", "Mathis", "Martin", "Laurence", "Paul", "Ambre", "Gaston"]
defaultSymptoms = ["Unexplained Pain", "Respiratory Problems", "Digestive Problems", "Bleedings", "Physical Changes", "Exam stress", "Evening tiredness"]


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

    usedNames = []
    usedSymptoms = []
    patients = []
    for _ in range(n):

        randomName = choice(defaultNames)
        while usedNamesIsFull(usedNames) or randomName in usedNames:
            randomName = choice(defaultNames)
            if usedNamesIsFull(usedNames):
                usedNames.clear()
        usedNames.append(randomName)

        randomSymptom = choice(defaultSymptoms)
        while usedSymptomsIsFull(usedSymptoms) or randomSymptom in usedSymptoms:
            randomSymptom = choice(defaultSymptoms)
            if usedSymptomsIsFull(usedSymptoms):
                usedSymptoms.clear()
        usedSymptoms.append(randomSymptom)

        randomAge = randint(10, 80)
        patients.append(Patient(randomName, randomAge, randomSymptom))

    for patient in patients:
        print(patient.getSymptoms())

    return patients


def usedNamesIsFull(usedNames):
    for name in defaultNames:
        if name not in usedNames:
            return False
    return True


def usedSymptomsIsFull(usedSymptoms):
    for name in defaultSymptoms:
        if name not in usedSymptoms:
            return False
    return True
