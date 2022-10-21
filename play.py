class Play:
    def __init__(self, value, emoji= None, wins=[]):
        self.value = value
        self.wins = wins
        self.emoji = emoji
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def __str__(self):
        return self.value

    def __gt__(self, other):
        return other in self.wins

    
