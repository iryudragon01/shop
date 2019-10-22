from .models import Item,Top_up

allitem=Item.objects.all()
for item in allitem:
    print(item.name)