# Traffic light controller. Red, yellow, and green. North, South, East, and West.
# Optional, but ig add pedistritation crossing.
import time

# Colors
red = "RED"
yellow = "YELLOW"
green = "GREEN"
# Directions
NS = "North_South"
EW = "East_West"
# Current State
Current_NS = red
Current_EW = green

print(f"{NS}: {Current_NS}")
print(f"{EW}: {Current_EW}")

# Pedristation button
def cross_the_street():
    while True:
        crossing = input("Is there a pedristation crossing? no spaces in answer.")
        if crossing == "yes":
            direction = input("what direction are you facing?")
            if direction.lower() == "north":
                print("So you are facing North.")
                direction = "north"
            elif direction.lower() == "south":
                print("So you are facing South.")
                direction = "south"
            elif direction.lower() == "east":
                print("So you are facing East.")
                direction = "east"
            elif direction.lower() == "west":
                print("So you are facing West.")
                direction = "west"
            else:
                print("What direction are you facing: north, south, east, west? ")

            street = input("What direction do you want to go? ")
            if street.lower() == "north":
                print("So you want to go North, ok.")
                street = "north"
            elif street.lower() == "south":
                print("So you want to go South, ok.")
                street = "south"
            elif street.lower() == "east":
                print("So you want to go East, ok.")
                street = "east"
            elif street.lower() == "west":
                print("So you want to go West, ok.")
                street = "west"
            else:
                print("What direction do you want to go: north, south, east, west? ")

        elif crossing == "no":
            print("Ok, alright... ")
        else:
            print("Is a pedristation crossing the street? Type 'yes' or 'no': ")
        break

        # If they want to go east or west, they cross the EW street
        #If the user wants to go north or south, they cross the NS street
    if direction == "north" or direction == "south":
        if street == "north" or street == "south":
            if Current_NS == red:
                print("All clear you can cross the street. ")
            elif Current_NS == yellow:
                print("Wait for the signal for the North-South intersection to be red. ")
            else:
                print("Do not cross the street. ")
        elif street == "east" or street == "west":
            if Current_NS == red:
                print("All clear you can cross the street. ")
            elif Current_NS == yellow:
                print("Wait for the signal for the East-West intersection to be red. ")
            else:
                print("Do not cross the street. ")
    elif direction == "east" or direction == "west":
        if street == "north" or street == "south":
            if Current_NS == red:
                print("All clear you can cross the street. ")
            elif Current_NS == yellow:
                print("Wait for the signal for the North-South intersection to be red. ")
            else:
                print("Do not cross the street. ")
    elif street == "east" or street == "west":
            if Current_NS == red:
                print("All clear you can cross the street. ")
            elif Current_NS == yellow:
                print("Wait for the signal for the East-West intersection to be red. ")
            else:
                print("Do not cross the street. ")


# Logic conditions
cross_the_street()
while True:
    if Current_NS == red:
        print(f"{NS}, STOP, Wait until signal is green. ")
    elif Current_NS == yellow:
        print(f"{NS}, Prepare to stop. ")
    else:
        print(f"{NS}, Proceed. ")

    if Current_EW == red:
        print(f"{EW}, STOP, Wait until signal is green. ")
    elif Current_EW == yellow:
        print(f"{EW}, Prepare to stop. ")
    else:
        print(f"{EW}, Proceed. ")

    time.sleep(5)
# State transition
    if Current_NS == green:
        Current_NS = yellow
        Current_EW = red
        print(f"{NS}: {Current_NS}")
        print(f"{EW}: {Current_EW}")

    elif Current_NS == yellow:
        Current_NS = red
        Current_EW = green
        print(f"{NS}: {Current_NS}")
        print(f"{EW}: {Current_EW}")

    elif Current_NS == red and Current_EW == green:
        Current_EW = yellow
        print(f"{NS}: {Current_NS}")
        print(f"{EW}: {Current_EW}")

    elif Current_EW == yellow:
        Current_EW = red
        Current_NS = green
        print(f"{NS}: {Current_NS}")
        print(f"{EW}: {Current_EW}")


