# Notes from the TryHackMe Room: 

found at: https://tryhackme.com/r/room/enumerationbruteforce
https://tryhackme.com/r/room/enumerationbruteforce

## Enumeration & Brute Force
### Enumerate and brute force authentication mechanisms.

#### Introduction
Authentication enumeration is a fundamental aspect of security testing, concentrating specifically on the mechanisms that protect sensitive aspects of web applications; this process involves methodically inspecting various authentication components ranging from username validation to password policies and session management. Each of these elements is meticulously tested because they represent potential vulnerabilities that, if exploited, could lead to significant security breaches.

#### Objectives
By the end of this room, you will:

Understand the significance of enumeration and how it sets the stage for effective brute-force attacks.
Learn advanced enumeration methods, mainly focusing on extracting information from verbose error messages.
Comprehend the relationship between enumeration and brute-force attacks in compromising authentication mechanisms.
Gain practical experience using tools and techniques for both enumeration and brute-force attacks.

#### Pre-requisites
Before starting this room, you should have a basic understanding of the following concepts:

Familiarity with HTTP and HTTPS, including request/response structures and common status codes.
Experience using tools like Burp Suite.
Basic proficiency in navigating and using the Linux command line.
Answer the questions below
Deploy the target VM attached to this task by pressing the green Start Machine button. After obtaining the machine's generated IP address, you can either use the AttackBox or your own VM connected to TryHackMe's VPN.

**Add 10.10.198.158 to your /etc/hosts file. For example:**

```Bash
$: sudo nano /etc/hosts
10.10.198.158    enum.thm
```

