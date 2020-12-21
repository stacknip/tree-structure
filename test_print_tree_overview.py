import inspect
from test_tree2 import dispatch
from django.http.response import JsonResponse

def print_overview(klass, parents=True):
    class_tree = inspect.getclasstree([klass])
    node_list = dispatch(class_tree)


print_overview(JsonResponse)
