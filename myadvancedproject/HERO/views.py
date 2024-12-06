from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to My Advanced Project</h1><p>Discover the features of this application!</p>")

def gallery_view(request):
    return HttpResponse("<h1>Gallery</h1><p>Explore a collection of images and artworks.</p>")

def blog_view(request):
    return HttpResponse("<h1>Blog</h1><p>Read our latest blog posts and articles.</p>")

def team_view(request):
    return HttpResponse("<h1>Our Team</h1><p>Meet the brilliant minds behind this project.</p>")

def testimonials_view(request):
    return HttpResponse("<h1>Testimonials</h1><p>See what our users have to say about us.</p>")
