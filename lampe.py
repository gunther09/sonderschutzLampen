import random

PULS = ["Löwenzahn", "Farn", "Moos", "Server 7"]
DIAGNOSE = ["blüht leicht", "braucht ein Update", "ist photosynthetisch überlastet", "wurde von Bienen gehackt"]


def sonderschutz():
    return f"{random.choice(PULS)} {random.choice(DIAGNOSE)}. Bitte 3 Gänseblümchen einnehmen."


if __name__ == "__main__":
    print(sonderschutz())
