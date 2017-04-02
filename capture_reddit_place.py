#!/usr/bin/env python

# Requirements:
#  * PIL
#  * requests

import datetime
import logging
import requests
from PIL import Image

BITMAP_URL = "https://www.reddit.com/api/place/board-bitmap"
BITMAP_WIDTH = 1000
BITMAP_HEIGHT = 1000

COLOR_MAP = (
  (255, 255, 255),
  (228, 228, 228),
  (136, 136, 136),
  (34, 34, 34),
  (255, 167, 209),
  (229, 0, 0),
  (229, 149, 0),
  (160, 106, 66),
  (229, 217, 0),
  (148, 224, 68),
  (2, 190, 1),
  (0, 211, 221),
  (0, 131, 199),
  (0, 0, 234),
  (207, 110, 228),
  (130, 0, 128),
)

logging.basicConfig(level=logging.INFO)
_log = logging

def get_raw_bitmap_data():
    response = requests.get(BITMAP_URL)
    response.raise_for_status()
    _log.debug("Response size: {}".format(len(response.content)))
    return response.content

def save_as_png(raw_data, file_name):
    img = Image.new('RGB', (BITMAP_WIDTH, BITMAP_HEIGHT), "black")
    pixels = img.load()

    # The raw data returned is a 2-dimensional array of pixel data. Each byte represents 2 pixels. The first
    # 4 bytes are .. ?
    buffer = bytearray()
    buffer.extend(raw_data)
    buffer_index = 4

    for y in xrange(BITMAP_HEIGHT):
        for x in xrange(BITMAP_WIDTH / 2):
            pixel_data = int(buffer[buffer_index])
            pixel1 = pixel_data >> 4
            pixel2 = pixel_data & 0x0f
            pixels[x * 2, y] = COLOR_MAP[pixel1]
            pixels[x * 2 + 1, y] = COLOR_MAP[pixel2]
            buffer_index += 1

    img.save(file_name, "PNG")

def capture_place():
    file_name = datetime.datetime.now().strftime("theplace_%Y%m%d_%H%M%S") + ".png"
    save_as_png(get_raw_bitmap_data(), file_name)

if __name__ == "__main__":
    capture_place()
