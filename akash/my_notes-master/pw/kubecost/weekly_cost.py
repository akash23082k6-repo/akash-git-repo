import os.path
import boto3
import email
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import date

def send_email_with_attachment():
    current_date= date.today()
    SENDER = "nandini.bhatt@pw.live"
    RECIPIENT = ["gaurav.yadav1@pw.live", "manan.verma@pw.live", "ashutosh.yadav_consultant@pw.live", "mrituyanjay.sinha_consultant@pw.live"]
    AWS_REGION = "ap-south-1"
    SUBJECT = f"Weekly Kubecost Report {current_date}"
    TMP_FILE_NAME = '/tmp/report.csv'
    
    # Prepare the email message
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = ", ".join(RECIPIENT)
    
    # Add the body text
    BODY_TEXT = f"Hi \nPlease find the Kubecost report     \n\n\nThanks & regards \n {current_date}"
    textpart = MIMEText(BODY_TEXT)
    msg.attach(textpart)
    
    # Add the attachment
    ATTACHMENT = TMP_FILE_NAME
    att = MIMEApplication(open(ATTACHMENT, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=ATTACHMENT)
    msg.attach(att)
    
    # Send the email using Amazon SES
    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_raw_email(
            Source=SENDER,
            Destinations=RECIPIENT,
            RawMessage={'Data': msg.as_string()}
        )
        print("Email sent! Message ID:", response['MessageId'])
    except ClientError as e:
        print("Error occurred while sending email:", e.response['Error']['Message'])

# Call the function
send_email_with_attachment()
