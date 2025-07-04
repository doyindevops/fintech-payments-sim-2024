import json
import os
import boto3
import uuid
from datetime import datetime



def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TRANSACTIONS_TABLE'])
    # ...rest of your code

    try:
        body = json.loads(event['body'])
        transaction_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        item = {
            'transaction_id': transaction_id,
            'amount': body['amount'],
            'currency': body.get('currency', 'USD'),
            'timestamp': now,
            'status': 'processed'
        }
        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'transaction_id': transaction_id, 'status': 'success'})
        }
    except Exception as e:
        import traceback
        print("Lambda error:", repr(e))
        traceback.print_exc()
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
