from django.http import HttpResponse


def hello_world(request):
    return HttpResponse(""" <a href='/home'>Home</a> 
    <a href='/about'>About</a> <a href='/my_blog'>My Blog</a> <a href='/project'>Project</a>
    <a href='/contact'>Contact</a>""")

def home(request):
    return HttpResponse("""<a href='/hello_world'>Hello World! <a href='/about'>About</a> 
    <a href='/my_blog'>My Blog</a> <a href='/project'>Project</a> 
    <a href='/contact'>Contact</a>""")

def about(request):
    return HttpResponse("""<a href='/hello_world'>Hello World! </a> <a href='/home'>Home</a>  
    <a href='/my_blog'>My Blog</a> <a href='/project'>Project</a> 
    <a href='/contact'>Contact</a>""")

def my_blog(request):
    return HttpResponse("""<a href='/hello_world'>Hello World! </a>
    <a href='/home'>Home</a> <a href='/about'>About</a> <a href='/project'>Project</a> 
    <a href='/contact'>Contact</a>""")
    
def project(request):
    return HttpResponse("""<a href='/hello_world'>Hello World!</a>
    <a href='/home'>Home</a> <a href='/about'>About</a> 
    <a href='/contact'>Contact</a> <a href='/my_blog'>My Blog</a>""")
    
def contact(request):
    return HttpResponse("""<a href='/hello_world'>Hello World!</a> <a href='/home'>Home</a> 
    <a href='/about'>About</a> <a href='/my_blog'>My Blog</a> 
    <a href='/project'>Project</a>""")
    