from datetime import datetime, timedelta

# Part 1: Current date and time
def display_current_datetime():
    current_datetime = datetime.now()
    fomatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Part 2: Future date calculation
def calculate_future_date():
    days = input("Number of days to add to the current date: ")
    current_datetime = datetime.now()

    try:
        days_to_add = int(days)
        future_date = current_datetime + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()