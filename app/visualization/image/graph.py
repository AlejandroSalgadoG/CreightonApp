from PIL import Image

from visualization.image.grid import Grid


class Graph:
    def __init__(self):
        self.vertical_margin = 50
        self.horizontal_margin = 50
        self.grid = Grid()

    def build(self) -> Image:
        grid_image = self.grid.build()
        grid_height, grid_width = grid_image.size

        image_height = grid_height + self.vertical_margin * 2
        image_width = grid_width + self.horizontal_margin * 2

        image = Image.new('RGB', (image_height, image_width))
        image.paste(grid_image, (self.horizontal_margin, self.vertical_margin))
        return image
