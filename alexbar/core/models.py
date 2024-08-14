from django.db import models
import os

class Section(models.Model):
    name = models.CharField(max_length=22, db_index=True, verbose_name="Section name")
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return "Section: " + self.name

class Category(models.Model):
    name = models.CharField(max_length=26, db_index=True, verbose_name="Category name")
    posts = models.ManyToManyField('Post', null=True, blank=True, related_name="+")

    def __str__(self):
        return "Category: " + self.name

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    position = models.IntegerField(default=0, unique=True, db_index=True, verbose_name="Position")
    name = models.CharField(max_length=20, db_index=True, verbose_name="Name")
    description = models.CharField(max_length=41, blank=True, null=True, db_index=True, verbose_name="Description")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    preview_image = models.ImageField(upload_to='posts/previews/', blank=True)
    small_preview = models.BooleanField(default=False, verbose_name="Small preview")
    slug = models.SlugField(max_length=100, null=False, blank=False, unique=True, db_index=True, verbose_name="URL")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.name} of {self.date}"
    
    def save(self, *args, **kwargs):
        if self.category != None:
            self.category.posts.add(self)
        else:
            cat = Category.objects.all()
            for c in cat:
                c.posts.remove(self)

        if self.position is 0:
            if Post.objects.count() > 0:
                max_position = Post.objects.aggregate(models.Max('position'))['position__max']
                self.position = max_position + 1
            else:
                self.position = 1

        super(Post, self).save(*args, **kwargs) 

    
    def delete(self, *args, **kwargs):
        if self.preview_image:
            if os.path.isfile(self.preview_image.path):
                os.remove(self.preview_image.path)
        
        super(Post, self).delete(*args, **kwargs)

    class Meta:
        ordering = ['date']

# ============================================================
# IDEAS

class Idea(models.Model):
    name = models.CharField(max_length=70, db_index=True, verbose_name="Name")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return f"Idea {self.name} of {self.date}"