import boto3

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

def get_sqs_message(sqs_url):
    url = sqs_url

    try:
        response = sqs.receive_message(
            QueueUrl=url,
        )

    except Exception as e:
        print('=====Error=====')
        print('get_sqs_message')
        print('ERROR:' + str(e))
        print('===============')
        return None

    return response

sqsUrl = "https://sqs.ap-northeast-1.amazonaws.com/921224632704/python-celery"
sqs = boto3.client('sqs')

queMessage = get_sqs_message(sqsUrl)
f = queMessage['Messages']
print(f)
m = queMessage['Messages']
print(m[0]['Body'])