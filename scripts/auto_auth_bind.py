"""
If you cannot run Python Locally, you can copy-paste the contents of this file to
this website and run it there:

https://www.online-python.com/
"""


def generate_keybind(player_names, key='p'):
    """
    Generate a keybind command for authenticating multiple players.

    :param player_names: List of player names to be authenticated.
    :param key: Optional key binding (default: 'p').
    :return: String representing the generated keybind command.
    """
    return f'bind {key} ' + ';'.join([f'chat.say "/auth {name}"' for name in player_names])


player_list = [
    "Gyro",
    "Devs",
    "Lex",
    "Sheep",
    "Chilling",
    "TDP",
    "Adips",
    "ScRuFFnuF",
    "Stoflap",
    "Waslap",
    "Natlap",
    "Toast",
    "Moses",
    "Eros",
    "Ozmah",
    "VoidFletcher",
]

result = generate_keybind(player_list)
print(result)
