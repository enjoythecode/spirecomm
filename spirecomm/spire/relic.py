class Relic:

    def __init__(self, relic_id, name, counter=0, price=0):
        self.relic_id = relic_id
        self.name = name
        self.counter = counter
        self.price = price

    @classmethod
    def from_json(cls, json_object):
        return cls(
            json_object["id"],
            # name field is not always present in the game data. for example, shop screen state only has id, price, and counter
            json_object.get("name", None), 
            json_object["counter"],
            json_object.get("price", 0))
