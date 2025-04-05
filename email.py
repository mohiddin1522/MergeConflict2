import re
email_pattern = r"[A-Za-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "contact us at mohiddin2662@gmail.com"
match = re.search(email_pattern, text)
if match:
    print("Found an email address:", match.group())
    
#validate a password & url