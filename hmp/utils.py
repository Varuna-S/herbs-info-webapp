from simple_search import search_filter
from .models import *
from turtledemo import planet_and_moon
import json
from bson import json_util

def search(query,searchBy):
    if(searchBy=="none"):
        search_fields = ['plant_name','com_name','scien_name']
        f=search_filter(search_fields, query)
        plant=Plant.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant)
    elif(searchBy=="division"):
        search_fields = ['div_id__div_name']
        f=search_filter(search_fields, query)
        plant=Plant.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant) 
    elif(searchBy=="class"):
        search_fields = ['cls_id__cls_name']
        f=search_filter(search_fields, query)
        plant=Plant.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant) 
    elif(searchBy=="order"):
        search_fields = ['ord_id__ord_name']
        f=search_filter(search_fields, query)
        plant=Plant.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant)
    elif(searchBy=="family"):
        search_fields = ['fam_id__fam_name']
        f=search_filter(search_fields, query)
        plant=Plant.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant)
    elif(searchBy=="genus"):
        search_fields = ['gen_id__gen_name']
        f=search_filter(search_fields, query)
        plant=Plant.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant)
    elif(searchBy=="species"):
        search_fields = ['spe_id__spe_name']
        f=search_filter(search_fields, query)
        plant=Plant.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant)
    else:
        search_fields = ['mc_id__mc_name']
        f=search_filter(search_fields, query)
        plant=MedicalConditionRecovery.objects.filter(f)
        plantDesc,plantImg=getOtherInfo(plant)
    plantsInfo=[]
    for info,desc,imgs in zip(plant,plantDesc,plantImg):
            print(info.div_id.div_name)
            x=PlantInfo(info.plant_id,info.plant_name,info.scien_name,info.com_name,info.div_id.div_name,info.cls_id.cls_name,info.ord_id.ord_name,info.fam_id.fam_name,info.gen_id.gen_name,info.spe_id.spe_name,desc.description,desc.origin,desc.phytoconstituents,desc.toxicity,desc.contraindications,desc.parts_used,desc.vascular_info,desc.seed_info,desc.flowering_info,desc.used_for_medical_issues,imgs.img,info.slug)
            plantsInfo.append(x)
    return plantsInfo

def getPlantInfo(plant_id):
    plant=Plant.objects.get(plant_id__exact=plant_id)
    plantDesc=PlantDescription.objects.get(plant_id__exact = plant_id)
    plantImg=Image.objects.get(plant_id__exact = plant_id)
    x=PlantInfo(plant.plant_id,plant.plant_name,plant.scien_name,plant.com_name,plant.div_id.div_name,plant.cls_id.cls_name,plant.ord_id.ord_name,plant.fam_id.fam_name,plant.gen_id.gen_name,plant.spe_id.spe_name,plantDesc.description,plantDesc.origin,plantDesc.phytoconstituents,plantDesc.toxicity,plantDesc.contraindications,plantDesc.parts_used,plantDesc.vascular_info,plantDesc.seed_info,plantDesc.flowering_info,plantDesc.used_for_medical_issues,plantImg.img,plant.slug)
    return x
    
    
def getOtherInfo(plant):
    plant_items=set()
    for item in plant:
        plant_items.add(item.plant_id)
    plantDesc=PlantDescription.objects.filter(plant_id__in = plant_items)
    plantImg=Image.objects.filter(plant_id__in = plant_items)
    return plantDesc,plantImg


