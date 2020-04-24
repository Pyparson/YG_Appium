import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

class EmailSender:
    @classmethod
    def send_email(self, smtp_server, username, password, receivers, file, subject="Auto Test Report"):
        result_file_name = file.split("\\")[-1]
        sender = username
        receivers = receivers
        msg_root = MIMEMultipart('related')
        msg_root['Subject'] = subject + str(datetime.now()).split('.')[0]
        msg_root["From"] = sender
        msg_root["To"] = ", ".join(receivers)
        with open(file, "rb") as f:
            content = f.read()
        msg_content_html = MIMEText(content, 'html', 'utf-8')
        msg_attach = MIMEText(content, 'base64', 'utf-8')
        msg_attach["Content-Type"] = 'application/octet-stream'
        msg_attach["Content-Disposition"] = 'attachment; filename=%s' % result_file_name
        msg_root.attach(msg_content_html)
        msg_root.attach(msg_attach)
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(username, password)
        smtp.sendmail(sender, receivers, msg_root.as_string())
        smtp.quit()