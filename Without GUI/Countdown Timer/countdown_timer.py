import time
import sys

def countdown_timer(seconds):
    """Runs a countdown timer for the given number of seconds."""
    try:
        while seconds >= 0:
            mins, secs = divmod(seconds, 60) # Calculate minutes and seconds
            # Format the timer display
            timer_display = f"{mins:02d}:{secs:02d}"   
            print(timer_display, end='\r')  # Overwrites the previous line
            time.sleep(1) # Sleep for 1 second
            # Decrement the seconds
            seconds -= 1
        print("\n⏰ Time's up! ⏰")
    except KeyboardInterrupt:
        print("\n⏸ Countdown interrupted!")
        # Optionally, you can add any cleanup code here if needed
        # For example, you might want to reset the terminal or clear the screen.
        # os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen (optional)
        # Note: This will clear the screen after the countdown is finished.
        # You can uncomment the above line if you want to clear the screen.

def get_user_time():
    '''Gets user input for the countdown timer in minutes or seconds.'''
    while True:
        try:
            user_input = input("Enter time (e.g., '2m' for 2 minutes or '30s' for 30 seconds): ").strip().lower() # Strips whitespace and converts to lowercase
            if user_input.endswith('m'):
                minutes = int(user_input[:-1])
                seconds = minutes * 60 # Convert minutes to seconds
                break
            elif user_input.endswith('s'):
                seconds = int(user_input[:-1]) # Extract seconds
                if seconds < 0:
                    raise ValueError("Seconds cannot be negative.") # Check for negative seconds
                break
            else:
                print("⚠️ Invalid format. Please use 'Xm' for minutes or 'Xs' for seconds.") # Handle invalid format
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid number followed by 'm' or 's'.") # Handle invalid input
        except Exception as e:
            print(f"An error occurred: {e}") # Handle any other exceptions

def get_user_time():
    """Prompts the user to enter time in minutes or seconds."""
    while True:
        try:
            user_input = input("Enter time (e.g., '2m' for 2 minutes or '30s' for 30 seconds): ").strip().lower()
            if user_input.endswith('m'):
                return int(user_input[:-1]) * 60  # Convert minutes to seconds
            elif user_input.endswith('s'):
                return int(user_input[:-1])
            else:
                print("⚠️ Invalid format! Use 'Xm' for minutes or 'Ys' for seconds.")
        except ValueError:
            print("⚠️ Please enter a valid number followed by 'm' or 's'.")
        except Exception as e:
            print(f"An error occurred: {e}") # Handle any other exceptions

'''
Why Add an Alert?

Provides immediate feedback when the timer reaches zero.

Ensures the user notices the end of the countdown, even if they are not actively watching the screen.

Supports cross-platform compatibility, working on most operating systems.
'''

def alert_user():
    """Alerts the user when the timer ends."""
    print("\n⏰ Time's up! ⏰")
    try:
        # Works on most systems
        for _ in range(3):
            print("\a", end='')  # Terminal beep sound
            time.sleep(0.5) # Wait for half a second between beeps
    except:
        pass  # Ignore errors if sound doesn't play

if __name__ == "__main__":
    print("===== ⏳ Countdown Timer ⏳ =====")
    user_seconds = get_user_time()
    countdown_timer(user_seconds)
    alert_user()

'''
Why Use if __name__ == "__main__"?

Prevents unintended execution if the script is imported as a module in another program.

Ensures a structured workflow where user input, countdown, and alerts happen in sequence.

Keeps the main logic separate, making it easy to expand or modify the code in the future.
'''

'''
Countdown Timer Project Summary

What You Built:
---------------
- A working countdown timer using Python.

What You Learned:
-----------------
- How to format minutes and seconds using divmod().
- How to take user input for time (minutes and seconds).
- How to keep the timer display clean using '\r' to update on the same line.
- How to add a basic alert/notification when the timer ends.
- How to write code that runs smoothly without errors.

Ideas for Next Steps:
---------------------
- Let the user pause and resume the timer.
- Build a version with buttons and a timer screen using Tkinter (a GUI tool).
- Add a loop feature for repeating countdowns — great for workouts or study sessions.

Tip:
----
The best way to get better at Python is by making cool stuff — so keep building and trying new ideas!
'''
