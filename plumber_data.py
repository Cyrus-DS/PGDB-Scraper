import json
import csv

# Load JSON data
with open('plumber_response.json', 'r') as f:
    data = json.load(f)

people = data.get('publicRegisterContacts', [])

# Open CSV for writing
with open('certified_tradespeople_all_years.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        'fullName', 'email', 'contactNumber', 'licenceType', 'licenceYear'
    ])
    writer.writeheader()

    for person in people:
        name = person.get('fullName', '')
        email = person.get('publicEmail', '')
        contact = person.get('publicPhone', '')

        for history in person.get('licenceHistory', []):
            all_licences = []
            if history.get('current'):
                all_licences.append(history['current'])
            if history.get('previous'):
                all_licences.append(history['previous'])

            for licence in all_licences:
                licence_type = licence.get('licenceTypeName', '')
                years = licence.get('licenceYears', [])

                for year in years:
                    if int(year) >= 2015 and any(
                        keyword in licence_type
                        for keyword in ['Plumber', 'Gasfitter', 'Drainlayer']
                    ):
                        writer.writerow({
                            'fullName': name,
                            'email': email,
                            'contactNumber': contact,
                            'licenceType': licence_type,
                            'licenceYear': year
                        })
