from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    # Overriding the string representation of the object in the table.
    
    def __str__(self):
        return f'{self.title} from {self.year}'