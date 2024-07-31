import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import json

endpoint = os.getenv("ENDPOINT_URL", "https://devansh.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "devanshchatbot")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://devansh2266.search.windows.net")
search_key = os.getenv("SEARCH_KEY", "YuyRwnoH9DSAsMGlRf2efIxdwHvfZ6PuB3DjH7Y1tjAzSeBNTDRk")
search_index = os.getenv("SEARCH_INDEX_NAME", "devansh2266")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default")
      
client = AzureOpenAI(
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
    api_version="2024-05-01-preview",
)
      


def get_Chat_response(Query):
    completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
      "role": "user",
      "content": Query+'. dont include the references from documents, dont include document names'
    }],
    max_tokens=800,
    temperature=0,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False,
    extra_body={
      "data_sources": [{
          "type": "azure_search",
          "parameters": {
            "endpoint": f"{search_endpoint}",
            "index_name": "devansh2266",
            "semantic_configuration": "default",
            "query_type": "simple",
            "fields_mapping": {},
            "in_scope": True,
            "role_information": "You are a customer care chatbot for Bank of Baroda customer care. Respond accordingly. Make it precise under 50 words.",
            "filter": None,
            "strictness": 3,
            "top_n_documents": 5,
            "authentication": {
              "type": "api_key",
              "key": f"{search_key}"
            }
          }
        }]
      }
    )
    newjson=completion.to_json()
    data=json.loads(newjson)
    newdata=data["choices"][0]["message"]["content"]
    newstr=str(newdata)
    newstr.replace('[doc1]','')
    return newstr

