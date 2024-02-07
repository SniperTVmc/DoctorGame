
patients = []


def main():
    print("Welcome on the incredible GAME!")
    print()
    print("    Created by:")
    print("     - REMION Ambre")
    print("     - KRABANSKY Gaston")
    print()
    print("Do you want to read rules before playing? (Recommended for new players!) [Yes/No]")

    readRules = input(">>> ")
    if readRules == "Yes":
        showGameRules()

    readyToPlay = input("Are you ready to start the game? [Yes/No]")
    if readyToPlay == "Yes":
        startGame()
    else:
        print("Never mind, let's start the game!")
        print("Reminder: you're a doctor, don't forget to do your damn job! >:(")
        sleep(4)
        startGame()


def showGameRules():
    """Show the rules of the game in the console"""
    print()
    print("### RULES ###")
    print("In this game, you must heal five different patients.")
    print("All of patients are not necessarily infected,")
    print("so you have to find out if they are or not before you try to heal them.")
    print("But be aware! If you make a mistake, the patient will regret it forever... :D")
    print()


def startGame():
    """Start the game"""
    global patients
    patients = generatePatients()
    print("Starting of the game...")


if __name__ == '__main__':
    main()