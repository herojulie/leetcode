import base64
import json
import smtplib
from datetime import datetime, timezone
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send(image_file_name, campaign_name: str):
    # set up email and server
    smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate SMTP port (587 for TLS, 465 for SSL)
    smtp_username = 'jyqueenofcatan@gmail.com'
    smtp_password = 'fqsnbprlyghadtoh'  # 'NeverHaveIEverWon'
    sender_email = 'jyqueenofcatan@gmail.com'
    receiver_email = 'herojulie@gmail.com'

    # create email message
    # Create a message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = f'[LinkNYC] Update: Link Local Plus: A $100 + personalized template campaign <{campaign_name}>'

    # Add the email body as plain text or HTML
    email_body = "This is the email body."
    message.attach(MIMEText(email_body, 'plain'))

    # Attach the JPEG file
    img_file = open(f"/tmp/{image_file_name}", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(img_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="/tmp/{image_file_name}"')
    message.attach(part)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption (remove this line if using SSL)
        server.login(smtp_username, smtp_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred:', str(e))
    finally:
        server.quit()


def lambda_handler(event, context):
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%Z')

    event_body = json.loads(event.get("body"))
    name = event_body.get("campaignName", "TEMP_CAMPAIGN_NAME")
    image = event_body.get("base64Image")

    image_file_name = f'{name}_{current_time}.jpeg'

    try:
        if not name or not image:
            return Response(400, False).send_error_response('NOK. Name or base64Image is empty')

        with open(f"/tmp/{image_file_name}", "wb") as file:
            file.write(base64.b64decode(image))

        send(image_file_name, name)
        return Response(200, True).send_body_response({"message": "OK"})

    except Exception as e:
        return Response(500, False).send_error_response(str(e))


class Response:
    def __init__(self, status_code: int, status: bool):
        self.status_code = status_code
        self.status = status

    def send_error_response(self, error_message):
        return {
            'headers': {'Access-Control-Allow-Origin': '*'},
            'statusCode': self.status_code,
            'body': json.dumps({
                "ok": self.status,
                "message": error_message
            })
        }

    def send_body_response(self, body):
        return {
            'headers': {'Access-Control-Allow-Origin': '*'},
            'statusCode': self.status_code,
            'body': json.dumps(body)
        }
