import json
import os
from datetime import date

# File where your progress will be saved
DATA_FILE = "habit_history.json"

# The 5 core habits you want to track
HABITS = [
    "Workout (Light/Moderate)",
    "Studying (1-2 hours)",
    "Creating / Learning a Skill",
    "Clean Mind (No PMO)",
    "Saved a lil money"
]

def load_data():
    """Loads the habit history from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    """Saves the habit history to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def main():
    today = str(date.today())
    history = load_data()
    
    # If today hasn't been initialized yet, set all habits to False (unchecked)
    if today not in history:
        history[today] = {habit: False for habit in HABITS}
        save_data(history)
        
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=========================================")
        print(f"🇳🇬 DAILY HABIT TRACKER | Date: {today}")
        print(f"=========================================")
        
        # Display habits and status
        completed_count = 0
        print("\nYour Habits for Today:")
        for idx, habit in enumerate(HABITS, 1):
            status = "✅ Done" if history[today][habit] else "❌ Pending"
            if history[today][habit]:
                completed_count += 1
            print(f" {idx}. [{status}] {habit}")
            
        # Calculate and show completion percentage
        completion_rate = (completed_count / len(HABITS)) * 100
        print(f"\n🎯 Today's Progress: {completion_rate:.1f}%")
        print("=========================================")
        
        print("\nOptions:")
        print(" [1-5] Toggle habit status")
        print(" [Q]   Quit tracker")
        
        choice = input("\nEnter your choice: ").strip().lower()
        
        if choice == 'q':
            print("\nKeep building that discipline. See you tomorrow!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(HABITS):
            selected_habit = HABITS[int(choice) - 1]
            # Toggle the boolean value (True to False, or False to True)
            history[today][selected_habit] = not history[today][selected_habit]
            save_data(history)
        else:
            input("\nInvalid option! Press Enter to try again...")

if __name__ == "__main__":
    main()
