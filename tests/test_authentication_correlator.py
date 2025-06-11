from src.services.authentication_correlator import AuthenticationCorrelator
import unittest
from src.main import OktaLogAnalyzer

class TestOktaLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = OktaLogAnalyzer()
        self.sample_logs = [
            "2020-06-24T09:40:43.000-05:00 example.myaccessgateway.com auth header.myexample.com 10.0.0.110 - - \"GET / HTTP/2.0\" 302 163 \"-\" \"Mozilla/5.0\"",
            "2020-08-05T18:40:23.711-07:00 nodeB OAG ADMIN_CONSOLE CLUSTER MANAGER ADMIN NOMINATION INFO",
            "2020-06-25T07:00:02.119-05:00 example.myaccessgateway.com OAG_MONITOR MONITOR DISK_USAGE INFO DISK_USAGE [FILESYSTEM=\"/dev/mapper/centos-root\" MOUNT=\"/\" USAGE=\"12%\"]",
            "2020-07-07-18:45:57 example.myaccessgateway.com systemd[1]: Started Access Gateway Reverse Proxy.",
            "Dec 2 13:00:13 : oag-mgmt : TTY=pts/1 ; PWD=/home/oag-mgmt ; USER=root ; COMMAND=/opt/oag/bin/updateCert.sh -f"
        ]

    def test_analyze_access_logs(self):
        result = self.analyzer.analyze_access_logs(self.sample_logs)
        self.assertGreater(len(result), 0)

    def test_analyze_audit_logs(self):
        result = self.analyzer.analyze_audit_logs(self.sample_logs)
        self.assertGreater(len(result), 0)

    def test_analyze_monitor_logs(self):
        result = self.analyzer.analyze_monitor_logs(self.sample_logs)
        self.assertGreater(len(result), 0)

    def test_analyze_nginx_logs(self):
        result = self.analyzer.analyze_nginx_logs(self.sample_logs)
        self.assertGreater(len(result), 0)

    def test_analyze_sudo_logs(self):
        result = self.analyzer.analyze_sudo_logs(self.sample_logs)
        self.assertGreater(len(result), 0)

def test_correlate_data():
    correlator = AuthenticationCorrelator()
    dns_logs = [...]  # Sample DNS logs for testing
    okta_logs = [...]  # Sample Okta logs for testing
    correlated_data = correlator.correlate_data(dns_logs, okta_logs)
    assert isinstance(correlated_data, list)  # Ensure the output is a list
    # Additional assertions can be added based on expected output

def test_resolve_conflicts():
    correlator = AuthenticationCorrelator()
    data_sources = [...]  # Sample data sources for testing
    resolved_data = correlator.resolve_conflicts(data_sources)
    assert isinstance(resolved_data, dict)  # Ensure the output is a dictionary
    # Additional assertions can be added based on expected output

if __name__ == '__main__':
    unittest.main()