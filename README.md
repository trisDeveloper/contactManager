# Contact Manager

## Video Demo: https://youtu.be/DVx4n0wK3sY

## Description

The Contact Manager is a simple Python-based terminal application designed to help users easily manage their contacts. With this application, you can add, view, and delete contacts, and all contact information is persistently saved to a file. This ensures that your data remains intact even after closing and reopening the application.

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

### Exit Contact Program
- **Functionality**: Enables the user to save the contacts in `contacts.txt`file and exit the program.
- **Usage**: Choose option 4 and hit Enter.

## Project Structure

├── project.py
├── test_project.py
└── README.md
### project.py

This file contains the main application logic, including the main function and several helper functions.

#### Functions

- `load(file_path)`: Loads contacts from a specified file and returns them as a dictionary.
- `save(contacts, file_path)`: Saves the contacts dictionary to a specified file.
- `add(contacts, input_stream=None, output_stream=None)`: Prompts the user to enter a contact name and phone number, then adds this contact to the dictionary.
- `view(contacts, output_stream=None)`: Prints all contacts in the dictionary to the terminal.
- `delete(contacts, input_stream=None, output_stream=None)`: Prompts the user to enter the name of a contact to delete, then removes this contact from the dictionary if it exists.
- `main()`: Runs the main loop of the application, allowing the user to add, view, and delete contacts or exit the program.

### test_project.py

This file contains the tests for the main functions in `project.py`, ensuring that they work as expected.

#### Tests

- `test_load()`: Loads a test file with predefined contacts and checks if the returned dictionary matches the expected contacts.
- `test_save()`: Saves a new set of contacts to a test file and verifies the file contents match the expected data.
- `test_add()`:  Simulates user input to add a contact and verifies the contact is present with correct details.
- `test_view()`: Captures the output of viewing contacts and verifies it matches the expected formatted list.
- `test_delete()`: Simulates user input to delete a contact and verifies the contact is removed from the dictionary.

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