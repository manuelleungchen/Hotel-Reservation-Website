from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservationForm, RoomForm

from .models import Room, Reservation


# Create your views here.

def rooms(request):
    floor_4 = Room.objects.filter(floorNumber="4")
    floor_3 = Room.objects.filter(floorNumber="3")
    floor_2 = Room.objects.filter(floorNumber="2")
    floor_1 = Room.objects.filter(floorNumber="1")
    
    return render(request, "hotelApp/rooms.html", {"floor_4": floor_4, "floor_3": floor_3, "floor_2": floor_2, "floor_1": floor_1} )

def reserve(request, pk):

    room_selected = get_object_or_404(Room, pk=pk) # Gets the selected room
    loginUser = request.user  # Get current Login User

    newReservation = Reservation(room=room_selected, guest=loginUser)

    form = ReservationForm(request.POST or None, instance=newReservation)

    if form.is_valid():
        form.save()
        room_selected.available=False
        room_selected.save()

        return redirect('rooms')
    return render(request, "hotelApp/reserve.html", {"form": form})

def reservations(request):

    reservationsList = Reservation.objects.filter(guest=request.user)

    newList = []
    user = request.user

    for new in reservationsList:
        newList.append(new)

    return render(request, "hotelApp/reservations.html", {"reservations": newList, "user": user})


def cancel(request, pk):
    reservation_selected = get_object_or_404(Reservation, pk=pk) # Gets the selected reservation

    selectedRoom = get_object_or_404(Room, unitNumber=reservation_selected.room.unitNumber) # Gets the selected room

    # Room Costs
    if reservation_selected.room.bedsNumber == 1:
        rate = 99.99
    elif reservation_selected.room.bedsNumber == 2:
        rate = 149.99
    elif reservation_selected.room.bedsNumber == 3:
        rate = 249.99
    else:
        rate = 299.99

    cost = reservation_selected.room.bedsNumber * rate 
    totalDays = reservation_selected.endDate - reservation_selected.startDate
    totalCost = cost * totalDays.days

    if request.method == 'POST':
        selectedRoom.available=True
        selectedRoom.save()
        reservation_selected.delete()
        return redirect("reservations")
    return render(request, "hotelApp/cancellation.html", {"object": reservation_selected, "cost": cost, "days": totalDays.days, "totalCost": totalCost})




