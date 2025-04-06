"""
Main script for running preproccessing and matching of the case
"""
import utils
import os
import openai
import requests

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
def format_prompt(intake_form: utils.Intake_Form, prompt_template: str):
    prompt = prompt_template.format(
        accident_type = intake_form.get_accident_type(),
        involved_people = intake_form.get_involved_people(),
        injured = intake_form.is_injured(),
        injury_types = intake_form.get_injury_types(),
        sought_medical_care = intake_form.has_sought_medical_care(),
        filed_police_report = intake_form.has_filed_police_report(),
        insured = intake_form.is_insured(),
        witnesses = intake_form.has_witnesses(),
        incident_date = intake_form.get_incident_date(),
        affordability_costs = intake_form.has_affordability_concerns(),
        city = intake_form.get_city(),
        state = intake_form.get_state(),
        country = intake_form.get_medical_costs(),
        incident_description = intake_form.get_incident_description()
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

def match_case_with_firm(case: utils.Case):
    """
    Function to match a case object with a law firm
    
    Parameters:
        case (Case): case object defined in utils to be matched with law firm

    Returns:
        firm (LawFirm): firm object that will get the case referral
    """
    return 


def run(intake_form: utils.Intake_Form):
    """
    Main function for processing the form. Uses LLM to take form, put it into a
    summarized description of the case. Create case object, and then start the matching
    """
    #Load prompt in
    prompt_template = load_prompt("prompt1")
    #Format prompt
    prompt = format_prompt(intake_form, prompt_template)
    #Give Ollama the required data and prompt for it's output
    response = summarize_intake_with_LLM(prompt)
    #Creates a new case object
    new_case = utils.Case(intake_form.get_first_name(),
                          intake_form.get_last_name(),
                          intake_form.get_email(),
                          intake_form.get_phone(),
                          response)
    
    
    
    


    