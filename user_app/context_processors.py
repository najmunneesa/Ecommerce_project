from django.apps import apps

def cart_count(request):
    CartItem = apps.get_model('user_app', 'CartItem')
    if request.user.is_authenticated:
        count = CartItem.objects.filter(user=request.user).count()
        return {'cart_count': count}
    return {'cart_count': 0}
