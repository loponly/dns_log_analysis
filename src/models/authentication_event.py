class AuthenticationEvent:
    def __init__(self, user_id: str, timestamp: str, application: str):
        self.user_id = user_id
        self.timestamp = timestamp
        self.application = application

    def __repr__(self):
        return f"AuthenticationEvent(user_id={self.user_id}, timestamp={self.timestamp}, application={self.application})"