from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, ])
def render_view(request):
    print(request.query_params)

    return Response(request.query_params,template_name='index.html')


@api_view(['POST'])
def data_view(request):
    print(request.data)

    return Response(request.data)


@api_view(['POST'])
def form_data_view(request):
    print(request.data)
    print(request.FILES)

    return Response({})
