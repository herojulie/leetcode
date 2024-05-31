import base64
import boto3
import json
import smtplib
from datetime import datetime, timezone
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http import HTTPStatus


smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
smtp_port = 587  # Replace with the appropriate SMTP port (587 for TLS, 465 for SSL)
smtp_username = 'jyqueenofcatan@gmail.com'
smtp_password = 'fqsnbprlyghadtoh'  # 'NeverHaveIEverWon'
# sender_email = 'jyqueenofcatan@gmail.com'
sender_email, receiver_email = 'herojulie@gmail.com', 'jyqueenofcatan@gmail.com'


def send(email_message) -> (bool, str):
    # set up email and server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption (remove this line if using SSL)
        server.login(smtp_username, smtp_password)
        text = email_message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        return True, 'OK'
    except Exception as e:
        return False, f"An error occurred:, {str(e)}"
    finally:
        server.quit()


def create_image_filename(campaign_name: str) -> str:
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%Z')
    return f'{campaign_name}_{current_time}.jpeg'


def invalid_keys(params: dict[str, str]) -> list:
    return [key for key, value in params.items() if len(str(value)) == 0]


def create_email_message(params):
    image_file_name = create_image_filename(params['campaignName'])
    image_file_path = f"/tmp/{image_file_name}"
    with open(image_file_path, "wb") as file:
        file.write(base64.b64decode(params['base64Image']))

    # create email message
    # Create a message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = f"[LinkNYC] Update: Link Local Plus: " \
                         f"A ${params['price']} + personalized template campaign " \
                         f"<{params['campaignName']}>"

    # Add the email body as plain text or HTML
    email_body = f"Name: {params['customerName']}\n" \
                 f"Requested campaign start date: {params['startDate']}"
    message.attach(MIMEText(email_body, 'plain'))

    # Attach the JPEG file
    img_file = open(image_file_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(img_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{image_file_path}"')
    message.attach(part)

    return message


def lambda_handler(event, context):
    event_body = json.loads(event.get("body"))
    params = {
        "customerName": event_body.get("customerName"),
        "campaignName": event_body.get("campaignName"),
        "price": event_body.get("price"),
        "startDate": event_body.get("startDate"),
        "location": event_body.get("location"),
        "base64Image": event_body.get("base64Image")
    }

    invalid_keys_list = invalid_keys(params)
    if invalid_keys_list:
        return Response(HTTPStatus.BAD_REQUEST, False).send_error_response(f"NOK. Empty params: [{', '.join(invalid_keys_list)}]")

    try:
        ses_client = boto3.client('ses')

        email_message = create_email_message(params)
        response = ses_client.send_raw_email(
            RawMessage={
                'Data': email_message.as_string(),
            },
            # ConfigurationSetName=f"welcome-email-config-set-{get_env('ENVIRONMENT_NAME')}",
            # Tags=[{'Name': 'type', 'Value': 'welcome-email'}],
        )

        if is_ok(response):
            return Response(HTTPStatus.OK, True).send_body_response({"message": "OK"})

        return Response(HTTPStatus.INTERNAL_SERVER_ERROR, False).send_error_response(get_error_code(response))
    except Exception as e:
        return Response(HTTPStatus.INTERNAL_SERVER_ERROR, False).send_error_response(str(e))


def is_ok(res) -> bool:
    try:
        return True if res['ResponseMetadata']['HTTPStatusCode'] == HTTPStatus.OK else False
    except Exception:
        return False


def get_error_code(res) -> str:
    try:
        return res['Error']['Code']
    except Exception:
        return 'Error Code Not Found'


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


if __name__ == '__main__':
    from sample_params import my_params
    # file_path = '/Users/julieyang/Downloads/test-download.jpeg'  # Replace with the actual file path
    # attachment_image = open(file_path, "rb")
    # base64Image = attachment_image.read()
    my_event = {
        "body": json.dumps(my_params)
    }

    lambda_handler(my_event, {})
