from django.db import models
from django.contrib.auth.models import AbstractUser
import json

# Create your models here.
class User(AbstractUser):
  USERTYPE_CHOICES = (
    ('buyer', 'Buyer'),
    ('seller', 'Seller')
  )
  userType = models.CharField(choices=USERTYPE_CHOICES, default='buyer', max_length=9)
  profile_picture = models.ImageField(blank = True, upload_to = 'profile_images', default = 'profile_images/avatar.jpg')
  cover_picture = models.ImageField(blank = True, upload_to = 'cover_pictures', default = 'cover_pictures/cover.jpeg')
  paypal_email_address = models.EmailField()
  
  def getProducts(self):
    if self.userType == 'buyer':
      return self.cart.products.all()
    return self.store.products.all()

  def serialize(self):
    data_to_return = {'id': self.id, 'userName': self.username, 'firstName': self.first_name, 'lastName': self.last_name, 'profilePicture': self.profile_picture.url, 'postsMade': [post.serialize(self) for post in self.posts.order_by('-dateCreated')], 'userType': self.userType, 'accountDetails': self.account.get().serialize(), 'emailAddress': self.email, 'paypalEmail': self.paypal_email_address, 'profile': self.profile.serialize(), 'coverPicture': self.cover_picture.url}
    if self.userType == 'buyer':
      data_to_return['cart'] = self.cart.serialize()
    else:
      data_to_return['products'] = self.store.serialize()
      
    return data_to_return
  
  def __str__(self):
      return self.username
    

class User_profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
  bio = models.CharField(max_length = 200, default='About Me')
  status = models.CharField(max_length = 60, default = 'Currently Available')
  
  def __str__(self):
    return f"{self.user} {self.status}"
  
  def serialize(self):
    return {'bio': self.bio,'status': self.status}