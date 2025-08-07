import requests
import json
import io
from ibm_watsonx_orchestrate.agent_builder.tools import tool
import os
from dotenv import load_dotenv
import base64

@tool(description="Translate document using AI Service")
def document_translation_v3(content: str, original_language: str, new_language: str) -> str:
    
    # YOUR API_KEY HERE
    API_KEY = ""

    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', 
                                   data={"apikey": API_KEY, 
                                         "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'},
                                    headers={"Content-Type": "application/x-www-form-urlencoded"})

    
    mltoken = json.loads(token_response.text)["access_token"]

    payload_scoring = {
        "content": content,
        "original_language": original_language,
        "new_language": new_language,
    }

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/aee7525b-8462-4f0f-a6f0-448dd949b8f7/ai_service?version=2021-05-01', json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    
    output = response_scoring.json()

    text = output["translated_text"]

    return text