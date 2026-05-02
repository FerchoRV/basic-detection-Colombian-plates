import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(xml_path, output_path, classes):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Obtener dimensiones de la imagen
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    with open(output_path, 'w') as f:
        for obj in root.iter('object'):
            cls_name = obj.find('name').text
            if cls_name not in classes:
                continue
            
            cls_id = classes.index(cls_name)
            xmlbox = obj.find('bndbox')
            
            # Coordenadas Pascal VOC
            xmin = float(xmlbox.find('xmin').text)
            ymin = float(xmlbox.find('ymin').text)
            xmax = float(xmlbox.find('xmax').text)
            ymax = float(xmlbox.find('ymax').text)

            # Cálculo de YOLO (Normalizado 0-1)
            x_center = (xmin + xmax) / (2.0 * w)
            y_center = (ymin + ymax) / (2.0 * h)
            width = (xmax - xmin) / w
            height = (ymax - ymin) / h

            # Escribir línea: <class_id> <x_center> <y_center> <width> <height>
            f.write(f"{cls_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

# --- Configuración de rutas ---
input_dir = 'Dataset_Cascos/Labels'
output_dir = 'Dataset_Cascos/Labels_txt'
# Define aquí tus clases en el orden que desees (0, 1, 2...)
class_list = ['helmet'] 

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Procesar archivos
for filename in os.listdir(input_dir):
    if filename.endswith('.xml'):
        xml_file = os.path.join(input_dir, filename)
        txt_file = os.path.join(output_dir, filename.replace('.xml', '.txt'))
        convert_voc_to_yolo(xml_file, txt_file, class_list)

print(f"Proceso completado. Archivos guardados en: {output_dir}")