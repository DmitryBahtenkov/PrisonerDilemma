from abc import abstractmethod, ABC
from typing import List


class Strategy(ABC):
    def __init(self):
        pass

    @abstractmethod
    def execute(self, prisoner_id: str) -> bool:
        pass

    def rejection(self, prisoner_id: str):
        pass;

    def __repr__(self):
        return type(self).__name__


class AlwaysTrue(Strategy):
    def execute(self, prisoner_id: str) -> bool:
        return True


class AlwaysFalse(Strategy):
    def execute(self, prisoner_id: str) -> bool:
        return False


class EyeForEye(Strategy):
    def __init__(self):
        self.evils: List[str] = []

    def execute(self, prisoner_id: str) -> bool:
        if prisoner_id in self.evils:
            return False
        return True

    def rejection(self, prisoner_id: str):
        self.evils.append(prisoner_id)


class EyeForTwoEyes(Strategy):
    def __init__(self):
        self.first_evils: List[str] = []
        self.evils: List[str] = []

    def execute(self, prisoner_id: str) -> bool:
        if prisoner_id is self.evils:
            return False
        return True

    def rejection(self, prisoner_id: str):
        if prisoner_id in self.first_evils:
            self.evils.append(prisoner_id)
        else:
            self.first_evils.append(prisoner_id)
