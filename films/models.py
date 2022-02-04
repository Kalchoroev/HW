from django.db import models


# from

class Films(models.Model):
    GENRE_CHOISE = (
        ('Fantasy', 'Fantasy'),
        ('Detective', 'Detective'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Anime', 'Anime')
    )
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    director = models.CharField(max_length=100)
    genre = models.CharField(choices=GENRE_CHOISE, max_length=100)
    date_filmed = models.DateField(null=True, auto_now_add=True)

class Comment(models.Model):
    text = models.TextField(null=True)
    comment = models.ForeignKey(Films, on_delete=models.CASCADE, related_name="comment", null=True)
    def __str__(self):
        return self.comment