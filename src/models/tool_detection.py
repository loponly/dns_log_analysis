class ToolDetection:
    def __init__(self, domain: str, confidence_score: float, categories: list):
        self.domain = domain
        self.confidence_score = confidence_score
        self.categories = categories

    def __repr__(self):
        return f"ToolDetection(domain={self.domain}, confidence_score={self.confidence_score}, categories={self.categories})"