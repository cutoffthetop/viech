import numpy as np
import sklearn as sk
from PIL import Image, ImageDraw, ImageFont


class Mesh(list):

    def __init__(self, xy):
        self.start = xy

    def lineto(self, xy):
        if len(self):
            prev = self[-1][1]
        else:
            prev = self.start
        self.append(np.array([prev, xy]))


def construct():
    mesh = Mesh([.60, .10])
    mesh.lineto([.10, .70])
    mesh.lineto([.10, .90])
    mesh.lineto([.90, .90])
    mesh.lineto([.90, .80])
    mesh.lineto([.85, .40])
    mesh.lineto([.60, .10])
    return mesh


def render(mesh, size=800, margin=20):
    img = Image.new('RGB', (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for line in mesh:
        xy = line * np.array([size, size])
        draw.line(np.hstack(xy).tolist(), fill=(0, 255, 0), width=1)
        for p in [0, 1]:
            pos = (xy[p] + [5, 0])
            title = '{:.2f}, {:.2f}'.format(*line[p])
            draw.text(pos.tolist(), title, fill=(255, 0, 0))
    bounds = (size + 2 * margin, size + 2 * margin)
    frame = Image.new('RGB', bounds, (255, 255, 255))
    frame.paste(img, (margin, margin))
    return frame


def main():
    mesh = construct()
    img = render(mesh)
    img.show()
