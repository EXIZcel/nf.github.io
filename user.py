class User:
    users = []

    def __init__(self, id, name, about, image):
        self.id = id
        self.name = name
        self.image = image
        self.about = about

        users.append(self)

    def __repr__(self):
        return f'({self.id}|{self.name})'
    