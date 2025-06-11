import unittest
from src.services.dns_log_analyzer import DnsLogAnalyzer
from src.models.dns_log import DnsLog

class TestDnsLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = DnsLogAnalyzer()
        self.sample_logs = [
            DnsLog("2024-09-11 18:46:00", "Active Directory User ([email protected])", 
                   "Active Directory User ([email protected]),WIN11-SNG01-Example", 
                   "10.10.1.100", "24.123.132.133", "Allowed", "1 (A)", 
                   "NOERROR", "domain-visited.com.", 
                   "Software/Technology,Business Services,Allow List,Infrastructure and Content Delivery Networks,SaaS and B2B,Application", 
                   "AD Users", "AD Users,Anyconnect Roaming Client", 
                   "", "506165", "", "8234970"),
            DnsLog("2024-09-11 18:46:00", "Active Directory User ([email protected])", 
                   "Active Directory User ([email protected]),WIN11-SNG01-Example", 
                   "10.10.1.100", "24.123.132.133", "Blocked", "1 (A)", 
                   "NOERROR", "domain-visited.com.", 
                   "Chat,Social Networking", "AD Users", 
                   "AD Users,Anyconnect Roaming Client", 
                   "Social Networking", "506165", "", "8234970")
        ]

    def test_analyze_logs(self):
        result = self.analyzer.analyze_logs(self.sample_logs)
        self.assertIsInstance(result, dict)
        self.assertIn('allowed', result)
        self.assertIn('blocked', result)

    def test_detect_patterns(self):
        patterns = self.analyzer.detect_patterns(self.sample_logs)
        self.assertIsInstance(patterns, list)
        self.assertGreater(len(patterns), 0)

if __name__ == '__main__':
    unittest.main()