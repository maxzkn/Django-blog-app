from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):  # inherit from models.Model
    # now create one-to-one relationship with the existing User model and create a user associated with our Profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # if the user is deleted from db, delete profile
    # additional fields:
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    # default.jpg is the default pic that every
    # user will have and upload_to is the directory that images are uploaded to when we upload a profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # Max Profile

    def save(self):  # is a method that gets run after our model is saved (it already exists in our parent class, so
                     # we're gonna override it
        # first let's run save method of our parent class using super():
        super().save()  # parent's class save() method will run when we save an instance of this profile (save the
                        # large image)
        # now we will grab the image that is saved and resize it (import Image form PIL first).
        # now open the image for the instance that we're saving:
        img = Image.open(self.image.path)  # open image of the current instance
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)  # tuple of max sizes
            # https://djangosaur.tumblr.com/post/422589280/django-resize-thumbnail-image-pil
            img.thumbnail(output_size)  # resize, thumbnail keeps the aspect ratio of the image and scales it to the defined area
            img.save(self.image.path)  # save to same path 'self.image.path' to override large image
            # we can delete old images if we want also


