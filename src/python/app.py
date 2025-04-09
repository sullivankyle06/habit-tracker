from modules.habit_manager import HabitManager

manager = HabitManager()
manager.add_habit("Exercise")
print("Your habits:", manager.list_habits())