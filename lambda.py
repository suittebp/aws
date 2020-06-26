import json
import boto3

client = boto3.client('translate')
response = client.translate_text(
    Text='hand',
    SourceLanguageCode='en',
    TargetLanguageCode='es'
)

suitte = response['TranslatedText']

def lambda_handler(event, context):
    # TODO implement
    return suitte
    
