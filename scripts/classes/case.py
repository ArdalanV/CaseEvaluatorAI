from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

#Case object (many fields to be added or changed)
class Case():

    def __init__(self, first_name: str, last_name: str, email: str, phone_num: str,
                  case_description: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_num = phone_num
        self.case_description = case_description

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_phone_num(self):
        return self.phone_num
    
    def get_case_description(self):
        return self.case_description