import os
import shutil
from sklearn.model_selection import train_test_split

# Configuración de rutas
data_path = 'Dataset_cascos/Images'
labels_path = 'Dataset_cascos/Labels_txt'
output_base = 'dataset_yolo_cascos'

# Crear estructura de carpetas
for split in ['train', 'val']:
    os.makedirs(f'{output_base}/{split}/images', exist_ok=True)
    os.makedirs(f'{output_base}/{split}/labels', exist_ok=True)

# Obtener lista de imágenes
images = [f for f in os.listdir(data_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
train_imgs, val_imgs = train_test_split(images, test_size=0.4, random_state=42)

def move_files(files, split):
    for f in files:
        # Mover imagen
        shutil.copy(os.path.join(data_path, f), f'{output_base}/{split}/images/{f}')
        # Mover label correspondiente (mismo nombre pero .txt)
        label_file = os.path.splitext(f)[0] + '.txt'
        if os.path.exists(os.path.join(labels_path, label_file)):
            shutil.copy(os.path.join(labels_path, label_file), f'{output_base}/{split}/labels/{label_file}')

move_files(train_imgs, 'train')
move_files(val_imgs, 'val')

print("Dataset organizado en la carpeta 'dataset_yolo'")