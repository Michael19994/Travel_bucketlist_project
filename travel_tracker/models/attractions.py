class Attraction:
    def __init__(self, name, description, destination, date, id = None, visited = False):
        self.name = name
        self.description = description
        self.destination = destination
        self.date = date
        self.id = id 
        self.visited = visited

def set_visited(self):
    self.visited = True 