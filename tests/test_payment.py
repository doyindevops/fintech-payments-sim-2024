import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lambdas')))
import process_payment

def test_successful_payment(monkeypatch):
    # Mock the DynamoDB table put_item method
    class Table:
        def put_item(self, Item):
            return {"ResponseMetadata": {"HTTPStatusCode": 200}}

    monkeypatch.setattr(process_payment, "table", Table())

    event = {
        "body": json.dumps({"amount": 42, "currency": "USD"})
    }
    response = process_payment.lambda_handler(event, None)
    assert response["statusCode"] == 200
    body = json.loads(response["body"])
    assert body["status"] == "success"
    assert "transaction_id" in body
