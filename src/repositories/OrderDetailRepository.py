from .BaseRepository import BaseRepository
from src.models.OrderDetail import OrderDetail


class Repository(BaseRepository):
    def __init__(self):
        self.model = OrderDetail
