from models.event import *
import datetime

event1 = Event(datetime.date(2022,9,29), "Monserrat Caballe Concert", 20000, "Barcelona", "Opera concert")
event2 = Event(datetime.date(2023,8,30), "Benicassim Music Festival", 30000, "Alicante", "Pop Rock Music festival")

events = [event1, event2]

def add_events(event): 
    events.append(event)
