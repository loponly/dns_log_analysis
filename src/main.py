# File: /dns_log_analysis/dns_log_analysis/src/main.py

class DnsLogAnalysisTool:
    def __init__(self):
        from services.dns_log_analyzer import DnsLogAnalyzer
        from services.authentication_correlator import AuthenticationCorrelator
        from services.tool_detection_database import ToolDetectionDatabase

        self.dns_log_analyzer = DnsLogAnalyzer()
        self.authentication_correlator = AuthenticationCorrelator()
        self.tool_detection_database = ToolDetectionDatabase()

    def run_analysis(self, dns_logs, okta_logs, load_database=True):
        # Analyze DNS logs for patterns
        patterns = self.dns_log_analyzer.analyze_logs(dns_logs)
        
        # Correlate with authentication data
        correlated_data = self.authentication_correlator.correlate_data(dns_logs, okta_logs)
        
        # Load tool detection database only if requested and file exists
        if load_database:
            try:
                self.tool_detection_database.load_database('path/to/database/file')
            except FileNotFoundError:
                print("⚠️  Tool detection database not found, skipping database loading...")

        # Further processing can be done here
        return patterns, correlated_data

class OktaLogAnalyzer:
    def __init__(self):
        pass

    def analyze_access_logs(self, logs):
        # Analyze access logs for patterns
        return [log for log in logs if "GET" in log or "POST" in log]

    def analyze_audit_logs(self, logs):
        # Analyze audit logs for authentication and authorization events
        return [log for log in logs if "AUTH" in log or "ADMIN" in log]

    def analyze_monitor_logs(self, logs):
        # Analyze monitor logs for system status
        return [log for log in logs if "DISK_USAGE" in log or "KRB5" in log]

    def analyze_nginx_logs(self, logs):
        # Analyze NGINX logs for domain errors
        return [log for log in logs if "host not found" in log or "Reverse Proxy" in log]

    def analyze_sudo_logs(self, logs):
        # Analyze sudo logs for command usage
        return [log for log in logs if "COMMAND" in log]

def create_sample_dns_logs():
    """Create sample DNS logs for demonstration purposes"""
    from models.dns_log import DnsLog
    
    raw_logs = [
        '"2024-09-11 18:46:00","Active Directory User ([email protected])","Active Directory User ([email protected]),WIN11-SNG01-Example","10.10.1.100","24.123.132.133","Allowed","1 (A)","NOERROR","slack.com","Software/Technology,Business Services,Allow List,Infrastructure and Content Delivery Networks,SaaS and B2B,Application","AD Users","AD Users,Anyconnect Roaming Client","","506165","","8234970"',
        '"2024-09-11 18:46:05","Active Directory User ([email protected])","Active Directory User ([email protected]),WIN11-SNG01-Example","10.10.1.100","24.123.132.133","Allowed","1 (A)","NOERROR","github.com","Software/Technology,Business Services,Allow List,Infrastructure and Content Delivery Networks,SaaS and B2B,Application","AD Users","AD Users,Anyconnect Roaming Client","","506165","","8234970"',
        '"2024-09-11 18:46:10","Active Directory User ([email protected])","Active Directory User ([email protected]),WIN11-SNG01-Example","10.10.1.100","24.123.132.133","Blocked","1 (A)","NOERROR","facebook.com","Chat,Social Networking","AD Users","AD Users,Anyconnect Roaming Client","Social Networking","506165","","8234970"',
        '"2024-09-11 18:46:15","Active Directory User ([email protected])","Active Directory User ([email protected]),WIN11-SNG01-Example","10.10.1.100","24.123.132.133","Allowed","1 (A)","NOERROR","office365.com","Software/Technology,Business Services,Allow List,Infrastructure and Content Delivery Networks,SaaS and B2B,Application","AD Users","AD Users,Anyconnect Roaming Client","","506165","","8234970"',
        '"2024-09-11 18:46:20","Active Directory User ([email protected])","Active Directory User ([email protected]),WIN11-SNG01-Example","10.10.1.101","24.123.132.134","Allowed","1 (A)","NOERROR","zoom.us","Software/Technology,Business Services,Allow List,Infrastructure and Content Delivery Networks,SaaS and B2B,Application","AD Users","AD Users,Anyconnect Roaming Client","","506165","","8234970"',
    ]
    
    dns_logs = []
    for raw_log in raw_logs:
        # Parse CSV format: remove quotes and split by comma
        parts = [part.strip('"') for part in raw_log.split('","')]
        if len(parts) >= 16:
            dns_log = DnsLog(
                timestamp=parts[0],
                most_granular_identity=parts[1],
                identities=parts[2],
                internal_ip=parts[3],
                external_ip=parts[4],
                action=parts[5],
                query_type=parts[6],
                response_code=parts[7],
                domain=parts[8],
                categories=parts[9],
                most_granular_identity_type=parts[10],
                identity_types=parts[11],
                blocked_categories=parts[12],
                rule_id=parts[13],
                destination_countries=parts[14],
                organization_id=parts[15]
            )
            dns_logs.append(dns_log)
    
    return dns_logs

def create_sample_okta_logs():
    """Create sample Okta logs for demonstration purposes"""
    return [
        '2020-06-24T09:40:43.000-05:00 example.myaccessgateway.com auth header.myexample.com 10.0.0.110 - - "GET / HTTP/2.0" 302 163 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" "-" 0.073 -',
        '2020-08-05T18:40:23.711-07:00 nodeB OAG ADMIN_CONSOLE CLUSTER MANAGER ADMIN NOMINATION INFO Starting authorized nomination process - OAG Version - 2020.6.3',
        '2020-06-25T07:00:02.119-05:00 example.myaccessgateway.com OAG_MONITOR MONITOR DISK_USAGE INFO DISK_USAGE [FILESYSTEM="/dev/mapper/centos-root" MOUNT="/" USAGE="12%"] Mount / is 12% full',
        '2020-07-07-18:45:57 example.myaccessgateway.com systemd[1]: Started Access Gateway Reverse Proxy.',
        'Dec 2 13:00:13 : oag-mgmt : TTY=pts/1 ; PWD=/home/oag-mgmt ; USER=root ; COMMAND=/opt/oag/bin/updateCert.sh -f',
        '2020-06-24T10:15:30.000-05:00 example.myaccessgateway.com auth header.myexample.com 10.0.0.111 - - "POST /api/login HTTP/2.0" 200 512 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" "-" 0.145 -',
    ]

def run_example_analysis():
    """Run example analysis with sample data"""
    print("=" * 60)
    print("DNS Log Analysis Tool - Example Run")
    print("=" * 60)
    
    # Create sample data
    sample_dns_logs = create_sample_dns_logs()
    sample_okta_logs = create_sample_okta_logs()
    
    print(f"\n📊 Processing {len(sample_dns_logs)} DNS log entries...")
    print(f"📊 Processing {len(sample_okta_logs)} Okta log entries...")
    
    # Initialize the main analysis tool
    tool = DnsLogAnalysisTool()
    
    try:
        # Run the main analysis
        print("\n🔍 Running DNS log analysis...")
        patterns, correlated_data = tool.run_analysis(sample_dns_logs, sample_okta_logs, load_database=False)
        
        print("\n✅ Analysis Results:")
        print("-" * 40)
        print("Detected Patterns:", patterns)
        print("Correlated Data:", correlated_data)
        
        # Run Okta-specific analysis
        print("\n🔍 Running Okta log analysis...")
        analyzer = OktaLogAnalyzer()
        
        access_logs = analyzer.analyze_access_logs(sample_okta_logs)
        audit_logs = analyzer.analyze_audit_logs(sample_okta_logs)
        monitor_logs = analyzer.analyze_monitor_logs(sample_okta_logs)
        nginx_logs = analyzer.analyze_nginx_logs(sample_okta_logs)
        sudo_logs = analyzer.analyze_sudo_logs(sample_okta_logs)
        
        print("\n✅ Okta Analysis Results:")
        print("-" * 40)
        print(f"📄 Access Logs ({len(access_logs)} found):", access_logs)
        print(f"📄 Audit Logs ({len(audit_logs)} found):", audit_logs)
        print(f"📄 Monitor Logs ({len(monitor_logs)} found):", monitor_logs)
        print(f"📄 NGINX Logs ({len(nginx_logs)} found):", nginx_logs)
        print(f"📄 Sudo Logs ({len(sudo_logs)} found):", sudo_logs)
        
        # Example of extracting insights from the sample data
        print("\n💡 Sample Insights:")
        print("-" * 40)
        allowed_domains = [log for log in sample_dns_logs if log.action.lower() == 'allowed']
        blocked_domains = [log for log in sample_dns_logs if log.action.lower() == 'blocked']
        
        print(f"✅ Allowed DNS queries: {len(allowed_domains)}")
        print(f"❌ Blocked DNS queries: {len(blocked_domains)}")
        
        # Extract unique domains from DNS logs
        unique_domains = set()
        for log in sample_dns_logs:
            unique_domains.add(log.domain)
        
        print(f"🌐 Unique domains accessed: {len(unique_domains)}")
        print(f"🌐 Domains: {', '.join(sorted(unique_domains))}")
        
        # Show enterprise tool detection
        enterprise_tools = ['slack.com', 'github.com', 'office365.com', 'zoom.us']
        detected_tools = [domain for domain in unique_domains if domain in enterprise_tools]
        print(f"🔧 Enterprise tools detected: {', '.join(detected_tools)}")
        
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
        return False
    
    print("\n" + "=" * 60)
    print("✅ Example analysis completed successfully!")
    print("=" * 60)
    return True

def main():
    """Main function to handle command line arguments and run analysis"""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='DNS Log Analysis Tool')
    parser.add_argument('--dns-logs', type=str, help='Path to DNS logs file')
    parser.add_argument('--okta-logs', type=str, help='Path to Okta logs file')
    parser.add_argument('--example', action='store_true', help='Run with example data')
    parser.add_argument('--output', type=str, help='Output file path for results')
    
    args = parser.parse_args()
    
    if args.example or (not args.dns_logs and not args.okta_logs):
        # Run example analysis if no files provided or --example flag is used
        return run_example_analysis()
    
    # Validate file paths
    if not args.dns_logs or not args.okta_logs:
        print("❌ Error: Both --dns-logs and --okta-logs are required when not using --example")
        parser.print_help()
        return False
    
    try:
        # Read actual log files
        print(f"📂 Reading DNS logs from: {args.dns_logs}")
        with open(args.dns_logs, 'r') as f:
            raw_dns_lines = f.readlines()
        print(f"📄 Read {len(raw_dns_lines)} raw lines from DNS file")
        
        print(f"📂 Reading Okta logs from: {args.okta_logs}")
        with open(args.okta_logs, 'r') as f:
            okta_logs = f.readlines()
        print(f"📄 Read {len(okta_logs)} raw lines from Okta file")
        
        # Parse DNS logs from CSV format
        dns_logs = []
        for i, line in enumerate(raw_dns_lines):
            if i == 0:  # Skip header row
                continue
            line = line.strip()
            if line:
                try:
                    # Parse CSV format: handle quoted fields
                    import csv
                    import io
                    reader = csv.reader(io.StringIO(line))
                    parts = next(reader)
                    
                    if len(parts) >= 16:
                        from models.dns_log import DnsLog
                        dns_log = DnsLog(
                            timestamp=parts[0],
                            most_granular_identity=parts[1],
                            identities=parts[2],
                            internal_ip=parts[3],
                            external_ip=parts[4],
                            action=parts[5],
                            query_type=parts[6],
                            response_code=parts[7],
                            domain=parts[8],
                            categories=parts[9],
                            most_granular_identity_type=parts[10],
                            identity_types=parts[11],
                            blocked_categories=parts[12],
                            rule_id=parts[13],
                            destination_countries=parts[14],
                            organization_id=parts[15]
                        )
                        dns_logs.append(dns_log)
                    else:
                        print(f"⚠️  Skipping line {i+1}: insufficient columns ({len(parts)} found, 16 required)")
                except Exception as e:
                    print(f"⚠️  Error parsing line {i+1}: {str(e)}")
                    print(f"     Line content: {line[:100]}...")
        
        print(f"📊 Processing {len(dns_logs)} DNS log entries...")
        print(f"📊 Processing {len(okta_logs)} Okta log entries...")
        
        # Run analysis
        tool = DnsLogAnalysisTool()
        patterns, correlated_data = tool.run_analysis(dns_logs, okta_logs)
        
        # Run Okta analysis
        analyzer = OktaLogAnalyzer()
        access_logs = analyzer.analyze_access_logs(okta_logs)
        audit_logs = analyzer.analyze_audit_logs(okta_logs)
        monitor_logs = analyzer.analyze_monitor_logs(okta_logs)
        nginx_logs = analyzer.analyze_nginx_logs(okta_logs)
        sudo_logs = analyzer.analyze_sudo_logs(okta_logs)
        
        # Prepare results - convert DnsLog objects to dictionaries for JSON serialization
        def dns_log_to_dict(dns_log):
            return {
                'timestamp': dns_log.timestamp,
                'most_granular_identity': dns_log.most_granular_identity,
                'identities': dns_log.identities,
                'internal_ip': dns_log.internal_ip,
                'external_ip': dns_log.external_ip,
                'action': dns_log.action,
                'query_type': dns_log.query_type,
                'response_code': dns_log.response_code,
                'domain': dns_log.domain,
                'categories': dns_log.categories,
                'most_granular_identity_type': dns_log.most_granular_identity_type,
                'identity_types': dns_log.identity_types,
                'blocked_categories': dns_log.blocked_categories,
                'rule_id': dns_log.rule_id,
                'destination_countries': dns_log.destination_countries,
                'organization_id': dns_log.organization_id
            }
        
        # Convert patterns to serializable format
        serializable_patterns = {
            'allowed': [dns_log_to_dict(log) for log in patterns.get('allowed', [])],
            'blocked': [dns_log_to_dict(log) for log in patterns.get('blocked', [])]
        }
        
        results = {
            'dns_patterns': serializable_patterns,
            'correlated_data': correlated_data,
            'okta_analysis': {
                'access_logs': [log.strip() for log in access_logs],
                'audit_logs': [log.strip() for log in audit_logs],
                'monitor_logs': [log.strip() for log in monitor_logs],
                'nginx_logs': [log.strip() for log in nginx_logs],
                'sudo_logs': [log.strip() for log in sudo_logs]
            }
        }
        
        # Output results
        if args.output:
            import json
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"✅ Results saved to: {args.output}")
        else:
            print("\n✅ Analysis Results:")
            print("-" * 40)
            for key, value in results.items():
                print(f"{key}: {value}")
        
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error: File not found - {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)