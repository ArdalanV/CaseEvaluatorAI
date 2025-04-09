"""
Utility functions for the project are defined here
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date
from classes import case
from classes import law_firm    
from classes.intake_form import Intake_Form, IntakeFormRequest
import requests

#Convert the types for the prompt
def convert_type(val):
    assert type(val) != str, 'Must pass in a nonstring of type either: bool, date, int, NoneType'
    #Check if the val is a bool
    if isinstance(val, bool):
        return "Yes" if val else "No"
    #Check if the val is a date
    if isinstance(val, date):
        return f"{val.month}/{val.day}/{val.month}"
    #Check the val is an int
    if isinstance(val, int):
        return str(val)
    #Otherwise it's a NoneType
    return 'N/A'

def make_intake_form(form: IntakeFormRequest):
    """
    A function for processing the intake form that the user filled out on the 
    web application

    Parameters:
        form (IntakeFormRequest): The form that needs to be converted to intake form object
    
    Returns:
        intake (Intake_Form): Returns an intake form
    """
    intake_form = Intake_Form(**form.model_dump())
    return intake_form

#Loads desired prompt from prompts directory
def load_prompt(prompt: str):
    """
    Reads a prompt file from the prompts directory.

    Parameters:
        prompt : name of the .txt file to be used as a prompt from prompts directory

    Returns:
        str : the desired prompt to be used for the LLM call
    """
    #try reading the desired prompt
    try:
        with open(f"prompts/{prompt}.txt", "r", encoding="utf-8") as file:
            return file.read()
    #otherwise return False and kill the program
    except FileNotFoundError:
        print("Prompt was not found, please use valid prompt")

#Formats prompt
def format_prompt(intake_form: Intake_Form, prompt_template: str):
    #Put prompt variables in correct type
    prompt = prompt_template.format(
        accident_type = intake_form.get_accident_type(),
        num_involved_people = convert_type(intake_form.get_num_involved_people()),
        is_injured = convert_type(intake_form.get_is_injured()),
        injury_types = intake_form.get_injury_types(),
        sought_medical_care = convert_type(intake_form.get_sought_medical_care()),
        filed_police_report = convert_type(intake_form.get_filed_police_report()),
        is_insured = convert_type(intake_form.get_is_insured()),
        insurance_coverage = intake_form.get_insurance_coverage(),
        has_witnesses = convert_type(intake_form.has_witnesses()),
        incident_date = convert_type(intake_form.get_incident_date()),
        has_affordability_concerns = convert_type(intake_form.has_affordability_concerns()),  
        city = intake_form.get_city(),
        state = intake_form.get_state(),
        incident_description = intake_form.get_incident_description(),
        medical_costs = intake_form.get_medical_costs()
        )
    return prompt

#Makes the local LLM call 
def summarize_intake_with_LLM(prompt: str):
    """
    Makes an LLM call to summarize the intake form to be ready to email.

    Parameters:
        prompt (str): Formatted prompt being used from prompts directory

    Returns:
        (str) : The LLM summarized case intake form
    """
    try: 
        response = requests.post( "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False,
                "temperature": 0
            })
        return response.json(["response"])
    except Exception as e:
        print(f"Request Error from Local Llama model: {e}")

#Gets the firm that the case will be send to
def match_case_with_firm(case: case.Case):
    """
    Function to match a case object with a law firm
    
    Parameters:
        case (Case): case object defined in utils to be matched with law firm

    Returns:
        firm (LawFirm): firm object that will get the case referral
    """
    return 
    