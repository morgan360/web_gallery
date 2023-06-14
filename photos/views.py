from django.shortcuts import render, redirect
from .models import Category, Photo
from .forms import CustomUserCreationForm


# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all
    else:
        photos = Photo.objects.filter(
            category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories , 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})


def add_photo(request):
    if request.method == 'POST':
        data = request.POST
        category = Category.objects.get(id=data['category'])
        image = request.FILES.get('image')
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('photos:gallery')
    categories = Category.objects.all
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)
