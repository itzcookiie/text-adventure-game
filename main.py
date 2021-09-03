import keyboard
import os

room_mappings = {
    0: {
        "direction": "up",
        "temptation": "If You are the Son of God, command this stone to become bread.",
        "verse": "It is written, `Man shall not live by bread alone, but by every word of God.`"
    },
    1: {
        "direction": "left",
        "temptation": "All this authority I will give You, and their glory; for this has been delivered to me, and I give it to whomever I wish. Therefore, if You will worship before me, all will be Yours.",
        "verse": "Get behind Me, Satan! For it is written, `You shall worship the Lord your God, and Him only you shall serve.`"
    },
    2: {
        "direction": "right",
        "temptation": "If You are the Son of God, throw Yourself down from here. For it is written: `He shall give His angels charge over you to keep you`, and `in their hands they shall bear you up lest you dash your foot against a stone.’",
        "verse": "It has been said, `You shall not tempt the Lord your God.`"
    },
    3: {
        "direction": "down",
        "temptation": "Does God really love you? Look at your life. Why would God love you at of all people? You don't evangelise or do anything for God. What makes you so sure?",
        "verse": "The Lord has appeared of old to me, saying: Yes, I have loved you with an everlasting love, therefore with lovingkindness I have drawn you."
    }
}


class Room(object):
    def __init__(self, number, temptation):
        self.number = number
        self.temptation = temptation


class User(object):
    def __init__(self, username):
        self.username = username
        self.exp = 0
        self.rooms_cleared = []


def clear():
    os.system('cls')


def get_battle_choice(user, room_number):
    print("An enemy has appeared!")
    print("1) Fight")
    print("2) Flee")
    battle_choice = input("\n")
    clear()
    if int(battle_choice) == 1:
        print(f"""{room_mappings[room_number].get("temptation")}\n""")
        for i, room_mapping in room_mappings.items():
            print(f"""{i + 1}) {room_mapping.get("verse")}""")
        verse_answer = input("")
        clear()
        user_verse = room_mappings[int(verse_answer) - 1].get("verse")
        if user_verse == room_mappings[room_number].get("verse"):
            user.rooms_cleared.append(room_number)
            user.exp += 100
            print("You defeated the enemy and gained 100 exp!")
            input("Press enter to return back to the main room")
        else:
            print("That verse had no effect")
            print("You was not able to clear the room")
            input("Press enter to return back to the main room")
        clear()


def game_loop():
    rooms = {i: Room(i, room_mappings[i].get("temptation")) for i in range(4)}
    username = input("Welcome to the arena! Enter a username: ")
    user = User(username)
    clear()
    while True:
        rooms_left = len(rooms) - len(user.rooms_cleared)
        if not rooms_left:
            print(f"Congratuations {user.username}! You have cleared all the rooms!")
            print("You are a world class warrior!")
            print(f"You finished with {user.exp} exp!")
            print("Press esc to quit game")
            keyboard.wait('esc')
            break
        print(f"There are currently {len(rooms) - len(user.rooms_cleared)} rooms for you to enter")
        open_rooms = [roomNumber for roomNumber in rooms if roomNumber not in user.rooms_cleared]
        for roomNumber in open_rooms:
            print(f"""Room {roomNumber} - To enter go {room_mappings.get(roomNumber).get("direction").upper()}""")
        directions = [room_mappings[room_number].get("direction") for room_number in open_rooms]
        direction = keyboard.read_key()
        while direction not in directions:
            direction = keyboard.read_key()
        clear()
        current_room_number = [room_number for room_number in open_rooms if
                               direction == room_mappings[room_number].get("direction")].pop()
        get_battle_choice(user, current_room_number)


game_loop()
