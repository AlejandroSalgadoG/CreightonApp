from visualization.image.config import GraphConfig
from visualization.image.graph import Graph


if __name__ == "__main__":
    config = GraphConfig()
    graph = Graph(config)
    image = graph.build()
    image.show()
