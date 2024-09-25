class Group:
    def __init__(self, name: str, link: str):
        self.name = name
        self.schedule_link = link

    def to_dict(self):
        return {
            'name': self.name,
            'link': self.schedule_link
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['link'])


class Student:
    def __init__(self, link: str, first_name: str, second_name: str, group: Group, phone=''):
        self.link = link
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.group = group

    def to_dict(self):
        return {
            'link': self.link,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'phone': self.phone,
            'group': self.group
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['link'], data['first_name'], data['second_name'], data['phone'], data['group'])
