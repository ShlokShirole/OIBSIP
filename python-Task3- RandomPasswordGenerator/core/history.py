from datetime import datetime

class PasswordHistory:
    def __init__(self):
        self._history = []  # list of (password, timestamp)

    def add(self, password):
        # Avoid immediate duplicates
        if self._history and self._history[0][0] == password:
            return
        timestamp = datetime.now().strftime("%H:%M:%S")
        self._history.insert(0, (password, timestamp))

    def get_all(self):
        return self._history[:]  # return a copy

    def clear(self):
        self._history.clear()
