from .BaseRepository import BaseRepository
from src.models.SoldTicket import SoldTicket


class Repository(BaseRepository):
    def __init__(self):
        self.model = SoldTicket
