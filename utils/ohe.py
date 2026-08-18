from sklearn.preprocessing import OneHotEncoder

class ListOfData:
    def __init__(self):
        pass

    def ohe(self, col):
        pass

    def intent_list(self):
        self.intent_col = ['application_help', 'complaint', 'document_help', 'escalation',
       'follow_up', 'information_request', 'status_query']

        return self.intent_col

    def category_list(self):
        self.category_col =['certificates', 'drainage', 'electricity', 'public_health',
               'roads', 'sanitation', 'street_lighting', 'transport',
               'water_supply', 'welfare']
        
        return self.category_col



    def deparment_list(self):
        self.deparment_col = ['Drainage Department', 'Electricity Department',
       'Public Health Department', 'Revenue Department',
       'Roads Department', 'Sanitation Department',
       'Transport Department', 'Water Supply Department',
       'Welfare Department']
        
        return self.deparment_col

    def urgency_list(self):
        self.urgency_col = ['high', 'low', 'medium']
        
        return self.urgency_col

    def severity_list(self):
        self.severity = ['authority_issue', 'health_hazard', 'health_issue', 'health_risk',
       'information', 'information_query', 'public_hazard',
       'service_delay', 'service_failure', 'service_issue',
       'service_request', 'status']

        return self.severity

    

    