from django.shortcuts import redirect, render
from .models import Article
from .models import FeaturedPost
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-publication_date')
    featured = FeaturedPost.objects.all().order_by('-publication_date')
    return render(request,'index.html',{'featured':featured,'articles':articles})
   # return render(request,'index.html',{'articles':articles})
def signup(request):
   if request.method == "POST":
     #username = request.POST.get('username') tis is a method used to get username attribute from html template file by name
      firstname = request.POST['firstname'] # this is the same methhod as commented above for getting html attributes
      surname= request.POST['surname']
      username = request.POST['username']
      email = request.POST['email']
      dateOfBirth =request.POST['dob']
      gender = request.POST['gender']
      create_pwd =request.POST['password']
      comfirm_pwd = request.POST['comfirm-Password']
      
      if create_pwd != comfirm_pwd:
          return render(request,'signUp.html',{'error':'Passwords do not match'})

      myuser = User.objects.create_user(username,email,create_pwd)
      myuser.first_name =firstname
      myuser.last_name =surname
 
      myuser.save()

      return redirect('signin')

   return render(request ,'signUp.html')    
#signing class   
def signin(request):
    if request.method  =='POST':
        username =request.POST['username']
        password =request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None: #checks if the user was successfully authinticated
            login(request,user)

            return render(request,"index.html")
        else:
            return render(request,'login.html',{'error':'Invalid username or password'}) 
    return render(request,'login.html')
def signout(request):
    logout(request)
    return redirect('home')

#class for comments
def add_comment(request,article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        NameError =request.POST.get('name')
        comment_text =request.POST.get('comment_text')
        rating = int(request.POST.get('rating'))

        #create and save comment
        Comment.objects.create(article=article,name=name,comment_text=comment_text,rating=rating)
        return redirect('/myblogApp/')
       