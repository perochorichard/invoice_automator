import os
from InvoiceAnalyzer import InvoiceAnalyzer
from dotenv import load_dotenv
from pathlib import Path

def main():
    file_paths = []
    folder_path = Path("sample_invoices")
    for file_path in folder_path.iterdir():
        if file_path.is_file():
            print(f"###Adding {file_path}###")
            file_paths.append(file_path)

    load_dotenv()
    analyzer = InvoiceAnalyzer(
        endpoint=os.getenv("AZURE_ENDPOINT"), 
        key=os.getenv("AZURE_API_KEY")
        )
    
    analyzer.analyze(file_paths)

if __name__ == "__main__":
    main()