import os

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
REDIS_NS = os.getenv('REDIS_NS', 'indifferent')
