#!/usr/bin/env python
import random
import colorsys
from PIL import Image, ImageDraw, ImageChops


def random_color():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)


def interpolate(start_color, end_color, factor: float):
    reciprocal = 1 - factor
    return (
        int(start_color[0] * reciprocal + end_color[0] * factor),
        int(start_color[1] * reciprocal + end_color[0] * factor),
        int(start_color[2] * reciprocal + end_color[0] * factor)
    )


def generate_art(path: str):
    print("================================================")
    print("Let's generate an NFT!")
    print("===============================================\n")

    start_color = random_color()
    end_color = random_color()
    target_size = 128
    scale_factor = 2
    padding_px = 17 * scale_factor
    image_size = target_size * scale_factor
    image_bg_color = (0, 0, 0)
    image_mode = 'RGB'
    image = Image.new(mode=image_mode, size=(
        image_size, image_size), color=image_bg_color)

    # Draw lines
    draw = ImageDraw.Draw(image)
    points = []

    # Generate the points
    for i in range(10):
        random_point = (random.randint(padding_px, image_size - padding_px),
                        random.randint(padding_px, image_size - padding_px))

        points.append(random_point)

    # Draw bounding box
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    # Center the image
    delta_x = min_x - (image_size - max_x)
    delta_y = min_y - (image_size - max_y)

    for i, point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y // 2)

    # Draw the points
    line_width = 0
    n_points = len(points) - 1
    for i, point in enumerate(points):
        # Overlay canvas
        overlay_image = Image.new(mode=image_mode, size=(
            image_size, image_size), color=image_bg_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        p1 = point

        if i == n_points:
            p2 = points[0]
        else:
            p2 = points[i+1]

        line_xy = (p1, p2)
        color_factor = i / n_points
        line_color = interpolate(start_color, end_color, color_factor)
        line_width += 1 * scale_factor

        overlay_draw.line(xy=line_xy, fill=line_color, width=line_width)
        image = ImageChops.add(image, overlay_image)

    image.resize((target_size, target_size), resample=Image.ANTIALIAS)
    image.save(path)


def main():
    for i in range(10):
        generate_art(f'{i}.png')


if __name__ == '__main__':
    main()
