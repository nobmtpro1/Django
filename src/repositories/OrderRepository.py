from .BaseRepository import BaseRepository
from src.models.Order import Order


class OrderRepository(BaseRepository):
    def __init__(self):
        self.model = Order
