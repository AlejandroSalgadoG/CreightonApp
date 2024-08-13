from PIL import Image
from abc import abstractmethod, ABC

from cell import AnnotationCell, Cell, TitleCell, TagCell


class Row(ABC):
    def __init__(self):
        self.width = 35
        self.cells = [self.build_cell(pos) for pos in range(self.width)]

    @abstractmethod
    def build_cell(self, pos: int) -> Cell:
        pass

    def build(self) -> Image:
        cells = [cell.build() for cell in self.cells]
        widths = [cell.size[0] for cell in cells]

        width, height = cells[0].size
        total_width = sum(widths)

        image = Image.new('RGB', (total_width, height))

        x = 0
        for cell in cells:
            image.paste(cell, (x, 0))
            x += width

        return image


class TitleRow(Row):
    def build_cell(self, pos: int) -> Cell:
        return TitleCell(pos)


class ObservationRow:
    def __init__(self, pos: int):
        self.pos = pos
        self.tag_row = TagRow()
        self.annotation_row = AnnotationRow()

    def build(self) -> Image:
        tag_row = self.tag_row.build()
        annotation_row = self.annotation_row.build()

        width, height = tag_row.size
        _, height_annotation = annotation_row.size

        image = Image.new('RGB', (width, height + height_annotation))

        image.paste(tag_row, (0, 0))
        image.paste(annotation_row, (0, height))

        return image


class TagRow(Row):
    def build_cell(self, pos: int) -> Cell:
        return TagCell(pos)


class AnnotationRow(Row):
    def build_cell(self, pos: int) -> Cell:
        return AnnotationCell(pos)
