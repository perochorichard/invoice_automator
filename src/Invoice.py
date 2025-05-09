from dataclasses import dataclass

@dataclass
class Invoice:
    vendor_name:str
    id: str
    quantity: str
    total: str
    invoice_date: str
    due_date: str