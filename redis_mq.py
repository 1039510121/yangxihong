import redis
Queue="test"
redisPool = redis.ConnectionPool(host='localhost', port=6379, db=8)
client = redis.Redis(connection_pool=redisPool)
client.rpush(Queue,"123")
print(client.rpop(Queue))