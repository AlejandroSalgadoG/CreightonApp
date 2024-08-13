from PIL import Image, ImageDraw


def write(image: Image, msg: str, font_size: int = 14) -> Image:
    width, height = image.size
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), msg, font_size=font_size)
    draw.text(((width-w)/2, (height-h)/2), msg, font_size=font_size, fill="black")
    return image


class Cell:
    def __init__(self, pos: int, width: int = 50, height: int = 70):
        self.pos = pos
        self.width = width
        self.height = height

    def build(self) -> Image:
        image = Image.new('RGB', (self.width, self.height))
        ImageDraw.Draw(image).rectangle([0, 0, self.width, self.height], fill="white", outline="black", width=2)
        return image


class TitleCell(Cell):
    def __init__(self, pos: int):
        super().__init__(pos, height=50)
        self.font_size = 14
        self.id = str(self.pos+1)

    def build(self) -> Image:
        image = super().build()
        write(image, self.id, self.font_size)
        return image


class TagCell(Cell):
    pass


class AnnotationCell(Cell):
    pass