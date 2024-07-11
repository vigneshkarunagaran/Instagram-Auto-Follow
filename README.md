# Instagram Bot README

## Description
This Instagram Bot is a Python script that automates the process of logging into Instagram, browsing specified hashtags, liking posts, and following users. The bot also allows the user to decide whether to like, skip to the next post, move to the next hashtag, or close the session.

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Google Chrome browser and ChromeDriver

## Installation
1. **Install Python and Selenium:**
   Make sure you have Python installed on your machine. If not, download and install it from [Python's official website](https://www.python.org/).

   Install Selenium using pip:
   ```sh
   pip install selenium
   ```

2. **Download ChromeDriver:**
   Download the ChromeDriver that matches your Google Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract the downloaded file and note the path.

## Configuration
1. **Update ChromeDriver Path:**
   Replace the `chromedriver_path` variable in the script with the path to your downloaded ChromeDriver.
   ```python
   chromedriver_path = r'path\to\chromedriver.exe'
   ```

2. **Instagram Credentials:**
   Replace the `username` and `password` in the script with your Instagram credentials.
   ```python
   username.send_keys('your_username')
   password.send_keys('your_password')
   ```

3. **Hashtag List:**
   Modify the `hashtag_list` variable to include the hashtags you want to browse.
   ```python
   hashtag_list = ['shutterbug', 'note5pro', 'traveler']
   ```

## Running the Script
1. **Run the Script:**
   Execute the script using Python:
   ```sh
   python path_to_script.py
   ```

2. **Login and Verification:**
   The bot will open Instagram's login page, enter your credentials, and wait for a verification code. Enter the verification code when prompted.

3. **Interactions:**
   The bot will start browsing the specified hashtags. For each post, it will prompt you with a decision:
   - **l:** Like the post and follow the user if not already following.
   - **n:** Skip to the next post.
   - **h:** Move to the next hashtag.
   - **c:** Close the session and save the list of followed users.

## Debug Information
Throughout the script, debug information is printed to the console to help track the bot's actions:
- `[DEBUG] Login Success`
- `[DEBUG] Verification Success`
- `[DEBUG] Not now Success`
- `[DEBUG] Hashtag : <hashtag>`
- `[DEBUG] Follow Success`
- `[DEBUG] Like Success`
- `[DEBUG] Next Success`
- `[DEBUG] Summary`

## Saving Followed Users
The bot saves the list of followed users to a CSV file with a timestamp in the format `YYYYMMDD-HHMMSS_users_followed_list.csv`.

## Notes
- The bot includes a section for commenting on posts, which is currently commented out. You can uncomment and customize this section as needed.
- The bot's decisions are manual, requiring user input for each action.

## Troubleshooting
- Ensure the ChromeDriver path is correctly set.
- Verify that the correct Instagram credentials are entered.
- Check the compatibility of the ChromeDriver with your Google Chrome version.
- Ensure stable internet connectivity during the bot's execution.

For any issues or improvements, feel free to contribute or raise an issue on the repository.
