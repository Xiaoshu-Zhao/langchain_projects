from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items = []  # Type will be List[T]

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[-1]

    def is_empty(self) -> bool:
        return not self.items
    
    
number_stack = Stack[int]()
number_stack.push(1)
number_stack.push("world")
print(number_stack.pop())  # 输出: 2

string_stack = Stack[str]()
string_stack.push('hello')
string_stack.push('world')
print(string_stack.pop())  # 输出: world