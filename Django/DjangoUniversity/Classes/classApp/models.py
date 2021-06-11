from django.db import models

Classes_AVAIL = (
    ('beginner', 'beginner'),
    ('intermediate', 'intermediate'),
    ('advanced', 'advanced'),
)

course = (
    (0o34, 0o34),
    (0o335, 0o335),
    (0o366, 0o366),
)


class DjangoClasses(models.Model):
    pass
    title = models.CharField(max_length=60, choices=Classes_AVAIL),
    courseNumber = models.IntegerField(max_length=20, choices=course),
    instructorName = models.CharField(max_length=60),
    classDuration = models.DecimalField(default=1.0),

    objects = models.Manager()

    def __str__(self):
        return self.instructorName
