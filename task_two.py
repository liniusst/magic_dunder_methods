# pylint: disable= missing-docstring
from typing import List, Optional


class MyQueue:
    def __init__(self, q_list: List[Optional[int]]) -> None:
        self.q_list = q_list

    def __bool__(self) -> bool:
        return bool(self.q_list)

    def __repr__(self) -> str:
        return f"MyQueue({self.q_list})."

    def __len__(self) -> int:
        return len(self.q_list)


queue = MyQueue(q_list=[])
queue.q_list.append(1)
queue.q_list.append(2)
queue.q_list.append(3)
queue.q_list.append(4)
print(bool(queue))
print(repr(queue))
print(len(queue))
