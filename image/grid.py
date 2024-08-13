from PIL import Image

from row import ObservationRow, TitleRow


class Grid:
    def __init__(self):
        self.height = 6
        self.title_row = TitleRow()
        self.rows = [ObservationRow(pos) for pos in range(self.height)]

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
