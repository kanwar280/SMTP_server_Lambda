import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json

def lambda_handler(event, context):
    body = event['detailedMessage']
    text_message = str(body.get('text', 'No message provided'))
    message = Mail(
        from_email='skyops.team6@gmail.com',
        to_emails='skyops.team6@gmail.com',
        subject='Build Completed',
        html_content='<strong>Build Completed on Azure Devops.</strong>'+ text_message
    )
    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        message.add_cc('kanwarpreetsingh@loyalistcollege.com')
        message.add_cc('sachinkumar4@loyalistcollege.com')
        print(message)
        response = sg.send(message)
        return {
            'statusCode': 200,
            'body': 'Email sent successfully!'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Failed to send email: {str(e)}'
        }
