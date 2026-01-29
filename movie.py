

class Movie:
    def __init__(self, title:str, length_minutes: int, is_family_friendly: bool):
        self.title = title
        self.length_minutes = length_minutes 
        self.is_family_friendly = is_family_friendly 


    def watch(self, viewer_name: str) -> str:
        return f'{viewer_name} watches {self.title} for {self.length_minutes} minutes!' 
        