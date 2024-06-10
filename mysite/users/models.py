from django.db import models

from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return f'{self.user.username} Profile'