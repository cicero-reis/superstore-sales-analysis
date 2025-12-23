import json
import threading
import os

class JSONCache:
    def __init__(self, file_path=".langchain_cache.json"):
        self.file_path = file_path
        self.lock = threading.Lock()
        self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    self.cache = json.load(f)
                except Exception:
                    self.cache = {}
        else:
            self.cache = {}

    def _save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.cache, f)

    def lookup(self, prompt, llm_string=None):
        key = prompt if llm_string is None else f"{llm_string}:{prompt}"
        return self.cache.get(key)

    def update(self, prompt, llm_string, result):
        key = prompt if llm_string is None else f"{llm_string}:{prompt}"
        with self.lock:
            self.cache[key] = result
            self._save()
