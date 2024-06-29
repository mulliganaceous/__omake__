class Best_Combination():
    def __init__(self, values: list[int]):
        self.values = values
        self.stacks = []
        self.stack = None
        self.beststack = None

    def all_combinations(self, target: int) -> int:
        self.stacks = []
        self.stack = []
        self.beststack = [target]
        def backtrack(target: int) -> None:
            if len(self.stack) > self.beststack[-1]:
                return
            if target < 0:
                return
            if target == 0:
                if len(self.stack) < self.beststack[-1]:
                    print("\tBest known stack: {0:d}".format(len(self.stack)))
                    self.beststack.append(len(self.stack))
                self.stacks.append(1*self.stack)
                return
            toprank = len(self.values) - 1
            if len(self.stack) > 0:
                toprank = self.stack[-1]
            for rank in range(toprank, -1, -1):
                self.stack.append(rank)
                backtrack(target - self.values[rank])
                self.stack.pop()
        backtrack(target)

        for stack in self.stacks:
            print("\t{0:s}".format(str(list(map(lambda x: self.values[x], stack)))))
        print("There are {0:d} ways to drop {1:d} XP.".format(len(self.stacks), target))

        return self.stacks, self.beststack


