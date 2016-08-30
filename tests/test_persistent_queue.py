import unittest

from pyfakefs import fake_filesystem_unittest

from persistent_queue import PersistentQueue


class TestPersistentQueue(fake_filesystem_unittest.TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_count(self):
        queue = PersistentQueue()
        self.assertEqual(len(queue), 0)
        self.assertEqual(queue.count(), 0)

        queue.push(1)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.count(), 1)

        queue.push(2)
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue.count(), 2)

        for i in range(100 + 1):
            queue.push(i)

        self.assertEqual(len(queue), 103)
        self.assertEqual(queue.count(), 103)

    def test_clear(self):
        queue = PersistentQueue()
        queue.push(5)
        queue.push(50)

        # self.assertEqual(queue.peek(2), [5, 50])
        self.assertEqual(len(queue), 2)
        queue.clear()
        self.assertEqual(len(queue), 0)

    def test_push(self):
        pass

    def test_pop(self):
        pass

    def test_peek(self):
        pass



if __name__ == '__main__':
    unittest.main()
