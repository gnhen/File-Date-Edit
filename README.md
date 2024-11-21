# convertEXE.py

## Overview
`convertEXE.py` is a Python utility designed to modify the creation and modification dates of files on a Windows system. This script allows users to specify a date and time for the file attributes, giving flexibility in managing file metadata. The tool also includes intelligent parsing for various time formats and automates time adjustments. I'd love to make a web version but I am not spending any money on it lol.

## Features
- **Customizable Dates and Times:** Specify both creation and modification dates in user-friendly formats.
- **Relative Time Adjustments:** Automatically adjusts the creation date to 17 hours and 13 minutes before the specified modification date.
- **Time Parsing:** Supports common time formats, including `1138pm` (11:38 PM) and `113832pm` (11:38:32 PM). If seconds are omitted, the script generates them randomly.
- **Error Handling:** Provides clear error messages and usage examples for invalid inputs.
- **Interactive Command-Line Interface:** Step-by-step prompts guide users through the process.

## How It Works
1. **Date Input:**
   - Enter the desired date in `MMDDYYYY` format or use the keyword `today` to select the current date.
2. **Time Input:**
   - Specify the desired time using formats like `1138pm` or `113832pm`. Alternatively, use the keyword `now` for the current time.
3. **Processing:**
   - Combines the date and time into a single timestamp for the modification date.
   - Calculates the creation date by subtracting 17 hours and 13 minutes from the modification timestamp.
4. **File Updates:**
   - Uses `os.utime` to update the modification timestamp.
   - Utilizes the `win32_setctime` library to update the creation timestamp.

## Benefits
- **Easy to Use:** Interactive interface requires no prior coding knowledge.
- **Precise Metadata Control:** Helps manage file timestamps for organizational or archival purposes.
- **Compatible with Windows:** Specifically designed for Windows systems, ensuring smooth operation.

## Usage Instructions
1. Download the executable (`File.Date.Changer.exe`) from the [Releases](https://github.com/gnhen/File-Date-Edit/releases) tab.
3. Run the executable and follow the interactive prompts to update your file's metadata.
4. Press `Q` at any point to exit the program.

## Example
1. Start the tool.
2. Enter the file path:
   ```
   Enter the file path: C:\example\file.txt
   ```
3. Enter the desired date:
   ```
   Enter the date (MMDDYYYY or 'today'): 11212024
   ```
4. Enter the desired time:
   ```
   Enter the time (e.g., 1138pm, 113832pm, or 'now'): 103030am
   ```
5. The script confirms success:
   ```
   Successfully updated file dates for C:\example\file.txt
   Modification Date/Time: 11/21/2024 10:30:00 AM
   Creation Date/Time: 11/20/2024 05:17:00 PM
   ```

## Requirements
- Windows operating system
- Python (if using the script directly)
- Required Python Libraries:
  - `datetime`
  - `os`
  - `re`
  - `random`
  - `win32_setctime` (Install using `pip install pywin32`)

## Notes
- Ensure the file path provided exists. Otherwise, an error message will be displayed.
- Use valid formats for date and time to avoid parsing issues.

For any additional help or issues, check out the [Issues](https://github.com/gnhen/File-Date-Edit/issues) section.
