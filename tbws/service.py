import falcon

class Db:
    pass

class MemoryDb(Db):
    def __init__(self):
        self.db = {}

    def get_largest(self):
        largest = None
        for key in self.db:
            if not largest:
                largest = self.db[key]
            else:
                index=0
                for char in self.db[key]:
                    if index == len(largest):
                        largest = self.db[key]
                    elif char > largest[index]:
                        largest = self.db[key]
                    index+=1
        return largest

    def put(self, key, item):
        self.db[key] = item

    def get(self, key):
        return self.db[key]

# This resource is for getting the largest thing
class GetLargestThingResource:

    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = self.db.get_largest()

# This resource is used for putting things
class PutThingsResource:

    def __init__(self, db):
        self.db = db

    def on_post(self, req, resp, key):
        self.db.put(key, req.stream.read())
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp, key):
        self.db.put(key, req.stream.read())
        resp.status = falcon.HTTP_202

# This resource is only used for getting things
class GetThingsResource:

    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, key):
        resp.status = falcon.HTTP_200
        resp.body = self.db.get(key)

db = MemoryDb()
app = api = falcon.API()
api.add_route('/things/put/{key}', PutThingsResource(db))
api.add_route('/things/get/{key}', GetThingsResource(db))
api.add_route('/things/get_largest', GetLargestThingResource(db))

