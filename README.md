# Notes from the TryHackMe Room: 

found at: https://tryhackme.com/r/room/enumerationbruteforce
https://tryhackme.com/r/room/enumerationbruteforce

## Enumeration & Brute Force
### Enumerate and brute force authentication mechanisms.

#### Introduction
Authentication enumeration is a fundamental aspect of security testing, concentrating specifically on the mechanisms that protect sensitive aspects of web applications; this process involves methodically inspecting various authentication components ranging from username validation to password policies and session management. Each of these elements is meticulously tested because they represent potential vulnerabilities that, if exploited, could lead to significant security breaches.

#### Objectives
By the end of this room, you will:

1. Understand the significance of enumeration and how it sets the stage for effective brute-force attacks.
2. Learn advanced enumeration methods, mainly focusing on extracting information from verbose error messages.
3. Comprehend the relationship between enumeration and brute-force attacks in compromising authentication mechanisms.
4. Gain practical experience using tools and techniques for both enumeration and brute-force attacks.

#### Pre-requisites
Before starting this room, you should have a basic understanding of the following concepts:

1. Familiarity with HTTP and HTTPS, including request/response structures and common status codes. 
2. Experience using tools like Burp Suite. 
3. Basic proficiency in navigating and using the Linux command line. 

**Add 10.10.198.158 to your /etc/hosts file. For example:**

```Bash
$: sudo nano /etc/hosts
10.10.198.158    enum.thm
```

