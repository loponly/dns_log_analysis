class ToolDetectionDatabase:
    def __init__(self):
        self.database = {}

    def load_database(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                domain, tool_info = line.strip().split(',', 1)
                self.database[domain] = tool_info

    def get_tool_info(self, domain):
        return self.database.get(domain, None)