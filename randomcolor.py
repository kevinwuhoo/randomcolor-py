#!/usr/env/bin python

import colorsys
import random
import yaml


class RandomColor(object):

    def __init__(self):
        # Load color dictionary and populate the color dictionary
        self.colormap = yaml.load(open('lib/colormap.yaml'))

        for color_name, color_attrs in self.colormap.items():
            lower_bounds = color_attrs['lower_bounds']
            sMin = lower_bounds[0][0]
            sMax = lower_bounds[len(lower_bounds) - 1][0]

            bMin = lower_bounds[len(lower_bounds) - 1][1]
            bMax = lower_bounds[0][1]

            self.colormap[color_name]['saturation_range'] = [sMin, sMax]
            self.colormap[color_name]['brightness_range'] = [bMin, bMax]

    def generate(self, hue=None, luminosity=None, count=1, format_='hex'):
        colors = []
        for _ in range(count):
            # First we pick a hue (H)
            H = self.pick_hue(hue)

            # Then use H to determine saturation (S)
            S = self.pick_saturation(H, hue, luminosity)

            # Then use S and H to determine brightness (B).
            B = self.pick_brightness(H, S, luminosity)

            # Then we return the HSB color in the desired format
            colors.append(self.set_format([H, S, B], format_))

        return colors

    def pick_hue(self, hue):
        hue_range = self.get_hue_range(hue)
        hue = self.random_within(hue_range)

        # Instead of storing red as two seperate ranges,
        # we group them, using negative numbers
        if (hue < 0):
            hue = 360 + hue

        return hue

    def pick_saturation(self, hue, hue_name, luminosity):

        if luminosity == 'random':
            return self.random_within([0, 100])

        if hue_name == 'monochrome':
            return 0

        saturation_range = self.get_saturation_range(hue)

        sMin = saturation_range[0]
        sMax = saturation_range[1]

        if luminosity == 'bright':
            sMin = 55
        elif luminosity == 'dark':
            sMin = sMax - 10
        elif luminosity == 'light':
            sMax = 55

        return self.random_within([sMin, sMax])

    def pick_brightness(self, H, S, luminosity):
        bMin = self.get_minimum_brightness(H, S)
        bMax = 100

        if luminosity == 'dark':
            bMax = bMin + 20
        elif luminosity == 'light':
            bMin = (bMax + bMin) / 2
        elif luminosity == 'random':
            bMin = 0
            bMax = 100

        return self.random_within([bMin, bMax])

    def set_format(self, hsv, format_):

            if format_ == 'hsvArray':
                return hsv
            elif format_ == 'hsv':
                return self.color_string('hsv', hsv)
            elif format_ == 'rgbArray':
                return self.hsv_to_rgb(hsv)
            elif format_ == 'rgb':
                return self.color_string('rgb', self.hsv_to_rgb(hsv))
            else:
                return self.hsv_to_hex(hsv)

    def get_minimum_brightness(self, H, S):

        lower_bounds = self.get_color_info(H)['lower_bounds']

        for i in range(len(lower_bounds)):

            s1 = lower_bounds[i][0]
            v1 = lower_bounds[i][1]

            s2 = lower_bounds[i + 1][0]
            v2 = lower_bounds[i + 1][1]

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

        elif color_input and color_input in self.colormap:
                color = self.colormap[color_input]
                if 'hue_range' in color:
                    return color['hue_range']

        else:
          return [0, 360]

    def get_saturation_range(self, hue):
        return self.get_color_info(hue)['saturation_range']

    def get_color_info(self, hue):
        # Maps red colors to make picking hue easier
        if hue >= 334 and hue <= 360:
            hue -= 360

        for color_name, color in self.colormap.items():
            if color['hue_range'] and hue >= color['hue_range'][0] and \
               hue <= color['hue_range'][1]:
                return self.colormap[color_name]

        # this should probably raise an exception
        return 'Color not found'

    @classmethod
    def random_within(cls, r):
        return random.randint(r[0], r[1])

    @classmethod
    def hsv_to_rgb(cls, hsv):
        h, s, v = hsv
        if h == 0:
            h = 1
        if h == 360:
            h = 359

        h = float(h)/360
        s = float(s)/100
        v = float(v)/100

        rgb = colorsys.hsv_to_rgb(h, s, v)
        return [int(c * 255) for c in rgb]

    @classmethod
    def hsv_to_hex(cls, hsv):
        r, g, b = cls.hsv_to_rgb(hsv)
        return '#%02x%02x%02x' % (r, g, b)

    @classmethod
    def color_string(cls, prefix, values):
        values = [str(x) for x in values]
        return "%s(%s)" % (prefix, ', '.join(values))
