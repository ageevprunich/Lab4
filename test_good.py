import unittest

from goods import Queue  
class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_add_item_string(self):
        result = self.queue.add_item("Order 1")
        self.assertTrue(result, "Не вдалося додати рядок до черги")

    def test_add_item_non_string(self):
        with self.assertRaises(Exception):
            self.queue.add_item(123)

    def test_pop(self):
        self.queue.add_item("Order 1")
        self.queue.add_item("Order 2")
        self.queue.pop()
        self.assertEqual(len(self.queue.queue), 1, "Не вдалося видалити елемент з черги")

    def test_view_list(self):
        self.queue.add_item("Order 1")
        self.queue.add_item("Order 2")
        result = self.queue.view_list()
        expected_result = ["Order 1", "Order 2"]
        self.assertEqual(result, expected_result, "Помилка при перегляді черги")

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
    
