import logging

from scapy.all import sniff, ARP
import pychromecast
from phue import Bridge

import settings

logger = logging.getLogger(__name__)

VIDEO_FILE = 'https://osf.io/zqnyu/?action=download&direct&mode=render'


def arp_display(pkt):
    cast = pychromecast.get_chromecast(friendly_name=settings.CHROMECAST_NAME)
    cast.wait()
    mc = cast.media_controller

    if pkt[ARP].op == 1:
        if pkt[ARP].psrc == '0.0.0.0':
            if pkt[ARP].hwsrc == settings.DASH_HMAC:
                logger.info('Ready to BLING')
                mc.play_media(VIDEO_FILE, 'video/mp4')


def set_hue_color():
    hue = settings.BRIDGE_IP

    goldenrod = [0.5136, 0.4444]

    bridge = Bridge(hue)
    lights = bridge.get_light_objects(mode='id').values()

    for light in lights:
        light.xy = goldenrod


if __name__ == '__main__':
    sniff(prn=arp_display, filter="arp", store=0, count=10)
    set_hue_color()
