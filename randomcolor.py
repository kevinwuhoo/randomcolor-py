#!/usr/env/bin python

import colorsys
import random


class RandomColor(object):

    def __init__(self):
        # Shared color dictionary
        self.colorDictionary = {}
        # Populate the color dictionary
        self.load_color_bounds()

    def generate(self, options={}):
        # Check if we need to generate multiple colors
        if "count" in options:
            count = options["count"]
        else:
            count = 1

        colors = []
        for _ in range(count):
            # First we pick a hue (H)
            H = self.pick_hue(options.get("hue", None))

            # Then use H to determine saturation (S)
            S = self.pick_saturation(H, options)

            # Then use S and H to determine brightness (B).
            B = self.pick_brightness(H, S, options)

            # Then we return the HSB color in the desired format
            colors.append(self.set_format([H, S, B], options))

        return colors

    def define_color(self, name, hueRange, lowerBounds):

        sMin = lowerBounds[0][0]
        sMax = lowerBounds[len(lowerBounds) - 1][0]

        bMin = lowerBounds[len(lowerBounds) - 1][1]
        bMax = lowerBounds[0][1]

        self.colorDictionary[name] = {
            'hueRange': hueRange,
            'lowerBounds': lowerBounds,
            'saturationRange': [sMin, sMax],
            'brightnessRange': [bMin, bMax]
        }

    def load_color_bounds(self):

        self.define_color('monochrome', None, [
            [0, 0],
            [100, 0]
        ])

        self.define_color('red', [-26, 18], [
            [20, 100],
            [30, 92],
            [40, 89],
            [50, 85],
            [60, 78],
            [70, 70],
            [80, 60],
            [90, 55],
            [100, 50]
        ])

        self.define_color('orange', [19, 46], [
            [20, 100],
            [30, 93],
            [40, 88],
            [50, 86],
            [60, 85],
            [70, 70],
            [100, 70]
        ])

        self.define_color('yellow', [47, 62], [
            [25, 100],
            [40, 94],
            [50, 89],
            [60, 86],
            [70, 84],
            [80, 82],
            [90, 80],
            [100, 75]
        ])

        self.define_color('green', [63, 178], [
            [30, 100],
            [40, 90],
            [50, 85],
            [60, 81],
            [70, 74],
            [80, 64],
            [90, 50],
            [100, 40]
        ])

        self.define_color('blue', [179, 257], [
            [20, 100],
            [30, 86],
            [40, 80],
            [50, 74],
            [60, 60],
            [70, 52],
            [80, 44],
            [90, 39],
            [100, 35]
        ])

        self.define_color('purple', [258, 282], [
            [20, 100],
            [30, 87],
            [40, 79],
            [50, 70],
            [60, 65],
            [70, 59],
            [80, 52],
            [90, 45],
            [100, 42]
        ])

        self.define_color('pink', [283, 334], [
            [20, 100],
            [30, 90],
            [40, 86],
            [60, 84],
            [80, 80],
            [90, 75],
            [100, 73]
        ])

    def pick_hue(self, hue):
        hueRange = self.get_hue_range(hue)
        hue = self.random_within(hueRange)

        # Instead of storing red as two seperate ranges,
        # we group them, using negative numbers
        if (hue < 0):
            hue = 360 + hue

        return hue

    def pick_saturation(self, hue, options):

        if 'luminocity' in options and options['luminosity'] == 'random':
            return self.random_within([0, 100])

        if options.get('hue') == 'monochrome':
            return 0

        saturationRange = self.get_saturation_range(hue)

        sMin = saturationRange[0]
        sMax = saturationRange[1]

        if 'luminocity' in options and options['luminosity'] == 'bright':
            sMin = 55
        elif 'luminocity' in options and options['luminosity'] == 'dark':
            sMin = sMax - 10
        elif 'luminocity' in options and options['luminosity'] == 'light':
            sMax = 55

        return self.random_within([sMin, sMax])

    def pick_brightness(self, H, S, options):
        bMin = self.get_minimum_brightness(H, S)
        bMax = 100

        if 'luminocity' in options and options['luminosity'] == 'dark':
            bMax = bMin + 20
        elif 'luminocity' in options and options['luminosity'] == 'light':
            bMin = (bMax + bMin) / 2
        elif 'luminocity' in options and options['luminosity'] == 'random':
            bMin = 0
            bMax = 100

        return self.random_within([bMin, bMax])

    def set_format(self, hsv, options):

            if 'format' in options and options['format'] == 'hsvArray':
                return hsv
            elif 'format' in options and options['format'] == 'hsv':
                return self.color_string('hsv', hsv)
            elif 'format' in options and options['format'] == 'rgbArray':
                return colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
            elif 'format' in options and options['format'] == 'rgb':
                return self.color_string('rgb', colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2]))
            else:
                return self.hsv_to_hex(hsv)

    def get_minimum_brightness(self, H, S):

        lowerBounds = self.get_color_info(H)['lowerBounds']

        for i in range(len(lowerBounds)):

            s1 = lowerBounds[i][0]
            v1 = lowerBounds[i][1]

            s2 = lowerBounds[i + 1][0]
            v2 = lowerBounds[i + 1][1]

            if S >= s1 and S <= s2:

                m = (v2 - v1) / (s2 - s1)
                b = v1 - m * s1

                return m * S + b

        return 0

    def get_hue_range(self, color_input):
        if color_input and color_input.isdigit():
            number = int(color_input)

            if number < 360 and number > 0:
                return [number, number]

        elif color_input and color_input in self.colorDictionary:
                color = self.colorDictionary[color_input]
                if 'hueRange' in color:
                    return color['hueRange']

        else:
          return [0, 360]

    def get_saturation_range(self, hue):
        return self.get_color_info(hue)['saturationRange']

    def get_color_info(self, hue):
        # Maps red colors to make picking hue easier
        if hue >= 334 and hue <= 360:
            hue -= 360

        for color_name, color in self.colorDictionary.items():
            if color['hueRange'] and hue >= color['hueRange'][0] and \
               hue <= color['hueRange'][1]:
                return self.colorDictionary[color_name]

        return 'Color not found'

    @classmethod
    def random_within(cls, r):
        return random.choice(range(r[0], r[1] + 1))

    @classmethod
    def hsv_to_hex(cls, hsv):
        h, s, v = hsv
        if h == 0:
            h = 1
        if h == 360:
            h = 359
        h = float(h)/360

        s = float(s)/100
        v = float(v)/100

        rgb = colorsys.hsv_to_rgb(h, s, v)
        r, g, b = [int(c * 255) for c in rgb]
        return '#%02x%02x%02x' % (r, g, b)

    @classmethod
    def color_string(cls, prefix, values):
        return "%s(%s)" % (prefix, ', '.join(values))
