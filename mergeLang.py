import numpy as np
from translate import *
from compare import *

# These cutoff's are static calculated based on the provided dataset for optimal performance
Cutoff1=83
Cutoff2=95

# Merges similar fields using fuzzy score
def mergeLang(x):
    building=x[0]
    street=x[1]
    landmark=x[2]
    locality=x[3]
    vtc=x[4]
    district=x[5]
    state=x[6]
    subdistrict = x[7]
    pincode = x[8]
    langcode=x[9]
    
    lis = [street,landmark,locality,vtc,district,state]
    converted = transToEng(lis, langcode)
    if(type(converted) is not dict):
        return np.nan
    streetEng=converted['street']
    landmarkEng=converted['landmark']
    localityEng=converted['locality']
    vtcEng=converted['vtc']
    districtEng=converted['district']
    stateEng=converted['state']
    
    #Merging street and landmark if similar based on fuzzy score
    if(street==street and landmark==landmark):
        if comp(streetEng,landmarkEng)>=Cutoff1:
            street=street
            landmark=''

    #Merging locality and landmark if similar based on fuzzy score
    if(landmark==landmark and locality==locality):
        if comp(landmarkEng,localityEng)>=Cutoff1:
            landmark=''
            locality=locality

    #Merging street and locality if similar based on fuzzy score
    if(street==street and locality==locality):
        if comp(streetEng,localityEng)>=Cutoff1:
            street=street
            locality=''

    #Merging vtc and locality if similar based on fuzzy score
    if(vtc==vtc and locality==locality):
        if comp(vtcEng,localityEng)>=Cutoff1:
            locality=locality
            vtc=''        
    
    #Merging vtc and district if similar based on fuzzy score
    if(vtc==vtc and district==district):
        if comp(vtcEng,districtEng)>=Cutoff2:
            district=district
            vtc=''

    lisAddress=[building,street,landmark,locality,vtc,district,state]
    
    outputAddress={
            "house": building,
            "street": street,
            "landmark": landmark,
            "locality": locality,
            "vtc": vtc,
            "district": district,
            "state": state,
            "subdistrict" : subdistrict,
            "pincode": pincode
        }

    # add=""
    # for i in lisAddress:
    #     if(i==i):
    #         add=add+i+","
    return outputAddress