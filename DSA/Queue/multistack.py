import math
class MultiStack:
    def __init__(self, total_size):
        self.total_size = total_size
        self.stack_list = [0] * total_size
        self.stacknum = 3
        self.stack_size = [0] * self.stacknum
        self.stacks_parts = math.ceil(self.total_size/self.stacknum)

    def __str__(self):
        return ' -> '.join([str(item) for item in self.stack_list])

    def stackIndexRange(self, stacknum):
        start, last = (stacknum * self.stacks_parts), (stacknum * self.stacks_parts) + self.stacks_parts
        return self.stack_list[start:last]

    def add(self, value, stacknum):
        if stacknum > self.stacknum - 1:
            return f'Only {self.stacknum} stacks exists in list!'
        else:
            if self.stack_size[stacknum] >= len(self.stackIndexRange(stacknum)):
                print('Stack is full')
                return 'Stack is full.'
            else:
                indexToAdd = (stacknum * self.stacks_parts) + self.stack_size[stacknum]
                self.stack_list[indexToAdd] = value
                self.stack_size[stacknum] += 1

    def pop(self, stacknum):
        if stacknum > self.stacknum - 1:
            return f'Only {self.stacknum} stacks exists in list!'
        else:
            if not any(self.stackIndexRange(stacknum)):
                print('Stack is already empty!')
            else:
                indexToPop = (stacknum * self.stacks_parts) + (self.stack_size[stacknum] - 1)
                self.stack_list[indexToPop] = 0
                self.stack_size[stacknum] -= 1


ms = MultiStack(12)

ms.add(12,0)
ms.add(233,0)
ms.add(1341,0)
ms.add(11,0)

ms.add(22,1)
ms.add(23,2)
ms.add(133,2)
ms.add(444,1)
print(ms)
ms.pop(0)
ms.pop(0)
ms.pop(0)
ms.pop(1)
ms.pop(1)
print(ms)

