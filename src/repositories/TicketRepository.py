from .BaseRepository import BaseRepository
from src.models.Ticket import Ticket
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
from src.services.utilities.uploadFile import uploadFile, validateFile

# validation
class TicketSchema(Schema):
    type = fields.String(required=True, validate=validate.Length(min=1, max=255))
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    date = fields.String(required=True, validate=validate.Length(min=1, max=255))
    time_from = fields.String(required=True, validate=validate.Length(min=1, max=255))
    to = fields.String(required=True, validate=validate.Length(min=1, max=255))
    quantity = fields.Integer(
        required=True, validate=validate.Range(min=1, max=10**11 - 1)
    )
    address = fields.String(required=True, validate=validate.Length(min=1, max=255))
    price = fields.Integer(
        required=True, validate=validate.Range(min=1, max=10**20 - 1)
    )
    link_video = fields.String(required=True, validate=validate.Length(min=1, max=255))


class TicketRepository(BaseRepository):
    def __init__(self):
        self.model = Ticket

    def create(self, **kwargs):
        try:
            TicketSchema().load(kwargs, unknown=INCLUDE)
        except ValidationError as err:
            return {"status": False, "errors": err.messages}

        if not kwargs.get("image"):
            return {"status": False, "errors": {"image": ["File is required"]}}
        error = validateFile(kwargs.get("image"), "image", 10000000)
        if error:
            return {"status": False, "errors": {"image": [error]}}

        ticket = self.model()
        ticket.type = "online" if kwargs.get("type") == "online" else "offline"
        ticket.name = kwargs.get("name")
        ticket.price = kwargs.get("price")
        ticket.date = kwargs.get("date")
        ticket.time_from = kwargs.get("time_from")
        ticket.to = kwargs.get("to")
        ticket.quantity = kwargs.get("quantity")
        ticket.address = kwargs.get("address")
        ticket.link_video = kwargs.get("link_video")
        ticket.image = uploadFile(kwargs.get("image"), "/static/uploads/images/")
        ticket.save()
        return {"status": True}

    def update(self, object, **kwargs):
        try:
            TicketSchema().load(kwargs, unknown=INCLUDE)
        except ValidationError as err:
            return {"status": False, "errors": err.messages}

        if kwargs.get("image"):
            error = validateFile(kwargs.get("image"), "image", 10000000)
            if error:
                return {"status": False, "errors": {"image": [error]}}

        ticket = object
        ticket.type = "online" if kwargs.get("type") == "online" else "offline"
        ticket.name = kwargs.get("name")
        ticket.price = kwargs.get("price")
        ticket.date = kwargs.get("date")
        ticket.time_from = kwargs.get("time_from")
        ticket.to = kwargs.get("to")
        ticket.quantity = kwargs.get("quantity")
        ticket.address = kwargs.get("address")
        ticket.link_video = kwargs.get("link_video")
        if kwargs.get("image"):
            ticket.image = uploadFile(kwargs.get("image"), "/static/uploads/images/")
        ticket.save()
        return {"status": True}
