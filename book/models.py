from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import uuid
from PIL import Image

Biological_Classification = (
    ('kingdom', '界'),
    ('dividion', '门'),
    ('class', '纲'),
    ('order', '目'),
    ('family', '科'),
    ('genus', '属'),
    ('species', '种'),
)

Query_list = (
    ('12S[All Fields]', '12S'),
    ('16S[All Fields]', '16S'),
    ('COI[All Fields]', 'COI'),
    ('CO1[All Fields]', 'CO1'),
    ('COX1[All Fields]', 'COX1'),
)

NCBI_Database_list = (
    ('Assembly', 'Assembly'),
    ('Biocollections', 'Biocollections'),
    ('BioProject', 'BioProject'),
    ('BioSample', 'BioSample'),
    ('Books', 'Books'),
    ('ClinVar', 'ClinVar'),
    ('Conserved Domains', 'Conserved Domains'),
    ('dbGaP', 'dbGaP'),
    ('dbVar', 'dbVar'),
    ('Gene', 'Gene'),
    ('Genome', 'Genome'),
    ('GEO DataSets', 'GEO DataSets'),
    ('GEO Profiles', 'GEO Profiles'),
    ('GTR', 'GTR'),
    ('HomoloGene', 'HomoloGene'),
    ('Identical Protein Groups', 'Identical Protein Groups'),
    ('MedGen', 'MedGen'),
    ('MeSH', 'MeSH'),
    ('NLM Catalog', 'NLM Catalog'),
    ('Nucleotide', 'Nucleotide'),
    ('OMIM', 'OMIM'),
    ('PMC', 'PMC'),
    ('PopSet', 'PopSet'),
    ('Protein', 'Protein'),
    ('Protein Clusters', 'Protein Clusters'),
    ('Protein Family Models', 'Protein Family Models'),
    ('PubChem BioAssay', 'PubChem BioAssay'),
    ('PubChem Compound', 'PubChem Compound'),
    ('PubChem Substance', 'PubChem Substance'),
    ('PubMed', 'PubMed'),
    ('SNP', 'SNP'),
    ('SRA', 'SRA'),
    ('Structure', 'Structure'),
    ('Taxonomy', 'Taxonomy'),
    ('ToolKit', 'ToolKit'),
    ('ToolKitAll', 'ToolKitAll'),
    ('ToolKitBookgh', 'ToolKitBookgh')
)

Dereplicate_Methods = (
    ('strict', '只保留唯一的序列与分类无关'),
    ('single_species', '每个物种保留一个序列'),
    ('uniq_species', '每个物种保留所有唯一序列')
)

Export_Type_List = (
    ('sintax', '用于 VSEARCH 和 USEARCH'),
    ('rdp', '用于 RDP classifier'),
    ('qiif', '用于 QIIME and QIIME2'),
    ('dads', '用于 DADA2'),
    ('dads', '用于 DADA2'),
    ('idt', '用于 IDTAXA')
)

EMBL_Database_list = (
    ('env*', '环境序列'),
    ('fun*', 'fungi'),
    ('hum*', '人类序列'),
    ('inv*', 'invertebrate'),
    ('mam*', 'mammal'),
    ('mus*', 'mouse'),
    ('pln*', 'plant'),
    ('pro*', 'prokaryote'),
    ('rod*', 'rodent'),
    ('vrt*', 'vertebrate')
)

BOOK_STATUS =(
    (0, "On loan"),
    (1, "In Stock"),
)

FLOOR =(
    (1, "1st"),
    (2, "2nd"),
    (3, "3rd"),
)

OPERATION_TYPE =(
    ("success", "Create"),
    ("warning","Update"),
    ("danger","Delete"),
    ("info",'Close')
)

GENDER=(
    ("m","Male"),
    ("f","Female"),
)

BORROW_RECORD_STATUS=(
    (0,'Open'),
    (1,'Closed')
)

PGA_SPEED =(
    ('fast','fast'),
    ('medium','medium'),
    ('slow','slow'),
)

FILTER_METHOD =(
    ('strict', 'strict'),
    ('relaxed', 'relaxed'),
)

VISUAL_METHOD =(
    ('diversity', 'diversity'),
    ('amplicon_length', 'amplicon_length'),
    ('db_completeness', 'db_completeness'),
    ('phylo', 'phylo'),
    ('primer_efficiency', 'primer_efficiency'),
),

#Data Download
class NcbiDownloadModel(models.Model):
    Email_Address = models.EmailField(verbose_name='email', max_length=32)
    Database = models.CharField(verbose_name='database', max_length=100)
    Query = models.CharField(verbose_name='query', max_length=100)
    Batch_Size = models.IntegerField(verbose_name='batch_size')
    OriginalDownloadFile = models.CharField(verbose_name='original', max_length=200)
    SpeciesFile = models.FileField(verbose_name='speciesfile', default='fake_path')

    def __str__(self):
        return self.Email_Address
    def get_absolute_url(self):
        return reverse('ncbi_download_data')
    
    
class MitofishDownloadModel(models.Model):
    OriginalDownloadFile = models.CharField(verbose_name='original', max_length=200)

    def get_absolute_url(self):
        return reverse('mitofish_download_data')


#Sequence
class Primers(models.Model):
    Query = models.CharField(verbose_name="Query",  max_length=100, blank=False)
    Forword_Primer = models.CharField(verbose_name="Forword_Primer", max_length=100, unique=True, blank=False)
    Reverse_Primer = models.CharField(verbose_name="Forword_Primer", max_length=100, unique=True, blank=False)
    Sequence_Quantity = models.PositiveIntegerField(verbose_name="Sequence_quantity", default=0)
    Created_at = models.DateTimeField(verbose_name='Created_at',default=timezone.now)

    def __str__(self):
        return self.Query
    def get_absolute_url(self):
        return reverse('')

class Sequence(models.Model):
    Accession = models.CharField(verbose_name="Accession", max_length=100)
    Taxonomy_ID = models.CharField(verbose_name="Taxonomy_ID", max_length=100)
    Kingdom = models.CharField(verbose_name="Kingdom", max_length=100)
    Dividion = models.CharField(verbose_name="Dividion", max_length=100)
    Class = models.CharField(verbose_name="Class", max_length=100)
    Order = models.CharField(verbose_name="Order", max_length=100)
    Family = models.CharField(verbose_name="Family", max_length=100)
    Genus = models.CharField(verbose_name="Genus", max_length=100)
    Species = models.CharField(verbose_name="Species", max_length=100)
    Sequence_Description = models.CharField(verbose_name="Sequence_Description", max_length=5000, unique=True, )
    Primers = models.ForeignKey(
        Primers,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='Primers'
    )
    Loaction = models.CharField(verbose_name="Loaction",max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(verbose_name='Created_Time',default=timezone.now)

    def __str__(self):
        return self.Taxonomy_ID

    def get_absolute_url(self): 
        return reverse('sequence_list')
    




#Book

class Category(models.Model):
    
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    def get_absolute_url(self): 
        return reverse('category_list')

    # class Meta:
    #     db_table='category'

class Publisher(models.Model):
    
    name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    contact = models.EmailField(max_length=50,blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_by=models.CharField(max_length=20,default='yaozeliang')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('publisher_list')

class Book(models.Model):
    author = models.CharField("Author",max_length=20)
    title = models.CharField('Title',max_length=100)
    created_at = models.DateTimeField('Created Time',default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    total_borrow_times = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=10)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='category'
    )

    publisher=models.ForeignKey(
        Publisher,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='publisher'
    )

    status=models.IntegerField(choices=BOOK_STATUS,default=1)
    floor_number=models.IntegerField(choices=FLOOR,default=1)
    bookshelf_number=models.CharField('Bookshelf Number',max_length=10,default='0001')
    updated_by=models.CharField(max_length=20,default='2112124016')
    description = models.TextField()
    def get_absolute_url(self): 
        return reverse('book_list')
    
    def __str__(self):
        return self.title

class UserActivity(models.Model):
    created_by=models.CharField(default="",max_length=20)
    created_at =models.DateTimeField(auto_now_add=True)
    operation_type=models.CharField(choices=OPERATION_TYPE,default="success",max_length=20)
    target_model = models.CharField(default="",max_length=20)
    detail = models.CharField(default="",max_length=50)

    def get_absolute_url(self): 
        return reverse('user_activity_list')

class Member(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField(default=20)
    gender = models.CharField(max_length=10,choices=GENDER,default='m')

    city = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=50,blank=True)
    phone_number = models.CharField(max_length=30,blank=False)

    created_at= models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=20,default="")
    updated_by = models.CharField(max_length=20,default="")
    updated_at = models.DateTimeField(auto_now=True)

    card_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    card_number = models.CharField(max_length=8,default="")
    expired_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self): 
        return reverse('member_list')
    
    def save(self, *args, **kwargs):
        self.card_number = str(self.card_id)[:8]
        self.expired_at = timezone.now()+relativedelta(years=1)
        return super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# UserProfile
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to="profile/%Y%m%d/", blank=True,null=True)
    phone_number = models.CharField(max_length=30,blank=True)
    email = models.EmailField(max_length=50,blank=True)

    def save(self, *args, **kwargs):
        # 调用原有的 save() 的功能
        profile = super(Profile, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.profile_pic and not kwargs.get('update_fields'):
            image = Image.open(self.profile_pic)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.profile_pic.path)

        return profile

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self): 
        return reverse('home')


# Borrow Record

class BorrowRecord(models.Model):

    borrower = models.CharField(blank=False,max_length=20)
    borrower_card = models.CharField(max_length=8,blank=True)
    borrower_email = models.EmailField(max_length=50,blank=True)
    borrower_phone_number  = models.CharField(max_length=30,blank=True)
    book = models.CharField(blank=False,max_length=20)
    quantity = models.PositiveIntegerField(default=1)

    start_day = models.DateTimeField(default=timezone.now)
    end_day = models.DateTimeField(default=timezone.now()+timedelta(days=7))
    periode = models.PositiveIntegerField(default=0)

    open_or_close = models.IntegerField(choices=BORROW_RECORD_STATUS,default=0)
    delay_days = models.IntegerField(default=0)
    final_status = models.CharField(max_length=10,default="Unknown")

    created_at= models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=20,blank=True)
    closed_by = models.CharField(max_length=20,default="")
    closed_at = models.DateTimeField(auto_now=True)

    @property
    def return_status(self):
        if self.final_status!="Unknown":
            return self.final_status
        elif self.end_day.replace(tzinfo=None) > datetime.now()-timedelta(hours=24):
            return 'On time'
        else:
            return 'Delayed'

    @property
    def get_delay_number_days(self):
        
        if self.delay_days!=0:
            return self.delay_days
        elif self.return_status=='Delayed':
            return (datetime.now()-self.end_day.replace(tzinfo=None)).days
        else:
            return 0


    def get_absolute_url(self): 
        return reverse('record_list')

    def __str__(self):
        return self.borrower+"->"+self.book
    
    def save(self, *args, **kwargs):
        # profile = super(Profile, self).save(*args, **kwargs)
        self.periode =(self.end_day - self.start_day).days+1
        return super(BorrowRecord, self).save(*args, **kwargs)







