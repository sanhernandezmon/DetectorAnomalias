import redis

# Connect to the Redis instance
redis_conn = redis.Redis(host='localhost', port=6379)

# Subscribe to a channel
pubsub = redis_conn.pubsub()
pubsub.subscribe('my_channel')

# Connect to the emergency Redis instance
emergency_redis_conn = redis.Redis(host='localhost', port=6379)

# Process incoming messages
for message in pubsub.listen():
    if message['type'] == 'message':
        # Parse the message payload as a dictionary
        data = message['data'].decode('utf-8')
        message_dict = eval(data)

        # Check if the message is an emergency
        if message_dict.get('emergency', False):
            # If the message is an emergency, add it to the emergency Redis instance
            emergency_redis_conn.rpush('emergency_messages', data)
