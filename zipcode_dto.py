import json


class ZipCodeDTO(object):
    def __init__(self, columns):
        self.id = columns[0]
        self.zipcode = columns[1]
        self.city = columns[2]
        self.state = columns[3]
        if(None is columns[4]):
            self.neighborhood = ''
        else:
            self.neighborhood = columns[4]
        if(None is columns[5]):
            self.public_place = ''
        else:
            self.public_place = columns[5]
        if(None is columns[6]):
            self.description = ''
        else:
            self.description = columns[6]

    def to_json(self):
        return json.dumps(self.__dict__)
