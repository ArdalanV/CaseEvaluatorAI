"""
Main script for running preproccessing and matching of the case
"""
import utils

def process_intake_form(form: utils.IntakeFormRequest):
    """
    A function for processing the intake form that the user filled out on the 
    web application

    Parameters:
        form (IntakeFormRequest): The form that needs to be converted to intake form object
    
    Returns:
        intake (Intake_Form): Returns an intake form
    """
    intake = utils.Intake_Form(**form.model_dump())
    return intake



    