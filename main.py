from PIL import Image

def print_attributes(image: Image):
    width = image.width
    height = image.height
    format = image.mode
    name = image.filename
 
    print(f"Наименование — {name}\nШирина — {width}\nВысота — {height}\nЦветовая модель — {format}");

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
    
    image_croped = image_crop(image_rgb, 50, 0, 0, 0)
    image_croped.save("image_croped.jpg")
    