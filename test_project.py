import unittest
import os
from io import StringIO
from project import load, save, add, view, delete

class TestContactManager(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_contacts.txt'
        self.contacts = {
            'John Doe': '6753466343',
            'Thomas Shelby': '545434579'
        }
        save(self.contacts, self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_load(self):
        loaded_contacts = load(self.file_path)
        self.assertEqual(loaded_contacts, self.contacts)

    def test_save(self):
        new_contacts = {'Tris Bouden': '745445345566'}
        save(new_contacts, self.file_path)
        with open(self.file_path, 'r') as file:
            content = file.read().strip()
        self.assertEqual(content, 'Tris Bouden,745445345566')

    def test_add(self):
        contacts = {}
        input_data = StringIO('Tris Bouden\n745445345566\n')
        output = StringIO()
        add(contacts, input_data, output)
        self.assertIn('Tris Bouden', contacts)
        self.assertEqual(contacts['Tris Bouden'], '745445345566')

    def test_view(self):
        contacts = self.contacts
        output = StringIO()
        view(contacts, output)
        output.seek(0)
        result = output.read().strip()
        expected = "Contact List:\nName: John Doe, Phone: 6753466343\nName: Thomas Shelby, Phone: 545434579"
        self.assertEqual(result, expected)

    def test_delete(self):
        contacts = self.contacts
        input_data = StringIO('John Doe\n')
        output = StringIO()
        delete(contacts, input_data, output)
        self.assertNotIn('John Doe', contacts)
        self.assertIn('Thomas Shelby', contacts)

if __name__ == '__main__':
    unittest.main()
