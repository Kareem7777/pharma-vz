from django.db import models
# Create your models here.
# class user (models.Model):
#     user_id = models.CharField(primary_key=True,max_length=300,null=False)
#     user_name = models.CharField(max_length=300,null=False)
#     user_email= models.EmailField(max_length=300,null=False,unique=True)
#     user_password = models.CharField(max_length=300,null=False)
class categories(models.Model):
    c_id = models.CharField(primary_key = True , max_length=300,null=False,blank=False)
    c_name = models.CharField(max_length = 80 , null = False , blank = False)

class products (models.Model):
    p_id = models.CharField(primary_key=True,max_length=300,null=False)
    p_name = models.CharField(max_length=300,null=False)
    p_description =  models.CharField(max_length=1000)
    p_price =  models.IntegerField(null=False)
    p_category = models.ForeignKey(categories ,on_delete=models.SET_NULL,null=True,blank = True  )
    p_img = models.ImageField(upload_to = '' ,null = True,blank = True , default = 'default.png')

    def delete(self,*args,**kwargs):
        self.p_img.delete()
        super().delete(*args,**kwargs)
############################################################
class specialties (models.Model):
    specialties_id = models.CharField(primary_key=True,max_length=300,null=False)
    specialties_name = models.CharField(max_length=400,null=False)

class countries (models.Model):
    countries_id = models.CharField(primary_key=True,max_length=300,null=False)
    countries_name = models.CharField(max_length=400,null=False)

class regions (models.Model):
    regions_id = models.CharField(primary_key=True,max_length=300,null=False)
    regions_name = models.CharField(max_length=400,null=False)
    regions_f_countries= models.ForeignKey(countries,on_delete=models.SET_NULL,null=True,blank=True)





