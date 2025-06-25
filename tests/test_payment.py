import json
import sys
import os
import types

# Ensure we can import process_payment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lambdas')))
import process_payment

def test_successful_payment(monkeypatch):
    # Mock table object
    class FakeTable:
        def put_item(self, Item):
            return {"ResponseMetadata": {"HTTPStatusCode": 200}}

    # Patch process_payment.table to be a FakeTable instance
    monkeypatch.setattr(process_payment, "table", FakeTable())

    # Prepare test event
    event = {"body": json.dumps({"amount": 42, "currency": "USD"})}
    response = process_payment.lambda_handler(event, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["status"] == "success"
    assert "transaction_id" in body
