"""
Utility functions for the project are defined here
"""

class IntakeForm:

    def __init__(self, name, email, phone, accident_type, involved_people, injured,
                 injury_types, sought_medical_care, filed_police_report,
                 insured, witnesses, incident_date,
                 incident_description, affordability_concerns, location, medical_costs):

        self.name = name
        self.email = email
        self.phone = phone
        self.accident_type = accident_type
        self.involved_people = involved_people
        self.injured = injured
        self.injury_types = injury_types
        self.sought_medical_care = sought_medical_care
        self.filed_police_report = filed_police_report
        self.insured = insured
        self.witnesses = witnesses
        self.incident_date = incident_date
        self.incident_description = incident_description
        self.affordability_concerns = affordability_concerns
        self.location = location
        self.medical_costs = medical_costs

    @property
    def get_name(self):
        return self.name

    @property
    def get_email(self):
        return self.email
    
    @property
    def get_phone(self):
        return self.phone
    
    @property
    def get_accident_type(self):
        return self.accident_type
    
    @property
    def get_involved_people(self):
        return self.involved_people
    
    @property
    def is_injured(self):
        return self.injured
    
    @property
    def get_injury_types(self):
        return self.injury_types

    @property
    def has_sought_medical_care(self):
        return self.sought_medical_care

    @property
    def has_filed_police_report(self):
        return self.filed_police_report

    @property
    def is_insured(self):
        return self.insured

    @property
    def has_witnesses(self):
        return self.witnesses

    @property
    def get_incident_date(self):
        return self.incident_date

    @property
    def get_incident_description(self):
        return self.incident_description

    @property
    def has_affordability_concerns(self):
        return self.affordability_concerns

    @property
    def get_location(self):
        return self.location

    @property
    def get_medical_costs(self):
        return self.medical_costs

