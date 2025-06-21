def unique_email(emails):
    unique = set()
    for email in emails:
        local,domain = email.split('@')
        local= local.split('+')[0].replace('.', '')
        unique.add(local+ '@' + domain)
    return len(unique)



emails = ["test.email+alex@domain.com", "test.email@domain.com", "test+filter@domain.com"]
print(f"unique emails: {unique_email(emails)}")