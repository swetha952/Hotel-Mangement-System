import os
from dotenv import load_dotenv
import mysql.connector as m
import random

dotenv_path = dotenv_path = "C:\\Users\\sweth\\OneDrive\\github\\.env"

if os.path.exists(dotenv_path):
    print("✅ Found .enq file!")
    load_dotenv(dotenv_path)
else:
    print("❌ .env file not found at", dotenv_path)
    
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASS:", os.getenv("DB_PASS"))
print("DB_NAME:", os.getenv("DB_NAME"))

d = m.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
cur = d.cursor()

print('''         CELESTIAL OASIS INN
            HOTEL BOOKING         ''')
menu = '''          1.Enter booking details
          2.Booking record 
          3.Calculate Food bill
          4.Calculate Activities bill
          5.Generate total bill
          6.Exit'''

print(menu)

l = [0, 0, 0]


def is_valid_customer_id(cid):
    cur = con.cursor()
    cur.execute("SELECT * FROM Customer WHERE Cid = %s", (cid,))
    return cur.fetchone() is not None  # return True if customer exists

def get_booking_dates(cid):
    cur = con.cursor()
    cur.execute("SELECT BookInDate, CheckOutDate FROM Customer WHERE Cid = %s", (cid,))
    dates = cur.fetchone()
    if dates:
        return dates[0], dates[1]  
    return None, None
a=0
room_bookings = {}  # Store room choices keyed by customer ID

def bdetails():
    global l

    cur = con.cursor()
    while True:
                cid = random.randint(1000, 9999)
                cur.execute('SELECT * FROM Customer WHERE Cid = %s', (cid,))
                if not cur.fetchone():
                            break
    print(f"Generated unique Customer ID: {cid}")
    
    name = input('Enter name: ')
    
    while True:
        ph = input('Enter phone number (10 digits): ')
        if ph.isdigit() and len(ph) == 10:
            break
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")
    
    while True:
        age = input('Enter your age: ')
        if age.isdigit() and len(age) == 2 and int(age) >= 18:
            break
        else:
            print("Invalid")
    while True:
        bookin = input('Enter check-in date (YYYY-MM-DD): ')
        bookot = input('Enter check-out date (YYYY-MM-DD): ')
        if bookin < bookot:
                break
        else:
            print("Check-out date must be after check-in date. Please try again.")

    cur.execute(
        'INSERT INTO Customer (Cid, Name, phoneno, Age, BookInDate, CheckOutDate) VALUES (%s, %s, %s, %s, %s, %s)',
        (cid, name, ph, age, bookin, bookot)
    )
    con.commit()
    print("Details entered successfully! Proceeding to room booking.")  ###CHANGED
    roomrent(cid)  ###CHANGED - Direct to room booking after entering details
    return 



def calculate_days(bookin, bookot):
    in_year, in_month, in_day = map(int, bookin.split('-'))
    out_year, out_month, out_day = map(int, bookot.split('-'))
    in_total_days = in_year * 365 + in_month * 30 + in_day
    out_total_days = out_year * 365 + out_month * 30 + out_day
    num_days = out_total_days - in_total_days
    if num_days <= 0:
        print("Check-out date must be after check-in date.")
        return None
    return num_days
initial_room_count = {'Single': 30
                      , 'Deluxe Double': 5, 'Presidential suite': 3}

def get_available_rooms(room_type, bookin, bookot):
    """Calculate available rooms for the given type and dates based on existing bookings."""
    cur = con.cursor()
    
    
    cur.execute("""
        SELECT COUNT(*) FROM RoomBooking 
        WHERE RoomType = %s AND 
              ((BookInDate <= %s AND CheckOutDate > %s) OR 
               (BookInDate < %s AND CheckOutDate >= %s))
    """, (room_type, bookin, bookin, bookot, bookot))
    
    booked_rooms = cur.fetchone()[0]
    available_rooms = initial_room_count[room_type] - booked_rooms
    
    return available_rooms

room_chosen=[]
def roomrent(cid):
    
    global l
    if not is_valid_customer_id(cid):
        print("Invalid customer ID. Please try again.")
        return
    
    bookin, bookot = get_booking_dates(cid)
    if not bookin or not bookot:
        print("Booking dates not found for the given customer ID.")
        return

    print('The rooms available are:')
    print('''             1. Single --- 10,000/day  
             2. Deluxe Double --- 30,000/day
             3. Presidential suite --- 1,00,000/day
             4. Exit''')

    try:
        ch1 = int(input('Enter your room choice: '))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if ch1 == 1:
        room_type = 'Single'
        rent_per_day = 10000
        room_chosen.append('Single Room')
    elif ch1 == 2:
        room_type = 'Deluxe Double'
        rent_per_day = 30000
        room_chosen.append('Deluxe Double Room')
    elif ch1 == 3:
        room_type = 'Presidential suite'
        rent_per_day = 100000
        room_chosen.append('Presidential Suite')
    elif ch1 == 4:

        return   #replaced break with return to exit the fn
    else:
        print('Invalid choice.')
        return


    num_days = calculate_days(str(bookin), str(bookot))

    if num_days is None:
        return

    total_rent = num_days * rent_per_day
    l[0] = total_rent
    
    print("Total room rent =", total_rent)
    available_rooms = get_available_rooms(room_type, bookin, bookot)
    if available_rooms <= 0:
        print(f"Sorry, no {room_type} rooms available for the selected dates.")
        return

    # If booking is successful, update the booking in the database
    cur = con.cursor()
    cur.execute('INSERT INTO RoomBooking (Cid, RoomType, BookInDate, CheckOutDate) VALUES (%s, %s, %s, %s)', 
                (cid, room_type, bookin, bookot))
    con.commit()
    print(f'Booking successful! {available_rooms - 1} {room_type} rooms left for the selected dates.')

    return total_rent

def brecord():
    global l 
    cur = con.cursor()
    cid = int(input('Enter customer ID: '))
    if not is_valid_customer_id(cid):
        print("Invalid customer ID. Please try again.")
        return

    cur.execute("SELECT * FROM Customer WHERE Cid = %s", (cid,))
    x = cur.fetchone()
    if x:
        print("CID:", x[0])
        print("Name:", x[1])
        print("Phone:", x[2])
        
        print("Age:", x[3])
        print("Check-in Date:", str(x[4]))
        print("Check-out Date:", str(x[5]))
    else:
        print("No customer found with CID", cid)
        
food_chosen=[]
def foodbill(cid):
    global l
    global food_chosen
    if not is_valid_customer_id(cid):
        print("Invalid customer ID. Please try again.")
        return
    
    bookin, bookot = get_booking_dates(cid)
    if not bookin or not bookot:
        print("Booking dates not found for the given customer ID.")
        return

    print('The food options available are:')
    print('''1. Vegetarian --- 2500/day
2. Non-Vegetarian --- 3500/day
3. Exit''')
    qty=int(input("enter the no of people:"))
    ch2 = int(input('Enter your food choice: '))
    if ch2 == 1:
        fc = 2500
        ftype='Vegetarian'
        food_chosen.append('Vegetarian')
    elif ch2 == 2:
        fc = 3500
        ftype='Non-Vegetarian'
        food_chosen.append('Non-Vegetarian')

    elif ch2 == 3:

        return   #replaced break with return to exit the fn
    else:
        print('Invalid choice.')
        return


    cur = con.cursor()
    cur.execute('INSERT INTO FoodOrder (cid, foodtype, fprice,quantity) VALUES (%s, %s, %s,%s)', 
                (cid,ftype,fc,qty))
    con.commit()
    num_days = calculate_days(str(bookin), str(bookot))
    if num_days is None:
        return

    total_foodcost = num_days * fc
    print("Total food cost =", total_foodcost)
    l[2] = total_foodcost

act_chosen = []   
def activities(cid):
    global l
    global act_chosen
    if not is_valid_customer_id(cid):
        print("Invalid customer ID. Please try again.")
        return
    
    bookin, _ = get_booking_dates(cid)
    if not bookin:
        print("Booking date not found for the given customer ID.")
        return

    total_activity_cost = 0
    while True:
        print('The activities available are:')
        print('''1. City tour --- 6000/day
2. Water sports --- 400/hour
3. Gym --- 1500/hour
4. Spa/Massage --- 2000/hour
5. Arcade --- 500/hour
6. Exit''')

        ch3 = int(input('Enter your activity choice: '))

        if ch3 == 1:
            dur = 1
            price = 6000 * dur
            total_activity_cost += price
            act='City Tour'
            act_chosen.append('City Tour')  

        elif ch3 == 2:
            dur = int(input("Enter number of hours: "))
            price = 400 * dur
            act='Water Sports'
            total_activity_cost += price
            
            act_chosen.append('Water Sports')

        elif ch3 == 3:
            dur = int(input("Enter number of hours: "))
            price = 1500 * dur
            total_activity_cost += price
            act='Gym'
            act_chosen.append('Gym')

        elif ch3 == 4:
            dur = int(input("Enter number of hours: "))
            price = 2000 * dur
            act='Spa/Massage'
            total_activity_cost += price
            act_chosen.append('Spa/Massage')

        elif ch3 == 5:
            dur = int(input("Enter number of hours: "))
            price = 500 * dur
            act='Arcade'
            total_activity_cost += price
            act_chosen.append('Arcade')

        elif ch3 == 6:
            print("Total activity cost =", total_activity_cost)
            
            l[1] = total_activity_cost
            break

        else:
            print('Invalid choice. Please try again.')
            continue
        cur = con.cursor()
        cur.execute('INSERT INTO ActivityBooking (Cid, BookingDate, activity, actcost) VALUES (%s, %s, %s, %s)', 
                (cid, bookin, act, price))
        con.commit()

def totalbill(cid):
    global food_chosen
    global act_chosen
    global room_chosen

   
    food_chosen.clear()
    act_chosen.clear()
    room_chosen.clear()
    
    if not is_valid_customer_id(cid):
        print("Invalid customer ID. Please try again.")
        return
    
    bookin, bookot = get_booking_dates(cid)  
    if not bookin or not bookot:
        print("Booking dates not found for the given customer ID.") 
        return
    
    #fetching room details
    cur = con.cursor()
    cur.execute("SELECT RoomType FROM RoomBooking WHERE Cid = %s", (cid,))
    room_result = cur.fetchone()
    if room_result:
        room_chosen.append(room_result[0])
        
    #fetching food details
    cur.execute("SELECT foodtype FROM FoodOrder WHERE Cid = %s", (cid,))
    food_result = cur.fetchone()
    if food_result:
        food_chosen.append(food_result[0])
    
    #fetching activity details
    cur.execute("SELECT Activity FROM ActivityBooking WHERE Cid = %s", (cid,))
    activities_result = cur.fetchall() #fetchall used to fetch all activities
    for activity in activities_result:
        act_chosen.append(activity[0])
    
    

    total_bill=sum(l)
    cur.execute("INSERT INTO Bill (Cid, TotalBill) VALUES (%s, %s)", (cid, total_bill))
    con.commit()

    cur.execute("SELECT TotalBill FROM Bill WHERE Cid = %s", (cid,))  
    t_bill = cur.fetchone()  
    if t_bill:
        t_bill = t_bill[0]  
    else:
        t_bill = "Not Found"
    
  
    print('==============================')
    print('         TOTAL BILL           ')
    print('==============================')
    print(f"Customer ID   :       {cid}")
    print(f"Check-In Date :     {bookin}")
    print(f"Check-Out Date:    {bookot}")
    print('------------------------------')
    
    if room_chosen:
        for room in room_chosen:
            print('Room Chosen:  ',room)
    else:
        print('Room Chosen:     None')
            
    if food_chosen:
        for food in food_chosen:
            print('Food Chosen:  ',food)
    else:
        print('Food Chosen:     None')

    if act_chosen:
        for act in act_chosen:
            print('Activity Chosen: ',act)
    else:
        print('Activity Chosen:     None')
        
    
    print("Total bill   :",     t_bill)
    print('==============================')

   


while True:
    try:
        ch = int(input('Enter choice: '))
        if ch == 1:
            bdetails()
            cid = int(input('Enter customer ID: '))
            roomrent(cid)
            

            if a == 1:
                        continue
                        cid = int(input('Enter customer ID: '))
                        roomrent(cid)
            
        elif ch == 2:
            brecord()
            
        elif ch == 3:
            cid = int(input('Enter customer ID: '))
            foodbill(cid)
        elif ch == 4:
            cid = int(input('Enter customer ID: '))
            activities(cid)
        elif ch == 5:
            cid = int(input('Enter customer ID: '))
            totalbill(cid)
        elif ch == 6:
            break
        else:
            print("Invalid choice. Please select a valid option.")
            print(menu)
    except ValueError:
        print("Please enter a valid integer choice.")
        print(menu)

