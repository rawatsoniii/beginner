from simpleimage import SimpleImage

def main():
    image_name = input("Please enter an image file: ")
    image = SimpleImage(image_name)
    for pixel in image():
        sepia_pixel(pixel)
    image.show()

def sepia_pixel(pixel):
    R = pixel.red
    G = pixel.green
    B = pixel.blue
    pixel.red = 0.393 * R + 0.769 * G + 0.189 * B
    pixel.green = 0.349 * R + 0.686 * G + 0.168 * B
    pixel.blue = 0.272 * R + 0.534 * G + 0.131 * B

if __name__ == '__main__':
    main()
