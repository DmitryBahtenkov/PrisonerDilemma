from prisoner import Prisoner
from strategy import AlwaysTrue, AlwaysFalse, EyeForEye, EyeForTwoEyes
from typing import List, Tuple
from itertools import product

D = 500
C = 300
d = 50
c = 100

p1: Prisoner = Prisoner(strategy=AlwaysTrue())
p2: Prisoner = Prisoner(strategy=AlwaysFalse())
p3: Prisoner = Prisoner(strategy=EyeForEye())
p4: Prisoner = Prisoner(strategy=EyeForTwoEyes())

combinations: List[Tuple[Prisoner, Prisoner]] = []

#todo: подумать как перемешать
for p in product([p1, p2, p3, p4], repeat=2):
    combinations.append((p[0], p[1]))

if __name__ == '__main__':
    for (p1, p2) in combinations:
        p1_choice: bool = p1.choice(prisoner_id=p2.id)
        p2_choice: bool = p2.choice(prisoner_id=p1.id)

        if p1_choice is True and p2_choice is False:
            p1.add_score(c)
            p2.add_score(D)
        elif p1_choice is True and p2_choice is True:
            p1.add_score(C)
            p1.add_score(C)
        elif p1_choice is False and p2_choice is True:
            p2.add_score(D)
            p1.add_score(c)
        elif p1_choice is False and p2_choice is False:
            p1.add_score(d)
            p2.add_score(d)

        print(p1)
        print(p2)



