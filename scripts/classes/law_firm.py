from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

#Law Firm object (many more fields to be added later)
class LawFirm():

    def __init__(self, email: str, firm_name: str, location: str, size: str):
        self.email = email
        self.firm_name = firm_name
        self.location = location
        self.size = size

    def get_firm_name(self):
        return self.firm_name
    
    def get_self_location(self):
        return self.location
    
    def get_size(self):
        return self.size