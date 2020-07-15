import redis
tt=1024
date=tt.to_bytes(length=4, byteorder='little', signed=True)
buf=bytearray()
buf.extend(date)
print(buf)
print(buf)
print(date[0])
print(date[1])

st="1234"
st.encode()
buf.extend(st.encode())
print(buf)


Queue="test"
redisPool =redis.ConnectionPool(host='localhost', port=6379, db=8)
client = redis.Redis(connection_pool=redisPool)
client.rpush(Queue,bytes(buf))
t=client.rpop(Queue)
print(type(t))
print(len(t))
for i in range(0,len(t)):
    print(t[i])

