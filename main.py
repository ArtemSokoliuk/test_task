import asyncio
from itertools import product
import time

import aioredis

loop = asyncio.get_event_loop()


def create_field(x_size=512, y_size=512):
    field = set()
    for cord in product(range(1, x_size + 1), range(1, y_size + 1)):
        field.add(cord)
    return field


def get_coordinates(x, y):
    return str(x) + ":" + str(y)



class User:
    _max_jobs = 4

    def __init__(self, jobs_count):
                    

async def go():
    redis = await aioredis.create_redis(
        'redis://localhost', loop=loop)
    await redis.set('my-key', 'value')
    val = await redis.get('my-key')
    print(val)
    redis.close()
    await redis.wait_closed()


# loop.run_until_complete(go())


if __name__ == '__main__':
    field = create_field()
    t1 = time.time()
    field = create_field()
    t2 = time.time()
    print(t2 - t1)
    # print(field)
    print(512 * 512)
    print(len(field))
