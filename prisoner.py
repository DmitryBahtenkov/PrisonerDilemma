import uuid
from strategy import Strategy


class Prisoner:
    def __init__(self, strategy: Strategy):
        self.strategy: Strategy = strategy
        self.id: str = str(uuid.uuid4())
        self.score = 0

    def choice(self, prisoner_id: str) -> bool:
        return self.strategy.execute(prisoner_id=prisoner_id)

    def reject(self, prisoner_id: str):
        self.strategy.rejection(prisoner_id=prisoner_id)

    def add_score(self, score: int):
        self.score += score

    def __repr__(self):
        return f'Prisoner {self.id}: {self.strategy}. Score: {self.score}'
