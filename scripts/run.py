"""
Main script for running preproccessing and matching of the case
"""
import utils

def process_intake_form(intake_form: utils.Intake_Form):
    """
    Main function for processing the form. Uses LLM to take form, put it into a
    summarized description of the case. Create case object, and then start the matching
    """
    processed_intake_form = intake_form
    return processed_intake_form

def match_case_with_firm(case: utils.Case):
    """
    Function to match a case object with a law firm
    
    Parameters:
        case (Case): case object defined in utils to be matched with law firm

    Returns:
        firm (Firm): firm object that will get the case referral
    """
    return 



    