from django.db import models
from slugify import slugify
from bson.json_util import default

class Class(models.Model):
    class Meta:
        db_table = 'class'
    cls_id=models.AutoField(primary_key=True)
    cls_name=models.TextField()
    
class Division(models.Model):
    class Meta:
        db_table='division'
    div_id=models.AutoField(primary_key=True)
    div_name=models.TextField()

class Family(models.Model):
    class Meta:
        db_table='family'
    fam_id=models.AutoField(primary_key=True)
    fam_name=models.TextField()
    
class Genus(models.Model):
    class Meta:
        db_table='genus'
    gen_id=models.AutoField(primary_key=True)
    gen_name=models.TextField()

class Species(models.Model):
    class Meta:
        db_table='species'
    spe_id=models.AutoField(primary_key=True)
    spe_name=models.TextField()
    
class Order(models.Model):
    class Meta:
        db_table='orders'
    ord_id=models.AutoField(primary_key=True)
    ord_name=models.TextField()
    
class MedicalCondition(models.Model):
    class Meta:
        db_table='med_condition'
    mc_id=models.AutoField(primary_key=True)
    mc_name=models.TextField()
    
class Plant(models.Model):
    class Meta:
        db_table='plant'
    plant_id=models.AutoField(primary_key=True)
    plant_name=models.TextField()
    scien_name=models.TextField()
    com_name=models.TextField(blank=True)
    div_id=models.ForeignKey(Division, on_delete=models.CASCADE)
    cls_id=models.ForeignKey(Class,on_delete=models.CASCADE,default='')
    ord_id=models.ForeignKey(Order,on_delete=models.CASCADE,default='')
    fam_id=models.ForeignKey(Family,on_delete=models.CASCADE,default='')
    gen_id=models.ForeignKey(Genus,on_delete=models.CASCADE,default='')
    spe_id=models.ForeignKey(Species,on_delete=models.CASCADE,default='')
    slug = models.SlugField(unique=False)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.scien_name)
        super(Plant, self).save(*args, **kwargs)

class PlantDescription(models.Model):
    class Meta:
        db_table='plant_description'
    plant_id=models.ForeignKey(Plant,on_delete=models.CASCADE,default='')
    description=models.TextField()
    origin=models.TextField()
    phytoconstituents=models.TextField()
    toxicity=models.TextField()
    contraindications=models.TextField()
    used_for_medical_issues=models.TextField()
    parts_used=models.TextField()
    vascular_info=models.TextField()
    seed_info=models.TextField()
    flowering_info=models.TextField()

class MedicalConditionRecovery(models.Model):
    class Meta:
        db_table='med_condition_recovery'
    mcr_id=models.AutoField(primary_key=True)
    plant_id=models.ForeignKey(Plant,on_delete=models.CASCADE,default='')
    mc_id=models.ForeignKey(MedicalCondition,on_delete=models.CASCADE,default='')
    

    
class Image(models.Model):
    class Meta: 
        db_table='image'
    img_id=models.AutoField(primary_key=True)
    img=models.ImageField(upload_to='images/',blank=True)
    plant_id=models.ForeignKey(Plant,on_delete=models.CASCADE,default='')
    
class ImageProto(models.Model):
    class Meta:
        db_table='imageproto'
    imgproto=models.ImageField(upload_to='images/',blank=True)
        

class PlantInfo:
    def __init__(self,plant_id,plant_name,scien_name,com_name,div_name,cls_name,ord_name,fam_name,gen_name,spe_name,description,origin,phytoconstituents,toxicity,contraindications,parts_used,vascular_info,seed_info,flowering_info,used_for_medical_issues,img,slug):
        self.plant_id=plant_id
        self.plant_name=plant_name
        self.scien_name=scien_name
        self.com_name=com_name
        self.div_name=div_name
        self.cls_name=cls_name
        self.ord_name=ord_name
        self.fam_name=fam_name
        self.gen_name=gen_name
        self.spe_name=spe_name
        self.description=description
        self.origin=origin
        self.phytoconstituents=phytoconstituents
        self.toxicity=toxicity
        self.contraindications=contraindications
        self.parts_used=parts_used
        self.vascular_info=vascular_info
        self.seed_info=seed_info
        self.flowering_info=flowering_info
        self.used_for_medical_issues=used_for_medical_issues
        self.img=img
        self.slug=slug

        

        
        
        

    

    
    
    
    
    
    
    
    
    
    