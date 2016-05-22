# -*- coding: utf-8 -*-
from time import sleep
import csv
import logging

from phue import Bridge
import pychromecast

import settings

logger = logging.getLogger(__name__)

VIDEO_FILE = 'https://osf.io/zqnyu/?action=download&direct&mode=render'
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
# CSV containing timing for color changes
CUE_FILE = 'timecolor.csv'
def _create_hue_cues():
    with open(CUE_FILE) as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        data = [(int(time), color.strip()) for time, color in reader]
    return data
# Maps timestamps (seconds) => color names (strings)
HUE_CUES = _create_hue_cues()
# Delay in seconds to correct for Chromecast connection time
DELAY = 3


def start_video():
    logger.debug('Starting video')
    cast = pychromecast.get_chromecast(friendly_name=settings.CHROMECAST_NAME)
    cast.wait()
    mc = cast.media_controller
    mc.play_media(VIDEO_FILE, 'video/mp4')


def setup_hue():
    hue = settings.BRIDGE_IP
    return Bridge(hue)

def change_light(bridge, color):
    lights = bridge.get_light_objects(mode='id').values()
    logger.info('Changing color: {}'.format(color))
    for light in lights:
        light.xy = HUE_COLORS[color]

def main():
    start_video()
    bridge = setup_hue()
    sleep(DELAY)
    for index, (time, color) in enumerate(HUE_CUES):
        change_light(bridge, color)
        try:
            next_time = HUE_CUES[index + 1][0]
        except IndexError:  # At last iteration
            continue
        delta = next_time - time
        sleep(delta)

if __name__ == "__main__":
    logging.basicConfig(
        format='[%(name)s]  %(levelname)s: %(message)s',
        level=getattr(logging, settings.LOG_LEVEL)
    )
    main()
