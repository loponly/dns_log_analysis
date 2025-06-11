import unittest
from src.services.tool_detection_database import ToolDetectionDatabase

class TestToolDetectionDatabase(unittest.TestCase):

    def setUp(self):
        self.database = ToolDetectionDatabase()
        self.test_file_path = 'test_tool_database.json'  # Path to a test JSON file

    def test_load_database(self):
        self.database.load_database(self.test_file_path)
        self.assertIsNotNone(self.database.data)
        self.assertGreater(len(self.database.data), 0)

    def test_get_tool_info(self):
        self.database.load_database(self.test_file_path)
        tool_info = self.database.get_tool_info('example.com')
        self.assertIsNotNone(tool_info)
        self.assertIn('domain', tool_info)
        self.assertIn('confidence_score', tool_info)

if __name__ == '__main__':
    unittest.main()