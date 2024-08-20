from PIL import Image

from visualization.image.config import GraphConfig
from visualization.image.row import ObservationRow, TitleRow


class Grid:
    def __init__(self, config: GraphConfig):
        self.height = config.grid_height
        self.title_row = TitleRow(config)
        self.rows = [ObservationRow(config, pos) for pos in range(self.height)]

    def build(self) -> Image:
        title_row = self.title_row.build()
        rows = [row.build() for row in self.rows]

        width, height = title_row.size
        total_heights = sum([row.size[1] for row in rows])

        image = Image.new('RGB', (width, total_heights + height))

        image.paste(title_row, (0, 0))
        
        y = height
        for row in rows:
            _, height = row.size
            image.paste(row, (0, y))
            y += height

        return image
