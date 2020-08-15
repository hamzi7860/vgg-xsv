import os, csv
import pandas as pd, numpy as np
from PIL import Image

def vgg_2_csv(src_dir, base_dir):
    src_dir = 'D:/BS-EE/CONVSYS_Internship/Python_Scripts/vgg_2_xsv_new/'
    csv_file = os.path.join(src_dir, 'Final(1969).csv')

    base_dir = 'D:/BS-EE/CONVSYS_Internship/Python_Scripts/vgg_2_xsv_new/'
    if not os.path.isdir(base_dir):
        os.makedirs(base_dir)
    img_dir = os.path.join(base_dir, 'JPEGImages')
    if not os.path.isdir(img_dir):
        os.makedirs(img_dir)
    csv_file_v2 = open(os.path.join(base_dir, 'labels.csv'), 'w')

    csvreader = csv.reader(open(csv_file, 'r'))
    next(csvreader)
    class_names = []
    sex_names = []
    color_names = []
    design_pattern = []
    type_names = []
    material_names = []
    size_shape = []    
    
    for row in csvreader:
        if row[0] == 'filename':
            continue
        print(row)
        coord = row[5]
        x1 = coord.split(',')[1].split(':')[1]
        y1 = coord.split(',')[2].split(':')[1]
        width = coord.split(',')[3].split(':')[1]
        height = coord.split(',')[4].split(':')[1]
        height = height.replace('}','')
        x2 = str(int(x1) + int(width))
        y2 = str(int(y1) + int(height))

        class_name = row[6].split(',')[0].split(':')[1].replace('/', '_').replace('"','')
        if not class_name in class_names:
            class_names.append(class_name)
        
        sex = row[6].split(',')[1].split(':')[1].replace('"','')
        if not sex in sex_names:
            sex_names.append(sex)
        
        color = row[6].split(',')[2].split(':')[1].replace('"','')
        if not color in color_names:
            color_names.append(color)
        
        design = row[6].split(',')[3].split(':')[1].replace('"','')
        if not design in design_pattern:
            design_pattern.append(design)
            
        types = row[6].split(',')[4].split(':')[1].replace('"','')
        if not types in type_names:
            type_names.append(types)
        
        material = row[6].split(',')[5].split(':')[1].replace('"','')
        if not material in material_names:
            material_names.append(types)
        
        size = row[6].split(',')[6].split(':')[1].replace('}','')
        if not size in size_shape:
            size_shape.append(types)
        

        csv_file_v2.write(row[0]+','+x1+','+y1+','+x2+','+y2+','+class_name+','+sex+','+color+','+design+','+types+','+material+','+size+'\n')
    csv_file_v2.close()
    class_names = sorted(j.strip() for j in class_names)
    class_names_dict = {i:cn for i, cn in enumerate(class_names)}
    print(class_names_dict)

vgg_2_csv('D:/BS-EE/CONVSYS_Internship/Python_Scripts/vgg_2_xsv_new/', 'D:/BS-EE/CONVSYS_Internship/Python_Scripts/vgg_2_xsv_new/')


