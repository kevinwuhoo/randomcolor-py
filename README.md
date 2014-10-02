randomcolor
===========

A port of [David Merfield's randomColor](https://github.com/davidmerfield/randomColor)  ([currently davidmerfield/randomColor@4b6b10f](https://github.com/davidmerfield/randomColor/commit/4b6b10f1f012d64987b1853a250f3124470bcb06)) to python.

Usage
-----

Generating a completly random color:
``` python
import randomColor
rand_color = randomcolor.RandomColor()
print rand_color.generate()
```

Generating 3 random blue colors:
``` python
print rand_color.generate({'hue': 'blue', 'count': 3})
```

Refer to the [README at davidmerfield/randomColor](https://github.com/davidmerfield/randomColor/blob/4b6b10f1f012d64987b1853a250f3124470bcb06/README.md) for full usage details.

TODO
----

* Write a simple visual test suite.
* Package
