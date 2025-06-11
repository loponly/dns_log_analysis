class DnsLog:
    def __init__(self, timestamp, most_granular_identity, identities, internal_ip, external_ip, action, query_type,
                 response_code, domain, categories, most_granular_identity_type, identity_types, blocked_categories,
                 rule_id, destination_countries, organization_id):
        self.timestamp = timestamp
        self.most_granular_identity = most_granular_identity
        self.identities = identities
        self.internal_ip = internal_ip
        self.external_ip = external_ip
        self.action = action
        self.query_type = query_type
        self.response_code = response_code
        self.domain = domain
        self.categories = categories
        self.most_granular_identity_type = most_granular_identity_type
        self.identity_types = identity_types
        self.blocked_categories = blocked_categories
        self.rule_id = rule_id
        self.destination_countries = destination_countries
        self.organization_id = organization_id

    def __repr__(self):
        return f"DnsLog(timestamp={self.timestamp}, domain={self.domain}, action={self.action})"