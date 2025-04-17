"""
Write a Habit class (name, frequency, streak, dates completed)
Add a HabitManager to manage the collection and logic

A Habit class with:
name (str)
frequency (e.g. "daily", str or enum)
dates_completed (set of ISO date strings or date objects)
Methods like:
mark_done(date: Optional[date] = today)
current_streak()
is_done_today()
A HabitManager class to:
Add/remove/list habits
Get report (streaks, completion %)
Save/load (we’ll hook this up to storage.py later)


"""

## CLI Interface

if __name__ == "__main__":
    habitmanager = HabitManager()
    try:
        habitmanager.load_from_file(DATA_FILE)
        print("✅ Habits loaded.")
    except FileNotFoundError:
        print("No saved habits found.")

    while True:

        print("\nWelcome to the habit tracker\n")
        print("1. Add habit\n2. Mark done\n3. List streaks\n4. Quit\n")
        choice = input("Choose an option:\n")

        if choice == "1":
            name = input("\nWhat is the habit?\n")
            frequency = input("\nHow often do you want to do it?\n")
            habitmanager.add_habit(name, frequency)
            habitmanager.save_to_file(DATA_FILE)
            print(f"\nHabit created:\n{name}")

        elif choice == "2":
            print("")
            habits = habitmanager.list_habits()
            if habitmanager.print_habits():
                selection = int(input("\nWhich habit did you complete?\n")) - 1
            if 0 <= selection < len(habits):
                habits[selection].mark_done()
                habitmanager.save_to_file(DATA_FILE)
                print(f"\nMarked {habits[selection].name} as done.")
            else:
                print("\nYou did not select a valid habit.\n")

        elif choice == "3":
            if not habitmanager.list_habits():
                print("\nNo habits yet\n")
            else:
                allstreaks = habitmanager.get_all_streaks()
                print("\n")
                for name, streak in allstreaks.items():
                    print(f"{name}: {streak}")

        elif choice == "4":
            habitmanager.save_to_file(DATA_FILE)
            break
        else:
            print("\nInvalid option\n")
