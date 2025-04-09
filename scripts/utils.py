"""
Utility functions for the project are defined here
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date
from classes.case import Case
from classes.law_firm import Law_Firm  
from classes.intake_form import Intake_Form, IntakeFormRequest
import smtplib
from email.message import EmailMessage
import requests

#Convert the types for the prompt
def convert_type(val):
    """
    Helper function for converting the Intake Form instance attributes for the prompt.

    Parameters:
        val: Intake Form instance attribute to be converted

    Returns:
        Some converted parameter
    """
    assert type(val) != str, 'Must pass in a nonstring of type either: bool, date, int, NoneType'
    #Check if the val is a bool
    if isinstance(val, bool):
        return "Yes" if val else "No"
    #Check if the val is a date
    if isinstance(val, date):
        return f"{val.month}/{val.day}/{val.year}"
    #Check the val is an int
    if isinstance(val, int):
        return str(val)
    #Otherwise it's a NoneType
    return 'N/A'

def make_case(first_name: str, last_name: str, email: str, phone_num: str, case_description: str) -> Case:
    """
    Helper function that makes case instance for more readable code

    Parameters:
        first_name (str): First name of claimant
        last_name (str): Last name of claimant
        email (str): Email of the claimant
        phone_num (str): Phone number of the claimant
        case_description (str): LLM summarized summary of the Intake Form

    Returns:
        (Case) : New Case instance to be used in the program or stored to database
    """
    return Case(first_name, last_name, email, phone_num, case_description)

def make_intake_form(form: IntakeFormRequest) -> Intake_Form:
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
def load_prompt(prompt: str) -> str:
    """
    Reads a prompt file from the text_files directory.

    Parameters:
        prompt (str): name of the .txt file to be used as a prompt from prompts directory

    Returns:
        str : the desired prompt to be used for the LLM call
    """
    #try reading the desired prompt
    try:
        with open(f"../text_files/{prompt}.txt", "r", encoding="utf-8") as file:
            return file.read()
    #otherwise return False and kill the program
    except FileNotFoundError:
        print("Prompt was not found, please use valid prompt")

#Loads email
def load_email() -> str:
    """
    Reads an email file from the text_files directory

    Parameters:
        None
    
    Returns:
        (str) of the email template
     """
    try:
        with open(f"../text_files/email.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Email not found, please get a valid email file")

#Formats prompt
def format_prompt(intake_form: Intake_Form, prompt_template: str):
    """
    Helper function for proper prompt formatting.

    Parameters:
        intake_form (Intake_Form): Intake form instance to fill the prompt template
        prompt_tempalate (str): Prompt template to be used from text_files directory

    Returns:
        str: Correctly formatted prompt ready to query LLM
    """
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

#Gets the firm that the case will be send to
def match_case_with_firm(case: Case):
    """
    Function to match a case object with a law firm
    
    Parameters:
        case (Case): case object defined in utils to be matched with law firm

    Returns:
        firm (LawFirm): firm object that will get the case referral
    """
    return 

#Makes the local LLM call 
def summarize_intake_with_LLM(prompt: str) -> str:
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
        return response.json()(["response"])
    except Exception as e:
        print(f"Request Error from Local Llama model: {e}")

def create_email_body(case: Case, firm: Law_Firm) -> str:
    """
    Helper function for creating the body of the email to be sent to law firm
    to notify of case lead.

    Parameters:
        case (Case): Case instance of the newly generated case to be referred
        firm (Law_Firm): Law_Firm instance of the firm that was chosen to be referred

    Returns:
        str: A string with the proper email body to be sent out
    """
    email_template = load_email()
    email_body = email_template.format(
        firm_name = firm.get_firm_name(),
        first_name = case.get_first_name(),
        last_name = case.get_last_name(),
        case_description = case.get_case_description(),
    )        
    return email_body

def send_email(case: Case, law_firm: Law_Firm, from_email: str, app_password):
    """
    Send an email using Gmail SMTP server with an App Password.

    Parameters:
        subject (str): Subject of the email
        body (str): Body of the email (plain text)
        to_email (str): Recipient's email address
        from_email (str): Sender's Gmail address
        app_password (str): App password (not your Gmail login password)

    Returns:
        (None)
    """
    email_body = create_email_body(case, law_firm)
    msg = EmailMessage()
    msg['Subject'] = "URGENT: Potential New Case"
    #This would be some ScaleLegal email
    msg['From'] = from_email
    msg['To'] = law_firm.get_email()
    msg.set_content(email_body)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("ardala", app_password)
            smtp.send_message(msg)
            print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
    