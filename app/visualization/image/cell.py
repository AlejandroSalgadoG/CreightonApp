from PIL import Image, ImageDraw

from visualization.image.config import GraphConfig


def write(image: Image, msg: str, font_size: int = 14) -> Image:
    width, height = image.size
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), msg, font_size=font_size)
    draw.text(((width-w)/2, (height-h)/2), msg, font_size=font_size, fill="black")
    return image


class Cell:
    def __init__(self, pos: int, width: int, height: int):
        self.pos = pos
        self.width = width
        self.height = height

    def build(self) -> Image:
        image = Image.new('RGB', (self.width, self.height))
        ImageDraw.Draw(image).rectangle([0, 0, self.width, self.height], fill="white", outline="black", width=2)
        return image


class TitleCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.title_cell_height)
        self.font_size = config.title_font_size
        self.id = str(self.pos+1)

    def build(self) -> Image:
        image = super().build()
        write(image, self.id, self.font_size)
        return image


class TagCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.tag_cell_height)


class AnnotationCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.annotation_cell_height)
