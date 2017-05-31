import logging
from scipy import misc
from scipy import ndimage

import pylab

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("gtk")

_logger = logging.getLogger(__name__)


class ImageConverter:
    def __init__(self, img):
        self.name = img
        self.image = misc.imread(img, mode="RGB")
        self.gray_image = misc.imread(img, mode="L")

    def to_ndarray(self):
        _logger.info("nd array shape  = {}".format(self.image.shape))
        return self.image

    def to_gray(self):
        _logger.info("nd array shape  = {}".format(self.gray_image.shape))
        misc.imsave('data/sample1-gray.jpg', self.gray_image)
        return self.gray_image

    def to_gray_blur(self):
        _logger.info("Blurring gray image")
        im = ndimage.gaussian_filter(self.gray_image, sigma=3)
        misc.imsave('data/sample1-gray-blur.jpg', im)

    def to_blur(self):
        _logger.info("Blurring image")
        im = ndimage.gaussian_filter(self.image, sigma=1.2)
        misc.imsave('data/sample1-blur.jpg', im)

    def to_sharpen(self):
        blurred_f = ndimage.gaussian_filter(self.image, 0.5)
        filter_blurred_f = ndimage.gaussian_filter(self.image, 0.1)
        alpha = 3
        sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)
        misc.imsave('data/sample1-sharp.jpg', sharpened)
