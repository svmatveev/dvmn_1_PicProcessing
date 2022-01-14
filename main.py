from PIL import Image
import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='Image processing parameters')
    parser.add_argument('path', type=str, help='Path to image')
    parser.add_argument('--resolution', type=int, default=80, help='Thumbnail resolution')
    args = parser.parse_args()
    return args

def print_attributes(image: Image):
    width = image.width
    height = image.height
    format = image.mode
 
    print(f"Ширина — {width}\nВысота — {height}\nЦветовая модель — {format}");

def image_crop(image: Image,
                offset_width_l: int,
                offset_height_l: int,
                offset_width_r: int,
                offset_height_r: int) -> Image:
    image_croped = image.crop((offset_width_l,
                                offset_height_l,
                                (image.width - offset_width_r),
                                (image.height - offset_height_r)))
    return image_croped
                
def shift_image_layer(rgb_image: Image,
                    offset: int) -> Image:
    image_red_ch, image_green_ch, image_blue_ch = image_rgb.split()
    image_croped_red = image_crop(image_red_ch, offset*2, 0, 0, 0)
    image_croped_blue = image_crop(image_blue_ch, 0, 0, offset*2, 0)
    image_croped_green = image_crop(image_green_ch, offset, 0, offset, 0)
    img = Image.merge("RGB", (image_croped_red, image_croped_green, image_croped_blue))
    return img

if __name__ == "__main__":

    args = parse_arguments()
    file_path = args.path

    abs_path = os.path.abspath(file_path)
    dir_abs_name = os.path.dirname(abs_path)
    file_name = os.path.basename(abs_path)

    image = Image.open(abs_path)
    image_rgb = image.convert("RGB")
    new_image_full = shift_image_layer(image_rgb, 10)
    new_image_full.save(dir_abs_name + "/" + file_name + "_edited.jpg", "JPEG")

    new_image_full.thumbnail((args.resolution, args.resolution))
    new_image_full.save(dir_abs_name + "/" + file_name + f"_edited_thumbnail_{args.resolution}.jpg", "JPEG")