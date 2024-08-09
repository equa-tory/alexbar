from django.db import models
import os

class Section(models.Model):
    name = models.CharField(max_length=22, db_index=True, verbose_name="Section name")
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return "Section: " + self.name

class Category(models.Model):
    name = models.CharField(max_length=26, db_index=True, verbose_name="Category name")
    posts = models.ManyToManyField('Post', related_name="+")

    def __str__(self):
        return "Category: " + self.name

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    position = models.IntegerField(default=0, unique=True, db_index=True, verbose_name="Position")
    name = models.CharField(max_length=35, db_index=True, verbose_name="Name")
    description = models.CharField(max_length=41, db_index=True, verbose_name="Description")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    preview_image = models.ImageField(upload_to='posts/previews/', null=False, blank=False)
    slug = models.SlugField(max_length=100, null=False, blank=False, unique=True, db_index=True, verbose_name="URL")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.name} of {self.date}"
    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        self.category.posts.add(self)
    
    def delete(self, *args, **kwargs):
        if self.preview_image:
            if os.path.isfile(self.preview_image.path):
                os.remove(self.preview_image.path)
        
        super(Post, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['date']