from compare import *
import numpy as np

# These cutoff's are static calculated based on the provided dataset for optimal performance
Cutoff1=85
Cutoff2=95

# Merges similar fields using fuzzy score
def merge(x):
    building=x[0]
    street=x[1]
    landmark=x[2]
    locality=x[3]
    vtc=x[4]
    district=x[5]
    state=x[6]
    subdistrict = x[7]
    pincode = x[8]
    
    #Merging street and landmark if similar based on fuzzy score
    if(street==street and landmark==landmark):
        if comp(street,landmark)>=Cutoff1:
            street=street
            landmark=''

    #Merging locality and landmark if similar based on fuzzy score
    if(landmark==landmark and locality==locality):
        if comp(landmark,locality)>=Cutoff1:
            landmark=''
            locality=locality

    #Merging street and locality if similar based on fuzzy score
    if(street==street and locality==locality):
        if comp(street,locality)>=Cutoff1:
            street=street
            locality=''

    #Merging vtc and locality if similar based on fuzzy score
    if(vtc==vtc and locality==locality):
        if comp(vtc,locality)>=Cutoff1:
            locality=locality
            vtc=''        
    
    #Merging vtc and district if similar based on fuzzy score
    if(vtc==vtc and district==district):
        if comp(vtc,district)>=Cutoff2:
            district=district
            vtc=''

    lisAddress=[building,street,landmark,locality,vtc,district,state]
    dict={
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
    return dict