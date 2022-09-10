from .BaseRepository import BaseRepository
from src.models.Ticket import Ticket


class Repository(BaseRepository):
    def __init__(self):
        self.model = Ticket
