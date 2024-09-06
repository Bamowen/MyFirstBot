from random import choice

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Silence looms'
    elif 'hello' in lowered:
        return 'Hello there!'
    else:
        return choice(["Bla", "Bleh", "Bluh"])
    