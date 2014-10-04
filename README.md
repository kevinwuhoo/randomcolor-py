randomcolor
===========

A port of [David Merfield's randomColor](https://github.com/davidmerfield/randomColor)  ([currently davidmerfield/randomColor@4b6b10f](https://github.com/davidmerfield/randomColor/commit/4b6b10f1f012d64987b1853a250f3124470bcb06)) to python.

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

Refer to the [README at davidmerfield/randomColor](https://github.com/davidmerfield/randomColor/blob/4b6b10f1f012d64987b1853a250f3124470bcb06/README.md) for full usage details.

Tests
-----
Run `python test_randomcolor.py` to generate an html page with random colors
generated from using this package. Open `randomcolors.html` to confirm that
the colors fall within the parameters pased in. This is in lieu of standard
unit tests since it's much easier to visually confirm that the colors generated
are correct than determine correctness programatically.
