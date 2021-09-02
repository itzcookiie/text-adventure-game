import keyboard

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


def get_battle_choice(room_number):
    battle_choice = input("\n")
    if int(battle_choice) == 1:
        print(f"""{room_mappings[room_number].get("temptation")}\n""")
        for i, room_mapping in room_mappings.items():
            print(f"""{i+1}) {room_mapping.get("verse")}""")
        verse_answer = input("")
        if room_mappings[int(verse_answer)-1].get("verse") == room_mappings[room_number].get("verse"):
            user.rooms_cleared.append(room_number)
            print("You defeated the enemy!")
            input("Press enter to continue")
            return

def ask_next_room(user_input):
    return input("What room would you like to enter?\nRoom 0 [0]\nRoom 1 [1]\nRoom 2 [2]\nRoom 3 [3]")


rooms = {i: Room(i, room_mappings[i].get("temptation")) for i in range(4)}
username = input("Welcome to the arena! Enter a username: ")
user = User(username)
while True:
    print(f"There are currently {len(rooms) - len(user.rooms_cleared)} rooms for you to enter")
    for roomNumber, room in rooms.items():
        if roomNumber not in user.rooms_cleared:
            print(f"""Room {roomNumber} - To enter go {room_mappings.get(roomNumber).get("direction").upper()}""")
    current_room_number = None
    direction = keyboard.read_key()
    if direction == "up":
        current_room_number = 0
        print("An enemy has appeared!")
        print("What will you do?")
        print("1) Fight")
        print("2) Flee")
        get_battle_choice(current_room_number)


