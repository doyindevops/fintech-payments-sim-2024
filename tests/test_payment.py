import json
import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lambdas')))
import process_payment

def test_successful_payment(monkeypatch):
    # Fake DynamoDB Table and resource
    class FakeTable:
        def put_item(self, Item):
            return {"ResponseMetadata": {"HTTPStatusCode": 200}}
    class FakeDynamoResource:
        def Table(self, name):
            return FakeTable()
    # Patch boto3.resource to return our fake resource
    monkeypatch.setattr(process_payment, "boto3", __import__('boto3'))
    monkeypatch.setattr(process_payment.boto3, "resource", lambda service: FakeDynamoResource())
    # Set the environment variable expected by the handler
    monkeypatch.setenv("TRANSACTIONS_TABLE", "transactions")
    # Prepare and send the fake event
    event = {"body": json.dumps({"amount": 42, "currency": "USD"})}
    response = process_payment.lambda_handler(event, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["status"] == "success"
    assert "transaction_id" in body
