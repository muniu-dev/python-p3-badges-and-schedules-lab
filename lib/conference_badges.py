def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [f'Hello, my name is {name}.' for name in names]

def assign_rooms(names):
    rooms = range(1, 9)
    room_list = []
    for room in rooms:
        room_list.append(f'Hello, {names[room-1]}! You\'ll be assigned to room {room}!')
    return room_list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assigned_room in assign_rooms(names):
        print(assigned_room)