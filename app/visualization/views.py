from django.http import HttpResponse

from visualization.image.graph import Graph

def index(request):
    graph = Graph()
    image = graph.build()
    image.save("output.jpg")
    return HttpResponse("image generated")