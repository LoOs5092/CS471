from django.shortcuts import render

# Create your views here.
def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def links(request):
 return render(request, "bookmodule/links.html")
def textformats(request):
 return render(request, "bookmodule/text/formatting.html")
def listing(request):
 return render(request, "bookmodule/listing.html")
def table(request):
 return render(request, "bookmodule/table.html")