#!/usr/env/bin python

import os
import colorsys
import random
import json
import sys


class RandomColor(object):

    def __init__(self, seed=None):
        # Load color dictionary and populate the color dictionary
        with open(os.path.join(os.path.dirname(__file__), 'lib/colormap.json')) as fh:
            self.colormap = json.load(fh)

        self.seed = seed if seed else random.randint(0, sys.maxsize)
        self.random = random.Random(self.seed)

        for color_name, color_attrs in self.colormap.items():
            lower_bounds = color_attrs['lower_bounds']
            s_min = lower_bounds[0][0]
            s_max = lower_bounds[len(lower_bounds) - 1][0]

            b_min = lower_bounds[len(lower_bounds) - 1][1]
            b_max = lower_bounds[0][1]

            self.colormap[color_name]['saturation_range'] = [s_min, s_max]
            self.colormap[color_name]['brightness_range'] = [b_min, b_max]

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
            hue += 360

        return hue

    def pick_saturation(self, hue, hue_name, luminosity):

        if luminosity == 'random':
            return self.random_within([0, 100])

        if hue_name == 'monochrome':
            return 0

        saturation_range = self.get_saturation_range(hue)

        s_min = saturation_range[0]
        s_max = saturation_range[1]

        if luminosity == 'bright':
            s_min = 55
        elif luminosity == 'dark':
            s_min = s_max - 10
        elif luminosity == 'light':
            s_max = 55

        return self.random_within([s_min, s_max])

    def pick_brightness(self, H, S, luminosity):
        b_min = self.get_minimum_brightness(H, S)
        b_max = 100

        if luminosity == 'dark':
            b_max = b_min + 20
        elif luminosity == 'light':
            b_min = (b_max + b_min) / 2
        elif luminosity == 'random':
            b_min = 0
            b_max = 100

        return self.random_within([b_min, b_max])

    def set_format(self, hsv, format_):
        if 'hsv' in format_:
            color = hsv
        elif 'rgb' in format_:
            color = self.hsv_to_rgb(hsv)
        elif 'hex' in format_:
            r, g, b = self.hsv_to_rgb(hsv)
            return '#%02x%02x%02x' % (r, g, b)
        else:
            return "unrecognized format"

        if "Array" in format_ or format_ == 'hex':
            return color
        else:
            prefix = format_[:3]
            color_values = [str(x) for x in color]
            return "%s(%s)" % (prefix, ', '.join(color_values))

    def get_minimum_brightness(self, H, S):
        lower_bounds = self.get_color_info(H)['lower_bounds']

        for i in range(len(lower_bounds) - 1):
            s1 = lower_bounds[i][0]
            v1 = lower_bounds[i][1]

            s2 = lower_bounds[i + 1][0]
            v2 = lower_bounds[i + 1][1]

            if s1 <= S <= s2:
                m = (v2 - v1) / (s2 - s1)
                b = v1 - m * s1

                return m * S + b

        return 0

    def get_hue_range(self, color_input):
        if color_input and color_input.isdigit():
            number = int(color_input)

            if 0 < number < 360:
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
        if 334 <= hue <= 360:
            hue -= 360

        for color_name, color in self.colormap.items():
            if color['hue_range'] and color['hue_range'][0] <= hue <= color['hue_range'][1]:
                return self.colormap[color_name]

        # this should probably raise an exception
        return 'Color not found'

    def random_within(self, r):
        return self.random.randint(int(r[0]), int(r[1]))

    @classmethod
    def hsv_to_rgb(cls, hsv):
        h, s, v = hsv
        h = 1 if h == 0 else h
        h = 359 if h == 360 else h

        h = float(h)/360
        s = float(s)/100
        v = float(v)/100

        rgb = colorsys.hsv_to_rgb(h, s, v)
        return [int(c * 255) for c in rgb]
