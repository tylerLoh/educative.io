import asyncio
import random
import os

mutex = asyncio.Lock()

# read file and remove trailing whitespace into list
with open('tree.txt') as fp:
    bless = list(fp.readline())
    bless += list(fp.readline().rstrip())
# bless = list(open('tree.txt').readline().rstrip())
tree = list(open('tree.txt').read().rstrip())


def change_color(color, text='*'):
    if color == 'R':
        return f'\033[91m{text}\033[0m'
    if color == 'G':
        return f'\033[92m{text}\033[0m'
    if color == 'Y':
        return f'\033[93m{text}\033[0m'
    if color == 'B':
        return f'\033[94m{text}\033[0m'


async def lights(color, indexes):
    off = True
    while True:
        for index in indexes:
            tree[index] = change_color(color=color) if off else '*'

        async with mutex:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(''.join(tree))

        off = not off

        await asyncio.sleep(random.uniform(0.3, .5))


async def bless_lights(indexes):
    while True:
        for index, v in enumerate(indexes):
            tree[index] = change_color(random.choice(['R', 'G', 'Y', 'B']),
                                       text=bless[index])
        await asyncio.sleep(random.uniform(0.3, .5))


yellow = []
red = []
green = []
blue = []

for i, value in enumerate(tree):
    if value == 'Y':
        yellow.append(i)
        tree[i] = '*'
    if value == 'R':
        red.append(i)
        tree[i] = '*'
    if value == 'G':
        green.append(i)
        tree[i] = '*'
    if value == 'B':
        blue.append(i)
        tree[i] = '*'


async def main():
    await asyncio.gather(
        lights('Y', yellow),
        lights('R', red),
        lights('G', green),
        lights('B', blue),
        bless_lights(bless)
    )


# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(
#     lights('Y', yellow),
#     lights('R', red),
#     lights('G', green),
#     lights('B', blue),
#     bless_lights(bless)
# ))
# loop.close()
asyncio.run(main())
