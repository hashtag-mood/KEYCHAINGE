from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def blog(request) :
    return render(request, 'blog.html')

def cart(request) :
    return render(request, 'cart.html')

def category(request) :
    return render(request, 'category.html')

def checkout(request) :
    return render(request, 'checkout.html')

def confirmation(request) :
    return render(request, 'confirmation.html')

def contact(request) :
    return render(request, 'contact.html')

def elements(request) :
    return render(request, 'elements.html')

def feature(request) :
    return render(request, 'feature.html')

def login(request) :
    return render(request, 'login.html')

def SingleBlog(request) :
    return render(request, 'single-blog.html')

def SingleProduct(request) :
    return render(request, 'single-product.html')

def tracking(request) :
    return render(request, 'tracking.html')

def head(request) :
    return render(request, 'head.html')

def header(request) :
    return render(request, 'header.html')

def footer(request) :
    return render(request, 'footer.html')