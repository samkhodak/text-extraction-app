"""
This file contains any utility functions that deal with image encoding/drawing.
"""

from PIL import Image
import base64
import io


def encode_image(image):
    """
    Takes an image object and encodes it into base64 binary. 
    :param image: werkzeug.FileStorage object
    :return: base64 bytes

    """
    im = Image.open(image)
    data = io.BytesIO()
    im.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return encoded_img_data