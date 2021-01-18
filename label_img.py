import os
import json
from bounding_box import boundingBox

vott_path = "/home/thomas/Computer Vision/Labelling_images_with_VoTT/vott_tags"
tags_path = "/home/thomas/Computer Vision/Labelling_images_with_VoTT/tags"

def waste_tag(type):
    if type == "glass":
        return 0
    if type == "bags":
        return 1
    if type == "wood":
        return 2

dir = os.listdir(os.path.join(vott_path))
for k in range(len(dir)):
    file = open(os.path.join(vott_path, dir[k]),)
    data = json.load(file)
    fileName = os.path.join(tags_path, data["asset"]["name"] + ".txt")
    txtFile =  open(fileName, "w+")
    for region in data["regions"]:
        bounding_box = boundingBox(waste_tag(region["tags"][0]), 
                                    region["boundingBox"]["left"] + region["boundingBox"]["width"]/2, 
                                    region["boundingBox"]["top"] + region["boundingBox"]["height"]/2 , 
                                    region["boundingBox"]["width"], 
                                    region["boundingBox"]["height"])
        txtFile.write('{} {} {} {} {}'.format(bounding_box.type, bounding_box.x, bounding_box.y, bounding_box.w, bounding_box.h) + "\r\n")
    

