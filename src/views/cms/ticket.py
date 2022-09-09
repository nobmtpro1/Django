from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import render
from src.repositories.TicketRepository import TicketRepository
from ...models import Ticket
from django.contrib.auth.decorators import permission_required


@permission_required("src.view_ticket")
def index(request):
    tickets = Ticket.objects.order_by("-id")
    return render(request, "cms/pages/ticket/index.html", {"tickets": tickets})


@permission_required("src.add_ticket")
def create(request):
    if request.method == "POST":
        ticketRepository = TicketRepository()
        result = ticketRepository.create(
            type=request.POST.get("type"),
            name=request.POST.get("name"),
            price=request.POST.get("price"),
            date=request.POST.get("date"),
            time_from=request.POST.get("time_from"),
            to=request.POST.get("to"),
            quantity=request.POST.get("quantity"),
            address=request.POST.get("address"),
            link_video=request.POST.get("link_video"),
            image=request.FILES.get("image"),
        )

        if not result.get("status"):
            return JsonResponse({"errors": result.get("errors")}, status=400)

        return JsonResponse(request.POST, status=200)

    return render(request, "cms/pages/ticket/create.html", {})


@permission_required("src.change_ticket")
def update(request, id):
    ticketRepository = TicketRepository()
    ticket = ticketRepository.getOne(id=id)

    if request.method == "POST":
        result = ticketRepository.update(
            ticket,
            type=request.POST.get("type"),
            name=request.POST.get("name"),
            price=request.POST.get("price"),
            date=request.POST.get("date"),
            time_from=request.POST.get("time_from"),
            to=request.POST.get("to"),
            quantity=request.POST.get("quantity"),
            address=request.POST.get("address"),
            link_video=request.POST.get("link_video"),
            image=request.FILES.get("image"),
        )

        if not result.get("status"):
            return JsonResponse({"errors": result.get("errors")}, status=400)

        return JsonResponse(request.POST, status=200)

    ticket.from_ = ticket.time_from
    return render(request, "cms/pages/ticket/update.html", {"ticket": ticket})


@permission_required("src.delete_ticket")
def delete(request):
    if request.method == "POST":
        ticketRepository = TicketRepository()
        result = ticketRepository.delete(
            ticketRepository.getOne(id=request.POST.get("id"))
        )

        if not result:
            return JsonResponse({"errors": "Fail"}, status=400)

        return JsonResponse(request.POST, status=200)
