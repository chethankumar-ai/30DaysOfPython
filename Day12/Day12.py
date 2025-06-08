# - Validate email addresses using regex
import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
# Test cases
if __name__ == "__main__":
    test_emails = ['hchethankumar17@gmail.com']
    for email in test_emails:
        if validate_email(email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")