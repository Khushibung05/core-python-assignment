def book_seat(booked, seat):
    if seat in booked:
        print("Seat already booked.")
    else:
        booked.append(seat)
    return booked

def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)
    else:
        print("Seat not booked yet.")
    return booked

def available_seats(total, booked):
    return [s for s in range(1, total + 1) if s not in booked]

# Example
total_seats = 10
booked_seats = [2, 5, 7]

booked_seats = book_seat(booked_seats, 3)
booked_seats = cancel_seat(booked_seats, 5)
print("Available seats:", available_seats(total_seats, booked_seats))
