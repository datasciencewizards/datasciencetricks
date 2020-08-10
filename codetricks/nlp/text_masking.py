# !pip install clean-text[gpl]

import cleantext

# replacing urls 
text = "www.stackoverflow.com is an amzing website"
cleantext.replace_urls(text, "<URL>")
>>>'<URL> is an amzing website'

# replacing emails
text = "My email id is username@example.com"
cleantext.replace_emails(text, "<EMAIL>")
>>>'My email id is <EMAIL>'
