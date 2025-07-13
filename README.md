# PGDB-Scraper
## Description
This scraper scrapes information from public websites, In this case the Plumbers, Gasfitters, drainlayers Board. (https://www.pgdb.co.nz/)
The scraper gets good information from websites with APIs and written in json format.
## Installation instructions
The installations to be done are minimal. The only website you need to sign up for is Postman(https://www.postman.com/) that enables you get the URL necessary for parsing the data.
It also helps to distinguish which language the website is using to make it easy to parse data.
Ensure you are familiar with Python language and an IDE of your choice in the case you need to alter the python script to fit the language identified by postman.
## Usage
The scraper can be used to get information from websites such as the one named above and with an API available. The most preferred language is Java script although it can be slightly modified to incorporate websites that are heave on HTML usage.
In this project case it was use to get information that included:
•	Full name
•	Email
•	Contact Number
•	License type (E.g. certification for plumber)
•	License year
### Step 1
Inspect the website to establish which language has been used. It serves to establish whether the website has an API.
If it doesn’t have the API then we can proceed to use selenium and beautiful soup to extract the data
### Step 2
After inspection and understanding how the website works, get the URL from the network tab, under the Headers section and under Request URL, you can copy the URL and paste in postman under the get request.
### Step 3
In the python script shared on this repository, replace the newly acquired json file and load the JSON data.
### Step 4
Run the script after the minor change. You should get a download of a CSV file with the details you have requested for in your amended code and as according to what is needed from your assignment.
## License
Before you use the scraper, check the API documentation if available and look into the Robots.txt file to understand which parts of the website data can be collected and to prevent you from being blocked or banned.
## Contact information
This project and product has been developed by Cyrus Wambugu who is an early career professional in Data science and passionate about the data world.
Reach me on LinkedIn: linkedin.com/in/cyrus-wambugu-b9476195
Email: Cyruswambugu91@gmail.com
 
