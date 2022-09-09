from .BaseRepository import BaseRepository
from src.models.SoldTicket import SoldTicket


class SoldTicketRepository(BaseRepository):
    def __init__(self):
        self.model = SoldTicket
