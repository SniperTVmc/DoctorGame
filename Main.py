import tkinter as tk
from random import random
from tkinter import ttk
from PIL import Image, ImageTk
from ClassPatient import *

patients = []
patientsCount = 5
currentPatient = 0
healPatient = 0
mainWindow = tk.Tk()

image_main = None
image_patient = None
image_asking = None
image_success = None
image_wrong = None
image_end = None
image_temu = None
image_infected = None
image_virus_clean = None
image_tumor = None
image_blood = None
image_lungs = None
image_bone = None
image_sleep = None
image_stress = None
image_dead = None


def resetMainWindow():
    for widget in mainWindow.winfo_children():
        widget.destroy()


def main():
    resetMainWindow()
    getMainUI(mainWindow)
    mainWindow.mainloop()


def compteurPatients():
    patient_counter_frame = ttk.Frame(mainWindow, relief="raised", borderwidth=2)
    patient_counter_frame.pack(side=tk.BOTTOM, padx=10, pady=10, anchor="sw")

    patient_counter_label = ttk.Label(patient_counter_frame, text=f"Patient Actuel : {currentPatient + 1}  / {patientsCount}",
                                      font=("Arial", 12))
    patient_counter_label.pack(padx=10, pady=5)


def endGame():
    resetMainWindow()

    image_pil = Image.open("data/end.png")
    global image_end
    image_end = ImageTk.PhotoImage(image_pil)

    imageFrame = tk.Frame(mainWindow)
    imageFrame.pack(pady=20)

    imageLabel = tk.Label(imageFrame, image=image_end)
    imageLabel.pack()

    labelAskBiopsy = tk.Label(mainWindow, text="Thanks for playing !", font=("Arial", 18))
    labelAskBiopsy.pack()

    labelAskBiopsy = tk.Label(mainWindow, text="You can now go back to the main menu to play again!", font=("Arial", 17))
    labelAskBiopsy.pack()

    labelAskBiopsy = tk.Label(mainWindow, text="TIP: You can change the amount of patient(s) to heal in the settings ;)", font=("Arial", 17))
    labelAskBiopsy.pack()

    buttonFrame = ttk.Frame(mainWindow)
    buttonFrame.pack(pady=20)

    buttonYes = ttk.Button(buttonFrame, text="Go back main menu", command=main, style='Green.TButton')
    buttonYes.grid(row=0, column=0, padx=20)

    labelAskBiopsy = tk.Label(mainWindow, text="Statistics:", font=("Arial", 16))
    labelAskBiopsy.pack()

    labelAskBiopsy = tk.Label(mainWindow, text=f"You treated {healPatient} out of {patientsCount}!", font=("Arial", 12))
    labelAskBiopsy.pack()

    if healPatient == patientsCount:
        labelAskBiopsy = tk.Label(mainWindow, text="Unbelievable! You're a perfect doctor and you've treated everyone! Congratulations!!!",
                                  font=("Arial", 12))
        labelAskBiopsy.pack()

    elif healPatient == (patientsCount / 2):
        labelAskBiopsy = tk.Label(mainWindow, text="Well... You're average, as we like to say in high school, aren't you?",
                                  font=("Arial", 12))
        labelAskBiopsy.pack()

    elif healPatient == 0:
        labelAskBiopsy = tk.Label(mainWindow, text="Oh, my God, you... You're a horrible doctor! Not even a patient to save, frankly. !",
                                  font=("Arial", 12))
        labelAskBiopsy.pack()


def nextPatient():
    global currentPatient
    currentPatient += 1
    if currentPatient < len(patients):
        doAppointment(patients[currentPatient])

    else:
        endGame()


def showBiopsyTreatmentResults(result):
    resetMainWindow()

    if result == "wrong":

        image_pil = Image.open("data/wrong.png")
        global image_wrong
        image_wrong = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_wrong)
        imageLabel.pack()

        labelAskBiopsy = tk.Label(mainWindow, text="You made the wrong choice! Your patient now have horribly pains and will die! Congratulations!", font=("Arial", 18))
        labelAskBiopsy.pack()

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

    else:

        image_pil = Image.open("data/success.png")
        global image_success
        image_success = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_success)
        imageLabel.pack()

        labelAskBiopsy = tk.Label(mainWindow, text="Congratulations! You've healed your patient, that's a fine job!.", font=("Arial", 18))
        labelAskBiopsy.pack()

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

        global healPatient
        healPatient += 1

    compteurPatients()


def startGame():

    global currentPatient
    currentPatient = 0
    global healPatient
    healPatient = 0

    global patients
    patients = []
    patients = generatePatients(patientsCount)
    print("Starting of the game...")
    doAppointment(patients[currentPatient])


def getCancerType(symptoms):
    if symptoms == "Unexplained Pain":
        return "Cancer of bone (sarcoma)"
    elif symptoms == "Respiratory Problems":
        return "Cancer of lungs"
    elif symptoms == "Digestive Problems":
        return "Cancer of lungs"
    elif symptoms == "Bleedings":
        return "Cancer of blood (Leukemia)"
    elif symptoms == "Physical Changes":
        return "Cancer of the immune system (Lymphoma)"
    else:
        return None


def doBiopsy(patient):
    resetMainWindow()
    random_number = random()
    print(random_number)
    if random_number <= 0.10:

        image_pil = Image.open("data/virus-clean.png")
        global image_virus_clean
        image_virus_clean = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_virus_clean)
        imageLabel.pack()

        labelAskBiopsy = tk.Label(mainWindow, text="Phew! All's well in the end, nothing serious, your patient is in good health.", font=("Arial", 18))
        labelAskBiopsy.pack()

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

        global healPatient
        healPatient += 1

    elif random_number <= 0.30:

        image_pil = Image.open("data/tumor.png")
        global image_tumor
        image_tumor = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_tumor)
        imageLabel.pack()

        labelAskBiopsy = tk.Label(mainWindow, text="Oh, dear... Your patient has a benign tumor. What do you want to do?", font=("Arial", 18))
        labelAskBiopsy.pack()

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonSurgery = ttk.Button(buttonFrame, text="A surgery.", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
        buttonSurgery.grid(row=0, column=0, padx=20)

        buttonAmputation = ttk.Button(buttonFrame, text="QUICK! An amputation now and quickly !", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
        buttonAmputation.grid(row=0, column=1, padx=20)

        buttonNoting = ttk.Button(buttonFrame, text="Nothing", command=lambda: showBiopsyTreatmentResults("correct"), style='Green.TButton')
        buttonNoting.grid(row=0, column=2, padx=20)


    else:

        label = tk.Label(mainWindow, text="Unfortunately, you have had a malignant tumor and it has developed...", font=("Arial", 16))
        label.pack()

        cancerType = getCancerType(patient.getSymptoms())
        label = tk.Label(mainWindow, text=f"And now you have {cancerType}...", font=("Arial", 16))
        label.pack()

        label = tk.Label(mainWindow, text="What do you want to do now?", font=("Arial", 18))
        label.pack()

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        if cancerType == "Cancer of bone (sarcoma)":

            image_pil = Image.open("data/bone.png")
            global image_bone
            image_bone = ImageTk.PhotoImage(image_pil)

            imageFrame = tk.Frame(mainWindow)
            imageFrame.pack(pady=20)

            imageLabel = tk.Label(imageFrame, image=image_bone)
            imageLabel.pack()

            buttonSurgery = ttk.Button(buttonFrame, text="Surgery", command=lambda: showBiopsyTreatmentResults("correct"), style='Green.TButton')
            buttonSurgery.grid(row=0, column=0, padx=20)

            buttonRadiation = ttk.Button(buttonFrame, text="Radiation", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonRadiation.grid(row=0, column=1, padx=20)

            buttonAmputation = ttk.Button(buttonFrame, text="Amputation", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonAmputation.grid(row=0, column=2, padx=20)

            buttonNothing = ttk.Button(buttonFrame, text="Nothing", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonNothing.grid(row=0, column=3, padx=20)

        elif cancerType == "Cancer of blood (Leukemia)":

            image_pil = Image.open("data/blood.png")
            global image_blood
            image_blood = ImageTk.PhotoImage(image_pil)

            imageFrame = tk.Frame(mainWindow)
            imageFrame.pack(pady=20)

            imageLabel = tk.Label(imageFrame, image=image_blood)
            imageLabel.pack()

            buttonSurgery = ttk.Button(buttonFrame, text="Surgery", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonSurgery.grid(row=0, column=0, padx=20)

            buttonChemotherapy = ttk.Button(buttonFrame, text="Chemotherapy", command=lambda: showBiopsyTreatmentResults("correct"), style='Green.TButton')
            buttonChemotherapy.grid(row=0, column=1, padx=20)

            buttonDrink = ttk.Button(buttonFrame, text="Drink alcohol and live happy, the life is good", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonDrink.grid(row=0, column=2, padx=20)

            buttonRadiation = ttk.Button(buttonFrame, text="Radiation", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonRadiation.grid(row=0, column=3, padx=20)

            buttonNothing = ttk.Button(buttonFrame, text="Nothing", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonNothing.grid(row=0, column=4, padx=20)

        elif cancerType == "Cancer of the immune system (Lymphoma)":

            buttonFrame2 = ttk.Frame(mainWindow)
            buttonFrame2.pack(pady=20)

            buttonAmputation = ttk.Button(buttonFrame2, text="Buy a new imune system on Temu FOR ONLY 2$ but with NINETYFIVECODE you have 95% discount for your first purchase (so just for 0.10$)", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonAmputation.grid(row=0, column=0, padx=20)

            buttonSurgery = ttk.Button(buttonFrame, text="Surgery", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonSurgery.grid(row=0, column=1, padx=20)

            buttonNothing = ttk.Button(buttonFrame, text="Nothing", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonNothing.grid(row=0, column=2, padx=20)

            buttonChemotherapy = ttk.Button(buttonFrame, text="Chemotherapy", command=lambda: showBiopsyTreatmentResults("correct"), style='Green.TButton')
            buttonChemotherapy.grid(row=0, column=3, padx=20)

            image_pil = Image.open("data/fake_temu.png")
            global image_temu
            image_temu = ImageTk.PhotoImage(image_pil)

            imageFrame = tk.Frame(mainWindow)
            imageFrame.pack(pady=20)

            imageLabel = tk.Label(imageFrame, image=image_temu)
            imageLabel.pack()

        elif cancerType == "Cancer of lungs":

            image_pil = Image.open("data/lungs.png")
            global image_lungs
            image_lungs = ImageTk.PhotoImage(image_pil)

            imageFrame = tk.Frame(mainWindow)
            imageFrame.pack(pady=20)

            imageLabel = tk.Label(imageFrame, image=image_lungs)
            imageLabel.pack()

            buttonRemove = ttk.Button(buttonFrame, text="Remove the lungs", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonRemove.grid(row=0, column=0, padx=20)

            buttonRadiation = ttk.Button(buttonFrame, text="Radiation", command=lambda: showBiopsyTreatmentResults("correct"), style='Green.TButton')
            buttonRadiation.grid(row=0, column=1, padx=20)

            buttonMask = ttk.Button(buttonFrame, text="Wear a mask", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonMask.grid(row=0, column=2, padx=20)

            buttonNothing = ttk.Button(buttonFrame, text="Nothing", command=lambda: showBiopsyTreatmentResults("wrong"), style='Green.TButton')
            buttonNothing.grid(row=0, column=3, padx=20)

    compteurPatients()


def noBiopsy():
    resetMainWindow()

    image_pil = Image.open("data/dead.png")
    global image_dead
    image_dead = ImageTk.PhotoImage(image_pil)

    imageFrame = tk.Frame(mainWindow)
    imageFrame.pack(pady=20)

    imageLabel = tk.Label(imageFrame, image=image_dead)
    imageLabel.pack()

    labelAskBiopsy = tk.Label(mainWindow, text="Stupid choice! Your patient died of cancer.", font=("Arial", 18))
    labelAskBiopsy.pack()

    labelAskBiopsy = tk.Label(mainWindow, text="If the analyses show signals of cancer, it's not for nothing!", font=("Arial", 18))
    labelAskBiopsy.pack()

    buttonFrame = ttk.Frame(mainWindow)
    buttonFrame.pack(pady=20)

    buttonYes = ttk.Button(buttonFrame, text="Next patient", command=nextPatient, style='Green.TButton')
    buttonYes.grid(row=0, column=0, padx=20)

    compteurPatients()


def askBiopsy(patient):
    resetMainWindow()

    image_pil = Image.open("data/asking.png")
    global image_asking
    image_asking = ImageTk.PhotoImage(image_pil)

    imageFrame = tk.Frame(mainWindow)
    imageFrame.pack(pady=20)

    imageLabel = tk.Label(imageFrame, image=image_asking)
    imageLabel.pack()

    labelAskBiopsy = tk.Label(mainWindow, text="Do you want to do a biopsy? ?", font=("Arial", 18))
    labelAskBiopsy.pack()

    buttonFrame = ttk.Frame(mainWindow)
    buttonFrame.pack(pady=20)

    buttonYes = ttk.Button(buttonFrame, text="Oui", command=lambda: doBiopsy(patient), style='Green.TButton')
    buttonYes.grid(row=0, column=0, padx=20)

    buttonNo = ttk.Button(buttonFrame, text="Non", command=noBiopsy, style='Red.TButton')
    buttonNo.grid(row=0, column=1, padx=20)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Green.TButton', foreground='green', background='#C9E6C9', font=("Helvetica", 14))
    style.configure('Red.TButton', foreground='red', background='#FFCCCC', font=("Helvetica", 14))

    compteurPatients()


def noAnalysis(patient):
    resetMainWindow()

    random_number = random()
    global healPatient
    global image_virus_clean

    if patient.getSymptoms() in ["Exam stress", "Evening tiredness"]:

        image_pil = Image.open("data/virus-clean.png")
        image_virus_clean = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_virus_clean)
        imageLabel.pack()

        label = ttk.Label(mainWindow,
                          text="Good thinking! It wasn't as bad as all that, and everything's fine!",
                          font=("Arial", 12))
        label.pack(pady=20)

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next Patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

        healPatient += 1

    elif random_number <= 0.20:

        image_pil = Image.open("data/virus-clean.png")
        image_virus_clean = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_virus_clean)
        imageLabel.pack()

        label = ttk.Label(mainWindow,
                          text="Perfect! Everything's fine, you've prescribed him some medicine and he will feel better in a few days.",
                          font=("Arial", 12))
        label.pack(pady=20)

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next Patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

        healPatient += 1

    else:

        image_pil = Image.open("data/dead.png")
        global image_dead
        image_dead = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_dead)
        imageLabel.pack()

        label = ttk.Label(mainWindow,
                          text="Oh no, you should have done more analysis, your patient has an infection, he's going to die...",
                          font=("Arial", 12))
        label.pack(pady=20)

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next Patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

    compteurPatients()


def moreAnalysis(patient):
    resetMainWindow()

    random_number = random()

    if patient.getSymptoms() in ["Exam stress", "Evening tiredness"]:

        if patient.getSymptoms() == "Exam stress":

            image_pil = Image.open("data/stress.png")
            global image_stress
            image_stress = ImageTk.PhotoImage(image_pil)

            imageFrame = tk.Frame(mainWindow)
            imageFrame.pack(pady=20)

            imageLabel = tk.Label(imageFrame, image=image_stress)
            imageLabel.pack()

            label = ttk.Label(mainWindow,
                              text="According to your analysis, your patient was only stressing about an exam. He lost $26 because of you!",
                              font=("Arial", 12))
            label.pack(pady=20)

        else:

            image_pil = Image.open("data/sleep.png")
            global image_sleep
            image_sleep = ImageTk.PhotoImage(image_pil)

            imageFrame = tk.Frame(mainWindow)
            imageFrame.pack(pady=20)

            imageLabel = tk.Label(imageFrame, image=image_sleep)
            imageLabel.pack()

            label = ttk.Label(mainWindow,
                              text="According to your analysis, your patient is simply tired at night! Just like any other human being on earth!",
                              font=("Arial", 12))
            label.pack(pady=20)

            label = ttk.Label(mainWindow,
                              text="Are you sure you're sleeping though? (If not, that's no good, you need sleep to stay healthy :p )",
                              font=("Arial", 12))
            label.pack(pady=20)


        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next Patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

    elif random_number <= 0.20:

        image_pil = Image.open("data/virus-clean.png")
        global image_virus_clean
        image_virus_clean = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_virus_clean)
        imageLabel.pack()

        label = ttk.Label(mainWindow,
                          text="According to your analysis, this is not a problem and your patient can go home.",
                          font=("Arial", 12))
        label.pack(pady=20)

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Next Patient", command=nextPatient, style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

        global healPatient
        healPatient += 1

    else:

        image_pil = Image.open("data/infected.png")
        global image_infected
        image_infected = ImageTk.PhotoImage(image_pil)

        imageFrame = tk.Frame(mainWindow)
        imageFrame.pack(pady=20)

        imageLabel = tk.Label(imageFrame, image=image_infected)
        imageLabel.pack()

        label = ttk.Label(mainWindow, text="Ouch! Your patient probably has cancer...", font=("Arial", 12))
        label.pack(pady=20)

        buttonFrame = ttk.Frame(mainWindow)
        buttonFrame.pack(pady=20)

        buttonYes = ttk.Button(buttonFrame, text="Continue", command=lambda: askBiopsy(patient), style='Green.TButton')
        buttonYes.grid(row=0, column=0, padx=20)

    compteurPatients()


def doAppointment(patient):
    resetMainWindow()

    image_pil = Image.open("data/patient.png")
    global image_patient
    image_patient = ImageTk.PhotoImage(image_pil)

    imageFrame = tk.Frame(mainWindow)
    imageFrame.pack(pady=20)

    imageLabel = tk.Label(imageFrame, image=image_patient)
    imageLabel.pack()

    labelSymptoms = tk.Label(mainWindow, text=f"Patient's name: {patient.getName()}", font=("Arial", 16))
    labelSymptoms.pack(pady=10)

    labelSymptoms = tk.Label(mainWindow, text=f"Patient's age: {patient.getAge()}", font=("Arial", 16))
    labelSymptoms.pack(pady=10)

    labelSymptoms = tk.Label(mainWindow, text=f"Patient's symptoms: {patient.getSymptoms()}", font=("Arial", 16))
    labelSymptoms.pack(pady=10)

    labelAskBiopsy = tk.Label(mainWindow, text="Would you like to do more analysis?", font=("Arial", 18))
    labelAskBiopsy.pack()

    buttonFrame = ttk.Frame(mainWindow)
    buttonFrame.pack(pady=20)

    buttonYes = ttk.Button(buttonFrame, text="Yes", command=lambda: moreAnalysis(patient), style='Green.TButton')
    buttonYes.grid(row=0, column=0, padx=20)

    buttonNo = ttk.Button(buttonFrame, text="No", command=lambda: noAnalysis(patient), style='Red.TButton')
    buttonNo.grid(row=0, column=1, padx=20)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Green.TButton', foreground='green', background='#C9E6C9', font=("Helvetica", 14))
    style.configure('Red.TButton', foreground='red', background='#FFCCCC', font=("Helvetica", 14))

    compteurPatients()


def play(window):
    resetMainWindow()

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    label = tk.Label(frame, text="Welcome on Don't Kill Your Patient !", font=("Arial", 20))
    label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    label.pack()

    frame = ttk.Frame(window)
    frame.pack(pady=20, padx=20, fill="x")

    label_title = ttk.Label(frame, text="Game rules:", font=("Arial", 26, "bold"), justify="center")
    label_title.pack(anchor="center", padx=2)

    label_text = ttk.Label(frame,
                           text="» In this game, you play a doctor who must heal patients. Be careful to perform the right operations, so as not to make your patient even sicker, or even kill him/her.",
                           wraplength=380, font=("Arial", 16), justify="center")
    label_text.pack(anchor="center", padx=15, pady=15)

    label_text = ttk.Label(frame,
                           text="» All patients are not necessarily infected, so you have to find out if they are or not before you try to heal them.",
                           wraplength=380, font=("Arial", 16), justify="center")
    label_text.pack(anchor="center", padx=15, pady=15)

    label_text = ttk.Label(frame,
                           text="» Be careful! If you make a mistake, the patient will regret it forever... :D",
                           wraplength=380, font=("Arial", 16), justify="center")
    label_text.pack(anchor="center", padx=15, pady=15)

    separator = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN)
    separator.pack(fill=tk.X, padx=5, pady=5)

    buttonFrame = ttk.Frame(mainWindow)
    buttonFrame.pack(pady=20)

    buttonStartGame = ttk.Button(buttonFrame, text="Start the game", command=startGame, style='BoutonVert.TButton')
    buttonStartGame.grid(row=0, column=0, padx=20)

    buttonReturn = ttk.Button(buttonFrame, text="Back", command=main, style='Bouton.TButton')
    buttonReturn.grid(row=0, column=1, padx=20)


def setPatientsCount(value, window):
    global patientsCount
    patientsCount = value
    global bouton_valider
    bouton_valider.config(text="You have changed this setting.", style="BoutonVert.TButton")
    window.after(1000, lambda: bouton_valider.config(text="Valider", style="Bouton.TButton"))


def leaveButton():
    mainWindow.quit()


def getMainUI(window):
    window.title("Don't Kill Your Patient - HOME")
    window.iconbitmap("data/doctor.ico")

    window.geometry("1280x720")
    window.resizable(width=False, height=False)

    image_pil = Image.open("data/mainBackground.png")
    global image_main
    image_main = ImageTk.PhotoImage(image_pil)

    canvas = tk.Canvas(window, bg="light grey", width=1280, height=720)
    canvas.pack()

    canvas.create_image(0, 0, anchor="nw", image=image_main)

    # Titre
    titre_label = tk.Label(window, text="Welcome on Don't Kill Your Patient !", font=("Helvetica", 24))
    titre_label.place(relx=0.75, rely=0.1, anchor="center")

    bouton_jouer = tk.Button(window, text="Play", command=lambda: play(window), font=("Helvetica", 20), padx=20,
                             pady=10,
                             borderwidth=0, highlightthickness=2, highlightbackground="green", background="#17ba17",
                             activebackground="green", relief="raised")
    bouton_jouer.place(relx=0.75, rely=0.3, anchor="center")

    bouton_options = tk.Button(window, text="Settings", command=openSettingsUI, font=("Helvetica", 20), padx=20,
                               pady=10,
                               borderwidth=0, highlightthickness=2, highlightbackground="orange", background="#FFD700",
                               activebackground="orange", relief="raised")
    bouton_options.place(relx=0.75, rely=0.3 + (bouton_jouer.winfo_reqheight() + 50) / 720,
                         anchor="center")

    bouton_quitter = tk.Button(window, text="Leave", command=leaveButton, font=("Helvetica", 20), padx=20,
                               pady=10, borderwidth=0, highlightthickness=2, highlightbackground="red",
                               background="#F08080", activebackground="red", relief="raised")
    bouton_quitter.place(relx=0.75, rely=0.3 + (bouton_jouer.winfo_reqheight() + 50) * 2 / 720,
                         anchor="center")

    bouton_credits = tk.Button(window, text="Credits", command=openCredits, font=("Helvetica", 20), padx=20,
                               pady=10,
                               borderwidth=0, highlightthickness=2, highlightbackground="blue", background="#1ea4d1",
                               activebackground="blue", relief="raised")
    bouton_credits.place(relx=0.75, rely=0.3 + (bouton_jouer.winfo_reqheight() + 50) * 3 / 720,
                         anchor="center")
    return window


def openSettingsUI():
    options_mainWindow = tk.Toplevel()
    options_mainWindow.title("Options")
    options_mainWindow.geometry("500x300")
    options_mainWindow.resizable(False, False)

    screen_width = options_mainWindow.winfo_screenwidth()
    screen_height = options_mainWindow.winfo_screenheight()
    window_width = 500
    window_height = 300
    x_coordinate = int((screen_width - window_width) / 2)
    y_coordinate = int((screen_height - window_height) / 2)
    options_mainWindow.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    valeur_curseur = tk.IntVar()
    valeur_curseur.set(patientsCount)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Bouton.TButton", font=("Helvetica", 12))
    style.configure("BoutonVert.TButton", font=("Helvetica", 12), background="green")
    style.map("BoutonVert.TButton", background=[("active", "green")])

    cadre = ttk.Frame(options_mainWindow)
    cadre.pack(expand=True, padx=20, pady=20)

    label_titre = ttk.Label(cadre, text="Settings", font=("Helvetica", 16))
    label_titre.grid(row=0, column=0, columnspan=2, pady=10)

    label_patient = ttk.Label(cadre, text="Number of patients:", font=("Helvetica", 12))
    label_patient.grid(row=1, column=0, pady=5, sticky="w")

    scale_patient = ttk.Scale(cadre, from_=1, to=10, orient="horizontal", length=200, variable=valeur_curseur,
                              command=lambda value: valeur_curseur.set(int(float(value))))
    scale_patient.grid(row=1, column=1, pady=5, sticky="w")

    label_valeur = ttk.Label(cadre, textvariable=valeur_curseur, font=("Helvetica", 12))
    label_valeur.grid(row=2, column=1, pady=5, sticky="w")

    global bouton_valider
    bouton_valider = ttk.Button(cadre, text="Confirm",
                                command=lambda: setPatientsCount(valeur_curseur.get(), mainWindow),
                                style="Bouton.TButton")
    bouton_valider.grid(row=3, column=0, columnspan=2, pady=10)

    def retour():
        options_mainWindow.destroy()

    bouton_retour = ttk.Button(cadre, text="Back", command=retour, style="BoutonRouge.TButton")
    bouton_retour.grid(row=4, column=0, columnspan=2, pady=10)
    style.configure("BoutonRouge.TButton", font=("Helvetica", 12), background="red", foreground="dark red")
    style.map("BoutonRouge.TButton", background=[("active", "red")])

    options_mainWindow.update_idletasks()
    options_mainWindow.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


def openCredits():
    options_mainWindow = tk.Toplevel()
    options_mainWindow.title("Credits")
    options_mainWindow.geometry("500x300")
    options_mainWindow.resizable(False, False)

    screen_width = options_mainWindow.winfo_screenwidth()
    screen_height = options_mainWindow.winfo_screenheight()
    window_width = 500
    window_height = 300
    x_coordinate = int((screen_width - window_width) / 2)
    y_coordinate = int((screen_height - window_height) / 2)
    options_mainWindow.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    cadre = ttk.Frame(options_mainWindow)
    cadre.pack(expand=True, padx=20, pady=20)

    label_titre = ttk.Label(cadre, text="Credits", font=("Helvetica", 16, "bold"))
    label_titre.grid(row=0, column=0, columnspan=2, pady=10)

    label_creators = ttk.Label(cadre, text="Original idea:", font=("Arial", 12, "underline"))
    label_creators.grid(row=1, column=0, sticky="w", pady=5)

    label_creators_names = ttk.Label(cadre, text="REMIOM Ambre & KRABANSKY Gaston", font=("Arial", 12))
    label_creators_names.grid(row=1, column=1, sticky="w", pady=5)

    label_developed_by = ttk.Label(cadre, text="Developed by:", font=("Arial", 12, "underline"))
    label_developed_by.grid(row=2, column=0, sticky="w", pady=5)

    label_developer_name = ttk.Label(cadre, text="Your Name or Team Name", font=("Arial", 12))
    label_developer_name.grid(row=2, column=1, sticky="w", pady=5)

    def retour():
        options_mainWindow.destroy()

    bouton_retour = ttk.Button(cadre, text="Back", command=retour, style="BoutonRouge.TButton")
    bouton_retour.grid(row=3, column=0, columnspan=2, pady=10)
    style = ttk.Style()
    style.configure("BoutonRouge.TButton", font=("Helvetica", 12), background="red", foreground="dark red")
    style.map("BoutonRouge.TButton", background=[("active", "red")])


if __name__ == '__main__':
    main()


#
# Hello, you who are reading this, thank you for playing my game, and if you haven't already, please do so quickly.
# This program/game was developed by KRABANSKY Gaston, with the original idea by REMION Ambre and KRABANSKY Gaston.
#
# For all the programmers who might also be reading this, if we're talking optimization and performance, I say: "Yes... :D".
# It's not optimized, but why not make it even better, even more beautiful, even more fun?
# You should know that this program took me a long time to complete (from 8 to 10 hours, including adaptation with Tkinter '_').
# You should also be aware that this program is basically a project for the school, so please bear with me.
#
# Thanks!
# Code available at https://github.com/SniperTVmc/DoctorGame
#