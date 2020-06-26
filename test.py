import boto3

client = boto3.client('translate')
response = client.translate_text(
    Text='hand',
    SourceLanguageCode='en',
    TargetLanguageCode='es'
)

print(response['TranslatedText'])


