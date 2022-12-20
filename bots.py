import redis

redis = redis.StrictRedis()

class ChatBot():
    def __init__(self):
        pass

class MemoryBot():
    def __init__(self, name=None)
        self.name = name or hash("this")
        self.REDHASH = "REDHASH_%s" % self.name

    def set(self, key, value):
        redis.hset(self.redhash, key, value)

    def get(self, key):
        redis.hget(self.redhash, key)

 
        
    
