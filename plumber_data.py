import json
import csv

# Load JSON data
with open('plumber_response.json', 'r') as f:
    data = json.load(f)

# Extracting values associated with the top level key
people = data.get('publicRegisterContacts', [])

# Create and open a new CSV file for writing
with open('certified_tradespeople_all_years.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=[
        'fullName', 'email', 'contactNumber', 'licenceType', 'licenceYear'
    ])
    writer.writeheader()

    # Looping through each dictionery in the people list to get details
    for person in people:
        name = person.get('fullName', '')
        email = person.get('publicEmail', '')
        contact = person.get('publicPhone', '')

        # Looping through list under licenceHistory key for current person
        for history in person.get('licenceHistory', []):
            all_licences = []
            if history.get('current'):# Add all current licenses to empty list
                all_licences.append(history['current'])
            if history.get('previous'):# Add all previous licenses to empty list
                all_licences.append(history['previous'])
            
            # Looping through all_licences to extract needed fields
            for licence in all_licences:
                licence_type = licence.get('licenceTypeName', '')
                years = licence.get('licenceYears', [])

                # Looping through years to check year and keywords
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
                        })# Writing a row to CSV for each valid license found 
