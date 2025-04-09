import unittest
from src.python.modules.habit_manager import HabitManager

class TestHabitManager(unittest.TestCase):
    def test_add_habit(self):
        manager = HabitManager()
        manager.add_habit("Read")
        self.assertIn("Read", manager.list_habits())

if __name__ == "__main__":
    unittest.main()
