country_number = {'India':+91,'United States':+1,"Singapore":+65}

# find the country code which is in the dictionary

print("Phone number for India:")

print(country_number.get('India','Not found'))

# find the country code which is not in the dictionary

print("Country code of Great Britain:")

print(country_number.get('great britain',"Not found"))