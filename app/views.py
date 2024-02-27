from django.shortcuts import render, redirect

from .models import NewsPost, Category, Contact, Franchise, Resume


def home(request):
    return render(request, 'home/home.html')


def menu(request):
  category = Category.objects.all()
  context = {
      'category': category,
  }

  return render(request, 'menu/menu.html', context=context)


def news(request):
    posts = NewsPost.objects.all()

    allowed_ids = []
    for post in posts:
        if post.id % 2 == 0:
            allowed_ids.append(post.id)

    context = {
        'posts': posts,
        'allowed_ids': allowed_ids,
    }

    return render(request, 'news/news.html', context=context)


def career(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        message = request.POST.get('message')
        file = request.FILES['file']

        Resume.objects.create(name=name, phone=phone, email=email, city=city, message=message, file=file)

        return redirect(to='career')

    return render(request, 'career/career.html')


def franchise(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        Franchise.objects.create(name=name, phone=phone)

        return redirect(to='franchise')

    return render(request, 'franchise/franchise.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        message = request.POST.get('message')

        Contact.objects.create(name=name, phone=phone, email=email, city=city, message=message)

        return redirect(to='contact')

    return render(request, 'contact/contact.html')
