## Rental Management System
#### **By Fatuma Sarah Ibrahim**

## Description
This is our End Of Phase 3 Personal Project at Moringa School.
This is a command-line interface (CLI) application written in Python for managing tenants, apartments, and landlords. It allows users to create and manage apartments, add and update tenants and perform various other operations.

## Tools used

- vs code

- sqlite3

- GitHub

- Git

- Python


## Setup/Installation requirements
## Prerequisites

- Python 3.x
- SQLite3 (included in Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://Fatmazahraa001/Rental-Management-System
```
2. Navigate to the cloned directory:
```bash
cd Rental Management System
```7
source venv/bin/activate # On Windows, use: source venv/Scripts/activate
```
4. Run the application:
```bash
python3 main.py
```
## Project Structure

- Phase-3-project     
    - lib/
        - apartment.py
        - config.py
        - landlord.py
        - tenant.py
    - houses.db
    - LICENSE.md
    - main.py
    - README.md
    

- `houses.db`: SQLite database file
- `lib/config.py`: Database configuration and table creation/deletion
- `lib/apartment.py`: Functions for managing apartments
- `lib/landlord.py`: Functions for managing landlords
- `lib/tenant.py`: Functions for managing tenants
- `main.py`: Entry point of the application
- `LICENSE` : This project is licensed under the MIT License. By using this software, you agree to the terms outlined in the license.
- `README.md`: Project README
## Running the Application

To run the application, simply type `python3 main.py` in your terminal.

## Core Deliverables

As a user, I should be able to;

- Create Tenant
- Fetch tenant by id
- Delete tenant
- Get total rent
- Fetch tenants by landlord id
- Get average rent for a specific landlord
- Get total tenants
- Update tenant details
- Fetch all tenants
- Create Landlord
- Get landlord by id
- Update landlord by id
- Delete landlord
- Count all landlords
- Fetch all landlords
- Create Apartment
- Get Apartment by Id
- Update apartment by id
- Fetch all apartments
- Delete apartment by Id
- Fetch apartment by landlord id
- Get total number of all apartments 
- Get all apartments in certain location
## Known Bugs
The application works perfectly well, no bugs.
