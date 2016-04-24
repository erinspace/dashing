import asyncio
import datetime
from phue import Bridge
import csv

import settings


def start_video():
    print('You used to you used to...')


def setup_hue():
    hue = settings.BRIDGE_IP
    return Bridge(hue)


def change_light(bridge, color):
    lights = bridge.get_light_objects(mode='id').values()
    for light in lights:
        light.xy = HUE_COLORS[color]

    print('*{}*'.format(color.upper()))


def create_hue_cues():
    with open('timecolor.csv') as f:
        data = [tuple(line) for line in csv.reader(f)]
    data.pop(0)
    return [(int(item[0]), item[1].strip()) for item in data]

HUE_COLORS = dict(
    goldenrod=[0.5136, 0.4444],
    green=[0.214, 0.709],
    lightblue=[0.2621, 0.3157],
    darkorchid=[0.296, 0.1409],
    silver=[0.3227, 0.329],
    mediumpurple=[0.263, 0.1773],
    forestgreen=[0.2097, 0.6732],
    slategray=[0.2762, 0.3009],
    mediumslateblue=[0.2179, 0.1424],
    mediumvioletred=[0.504, 0.2201],
    palevioletred=[0.4658, 0.2773],
    deepskyblue=[0.1576, 0.2368],
    cornflowerblue=[0.1905, 0.1945],
    rosybrown=[0.4026, 0.3227],
    darksalmon=[0.4837, 0.3479],
    yellowgreen=[0.3517, 0.5618],
    steelblue=[0.183, 0.2325],
    orangered=[0.6726, 0.3217],
    mediumorchid=[0.3365, 0.1735],
    slateblue=[0.2218, 0.1444],
    beige=[0.3402, 0.356]
)

HUE_CUES = create_hue_cues()


def main():
    loop = asyncio.get_event_loop()
    start_video()
    bridge = setup_hue()
    # start_time = loop.time()

    for delay, color in HUE_CUES:
        loop.call_later(delay, change_light, bridge, color)

    loop.run_forever()
    loop.close()

if __name__ == "__main__":
    main()
