import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class AWSSender:

    s = smtplib.SMTP()

    s.connect('', 587)

    s.starttls()

    s.login('', '')

    def quit(self):
        s.quit()

    def send(self, email, me):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Hello World!"
        msg['From'] = me
        msg['To'] = email

        # Create the body of the message (a plain-text and an HTML version).
        text = "Email send using a template!"
        html = open('template.html', 'r').read()

        html = html.replace('{{ content }}', text)

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        #msg = 'From: no-reply@howcode.org\nTo: francis@howcode.org\nSubject: Test email\n\nThis is a test email sent using Python!'

        self.s.sendmail(me, email, msg.as_string())
        print("Sent email to " + email, end="")

emaillist = open('list.txt', 'r').readlines()

aws = AWSSender()

for email in emaillist:
    aws.send(email, "no-reply@howcode.org")
