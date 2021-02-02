from abc import ABC, abstractmethod


class VirtualMultiply(ABC):
    def __init__(self):
        print("Abstract class")

    @abstractmethod
    def multiply(self, a, b):
        pass


class ClassicalMultiply(VirtualMultiply):
    def __init__(self):
        super().__init__()
        print("Subclass")

    def multiply(self, a, b):
        return a * b


class LoopMultiply(VirtualMultiply):
    def __init__(self):
        super().__init__()
        print("Subclass")

    def multiply(self, a, b):
        res = 1
        for i in range(1, a + 1):
            res = i * b
        return res


obj = ClassicalMultiply()
res = obj.multiply(2, 3)
print(res)