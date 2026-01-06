"""
Demo runner for Lab2 Linked-List exercises.
Runs:
- exercise1: create linked list, append/prepend/delete and display
- exercise2: count nodes (uses the same list)
- student_manager_demo: add/delete/find/list students (sorted by id)

Run from repo root:
python .\"Lab2 Linked-List\"\src\run_lab2.py
"""
from linkedlist import LinkedList, StudentLinkedList, DoublyLinkedList


def exercise1():
    print("--- Exercise 1: Basic LinkedList operations ---")
    llist = LinkedList()
    print("1. Append 1,2,3")
    llist.append(1)
    llist.append(2)
    llist.append(3)
    print("Result:", llist.to_list())

    print("\n2. Prepend 0")
    llist.prepend(0)
    print("Result:", llist.to_list())

    print("\n3. Delete 2")
    deleted = llist.delete(2)
    print("Deleted 2?", deleted)
    print("Result:", llist.to_list())

    return llist


def exercise2(llist: LinkedList):
    print("--- Exercise 2: Count and search ---")
    print("Linked List:", llist.to_list())
    print("Count nodes:", llist.count_nodes())
    key = 3
    pos = llist.search(key)
    print(f"Search {key}: position {pos} ( -1 means not found)")


def student_manager_demo():
    print("--- Student Manager (Linked List sorted by student_id) ---")
    sll = StudentLinkedList()
    print("Add students: (1002,Bob,3.0), (1001,Alice,3.5), (1003,Charlie,2.8)")
    sll.add_student(1002, 'Bob', 3.0)
    sll.add_student(1001, 'Alice', 3.5)
    sll.add_student(1003, 'Charlie', 2.8)
    print("List all students (sorted by id):")
    for sid, name, grade in sll.list_all():
        print(f"{sid} - {name} ({grade})")

    print("\nFind student 1002:", sll.find_by_id(1002))
    print("Delete student 1002")
    print("Deleted?", sll.delete_by_id(1002))
    print("Find 1002 after delete:", sll.find_by_id(1002))
    print("Final list:", sll.list_all())


def doubly_demo():
    print("--- Doubly Linked List demo ---")
    dl = DoublyLinkedList()
    dl.append('a')
    dl.append('b')
    dl.prepend('z')
    print("List:", dl.to_list())
    dl.delete('a')
    print("After delete 'a':", dl.to_list())


if __name__ == '__main__':
    l = exercise1()
    exercise2(l)
    print()
    student_manager_demo()
    print()
    doubly_demo()
