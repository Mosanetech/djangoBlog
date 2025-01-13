from django.db import models

# Create your models here.
#articles class
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    reading_time =models.PositiveIntegerField(help_text="Reading time in minutes")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   # articleImg = models.URLField()

    def __str__ (self):
        return self.title

#featured post class
class FeaturedPost(models.Model):
    mainImg =models.URLField()
    maintitle = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    paragraph = models.TextField()
    authorImg =models.URLField()
    username =models.CharField(max_length=100)
    publication_date =models.DateField()
    reading_time=models.PositiveBigIntegerField(help_text="Reading time in minutes")
    def __str__ (self):
        return self.title    
    #signup class
class SignUp(models.Model):
        first_name =models.CharField(max_length=30)
        last_name =models.CharField(max_length=30)
        username =models.CharField(max_length=50 ,unique=True)
        dateObirth =models.DateField()
        Gender_Choices =[
             ('male','Male'),('female','Female')
        ]
        gender=models.CharField(max_length=6,choices=Gender_Choices)
        email =models.EmailField(unique=True)
        password = models.CharField(max_length=225)

        def __str__(self):
             return self.username
#login class
class Login(models.Model):
     
     def __str__(self):
          return     
     #comment section
class Comment(models.Model):
           article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments') #link to article
           name = models.CharField(max_length=100)
           comment_text = models.TextField()
           rating = models.PositiveSmallIntegerField(choices=[(i,i) for i in range(1,6)])
           created_at =models.DateTimeField(auto_now_add=True)  

           def __str__(self):
                 return f"Comment by {self.name} on {self.article.title}"