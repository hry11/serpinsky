import pyglet
import random
window = pyglet.window.Window(1000, 1000, resizable=True)
pyglet.gl.glClearColor(0, 0, 0, 1)
main_batch = pyglet.graphics.Batch()


def draw_polygon(points):
    """
    draws a polygon
    :param points: list of tuples with vertices coordinates
    :return: list of pyglet.line objects
    """
    lines = list()
    for i in range(len(points)-1):
        lines.append(pyglet.shapes.Line(
            points[i][0], points[i][1],
            points[i+1][0], points[i+1][1], 3, color=(255, 225, 255),
            batch=main_batch))

    lines.append(pyglet.shapes.Line(
        points[-1][0], points[-1][1], points[0][0],
        points[0][1], 3, color=(255, 225, 255),
        batch=main_batch))
    return lines


def equilateral(bp, l):
    """
    returns an equilateral triangle
    :param bp: starting point tuple
    :param l: side length
    :return: list of tuple of vertex coordinates
    """
    points = [bp]
    points.append((bp[0] + l, bp[1]))
    points.append((bp[0] + l/2, bp[1] + l*0.8660254))
    return points


def random_serpinsky(it, tri_vert, bp=None):
    """
    start at any point in the triangle, then chooses a random
    vertex of the triangle, draws a point halfway,
    and repeats the process n times
    :param int it: number of iterations
    :param tri_vert: a tuple of the triangle's vertices
    :param bp: a tuple containing the coordinates of the starting point
    :return: None
    """

    if bp is None:
        bp = (sum([v[0] for v in tri_vert])/3, sum([v[1] for v in tri_vert])/3)

    newpoints = list()
    for i in range(it):
        vertex = random.choice(tri_vert)
        new = ((bp[0] + vertex[0]) / 2, (bp[1] + vertex[1]) / 2)
        bp = new
        newpoints.append(pyglet.shapes.Rectangle(
            x=new[0], y=new[1], width=1, height=1,
            color=(255, 0, 0), batch=main_batch))

    return newpoints


triangle = equilateral((0, 0), 1000)


@window.event
def on_draw():
    window.clear()
    t = draw_polygon(triangle)
    s = random_serpinsky(100000, triangle)
    main_batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
