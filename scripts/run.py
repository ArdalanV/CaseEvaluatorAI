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


def process_intake_form(intake_form: utils.Intake_Form):
    """
    Main function for processing the form. Uses LLM to take form, put it into a
    summarized description of the case. Create case object, and then start the matching
    """
    #Load prompt in
    prompt_template = load_prompt("prompt1")
    prompt = prompt_template.format(
        accident_type = intake_form.get_accident_type()
        involved_people = involved_people
        injured = injured
        injury_types = injury_types
        sought_medical_care = sought_medical_care
        filed_police_report = filed_police_report
        insured = insured
        witnesses = witnesses
        incident_date = incident_date
        incident_description = incident_description
        affordability_concerns = affordability_concerns
        location = location
        medical_costs = medical_costs
        )
    #Give Ollama the required data and prompt for it's output
    response = requests.post( "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
            "temperature": 0
        })
    return 


#Makes the local LLM call 
def summarize_intake_with_LLM(prompt: str, intake_form: utils.Intake_Form):
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



    