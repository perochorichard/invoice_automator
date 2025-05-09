import base64
from test import greet
import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

# sample document
filepath = r"C:\Users\ricc\Desktop\Python Test Files\Report 2\C20002323-I201844624.pdf"
def main():
    load_dotenv()
    endpoint = os.getenv("AZURE_ENDPOINT")
    key = os.getenv("AZURE_API_KEY")
    client  = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    with open(filepath, "rb") as f:
        data = f.read()

    #poller = client.begin_analyze_document("prebuilt-invoice", AnalyzeDocumentRequest(bytes_source=data))
    
    poller = client.begin_analyze_document("prebuilt-invoice", AnalyzeDocumentRequest(url_source=formUrl))
    invoices = poller.result()

    for idx, invoice in enumerate(invoices.documents):
        # vendor number.invoice number.item description.quantity.amount.invoice date.record date.batch number.
        print("--------Recognizing invoice #{}--------".format(idx + 1))
        invoice_id = invoice.fields.get("InvoiceId")
        if invoice_id:
            print(
                f"Invoice Id: {invoice_id.value_string} has confidence: {invoice_id.confidence}"
            )
        invoice_total = invoice.fields.get("InvoiceTotal")
        if invoice_total:
            print(
                f"Invoice total: {invoice_total.value_currency.amount} {invoice_total.value_currency.currency_code} has confidence: {invoice_total.confidence}"
            )
        print("----------------------------------------")

if __name__ == "__main__":
    main()