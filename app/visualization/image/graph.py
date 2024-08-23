from PIL import Image

from visualization.image.observation import Observation
from visualization.image.config import GraphConfig
from visualization.image.grid import Grid


class Graph:
    def __init__(self, config: GraphConfig):
        self.vertical_margin = config.vertical_margin
        self.horizontal_margin = config.horizontal_margin
        self.grid = Grid(config)

    def build(self, observations: list[Observation]) -> Image:
        grid_image = self.grid.build(observations)
        grid_height, grid_width = grid_image.size

        image_height = grid_height + self.vertical_margin * 2
        image_width = grid_width + self.horizontal_margin * 2

        image = Image.new('RGB', (image_height, image_width))
        image.paste(grid_image, (self.horizontal_margin, self.vertical_margin))
        return image
