from dataclasses import dataclass


@dataclass(frozen=True)
class GraphConfig:
    vertical_margin: int = 50
    horizontal_margin: int = 50
    grid_height: int = 6
    row_width: int = 35
    cell_width: int = 50
    title_font_size: int = 14
    title_cell_height: int = 50
    observation_cell_height: int = 70


