from tortoise.models import Model
from tortoise import fields



class Author(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    desc = fields.TextField()
    img = fields.BinaryField()


    def __str__(self) -> str:
        return self.name
    

class Tag(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)


    def __str__(self) -> str:
        return self.name
    

class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)


    def __str__(self) -> str:
        return self.name
    

class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    content = fields.TextField()
    img = fields.BinaryField()
    # author = fields.ForeignKeyField('models.Author', related_name='author', on_delete=fields.CASCADE)
    # category = fields.OneToOneField('models.Category', related_name='category', on_delete=fields.NO_ACTION)
    # tags = fields.ManyToManyField('models.Tag', related_name='tags')

    def __str__(self) -> str:
        return self.title
    

class ImageModel(Model):
    id = fields.IntField(pk=True)
    image_data = fields.BinaryField()

