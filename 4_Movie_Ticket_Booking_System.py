'''4. Movie Ticket Booking System
Scenario:
A cinema hall wants to manage ticket bookings. Write a program to keep track of 
**available** and **booked seats**. Allow users to **book** or **cancel** a seat.
Requirements:
- Use functions to handle seat booking and cancellation.
- Prevent booking an already booked seat.
Input Example:
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
Expected Output:
Available seats: [1, 4, 6, 8, 9, 10]'''
def book_seat(seat, booked, total):
    if seat in booked:
        print("Seat", seat, "is already booked!")
    elif seat < 1 or seat > total:
        print("Invalid seat number!")
    else:
        booked.append(seat)
        print("Seat", seat, "booked successfully!")

def cancel_seat(seat, booked):
    if seat in booked:
        booked.remove(seat)
        print("Seat", seat, "cancelled successfully!")
    else:
        print("Seat", seat, "was not booked.")

def available_seats(total, booked):
    available = []
    for seat in range(1, total+1):
        if seat not in booked:
            available.append(seat)
    return available

def show_seats(total, booked):
    print("\nSeat Status:")
    for seat in range(1, total+1):
        if seat in booked:
            print("Seat", seat, "-> Booked")
        else:
            print("Seat", seat, "-> Available")


# Main Program
total_seats = 10
booked_seats = [2, 5, 7]

while True:
    print("\n--- Movie Ticket Booking System ---")
    print("1. Book a seat")
    print("2. Cancel a seat")
    print("3. Show available seats")
    print("4. Show all seat status")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        seat_no = int(input("Enter seat number to book: "))
        book_seat(seat_no, booked_seats, total_seats)
    elif choice == 2:
        seat_no = int(input("Enter seat number to cancel: "))
        cancel_seat(seat_no, booked_seats)
    elif choice == 3:
        print("Available seats:", available_seats(total_seats, booked_seats))
    elif choice == 4:
        show_seats(total_seats, booked_seats)
    elif choice == 5:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")

