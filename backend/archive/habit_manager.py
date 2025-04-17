"""
from __future__ import annotations
import json
from typing import List, Optional


# This is the old HabitManager class with in-memory storage
class HabitManager:
    def __init__(self):
        self.habits: List[Habit] = []

    def add_habit(self, name: str, frequency: str) -> None:
        habit = Habit(name, frequency)
        self.habits.append(habit)

    def get_habit(self, name: str) -> Optional[Habit]:
        for i in self.habits:
            if i.name == name:
                return i
        return None

    def remove_habit(self, name: str) -> bool:
        for i in self.habits:
            if i.name == name:
                self.habits.remove(i)
                return True  # Confirm it was deleted
        return False  # Not found

    def list_habits(self) -> List[Habit]:
        return self.habits

    def get_all_streaks(self) -> dict[str, int]:
        x = {}
        for i in self.habits:
            x[i.name] = i.calculate_streak()
        return x

    def print_habits(self) -> bool:
        habits = self.list_habits()
        if not habits:
            print("No habits yet.")
            return False
        for idx, habit in enumerate(habits):
            print(f"{idx+1}. {habit.name}")
        return True

    def save_to_file(self, filename) -> None:
        data = [habit.to_dict() for habit in self.habits]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename) -> None:
        with open(filename, "r") as f:
            data = json.load(f)
            self.habits = [Habit.from_dict(d) for d in data]


habitmanager = HabitManager()
"""