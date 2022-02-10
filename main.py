import argparse
from pathlib import Path

from PIL import Image


def parse_arguments():
    parser = argparse.ArgumentParser(description='Image processing parameters')
    parser.add_argument('path', type=str, help='Path to image')
    parser.add_argument('--resolution',
                        type=int,
                        default=80,
                        help='Thumbnail resolution')
    parser.add_argument('--precision',
                        type=int,
                        default=10,
                        help='Thumbnail resolution 0 <= precision <= 100.\
                              Restricted with that range if other values \
                              specified')
    args = parser.parse_args()
    return args


def crop_image(image: Image,
               left_width_offset: int,
               right_width_offset: int) -> Image:
    cropped_image = image.crop((left_width_offset,
                                0,
                                image.width - right_width_offset,
                                image.height))
    return cropped_image


def main():
    args = parse_arguments()

    file_path = args.path
    origin_file_path = Path(file_path)
    dir_abs_name = origin_file_path.parent
    file_name = origin_file_path.name

    image = Image.open(origin_file_path)
    image = image.convert("RGB")

    precision = args.precision
    if precision >= 100:
        precision = 100
    elif precision <= 0:
        precision = 0
    offset = int(image.width / 100 * precision)

    red_image_ch, green_image_ch, blue_image_ch = image.split()
    red_cropped_image = Image.blend(crop_image(red_image_ch, offset * 2, 0),
                                   crop_image(red_image_ch, offset, offset),
                                   .5)
    blue_cropped_image = Image.blend(crop_image(blue_image_ch, 0, offset * 2),
                                    crop_image(blue_image_ch, offset, offset),
                                    .5)
    green_cropped_image = crop_image(green_image_ch, offset, offset)
    image = Image.merge("RGB", (red_cropped_image,
                                green_cropped_image,
                                blue_cropped_image))

    image.save(str(Path(dir_abs_name, file_name + "_edited.jpg")), "JPEG")
    image.thumbnail((args.resolution, args.resolution))
    image.save(str(Path(dir_abs_name,
               file_name +
               f"_edited_thumbnail_{args.resolution}.jpg")),
               "JPEG")


if __name__ == "__main__":
    main()
