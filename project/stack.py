from typing import List


class Stack:
    def __init__(self) -> None:
        self.data: List[str] = []


    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not any(self.data)

    def __str__(self) -> str:
        return "[" + ", ".join(reversed(self.data)) + "]"


stack = Stack()
stack.push("5")
print(stack.pop() + 4 )


