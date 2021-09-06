from pydantic import BaseModel

class DocFile(BaseModel):
    supplier_name: str
    supplier_details: str
    receiver_name:str
    receiver_details: str
    tax_rate: str
    tva_amount: str
    invoice_number: str
    invoice_date: str
    total_ht: str
    total: str
    product_designation: str
