from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from hmp.models import Plant, Division, Class, Genus ,Order ,Species ,PlantDescription,MedicalCondition,Image,\
    ImageProto,MedicalConditionRecovery, Family
from dataclasses import fields
from betterforms.multiform import MultiModelForm
from multiprocessing.connection import families
from enum import unique

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username', 'email', 'password1','password2'] 
    class Meta:
        model=User
        fields={'username','email','password1','password2'}
        
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None,
            }   
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.username =self.cleaned_data['username']
        user.email=self.cleaned_data['email']
        
        if commit:
            user.save()
            
        return user
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None
            

class PlantForm(forms.ModelForm):
    plant_name=forms.CharField(label='Plant Name', required=False);
    scien_name=forms.CharField(label='Scientific Name', required=True)
    com_name=forms.CharField(label='Common Name', required=False)
    class Meta:
        model=Plant
        fields=('plant_name','scien_name','com_name')
        help_texts = {
            'scien_name': None,
        }
    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)
        for fieldname in ['plant_name','scien_name', 'com_name']:
            self.fields[fieldname].help_text = None    
    
        
        
class DivisionForm(forms.ModelForm):
    div_name=forms.CharField(label='Division', required=False)
    class Meta:
        model=Division
        fields=('div_name',)

class FamilyForm(forms.ModelForm):
    fam_name=forms.CharField(label='Family', required=False)
    class Meta:
        model=Family
        fields=('fam_name',)
        
class ClassForm(forms.ModelForm):
    cls_name=forms.CharField(label='Class', required=False)
    class Meta:
        model=Class
        fields=('cls_name',)

class GenusForm(forms.ModelForm):
    gen_name=forms.CharField(label='Genus', required=False)
    class Meta:
        model=Genus
        fields=('gen_name',)

class OrderForm(forms.ModelForm):
    ord_name=forms.CharField(label='Order', required=False)
    class Meta:
        model=Order
        fields=('ord_name',)

class SpeciesForm(forms.ModelForm):
    spe_name=forms.CharField(label='Species', required=False)
    class Meta:
        model=Species
        fields=('spe_name',)
        
class DescriptionForm(forms.ModelForm):
    description=forms.CharField(label='Description', required=False)
    origin=forms.CharField(label='Origin', required=False)
    phytoconstituents=forms.CharField(label='Phytoconsituents', required=False)
    toxicity=forms.CharField(label='Toxicity', required=False)
    contraindications=forms.CharField(label='Contraindications',required=False)
    parts_used=forms.CharField(label='Parts Used', required=False)
    vascular_info=forms.CharField(label='Vascularity', required=False)
    seed_info=forms.CharField(label='Seed Information', required=False)
    flowering_info=forms.CharField(label='Flowering Information', required=False)
    class Meta:
        model=PlantDescription
        fields=('description','origin','phytoconstituents','toxicity','contraindications','parts_used','vascular_info','seed_info','flowering_info',)
        
class MedicalConditionForm(forms.ModelForm):
    mc_name=forms.CharField(label='Medical Uses', required=False);
    class Meta:
        model=MedicalCondition
        fields=('mc_name',)
        
class ImageForm(forms.ModelForm):
    img=forms.ImageField(label='Upload Image',required=False)
    class Meta:
        model=Image
        fields=('img',)
        labels = {
            'img': 'Image',
        }
class ImageProtoForm(forms.ModelForm):
    imgproto=forms.ImageField(label='Upload Image',)
    class Meta:
        model=ImageProto
        fields=('imgproto',)
        
class MedicalConditionRecoveryForm(forms.ModelForm):
    mcr_id=forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model=MedicalConditionRecovery
        fields=('mcr_id',)
        
class InsertForm(MultiModelForm):
    form_classes={
        'plant':PlantForm,
        'division':DivisionForm,
        'class':ClassForm,
        'order':OrderForm,
        'family':FamilyForm,
        'genus':GenusForm,
        'species':SpeciesForm,
        'description':DescriptionForm,
        'medcondition':MedicalConditionForm,
        'image':ImageForm,
        }
    def save(self, commit=True):
        objects = super(InsertForm, self).save(commit=False)

        if commit:
            div = objects['division']
            if(div.div_name==''):
                try:
                    div=Division.objects.get(div_name__iexact=div.div_name)
                except Division.DoesNotExist:
                    pass
                except Division.MultipleObjectsReturned:
                    pass
            div.save(False)
            cls = objects['class']
            if(cls.cls_name==''):
                try:
                    cls=Class.objects.get(cls_name__iexact=cls.cls_name)
                except Class.DoesNotExist:
                    pass
                except Class.MultipleObjectsReturned:
                    pass
            cls.save(False)
            fam=objects['family']
            if(fam.fam_name==''):
                try:
                    fam=Family.objects.get(fam_name__iexact=fam.fam_name)
                except Family.DoesNotExist:
                    pass
                except Family.MultipleObjectsReturned:
                    pass
            fam.save(False)
            gen=objects['genus']
            if(gen.gen_name==''):
                try:
                    gen=Genus.objects.get(gen_name__iexact=gen.gen_name)
                except Genus.DoesNotExist:
                    pass
                except Genus.MultipleObjectsReturned:
                    pass
            gen.save(False)
            spe=objects['species']
            if(spe.spe_name==''):
                try:
                    spe=Species.objects.get(spe_name__iexact=spe.spe_name)
                except Species.DoesNotExist:
                    pass
                except Species.MultipleObjectsReturned:
                    pass
            spe.save(False)
            ord=objects['order']
            if(ord.ord_name==''):
                try:
                    order=Order.objects.get(ord_name__iexact=ord.ord_name)
                except Order.DoesNotExist:
                    pass
                except Order.MultipleObjectsReturned:
                    pass
            ord.save(False)
            mc=objects['medcondition']
            mc.save(False)
            plant=objects['plant']
            plant.div_id=div
            plant.cls_id=cls
            plant.ord_id=ord
            plant.fam_id=fam
            plant.gen_id=gen
            plant.spe_id=spe
            plant.save(False)
            desc=objects['description']

            desc.plant_id=plant
            desc.save(False)
            img=objects['image']

            img.plant_id=plant
            img.save(False)

        return objects



