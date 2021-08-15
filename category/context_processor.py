from .models import Category

def category_list(request):
    lists = Category.objects.all()
    return {'lists':lists}