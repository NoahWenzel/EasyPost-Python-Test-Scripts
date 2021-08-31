'''
Takes information from a shipment JSON (stored in seperate file ShipmentID.py) and recreates the shipment under my EasyPost user account.
'''

import easypost, json
import ShipmentID, Key

# easypost.api_key = Key.production_api_key
easypost.api_key = Key.test_api_key

ship = ShipmentID.ship

# # Extract all of the information

to_address = easypost.Address.create(  
  carrier_facility = ship['to_address']['carrier_facility'],
  city = ship['to_address']['city'],
  company = ship['to_address']['company'],
  country = ship['to_address']['country'],
  email = ship['to_address']['email'],
  federal_tax_id = ship['to_address']['federal_tax_id'],
  name = ship['to_address']['name'],
  phone = ship['to_address']['phone'],
  residential = ship['to_address']['residential'],
  state = ship['to_address']['state'],
  state_tax_id = ship['to_address']['state_tax_id'],
  street1 = ship['to_address']['street1'],
  street2 = ship['to_address']['street2'],
  zip = ship['to_address']['zip']
)

from_address = easypost.Address.create(
  carrier_facility = ship['from_address']['carrier_facility'],
  city = ship['from_address']['city'],
  company = ship['from_address']['company'],
  country = ship['from_address']['country'],
  email = ship['from_address']['email'],
  federal_tax_id = ship['from_address']['federal_tax_id'],
  name = ship['from_address']['name'],
  phone = ship['from_address']['phone'],
  residential = ship['from_address']['residential'],
  state = ship['from_address']['state'],
  state_tax_id = ship['from_address']['state_tax_id'],
  street1 = ship['from_address']['street1'],
  street2 = ship['from_address']['street2'],
  zip = ship['from_address']['zip'],
)

return_address = easypost.Address.create(
  carrier_facility = ship['return_address']['carrier_facility'],
  city = ship['return_address']['city'],
  company = ship['return_address']['company'],
  country = ship['return_address']['country'],
  email = ship['return_address']['email'],
  federal_tax_id = ship['return_address']['federal_tax_id'],
  name = ship['return_address']['name'],
  phone = ship['return_address']['phone'],
  residential = ship['return_address']['residential'],
  state = ship['return_address']['state'],
  state_tax_id = ship['return_address']['state_tax_id'],
  street1 = ship['return_address']['street1'],
  street2 = ship['return_address']['street2'],
  zip = ship['return_address']['zip'],
)

buyer_address = easypost.Address.create(
  carrier_facility = ship['buyer_address']['carrier_facility'],
  city = ship['buyer_address']['city'],
  company = ship['buyer_address']['company'],
  country = ship['buyer_address']['country'],
  email = ship['buyer_address']['email'],
  federal_tax_id = ship['buyer_address']['federal_tax_id'],
  name = ship['buyer_address']['name'],
  phone = ship['buyer_address']['phone'],
  residential = ship['buyer_address']['residential'],
  state = ship['buyer_address']['state'],
  state_tax_id = ship['buyer_address']['state_tax_id'],
  street1 = ship['buyer_address']['street1'],
  street2 = ship['buyer_address']['street2'],
  zip = ship['buyer_address']['zip'],
)

parcel = easypost.Parcel.create(
  length = ship['parcel']['length'],
  width = ship['parcel']['width'],
  height = ship['parcel']['height'],
  weight = ship['parcel']['weight'],
  predefined_package = ship['parcel']['predefined_package'],
)

if ship['customs_info']:
  customsArray = []
  for x in range(len(ship["customs_info"]["customs_items"])):
    # Create new customs_item
    customs_item = easypost.CustomsItem.create(
      description=ship['customs_info']['customs_items'][x]['description'],
      quantity=float(ship['customs_info']['customs_items'][x]['quantity']),
      value=float(ship['customs_info']['customs_items'][x]['value']),
      weight=float(ship['customs_info']['customs_items'][x]['weight']),
      code=ship['customs_info']['customs_items'][x]['code'],
      hs_tariff_number=ship['customs_info']['customs_items'][x]['hs_tariff_number'],
      origin_country=ship['customs_info']['customs_items'][x]['origin_country']
    )
    # Add it to the customsArray
    customsArray.append(customs_item)

  # Fill out the customs_info with adding customs_items array
  customs_info = easypost.CustomsInfo.create(
    eel_pfc=ship['customs_info']['eel_pfc'],
    customs_certify=ship['customs_info']['customs_certify'],
    customs_signer=ship['customs_info']['customs_signer'],
    contents_type=ship['customs_info']['contents_type'],
    contents_explanation=ship['customs_info']['contents_explanation'],
    restriction_type=ship['customs_info']['restriction_type'],
    restriction_comments=ship['customs_info']['restriction_comments'],
    non_delivery_option=ship['customs_info']['non_delivery_option'],
    customs_items=customsArray
    # customs_items=[customs_item0, customs_item1, customs_item2]
  )
else:
  customs_info = None


reference = ship['reference']

try:

  shipment = easypost.Shipment.create(
    to_address = to_address,
    from_address = from_address,
    return_address = return_address,
    buyer_address = buyer_address,
    is_return = ship['is_return'],
    reference = reference,
    parcel = parcel,
    carrier_accounts = [Key.UPS],
    customs_info = customs_info,
    options = ship['options'],
  )

except easypost.Error as e:
    print("Error Error Error")
    print(str(e))
    if e.param is not None:
        print("%r need's fixin" % e.param)



# From here you can do things like:

print(shipment)
# print(shipment['rates'])
