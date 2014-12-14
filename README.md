randomcolor
===========

A port of [David Merfield's randomColor](https://github.com/davidmerfield/randomColor)  ([currently davidmerfield/randomColor@58f5a89](https://github.com/davidmerfield/randomColor/commit/58f5a8963ae41bd9c1ca567921df3cf6be48e374)) to python.

Usage
-----

Generating a completly random color:
``` python
import randomcolor
rand_color = randomcolor.RandomColor()
print rand_color.generate()
```

Generating 3 random blue colors:
``` python
print rand_color.generate(hue="blue", count=3)
```

Refer to the [tests for examples](https://github.com/kevinwuhoo/randomcolor-py/blob/master/test_randomcolor.py) and [README at davidmerfield/randomColor](https://github.com/davidmerfield/randomColor/blob/58f5a8963ae41bd9c1ca567921df3cf6be48e374/README.md) for full usage details.

Tests
-----
Run `python test_randomcolor.py` to generate an html page with random colors
generated from using this package. Open `randomcolors.html` to confirm that
the colors fall within the parameters pased in. This is in lieu of standard
unit tests since it's much easier to visually confirm that the colors generated
are correct than determine correctness programatically.
