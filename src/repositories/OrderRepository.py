from .BaseRepository import BaseRepository
from src.models.Order import Order


class Repository(BaseRepository):
    def __init__(self):
        self.model = Order
