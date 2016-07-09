import randomcolor
import random


def main():

    hues = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink',
            'monochrome', 'random']
    luminosities = ['bright', 'light', 'dark', 'random']
    formats = ['rgb', 'hex']

    colors = []
    rand_color = randomcolor.RandomColor(42)

    rand = random.Random(42)
    rand_int = lambda: rand.randint(4, 10)

    colors.append(('one random color', rand_color.generate()))

    i = rand_int()
    colors.append((
        "%d random colors" % i,
        rand_color.generate(count=i)
    ))

    # test all hues
    for hue in hues:
        i = rand_int()
        colors.append((
            "%d random colors with %s hue" % (i, hue),
            rand_color.generate(hue=hue, count=i)
        ))

    # test all luminosities
    for luminosity in luminosities:
        i = rand_int()
        colors.append((
            "%d random colors with %s luminosity" % (i, luminosity),
            rand_color.generate(luminosity=luminosity, count=i)
        ))

    # test random combinations
    for _ in range(50):
        i = rand_int()
        hue = random.choice(hues)
        luminosity = random.choice(luminosities)
        format_ = random.choice(formats)
        colors.append((
            "%d random colors with %s hue, %s luminosity, and %s format"
                % (i, hue, luminosity, format_),
            rand_color.generate(hue=hue, luminosity=luminosity,
                                format_=format_, count=i)
        ))

    color_rows = colors_to_rows(colors)
    html = generate_html(color_rows)
    with open('randomcolors.html', 'w') as f:
        f.write(html)


def colors_to_rows(colors):
    s = ""
    for color_name, colors in colors:
        s += "<tr>"
        s += "<td>%s</td>" % (color_name)
        s += "<td>"
        for color in colors:
            s += "<div class='color' style='background-color:%s'></div>" % color
        s += "</td>"
        s += "</tr>"

    return s


def generate_html(table_rows):
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>randomcolor test</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
      .color {
        height: 30px;
        width: 30px;
        border-radius: 30px;
        display: inline-block;
      }
    </style>
  </head>

  <body>
  <div class="container">
    <div class="row col-md-10 col-md-offset-1">
    <h1>Random Color Test</h1>
    <table class="table">
      %s
    </table>
  </div>
  </body>
</html>
    """ % table_rows

if __name__ == "__main__":
    main()
