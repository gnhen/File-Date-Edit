import os
import sys
from datetime import datetime, timedelta
import re
import random
import win32_setctime


def parse_time(time_str):
    """
    Parse time string with optional seconds

    :param time_str: Time string to parse
    :return: datetime.time object
    """
    # Remove colons and convert to lowercase
    time_str = time_str.replace(":", "").lower()

    try:
        # Regex patterns to match different time formats
        # 1. HHMMSSAM/PM (with seconds)
        # 2. HHMM(AM/PM) (without seconds)
        patterns = [
            r"^(\d{2})(\d{2})(\d{2})(am|pm)$",  # with seconds
            r"^(\d{2})(\d{2})(am|pm)$",  # without seconds
        ]

        for pattern in patterns:
            match = re.match(pattern, time_str, re.IGNORECASE)
            if match:
                if len(match.groups()) == 4:
                    # Format with seconds
                    hours, minutes, seconds, meridiem = match.groups()
                elif len(match.groups()) == 3:
                    # Format without seconds
                    hours, minutes, meridiem = match.groups()
                    seconds = f"{random.randint(1, 59):02d}"

                # Convert to 24-hour format
                hours = int(hours)
                minutes = int(minutes)
                seconds = int(seconds)
                if meridiem.lower() == "pm" and hours != 12:
                    hours += 12
                elif meridiem.lower() == "am" and hours == 12:
                    hours = 0

                return datetime.strptime(
                    f"{hours:02d}{minutes:02d}{seconds:02d}", "%H%M%S"
                ).time()

        raise ValueError("Invalid time format")
    except Exception as e:
        print(f"Error: {e}")
        print("Use formats like:")
        print("  1138pm   (11:38 PM)")
        print("  113832pm (11:38:32 PM)")
        sys.exit(1)


def change_file_dates(file_path, date_string, time_string):
    """
    Change the modification and creation dates of a file.

    :param file_path: Path to the file
    :param date_string: Date in MMDDYYYY format or "today"
    :param time_string: Time in format like 1138pm, 113832pm, or "now"
    """
    # Strip any surrounding quotation marks from the file path
    file_path = file_path.strip("'\"")

    # Get absolute file path
    file_path = os.path.abspath(file_path)

    # Validate file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return

    # Validate date and time
    try:
        # Parse the input date
        if date_string.lower() == "today":
            input_date = datetime.today()
        else:
            input_date = datetime.strptime(date_string, "%m%d%Y")

        # Parse the input time
        if time_string.lower() == "now":
            input_time = datetime.now().time()
        else:
            input_time = parse_time(time_string)

        # Combine date and time
        mod_datetime = datetime.combine(input_date.date(), input_time)

        # Prompt for created date preference
        created_choice = (
            input(
                "Would you like to change the Created Date? If no, it will automatically make it 17 hours and 13 minutes before the modified date. (Y/N): "
            )
            .strip()
            .upper()
        )

        if created_choice == "Y":
            # Get custom creation date and time
            created_date = input("Enter creation date (MMDDYYYY or 'today'): ").strip()
            created_time = input("Enter creation time (HHMM or 'now'): ").strip()

            # Parse creation date
            if created_date.lower() == "today":
                created_input_date = datetime.today()
            else:
                created_input_date = datetime.strptime(created_date, "%m%d%Y")

            # Parse creation time
            if created_time.lower() == "now":
                created_input_time = datetime.now().time()
            else:
                created_input_time = parse_time(created_time)

            # Combine creation date and time
            creation_datetime = datetime.combine(
                created_input_date.date(), created_input_time
            )
        else:
            # Use original 17h13m rule
            creation_datetime = mod_datetime - timedelta(hours=17, minutes=13)

        # Convert dates to timestamps
        mod_timestamp = mod_datetime.timestamp()
        creation_timestamp = creation_datetime.timestamp()

        # Windows approach
        win32_setctime.setctime(file_path, creation_timestamp)
        os.utime(file_path, (mod_timestamp, mod_timestamp))

        print(f"Successfully updated file dates for {file_path}")
        print(
            f"Modification Date/Time: {mod_datetime.strftime('%m/%d/%Y %I:%M:%S %p')}"
        )
        print(
            f"Creation Date/Time: {creation_datetime.strftime('%m/%d/%Y %I:%M:%S %p')}"
        )

    except ValueError as e:
        print(f"Error: {e}. Use MMDDYYYY for date (e.g., 11172024)")
        print("Use time formats like:")
        print("  1138pm   (11:38 PM)")
        print("  113832pm (11:38:32 PM)")


def main():
    while True:
        file_path = input("Enter the file path: ").strip("'\"")
        date_string = input("Enter the date (MMDDYYYY or 'today'): ")
        time_string = input("Enter the time (e.g., 1138pm, 113832pm, or 'now'): ")

        change_file_dates(file_path, date_string, time_string)

        print("Press 'Q' to quit or any other key to continue...")
        if input().strip().lower() == "q":
            break


if __name__ == "__main__":
    main()
