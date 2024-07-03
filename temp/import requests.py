import requests
from datetime import datetime
import json

url = "https://apisetu.gov.in/certificate/v3/cisce/sscer"

payload = {
    "txnId": "f7f1469c-29b0-4325-9dfc-c567200a70f7",
    "format": "pdf",
    "certificateParameters": {
        "CUID": "6374638",
        "YOE": "2016",
        "IDXN": "1234567/001",
        "UID": "123412341234",
        "FullName": "Sunil Kumar",
        "DOB": "31-12-1980"
    },
    "consentArtifact": {
        "consent": {
            "consentId": "ea9c43aa-7f5a-4bf3-a0be-e1caa24737ba",
            "timestamp": datetime.now().isoformat(),
            "dataConsumer": {"id": "string"},
            "dataProvider": {"id": "string"},
            "purpose": {"description": "string"},
            "user": {
                "idType": "string",
                "idNumber": "string",
                "mobile": "string",
                "email": "string"
            },
            "data": {"id": "string"},
            "permission": {
                "access": "string",
                "dateRange": {
                    "from": "2019-08-24T14:15:22Z",
                    "to": "2019-08-24T14:15:22Z"
                },
                "frequency": {
                    "unit": "string",
                    "value": 0,
                    "repeats": 0
                }
            }
        },
        "signature": {"signature": "string"}
    }
}
headers = {
    "X-APISETU-CLIENTID": "WamuWamnu",
    "content-type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)