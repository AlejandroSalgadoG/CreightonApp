from PIL import Image, ImageDraw
from typing import Optional

from visualization.image.observation import Observation
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

    def build_empty(self, color="white") -> Image:
        image = Image.new('RGB', (self.width, self.height))
        ImageDraw.Draw(image).rectangle([0, 0, self.width, self.height], fill=color, outline="black", width=2)
        return image


class TitleCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.title_cell_height)
        self.font_size = config.title_font_size
        self.id = str(self.pos+1)

    def build(self) -> Image:
        image = super().build_empty()
        write(image, self.id, self.font_size)
        return image


class ObservationCell:
    def __init__(self, config: GraphConfig, pos: int):
        self.tag_cell = TagCell(config, pos)
        self.annotation_cell = AnnotationCell(config, pos)

    def build(self, observations: list[Observation]) -> Image:
        observation = observations.pop() if observations else None

        tag_image = self.tag_cell.build(observation)
        annotation_image = self.annotation_cell.build(observation)

        width, height = tag_image.size
        image = Image.new('RGB', (width, height*2))

        image.paste(tag_image, (0, 0))
        image.paste(annotation_image, (0, height))

        return image


class TagCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.observation_cell_height)

    def build(self, observation: Optional[Observation]) -> Image:
        if not observation:
            return super().build_empty()
        return super().build_empty(color=observation.color)


class AnnotationCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.observation_cell_height)

    def build(self, observation: Optional[Observation]) -> Image:
        image = super().build_empty()
        if not observation:
            return image
        return write(image, observation.frequency, 14)
