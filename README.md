randomcolor [![Build Status](https://travis-ci.org/kevinwuhoo/randomcolor-py.svg?branch=master)](https://travis-ci.org/kevinwuhoo/randomcolor-py)
===========

A port of [David Merfield's randomColor](https://github.com/davidmerfield/randomColor)  ([currently davidmerfield/randomColor@0.4.4](https://github.com/davidmerfield/randomColor/releases/tag/0.4.4)) to python. Tested against python versions 2.6, 2.7, 3.2, 3.3, 3.4, 3.5, pypy, and pypy3.

Usage
-----

Generating a completely random color:
``` python
import randomcolor
rand_color = randomcolor.RandomColor()
print(rand_color.generate())
```

Generating 3 random blue colors:
``` python
print(rand_color.generate(hue="blue", count=3))
```

Refer to the [tests for examples](https://github.com/kevinwuhoo/randomcolor-py/blob/master/tests/test_randomcolor.py) and [README at davidmerfield/randomColor](https://github.com/davidmerfield/randomColor/blob/0.4.4/README.md) for full usage details.

Tests
-----

Run `python setup.py test` to run the test suite with stored expected colors
generated from a seeded randomcolor object.

Run `python tests/test_randomcolor_visual.py` to generate an html page with random
colors generated from using this package. Open `randomcolors.html` to confirm
that the colors fall within the parameters pased in. This is in addition to unit
tests since it's much easier to visually confirm that the colors generated
are correct than determine correctness programatically.
