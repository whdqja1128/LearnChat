import json
import re


class Retrieval:
    def __init__(self, data_path: str = "./data/team12.json"):
        with open(data_path, "r") as file:
            data: dict[str, str] = json.load(file)
            self.data = data
            self.lowercase_keys = {key.lower(): key for key in self.data.keys()}

    def retrieve(self, query: str) -> str | None:
        query_lower = query.lower()
        
        words = re.findall(r'\b\w+\b', query_lower)
        
        for word in words:
            if word in self.lowercase_keys:
                original_key = self.lowercase_keys[word]
                return f"{original_key}: {self.data[original_key]}"
        
        for key_lower, original_key in self.lowercase_keys.items():
            if key_lower in query_lower:
                return f"{original_key}: {self.data[original_key]}"
        
        return None

    def print_data(self) -> None:
        print(self.data)