"""
Script for a modular defintion of a Law Firm class
"""

from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

#Law Firm object (many more fields to be added later)
class Law_Firm():

    def __init__(self, firm_name: str, email: str, location: str, size: str):
        self.firm_name = firm_name
        self.email = email
        self.location = location
        self.size = size

    def get_firm_name(self):
        return self.firm_name
    
    def get_email(self):
        return self.email
    
    def get_self_location(self):
        return self.location
    
    def get_size(self):
        return self.size