# Dashing

Playing hotline bling with dash buttons, python, chromecast, and magic

Conceived with TONS of help from this blog post:
https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8

----------

## Setup

- ``pip install -r requirements.txt``
- ``cp .env.example .env``
- Set your Dash button HMAC, bridge IP and chromecast friendly name in .env.

## New feature:
### Play hotline bling with your HUE lights to match the video
- Set dash button HMAC in local settings
- Set HUE bridge IP in local settings
- run lights.py in a python3 environment
- Sit back and watch the magic
