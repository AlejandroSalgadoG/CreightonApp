from datetime import date

from visualization.image.observation import Observation
from visualization.image.config import GraphConfig
from visualization.image.graph import Graph
from core.enums import (
    CodeEnum,
    ColorEnum,
    FrequencyEnum,
    ObservationEnum,
)


def get_observations() -> list[Observation]:
    return [
        Observation(
            date=date(2024, 6, 19),
            observation=ObservationEnum.OBS_L.value.code,
            color=ColorEnum.red.value,
            baby=False,
            frequency=FrequencyEnum.FREQ_AD.value.code,
            comment="ap ligero",
        ),
        Observation(
            date=date(2024, 6, 18),
            observation=ObservationEnum.OBS_2.value.code,
            color=ColorEnum.red.value,
            baby=False,
            code=CodeEnum.CODE_B.value.code,
            frequency=FrequencyEnum.FREQ_AD.value.code,
        ),
    ]


if __name__ == "__main__":
    config = GraphConfig()
    graph = Graph(config)
    image = graph.build()
    image.show()
