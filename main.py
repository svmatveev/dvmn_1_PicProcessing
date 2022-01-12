from PIL import Image

def print_attributes(image: Image):
    width = image.width
    height = image.height
    format = image.mode
    #ame = image.filename
 
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
                
                                 

if __name__ == "__main__":
    image = Image.open("monro.jpg")
    image_rgb = image.convert("RGB")

    image_red_ch, image_green_ch, image_blue_ch = image_rgb.split()

    image_merged = Image.merge("RGB", (image_red_ch, image_green_ch, image_blue_ch))
    image_merged.save("image_merged.jpg")
    
    offset = 10
    image_croped_red = image_crop(image_red_ch, offset*2, 0, 0, 0)
    # image_red_ch = Image.blend(image_red_ch, image_croped_red, .5)
    # image_red_ch.save("image_red_ch.jpg")

    image_croped_blue = image_crop(image_blue_ch, 0, 0, offset*2, 0)
    # image_blue_ch = Image.blend(image_blue_ch, image_croped_blue, .5)
    # image_red_ch.save("image_blue_ch.jpg")

    image_croped_green = image_crop(image_green_ch, offset, 0, offset, 0)
    # image_blue_ch = Image.blend(image_blue_ch, image_croped_blue, .5)
    # image_red_ch.save("image_blue_ch.jpg")

    print_attributes(image_croped_red)
    print_attributes(image_croped_blue)
    print_attributes(image_croped_green)
    
    new_image = Image.merge("RGB", (image_croped_red, image_croped_green, image_croped_blue))
    new_image.save("shifted_monro.jpg")
