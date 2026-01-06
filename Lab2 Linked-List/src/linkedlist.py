"""
Linked List implementations for Lab2.
Provides:
- Node, LinkedList (singly) with append, prepend, delete, search, to_list, count
- DoublyNode, DoublyLinkedList with append, prepend, delete, to_list
- StudentNode, StudentLinkedList with sorted insert by student_id, delete_by_id, find_by_id, list_all

This module is written for clarity and includes basic docstrings.
"""
from typing import Any, Optional, List, Tuple


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def prepend(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key: Any) -> bool:
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return True
        while cur and cur.next:
            if cur.next.data == key:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def search(self, key: Any) -> int:
        cur = self.head
        pos = 0
        while cur:
            if cur.data == key:
                return pos
            cur = cur.next
            pos += 1
        return -1

    def to_list(self) -> List[Any]:
        out = []
        cur = self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    def count_nodes(self) -> int:
        return len(self.to_list())


class DoublyNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['DoublyNode'] = None
        self.prev: Optional['DoublyNode'] = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None

    def append(self, data: Any) -> None:
        node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = node
            return
        assert self.tail is not None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def prepend(self, data: Any) -> None:
        node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node

    def delete(self, key: Any) -> bool:
        cur = self.head
        while cur:
            if cur.data == key:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                return True
            cur = cur.next
        return False

    def to_list(self) -> List[Any]:
        out = []
        cur = self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out


# Student linked list: stores tuples (student_id, name, grade) and keeps nodes sorted by student_id
class StudentNode:
    def __init__(self, student_id: int, name: str, grade: float):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next: Optional['StudentNode'] = None

    def to_tuple(self) -> Tuple[int, str, float]:
        return (self.student_id, self.name, self.grade)


class StudentLinkedList:
    def __init__(self):
        self.head: Optional[StudentNode] = None

    def add_student(self, student_id: int, name: str, grade: float) -> None:
        """Insert student keeping list sorted by student_id (ascending)."""
        node = StudentNode(student_id, name, grade)
        if not self.head or student_id < self.head.student_id:
            node.next = self.head
            self.head = node
            return
        cur = self.head
        while cur.next and cur.next.student_id < student_id:
            cur = cur.next
        # if same ID exists, insert after existing (could also replace)
        node.next = cur.next
        cur.next = node

    def delete_by_id(self, student_id: int) -> bool:
        cur = self.head
        if cur and cur.student_id == student_id:
            self.head = cur.next
            return True
        while cur and cur.next:
            if cur.next.student_id == student_id:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def find_by_id(self, student_id: int) -> Optional[Tuple[int, str, float]]:
        cur = self.head
        while cur:
            if cur.student_id == student_id:
                return cur.to_tuple()
            cur = cur.next
        return None

    def list_all(self) -> List[Tuple[int, str, float]]:
        out = []
        cur = self.head
        while cur:
            out.append(cur.to_tuple())
            cur = cur.next
        return out

    def display(self) -> None:
        cur = self.head
        while cur:
            print(f"{cur.student_id}: {cur.name} ({cur.grade})")
            cur = cur.next
