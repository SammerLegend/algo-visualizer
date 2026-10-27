import unittest

from bubble_sort import run as bubble_run
from binary_search import run as binary_run
from factorial import run as factorial_run
from fibonacci import run as fibonacci_run
from graph import Graph
from insertion_sort import run as insertion_run
from linear_search import run as linear_run
from linked_list import LinkedList
from merge_sort import run as merge_run
from quick_sort import run as quick_run
from queue import Queue
from selection_sort import run as selection_run
from stack import Stack
from hash_table import HashTable
from binary_tree import BinaryTree


class AlgorithmTests(unittest.TestCase):
    def test_sorting_algorithms(self):
        self.assertEqual(quick_run([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_run([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(merge_run([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_run([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(selection_run([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_search_algorithms(self):
        self.assertEqual(binary_run([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(binary_run([1, 2, 3, 4, 5], 9), -1)
        self.assertEqual(linear_run([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(linear_run([1, 2, 3, 4, 5], 9), -1)

    def test_stack_queue_and_linked_list(self):
        stack = Stack()
        for value in [10, 20, 30]:
            stack.push(value)
        self.assertEqual(stack.peek(), 30)
        self.assertEqual(stack.pop(), 30)
        self.assertFalse(stack.is_empty())

        queue = Queue()
        for value in [10, 20, 30]:
            queue.enqueue(value)
        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.dequeue(), 10)

        linked_list = LinkedList()
        for value in [10, 20, 30]:
            linked_list.insert(value)
        self.assertEqual(linked_list.to_list(), [10, 20, 30])
        linked_list.delete(20)
        self.assertEqual(linked_list.to_list(), [10, 30])

    def test_hash_table_and_tree(self):
        table = HashTable(5)
        table.insert("apple", 10)
        table.insert("banana", 20)
        self.assertEqual(table.get("apple"), 10)
        table.delete("apple")
        self.assertIsNone(table.get("apple"))

        tree = BinaryTree()
        for value in [50, 30, 70, 20, 40, 60, 80]:
            tree.insert(value)
        self.assertEqual(tree.inorder(), [20, 30, 40, 50, 60, 70, 80])

    def test_recursion_and_graph(self):
        self.assertEqual(factorial_run(5), 120)
        self.assertEqual(fibonacci_run(7), 13)

        graph = Graph()
        for value in ["A", "B", "C", "D"]:
            graph.add_vertex(value)
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        self.assertIn("B", graph.adjacency["A"])
        self.assertIn("C", graph.adjacency["A"])


if __name__ == "__main__":
    unittest.main()
