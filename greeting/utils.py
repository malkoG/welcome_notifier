from string import Template

from django.conf import settings
from django.forms.models import model_to_dict

import boto3

def send_emails(message_template, user_list):
    ses = boto3.client('ses', region_name='us-east-1')

    for user in user_list:
        info = model_to_dict(user)
        message = Template(message_template).substitute(**info)
        source = 'rijgndqw012@gmail.com'
        destination = {
            'ToAddresses': [ user.email ],
        }
        mail_contents = {
            'Subject': {
                'Data': '코딩워리어가 보낸 편지입니다.',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': message,
                    'Charset': 'UTF-8'
                }
            }
        }
        
        ses.send_email(
            Source=source,
            Destination=destination,
            Message=mail_contents
        )
        
    
def send_messages(message_template, user_list):
    sns = boto3.client('sns')
    
    for user in user_list:
        info = model_to_dict(user)
        message = Template(message_template).substitute(**info)
        print(message)
        sns.publish(
            PhoneNumber=info['phone_number'],
            Message=message
        )
