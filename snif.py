from scapy.all import *
import pychromecast


def arp_display(pkt):
    cast = pychromecast.get_chromecast(friendly_name="@$$castt")
    cast.wait()
    mc = cast.media_controller

    if pkt[ARP].op == 1:
        if pkt[ARP].psrc == '0.0.0.0':
            if pkt[ARP].hwsrc == '74:75:48:77:51:b2':
                print "Ready to BLING"
                mc.play_media('https://osf.io/zqnyu/?action=download&direct&mode=render', 'video/mp4')

print sniff(prn=arp_display, filter="arp", store=0, count=10)
