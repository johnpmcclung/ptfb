"""
help
start - start the car
stop - stop the car
quit - exit the game
anything else - i dont understand that
"""

command = ""
print("\nWelcome to the new car game. Type your command below. Type 'help' to see a list of available commands. \n")

started = False
stopped = True

while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("Available commands:")
        print("'Start': Start the car")
        print("'Stop': Stop the car")
        print("'Quit': Exit the game")
    elif command == "start":
        if started == False:
            print("Starting the car... Buckle up.")
            started = True
            stopped = False
        else:
            print("Car already started, can't start again!")
    elif command == "stop":
        if stopped == False:
            print("Stopping the car.")
            stopped = True
            started = False
        else:
            print("Car already stopped, can't stop!")
    elif command == "quit":
        print("Quitting the game. See you next time!")
        break
    else:
        print("Command not recognized, please see 'help' for a list of available commands.")
   
