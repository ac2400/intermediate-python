"""
from __future__ import annotations
from datetime import date
from typing import Set, Optional

# This is the old Habit class with in-memory storage
class Habit:
    def __init__(
        self,
        name: str,
        frequency: str,
        streak: int = 0,
        dates_completed: Optional[Set[date]] = None,
    ):
        self.name = name
        self.frequency = frequency
        self.streak = streak
        self.dates_completed = dates_completed or set()

    def mark_done(self, date_done: Optional[date] = None):
        if date_done is None:
            date_done = date.today()

        if date_done not in self.dates_completed:
            self.dates_completed.add(date_done)
            self.streak += 1

    def current_streak(self) -> int:
        return self.streak

    def is_done_today(self) -> bool:
        return date.today() in self.dates_completed

    def calculate_streak(self) -> int:
        backwards = sorted(self.dates_completed, reverse=True)
        if not backwards:
            return 0  # No completions yet
        if backwards[0] != date.today():
            return 0
        streak = 1  # so far we know you have a single day streak
        for i in range(1, len(backwards)):
            current = backwards[i]
            prev = backwards[i - 1]
            if (current - prev).days == 1:
                streak += 1
            else:
                return streak
        return streak

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "frequency": self.frequency,
            "streak": self.streak,
            "dates_completed": [d.isoformat() for d in self.dates_completed],
        }

    @staticmethod
    def from_dict(x: dict) -> Habit:
        return Habit(
            name=x["name"],
            frequency=x["frequency"],
            streak=x["streak"],
            dates_completed={date.fromisoformat(d) for d in x["dates_completed"]},
        )
"""
