import random

lotto_counter: dict = {key: 0 for key in range(1, 46)}


def draw6of45(prnt: bool = True):
    box = [i for i in range(1, 46)]
    draws = []
    for j in range(1, 7):
        rand = random.randrange(0, len(box) - j, 1)
        draws.append(box[rand])
        box[rand], box[len(box) - j] = box[len(box) - 1], box[rand]
    if prnt:
        print(draws)
    return draws


def lotto_statistic_updater(draws: list = []):
    for draw in draws:
        lotto_counter[draw] += 1


if __name__ == "__main__":
    print("lotto - start")
    # Exercise: programming a function drawing lotto-numbers / Aufgabe Programmiere Lottoziehung als Methode
    draw6of45()
    # Exercise: programming a function manipulate the statistic of the lotto-number-drawing /
    # Aufgabe Programmiere Lottoziehung Statistik als Methode
    for k in range(1000):
        lotto_statistic_updater(draw6of45(False))
    print(lotto_counter)
