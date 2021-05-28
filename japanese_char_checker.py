
from cp932_chars import get_cp932_chars

class JapaneseCharChecker:
    def __init__(self, remove_chars = []):
        self.chars = get_cp932_chars()
        self.remove_chars = set(remove_chars)

    def _line2boollist(self, line):
        return [c in self.chars for c in line if c not in self.remove_chars]
        
    def fullmatch(self, line):
        return all(self._line2boollist(line))

    def anymatch(self, line):
        return any(self._line2boollist(line))
