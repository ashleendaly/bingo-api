
import random
from typing import List

from src.models.incident import Incident


def generateBingoCard(incidentList: List[Incident], numIncidents: int):
    n = len(incidentList)
    return random.choices(incidentList, k=numIncidents)
