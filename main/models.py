from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField('Home name', max_length=50)
    about = models.TextField('Home about')
    img1 = models.ImageField('Home img1', upload_to='media')
    img2 = models.ImageField('Home img2', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'



class HomeProduct(models.Model):
    name = models.CharField('HomeProduct name', max_length=50)
    name2 = models.CharField('HomeProduct name2', max_length=50, null=True)
    price = models.IntegerField('HomeProduct price')
    price2 = models.IntegerField('HomeProduct price2', null=True)
    img = models.ImageField('HomeProduct img', upload_to='media')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct'
        verbose_name_plural = 'HomeProducts'




class HomeProduct1(models.Model):
    img = models.ImageField('HomeProduct1 img', upload_to='media')
    name = models.CharField('HomeProduct1 name', max_length=50)
    price = models.IntegerField('HomeProduct1 price')
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct1'
        verbose_name_plural = 'HomeProducts1'




class HomeProduct2(models.Model):
    img = models.ImageField('HomeProduct2 img', upload_to='media')
    name = models.CharField('HomeProduct2 name', max_length=50)
    price = models.IntegerField('HomeProduct2 price')
    
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeProduct2'
        verbose_name_plural = 'HomeProducts2'



class ShopProduct(models.Model):
    img = models.ImageField('ShopProduct img', upload_to='media')
    name = models.CharField('ShopProduct  name', max_length=50)
    price = models.IntegerField('ShopProduct  price')
     

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ShopProduct'
        verbose_name_plural = 'ShopProducts'



class Eror404(models.Model):
    img1 = models.ImageField('Eror 404 img1', upload_to='media',null=True)
    img2 = models.ImageField('Eror 404 img2', upload_to='media', null=True)
    name1 = models.CharField('Eror 404 name1', max_length=50)
    about = models.TextField('Eror 404 about')
    name2 = models.CharField('Eror 404 name2', max_length=50)
    

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Eror 404'
        verbose_name_plural = 'Erors 404'



class Checkout(models.Model):
    about = models.TextField('Checkout about')
    img1 = models.ImageField('Checkout img1', upload_to='media')
    img2 = models.ImageField('Checkout img2', upload_to='media')
    img3 = models.ImageField('Checkout img3', upload_to='media')
    
    

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'Chekcout'
        verbose_name_plural = 'Chekcouts'



class Footer(models.Model):
    about = models.TextField('Footer about')
    img = models.ImageField('Footer img', upload_to='media')
    name1 = models.CharField('Footer name1', max_length=50)
    name2 = models.CharField('Footer name2', max_length=50)

    
    

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'


class Category(models.Model):
    name = models.CharField('Category name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Shoose(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catshoose')
    name = models.CharField('Shoose name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shoose'
        verbose_name_plural = 'Shooses'


class Category2(models.Model):
    name = models.CharField('Category2 name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category2'
        verbose_name_plural = 'Categorys2'




class Brand(models.Model):
    name = models.CharField('Brand name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'



class Blog(models.Model):
    img1 = models.ImageField('Blog img1', upload_to='media')
    name1 = models.CharField('Blog name1', max_length=50)
    about = models.TextField('Blog about')


    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'



class BlogSingle(models.Model):
    name1 = models.CharField('BlogSingle name1', max_length=50)
    img1 = models.ImageField('BlogSingle img1', upload_to='media')
    about1 = models.TextField('BlogSingle about1')
    about2 = models.TextField('BlogSingle about2')
    about3 = models.TextField('BlogSingle about3')
    about4 = models.TextField('BlogSingle about4')
    


    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'BlogSingle'
        verbose_name_plural = 'BlogSingles'



class BlogSingle2(models.Model):
    name = models.CharField('BlogSingle2 name', max_length=50, null=True)
    img = models.ImageField('BlogSingle2 img', upload_to='media')
    about = models.TextField('BlogSingle2 about')
    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'BlogSingle2'
        verbose_name_plural = 'BlogSingles2'



class Cart(models.Model):
    name = models.CharField('Cart name', max_length=50)
    img = models.ImageField('Cart img', upload_to='media')
    about = models.TextField('Cart about')
    price = models.IntegerField('Cart  price')

    


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class Product(models.Model):
    name = models.CharField(("Detail Name"), max_length=100)
    image = models.ImageField(("Detail Photo"), upload_to='media')
    price = models.IntegerField(("Price"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'detail'
        verbose_name_plural = 'details'