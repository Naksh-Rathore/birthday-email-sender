# Birthday Email Reminder

This project is a Python script that automatically sends birthday greetings via email to recipients listed in a CSV file. It checks the current date and matches it against the birthdays in the file, sending a personalized message if a match is found.

## Features

- Sends personalized birthday emails
- Reads recipient data from a CSV file (`birthdays.csv`)
- Uses SMTP with TLS for secure email delivery
- Logs connection steps for debugging

## Requirements

- Python 3.x
- `pandas` library

Install the required package:

```
pip install pandas
```

## Configuration

1. **Email Setup**  
   - Replace the `from_email` variable with your Outlook email address.
   - Enter your **email password** in the `password` variable inside `send_mail`.
   - Make sure your Outlook account allows SMTP connections and is not blocking less secure apps.

2. **CSV File Format**  
   Create a `birthdays.csv` file in the same directory with the following columns:

   ```
   name,email,date,year
   John Doe,johndoe@example.com,07-22,2000
   ```

   - `name`: Recipient's name
   - `email`: Recipient's email address
   - `date`: Birthday in `MM-DD` format
   - `year`: Year of birth (used to calculate age)

3. **Optional**: Customize the email message inside the `email_content` string.

## Usage

Run the script:

```
python birthday_email.py
```

If there are any birthdays today, the script will send out emails to the corresponding recipients. Otherwise, it will print a message indicating that no birthdays are found.

## How It Works

1. Loads `birthdays.csv` using pandas
2. Checks if today's date matches any in the file
3. For each match:
   - Calculates the age
   - Composes a personalized email
   - Sends the email using `smtplib` through Outlook's SMTP server

## SMTP Details

- Host: `smtp-mail.outlook.com`
- Port: `587` (TLS)

## Security Note

Do **not** hardcode your password in production code. Consider using environment variables or secure credential storage.

## License

This project is licensed under the MIT License.
