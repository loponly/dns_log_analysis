class DnsLogAnalyzer:
    def analyze_logs(self, dns_logs):
        parsed_logs = self.parse_logs(dns_logs)
        grouped_logs = {"allowed": [], "blocked": []}
        for log in parsed_logs:
            if "allowed" in log.action.lower():
                grouped_logs["allowed"].append(log)
            elif "blocked" in log.action.lower():
                grouped_logs["blocked"].append(log)
        return grouped_logs

    def detect_patterns(self, dns_logs):
        patterns = []
        for log in dns_logs:
            if self.is_malicious(log):
                patterns.append(log)
        return patterns

    def parse_logs(self, dns_logs):
        return dns_logs  # No need to parse as logs are already structured

    def is_malicious(self, log):
        return "blocked" in log.action.lower()