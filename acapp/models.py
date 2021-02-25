from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):   
    user = models.OneToOneField(User,on_delete=models.CASCADE) ##關聯到原本的資料庫
    
    phone = models.CharField(max_length=11, verbose_name="手機號碼")
    job_title = models.CharField(max_length=100, verbose_name="職稱")
    id_card = models.CharField(max_length=12, verbose_name="身分證字號")
    # portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username
    
class postBlog(models.Model): 
    authBlogId=models.ForeignKey(Member,verbose_name='隸屬身份',on_delete=models.CASCADE)     #關聯立委的id
    #Blogid=models.AutoField(auto_created = True, primary_key = True)
    blog_title=models.CharField('標題名稱',max_length=255)         #標題名稱
    blog_content=models.TextField('標題內容',blank=True)         #標題內容
    #photo = models.URLField(blank=True)
    photo=models.ImageField(upload_to='image/', blank=False, null=False)
    blog_created_at=models.DateTimeField(auto_now = True)    #節點發建立時間  (自動獲取目前時間)
    
    def __str__(self):
        return self.blog_title