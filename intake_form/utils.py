"""
Utility functions for the project are defined here
"""

class Intake_Form():

    def __init__(self, is_injured, is_insured, liabilities, injuries, story):
        self.injured = is_injured
        self.insured = is_insured
        self.liabilities = liabilities
        self.injuries = injuries
        self.story = story

    def is_injured(self):
        return self.injured
    
    def is_insured(self):
        return self.insured
    
    def get_liabilities(self):
        return self.liabilities
    
    def get_injuries(self):
        return self.injuries
    
    def get_story(self):
        return self.story

    
