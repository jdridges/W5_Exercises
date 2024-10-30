#name, address, city, state, zip

#Q1
address_dict = {'name': 'Josh Rosen', 
                'address': '779 Windfall heights',
                'city': 'Glendale',
                'state': 'Arizona',
                'zip': '70719'}

#Q2 printing in mail format
print(f"""
{address_dict['name']}
{address_dict['address']}
{address_dict['city']}, {address_dict['state']}, {address_dict['zip']} 
""".strip())

#Q3 removing name
del address_dict['name']

#Q4 breaking name down into first name and last name
full_name = ({'first name': 'Josh'}, {'last name': 'Rosen'})

#Q5 adding Honorific
address_dict.update ({'honorific': 'Dr.'})

#Q6 printing updated Mail form
print( f"""
{address_dict['honorific']} {full_name[0]['first name']} {full_name[1]['last name']}
{address_dict['address']}
{address_dict['city']}, {address_dict['state']}, {address_dict['zip']}
""".strip())