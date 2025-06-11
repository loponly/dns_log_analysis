# dns_log_analysis
DNS Log Analysis & Tool Detection

## Description
Building a DNS log analysis tool for detecting potential security threats and unauthorized access attempts. The tool will analyze DNS query logs to identify patterns and anomalies that may indicate malicious activity.

## Core Requirements
This tool is designed to meet the following core requirements:

### Python Functions
- **`analyze_enterprise_dns_logs(dns_logs)`**:
  - Parse enterprise DNS logs and detect unauthorized SaaS usage.
  - Input: 100+ DNS log files with millions of queries.
  - Output: Detected tools with confidence scores.

- **`correlate_authentication_data(dns_logs, okta_logs)`**:
  - Correlate DNS traffic with authentication events.
  - Map user activity to specific enterprise software usage.
  - Handle conflicts between multiple data sources.

## Features
- **DNS Query Analysis**: Parse and analyze DNS query logs to extract relevant information.
- **Pattern Recognition**: Identify patterns in DNS queries that may indicate malicious activity, such as domain generation algorithms (DGA) or command and control (C2) communication.
- **Anomaly Detection**: Detect anomalies in DNS traffic that may suggest unauthorized access or data exfiltration.
- **Tool Detection Database**: Build a database with 400+ enterprise software entries mapped to domains.
- **Correlation Engine**: Match DNS queries to authentication events from Okta/Azure AD.
- **JSON Output**: Generate structured data ready for cost analysis engines.
- **AWS Lambda Integration**: Seamlessly integrate with existing AWS Lambda pipelines.

## Sprint Recovery Tasks (Week 1)
1. Parse 100+ enterprise DNS logs - extract domains, classify traffic patterns.
2. Build tool detection database - 400+ enterprise software entries with domain mapping.
3. Correlation engine - match DNS queries to authentication events from Okta/Azure AD.
4. JSON output format - structured data ready for cost analysis engine.
5. Integration with existing AWS Lambda pipeline (infrastructure already built).

## Example DNS Logs
### Allowed Action
```
"2024-09-11 18:46:00","Active Directory User ([email protected])","Active Directory User ([email protected]),WIN11-SNG01-Example","10.10.1.100","24.123.132.133","Allowed","1 (A)","NOERROR","domain-visited.com.","Software/Technology,Business Services,Allow List,Infrastructure and Content Delivery Networks,SaaS and B2B,Application","AD Users","AD Users,Anyconnect Roaming Client","","506165","","8234970"
```

### Blocked Action
```
"2024-09-11 18:46:00","Active Directory User ([email protected])","Active Directory User ([email protected]),WIN11-SNG01-Example","10.10.1.100","24.123.132.133","Blocked","1 (A)","NOERROR","domain-visited.com.","Chat,Social Networking","AD Users","AD Users,Anyconnect Roaming Client","Social Networking","506165","","8234970"
```

### Log Format
```
<timestamp><most granular identity><identities><internal ip><external ip><action><query type><response code><domain><categories><most granular identity type><identity types><blocked categories><rule id><destination countries><organization id>
```

### CSV Header Row
```
"Timestamp","Most Granular Identity","Identities","Internal IP","External IP","Action","Query Type","Response Code","Domain","Categories","Most Granular Identity Type","Identity Types","Blocked Categories","Rule ID","Destination Countries","Organization ID"
```
```

## Okta Log Format Examples

### Access Logs
Access Gateway access logs include information on HTTP access request events such as GET and POST.

#### Example Event
```
2020-06-24T09:40:43.000-05:00 example.myaccessgateway.com auth header.myexample.com 10.0.0.110 - - "GET / HTTP/2.0" 302 163 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" "-" 0.073 -
```

### Audit Logs
Access Gateway audit logs include information on authentication, authorization, and system-related events.

#### Example Event
```
2020-08-05T18:40:23.711-07:00 nodeB OAG ADMIN_CONSOLE CLUSTER MANAGER ADMIN NOMINATION INFO
Starting authorized nomination process - OAG Version - 2020.6.3
```

### Monitor Logs
Access Gateway monitor logs include information on system start/stop, disk usage, and Kerberos status.

#### Example Event
```
2020-06-25T07:00:02.119-05:00 example.myaccessgateway.com OAG_MONITOR MONITOR DISK_USAGE INFO DISK_USAGE [FILESYSTEM="/dev/mapper/centos-root" MOUNT="/" USAGE="12%"] Mount / is 12% full
```

### NGINX Logs
Access Gateway NGINX logs contain events such as system start/stop and inaccessible domain errors.

#### Example Event
```
2020-07-07-18:45:57 example.myaccessgateway.com systemd[1]: Started Access Gateway Reverse Proxy.
```

### Sudo Logs
Access Gateway audits sudo command usage by logging all events to the sudoers.log.

#### Example Event
```
Dec 2 13:00:13 : oag-mgmt : TTY=pts/1 ; PWD=/home/oag-mgmt ; USER=root ; COMMAND=/opt/oag/bin/updateCert.sh -f
```

## Usage
### Installation
```bash
pip install -r requirements.txt
```

### Running the Tool
```bash
python main.py