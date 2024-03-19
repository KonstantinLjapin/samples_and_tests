from PIL import Image, ImageDraw, ImageFont
import cowsay

cow: str = cowsay.get_output_string('cow', 'Hello World')
sw: int = len(cow.splitlines())
lw: int = len(cow.splitlines()[0])
image = Image.new("RGB", (180, 160), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.text((0, 0), cow, (10, 10, 10))
print(sw, lw)
image.show()


