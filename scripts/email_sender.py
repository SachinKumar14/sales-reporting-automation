import smtplib
from email.message import EmailMessage


def send_email_with_report(sender_email, app_password, receiver_email, file_path):
    """Send the generated Excel sales report via Gmail SMTP."""

    msg = EmailMessage()
    msg["Subject"] = "Automated Sales Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        "Hello,\n\nPlease find attached the latest automated sales report.\n\nRegards,\nSales Automation Bot"
    )

    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = file_path.split("/")[-1]

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=file_name
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Email sent successfully!")

   