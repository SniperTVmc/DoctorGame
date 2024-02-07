import tkinter as tk
from tkinter import ttk
from PIL.ImageTk import PhotoImage

from Main import startGame

patientsCount = 5


def leaveButton():
    root.quit()


def setPatientsCount(value):
    global patientsCount
    patientsCount = value
    bouton_valider.config(text="Vous avez modifié ce paramètre.", style="BoutonVert.TButton")
    root.after(1000, lambda: bouton_valider.config(text="Valider", style="Bouton.TButton"))


def getMainUI():
    window = tk.Tk()
    window.title("Menu d'accueil")
    window.geometry("1280x720")

    # Empêcher le redimensionnement de la fenêtre
    window.resizable(width=False, height=False)

    canvas = tk.Canvas(window, bg="light grey", width=1280, height=720)
    canvas.pack()

    # Chargement de l'image
    image_main = PhotoImage(file="data/mainBackground.png")
    label_image_main = tk.Label(window, image=image_main)
    label_image_main.place(relx=0.75, rely=0.5, anchor="center")

    # Titre
    titre_label = tk.Label(window, text="Welcome on XXX Game !", font=("Helvetica", 24))
    titre_label.place(relx=0.25, rely=0.1, anchor="center")

    # Bouton Jouer
    bouton_jouer = tk.Button(window, text="Jouer", command=startGame, font=("Helvetica", 20), padx=20, pady=10,
                             borderwidth=0, highlightthickness=2, highlightbackground="green", background="#90EE90",
                             activebackground="green", relief="raised")
    bouton_jouer.place(relx=0.25, rely=0.3, anchor="center")

    # Espace entre les boutons
    espace_entre_boutons = 50

    # Bouton Options
    bouton_options = tk.Button(window, text="Options", command=openSettingsUI, font=("Helvetica", 20), padx=20, pady=10,
                               borderwidth=0, highlightthickness=2, highlightbackground="orange", background="#FFD700",
                               activebackground="orange", relief="raised")
    bouton_options.place(relx=0.25, rely=0.3 + (bouton_jouer.winfo_reqheight() + espace_entre_boutons) / 720,
                         anchor="center")

    # Bouton Quitter
    bouton_quitter = tk.Button(window, text="Quitter", command=leaveButton, font=("Helvetica", 20), padx=20,
                               pady=10, borderwidth=0, highlightthickness=2, highlightbackground="red",
                               background="#F08080", activebackground="red", relief="raised")
    bouton_quitter.place(relx=0.25, rely=0.3 + (bouton_jouer.winfo_reqheight() + espace_entre_boutons) * 2 / 720,
                         anchor="center")

    # Crédit
    attribution_label = tk.Label(window, text="Created by REMION Ambre and KRABANSKY Gaston", font=("Helvetica", 12))
    attribution_label.place(relx=0.25, rely=0.9, anchor="center")
    return window


def openSettingsUI():
    # Fonction pour ouvrir la fenêtre d'options
    options_root = tk.Toplevel()
    options_root.title("Options")
    options_root.geometry("500x300")
    options_root.resizable(False, False)  # Empêcher le redimensionnement de la fenêtre

    # Centrer la fenêtre sur l'écran
    screen_width = options_root.winfo_screenwidth()
    screen_height = options_root.winfo_screenheight()
    window_width = 500
    window_height = 300
    x_coordinate = int((screen_width - window_width) / 2)
    y_coordinate = int((screen_height - window_height) / 2)
    options_root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Variable pour stocker la valeur du curseur
    valeur_curseur = tk.IntVar()
    valeur_curseur.set(5)  # Valeur par défaut

    # Style pour les boutons
    style = ttk.Style()
    style.theme_use('clam')  # Choisir un thème ttk
    style.configure("Bouton.TButton", font=("Helvetica", 12))
    style.configure("BoutonVert.TButton", font=("Helvetica", 12), background="green")
    style.map("BoutonVert.TButton", background=[("active", "green")])  # Style pour le survol du bouton

    # Cadre principal
    cadre = ttk.Frame(options_root)
    cadre.pack(expand=True, padx=20, pady=20)

    # Titre
    label_titre = ttk.Label(cadre, text="Options", font=("Helvetica", 16))
    label_titre.grid(row=0, column=0, columnspan=2, pady=10)

    # Étiquette pour le curseur
    label_patient = ttk.Label(cadre, text="Nombre de patients:", font=("Helvetica", 12))
    label_patient.grid(row=1, column=0, pady=5, sticky="w")

    # Curseur pour sélectionner le nombre de patients
    scale_patient = ttk.Scale(cadre, from_=1, to=10, orient="horizontal", length=200, variable=valeur_curseur, command=lambda value: valeur_curseur.set(int(float(value))))
    scale_patient.grid(row=1, column=1, pady=5, sticky="w")

    # Étiquette pour afficher la valeur du curseur
    label_valeur = ttk.Label(cadre, textvariable=valeur_curseur, font=("Helvetica", 12))
    label_valeur.grid(row=2, column=1, pady=5, sticky="w")

    # Bouton pour valider la nouvelle valeur
    global bouton_valider
    bouton_valider = ttk.Button(cadre, text="Valider", command=lambda: setPatientsCount(valeur_curseur.get()), style="Bouton.TButton")
    bouton_valider.grid(row=3, column=0, columnspan=2, pady=10)

    # Fonction pour revenir en arrière
    def retour():
        options_root.destroy()

    # Bouton de retour
    bouton_retour = ttk.Button(cadre, text="Retour", command=retour, style="BoutonRouge.TButton")
    bouton_retour.grid(row=4, column=0, columnspan=2, pady=10)
    style.configure("BoutonRouge.TButton", font=("Helvetica", 12), background="red", foreground="dark red")
    style.map("BoutonRouge.TButton", background=[("active", "red")])

    # Centrer la fenêtre sur l'écran
    options_root.update_idletasks()
    options_root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


root = getMainUI()
root.mainloop()