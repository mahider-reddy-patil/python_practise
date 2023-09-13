class Counter:
    def __init__(self):
        self._current=0

    def incrementment(self):
        self._current+=1

    def value(self):
        return self._current

    def reset(self):
        self._current=0



curr1=Counter()

curr1.incrementment()
curr1.incrementment()
curr1.incrementment()
curr1._current=-999
print(curr1.value())
