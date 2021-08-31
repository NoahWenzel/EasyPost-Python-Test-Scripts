'''
Take a shipment from Admin and converts it into a JSON dictionary so that I can extract things from it to use in the RecreateShipment.py
'''
import json

# Copy shipment JSON from admin make sure it stays inside the tripple quotes
ship = '''

'''

# Turn the string back into a valid JSON
#     This must be done because it changes all the syntax errors coppied from Admin 
#       Ex True instead of true, None instead of null, and False instead of false
ship = json.loads(ship)

