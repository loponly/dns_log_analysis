import unittest
from src.utils.json_formatter import format_to_json

class TestJsonFormatter(unittest.TestCase):

    def test_format_to_json(self):
        # Sample data for testing
        sample_data = {
            "timestamp": "2024-09-11 18:46:00",
            "most_granular_identity": "Active Directory User ([email protected])",
            "identities": "Active Directory User ([email protected]),WIN11-SNG01-Example",
            "internal_ip": "10.10.1.100",
            "external_ip": "24.123.132.133",
            "action": "Allowed",
            "query_type": "1 (A)",
            "response_code": "NOERROR",
            "domain": "domain-visited.com.",
            "categories": ["Software/Technology", "Business Services"],
            "most_granular_identity_type": "AD Users",
            "identity_types": ["AD Users", "Anyconnect Roaming Client"],
            "blocked_categories": [],
            "rule_id": "506165",
            "destination_countries": [],
            "organization_id": "8234970"
        }

        expected_json = '''{
    "timestamp": "2024-09-11 18:46:00",
    "most_granular_identity": "Active Directory User ([email protected])",
    "identities": "Active Directory User ([email protected]),WIN11-SNG01-Example",
    "internal_ip": "10.10.1.100",
    "external_ip": "24.123.132.133",
    "action": "Allowed",
    "query_type": "1 (A)",
    "response_code": "NOERROR",
    "domain": "domain-visited.com.",
    "categories": ["Software/Technology", "Business Services"],
    "most_granular_identity_type": "AD Users",
    "identity_types": ["AD Users", "Anyconnect Roaming Client"],
    "blocked_categories": [],
    "rule_id": "506165",
    "destination_countries": [],
    "organization_id": "8234970"
}'''

        # Call the function and compare the result
        result = format_to_json(sample_data)
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()