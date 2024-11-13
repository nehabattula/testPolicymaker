import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import openai
import os

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = "2023-03-15-preview"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing a request.')
    
    try:
        # retrieve prompt parameter from incoming request
        prompt = req.params.get('prompt')
        if not prompt:
            logging.error("No prompt provided in the request.")
            return func.HttpResponse("Please pass a prompt in the request", status_code=400)

        logging.info(f"Received prompt: {prompt}")

        try:
            # creates connection to blob using connection string 
            blob_service_client = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
            # same name while creating container
            container_name = "policy-documents"
            # file name
            blob_name = "your-policy-document.pdf"  # Replace with your file name
            logging.info(f"Connecting to blob: container={container_name}, blob={blob_name}")

            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            # download content as text
            document_content = blob_client.download_blob().content_as_text()
            logging.info("Successfully fetched document content.")
        except Exception as e:
            logging.error(f"Error accessing Azure Blob Storage: {e}")
            print(f"Error accessing Azure Blob Storage: {e}")
            return func.HttpResponse("Error accessing Azure Blob Storage", status_code=500)

        # Invoke OpenAI API , temperature - randomness of response
        # tokens - words/characters
        try:
            response = openai.Completion.create(
                engine="gpt-35-turbo",
                prompt=f"{document_content}\n\n{prompt}",
                max_tokens=500,
                temperature=0.7
            )
            generated_text = response.choices[0].text.strip()
            logging.info("Successfully generated response from Azure OpenAI.")
        except Exception as e:
            logging.error(f"Error calling Azure OpenAI service: {e}")
            print(f"Error calling Azure OpenAI service: {e}")
            return func.HttpResponse("Error calling Azure OpenAI service", status_code=500)

        return func.HttpResponse(generated_text, status_code=200)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")
        return func.HttpResponse("An unexpected error occurred", status_code=500)
