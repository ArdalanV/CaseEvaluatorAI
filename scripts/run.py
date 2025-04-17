"""
Main script for running preproccessing and matching of the case
"""
from scripts import utils
import json 
from scripts.classes.intake_form import Intake_Form

#Simluated Law Firms Database
with open(f"data/firms.json") as f:
    firms = json.load(f)

#Where the program gets systematically executed
def first_phase(intake_form: Intake_Form):
    """
    Main function for processing the form. Uses LLM to take form, put it into a
    summarized description of the case. Create case object, and then start the matching
    """
    #Load prompt in
    prompt_template = utils.load_prompt("prompt1")
    #Format prompt
    prompt = utils.format_prompt(intake_form, prompt_template)
    #Give Ollama the required data and prompt for it's output
    #response = utils.summarize_intake_with_LLM(prompt) 
    response = "Filler email for testing email functionality"
    #Creates a new case object
    new_case = utils.make_case(intake_form.get_first_name(),
                               intake_form.get_last_name(),
                               intake_form.get_email(),
                               intake_form.get_phone(),
                               response)
    #Get the Law Firm we matched with the case
    matched_firm = utils.match_case_with_firm(new_case)
    sender_email = "ardalanv4@gmail.com"
    app_password = "to_be_put_in"
    utils.send_email(new_case, matched_firm, sender_email, app_password)
    return "Check email"