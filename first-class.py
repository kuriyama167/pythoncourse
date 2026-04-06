def search(sequence, expected, finder):
    for item in sequence:
        if finder(item) == expected:
            return (item)
    raise ValueError(f"{expected} not found in")


friends = [
    {"name": "Rolf", "age": 25},
    {"name": "Adam", "age": 30}, 
    {"name": "Anne", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Rlf", get_friend_name))