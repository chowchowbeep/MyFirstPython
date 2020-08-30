from fighter import Fighter
from bomber import Bomber

# 다형성


def war_game(airforce):
    airforce.take_off()
    airforce.fly()
    airforce.attack()
    airforce.land()

if __name__ == "__main__":
    f15 = Fighter(2)
    war_game(f15)
    print()

    b29 = Bomber(3)
    war_game(b29)