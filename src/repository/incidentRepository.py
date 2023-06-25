from src.models.incident import Incident


class InMemoryIncidentRepository:

    def __init__(self):
        self.incidents = {}

    def addIncident(self, incident: Incident):
        self.incidents[incident.id] = incident

    def removeIncident(self, incident: Incident):
        del self.incidents[incident.id]

    def incidentOccured(self, incident: Incident):
        self.incidents[incident.id].count += 1

    def getIncidents(self):
        return self.incidents.values()


class DatabaseIncidentRepository:

    def __init__(self, db_url: str):
        # Initialize database connection
        pass

    def addIncident(self, incident: Incident):
        pass

    def removeIncident(self, incident: Incident):
        pass

    def incidentOccured(self, incident: Incident):
        pass
