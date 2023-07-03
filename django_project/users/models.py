from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship with User model
    image = models.ImageField(default='default.png', upload_to='profile_pics') # upload_to is the directory where the image is stored

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save() # run the save method of the parent class

        img = Image.open(self.image.path) # open the image of the current instance

        if img.height > 300 or img.width > 300: # resize the image if it is too large
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) # save the resized image to the same path
            
