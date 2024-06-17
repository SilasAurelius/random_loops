# List representing email addresses, "None" indicates an invalid
emails = ["user1@example.com", None, "user2@example.com", "user3@example.com", None]

# List to hold valid emails
valid_emails = []

# Iterate over the list of emails
for email in emails:
    # Skip the iteration if the email is invalid.
    if email is None:
        continue
    # Add the valid email to list.
    valid_emails.append(email)
#Print the list of valid emails
print("Valid emails: ", valid_emails)

for email in emails:
    if email is None:
        continue
    valid_emails.append(email)
print("Vald emails: ", valid_emails)