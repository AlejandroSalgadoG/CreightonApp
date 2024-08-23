from PIL import Image
from typing import Optional

from visualization.image.modificators import AnnotationModificator, TagModificator, TitleModificator
from visualization.image.observation import Observation
from visualization.image.config import GraphConfig


class Cell:
    def __init__(self, pos: int, width: int, height: int):
        self.pos = pos
        self.width = width
        self.height = height

    def build_img(self) -> Image:
        return Image.new('RGB', (self.width, self.height))


class TitleCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.title_cell_height)
        self.font_size = config.title_font_size
        self.id = str(self.pos+1)

    def build(self) -> Image:
        return TitleModificator(self.build_img(), self.font_size).write_id(self.id)


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
        modificator = TagModificator(self.build_img())
        return modificator.draw_cell("white") if not observation else modificator.write_tag(observation)


class AnnotationCell(Cell):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(pos, width=config.cell_width, height=config.observation_cell_height)
        self.font_size = config.annotation_font_size

    def build(self, observation: Optional[Observation]) -> Image:
        modificator = AnnotationModificator(self.build_img(), self.font_size)
        return modificator.draw_cell("white") if not observation else modificator.write_annotation(observation)
