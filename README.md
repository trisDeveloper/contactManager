# Contact Manager

## Video Demo: <URL HERE>

## Description

The Contact Manager is a Python-based terminal application designed to help users easily manage their contacts. With this application, you can add, view, and delete contacts, and all contact information is persistently saved to a file. This ensures that your data remains intact even after closing and reopening the application.

## Features

### Add Contact
- **Functionality**: Allows the user to add a new contact by entering the contact's name and phone number.
- **Usage**: Simply follow the prompts to input the contact's details.
- **Persistence**: The new contact is saved to the `contacts.txt` file.

### View Contacts
- **Functionality**: Displays all saved contacts in a readable format.
- **Usage**: Select the option to view contacts, and all contacts will be listed with their names and phone numbers.

### Delete Contact
- **Functionality**: Enables the user to delete a contact by specifying the contact's name.
- **Usage**: Enter the name of the contact you wish to delete, and the contact will be removed from the list and file.


## Running the Application

1. Clone the repository:
```sh
git clone https://github.com/trisDeveloper/contactManager.git
```
2. Navigate to the project directory:
```sh
cd ContactManager
```
3. Run the application:
```sh
python project.py
```

## Running Tests
1. Ensure you have pytest installed:
```sh
pip install pytest
```
2. Run the tests:
```sh
pytest test_project.py
```