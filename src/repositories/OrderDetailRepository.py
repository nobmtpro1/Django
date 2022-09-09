from .BaseRepository import BaseRepository
from src.models.OrderDetail import OrderDetail


class OrderDetailRepository(BaseRepository):
    def __init__(self):
        self.model = OrderDetail
