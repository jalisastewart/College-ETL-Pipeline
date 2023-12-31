Texas Universities

This project extracts data about universities from an API, processes the data, and loads it into a MySQL database. It focuses on Texas universities, providing information about the total number of universities and the specific ones in Texas.

# Prerequisites

- Python 3.x
- MySQL database
- API key (if applicable for the university data API)

# Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Texas_Colleges.git
   cd Texas_Colleges

# Requirements

pandas==1.3.3
sqlalchemy==1.4.25
mysql-connector-python==8.0.26
pyyaml==5.4.1

# Adding MySQL CSV File
I have included the CSV file extracted from MySQL, containing information about Texas colleges. You can find the file here: texas_colleges.csv.

To import this CSV file into your MySQL database:

Open your MySQL GUI tool.
Create a new database or use an existing one.
Navigate to the "Import" or "Data Import" section in your GUI tool.
Choose the CSV file (texas_colleges.csv) for import.
Map the columns as per your database schema.
Execute the import.
