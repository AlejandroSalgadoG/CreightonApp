from PIL import Image
from abc import ABC

from visualization.image.observation import Observation
from visualization.image.config import GraphConfig
from visualization.image.cell import ObservationCell, TitleCell


class Row(ABC):
    def __init__(self, config: GraphConfig):
        self.width = config.row_width

    def paint_cells(self, cells: list[Image]) -> Image:
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
    def __init__(self, config: GraphConfig):
        super().__init__(config)
        self.cells = [TitleCell(config, pos) for pos in range(self.width)]

    def build(self) -> Image:
        return self.paint_cells([cell.build() for cell in self.cells])


class ObservationRow(Row):
    def __init__(self, config: GraphConfig, pos: int):
        super().__init__(config)
        self.pos = pos
        self.cells = [ObservationCell(config, pos) for pos in range(self.width)]

    def build(self, observations: list[Observation]) -> Image:
        return self.paint_cells([cell.build(observations) for cell in self.cells])
