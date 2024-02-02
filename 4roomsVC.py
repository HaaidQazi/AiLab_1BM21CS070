
def vacuum_world():
    # Initializing goal_state for four rooms
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    cost = 0

    # User input for initial vacuum location and status of each room
    location_input = input("Enter Initial Location of Vacuum (A/B/C/D): ")
    print("Enter status of each room (1 - dirty, 0 - clean):")
    for room in goal_state:
        goal_state[room] = int(input(f"Status of Room {room}: "))

    print("Initial Location Condition: " + str(goal_state))

    # Function to clean a room
    def clean_room(room):
        nonlocal cost
        if goal_state[room] == 1:
            print(f"Cleaning Room {room}...")
            goal_state[room] = 0
            cost += 1  # Cost for cleaning
            print(f"Room {room} has been cleaned. Current cost: {cost}")
        else:
            print(f"Room {room} is already clean.")

    # Cleaning logic
    rooms = ['A', 'B', 'C', 'D']
    current_index = rooms.index(location_input)

    # Clean all rooms starting from the initial location
    for i in range(current_index, len(rooms)):
        clean_room(rooms[i])

    # Clean remaining rooms (if the initial location was not 'A')
    for i in range(0, current_index):
        clean_room(rooms[i])

    # Output final state and performance measure
    print("Final State of Rooms: " + str(goal_state))
    print("Performance Measurement (Total Cost): " + str(cost+4))

vacuum_world()
