#!/usr/bin/python3
from sys import argv
from sys import exit

def read_occupant_file (file):
    occupants = []
    f = open(file).read().splitlines()
    for line in f:
        if len(line) > 0:
            occupants.append(line)
    return occupants

def read_event_file (file):
    events = []
    f = open(file).read().splitlines()
    for line in f:
        if len(line) > 0:
            events.append(line)
    return events

def read_unsuitable_file (file):
    unsuitable = {}
    f = open(file).read().splitlines()
    for line in f:
        if len(line) > 0:
            arr = line.split("|")
            if len(arr) > 1:
                occupants = arr[1:]
                unsuitable[arr[0]] = occupants
    return unsuitable

def do_increase (val, max_val):
    if val >= max_val:
        return 0

    return val + 1

def distributor (occupants, events, unsuitable):
    if len(occupants) <= 0:
        raise Exception("No occupants given. Exiting...")
    if len(events) <= 0:
        raise Exception("No events given. Exiting...")

    occupation_counter = {}

    for occupant in occupants:
        occupation_counter[occupant] = 0

    current_occupant = -1
    for event in events:
        temp_occupants = []
        if event in unsuitable:
            for occ in occupants:
                if occ not in unsuitable[event]:
                    temp_occupants.append(occ)

            if len(temp_occupants) <= 0:
                temp_occupants = occupants
        else:
            temp_occupants = occupants
        for i in range(len(temp_occupants)):
            current_occupant = do_increase(current_occupant, len(temp_occupants) - 1)
            if occupation_counter[temp_occupants[current_occupant]] > min(occupation_counter.values()):
                continue

            break

        occupant = temp_occupants[current_occupant]
        print(event + " => " + occupant)
        occupation_counter[occupant] += 1

if __name__ == "__main__":
    usage = "Usage: " + argv[0] + " [occupants] [events] [unsuitable]\n" \
            + "  where\n" \
            + "  - occupants is file formatted like \"person1\\nperson2\"\n" \
            + "  - events is file formatted like \"event1\\nevent2\\nevent3\"\n" \
            + "  - unsuitable is file formatted like \"event|person|person2\\n"\
            + "\"\n  Unsuitable can be left out if none exists."

    if len(argv) in [3, 4]:
        occupants = read_occupant_file(argv[1])
        events = read_event_file(argv[2])
        unsuitable = {}
        if len(argv) == 4:
            unsuitable = read_unsuitable_file(argv[3])
            if len(unsuitable) <= 0:
                print("[WARNING] No unsuitable entries found.")
        distributor(occupants, events, unsuitable)
    else:
        print("Wrong argument count!")
        print(usage)
        exit()
