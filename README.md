# License plate detection with YOLO V8

## Data information

**Folder Data** 

The results of image labeling using label studio are located in the data folder.

**Folder test_images**

These are images for plate detection and trimming tests

## Virtual environments

**Requirements**

Due to library compatibility issues, there are two requirements.txt files.

1. **requirements_train.txt**: This is for model training and validation, related to the documents experimentation_yolo.ipynb and generate_dataset_yolo.ipynb

2. **requirements_time_real.txt**: Compatible libraries to turn on the camera or process videos with the obtained model and run the time_real.py file and perform real-time tests of detection and tracking of Colombian license plates.

## Codes

There are three code documents:

1. **generate_dataset_yolo.ipynb**: It allows you to adjust the labeled data exported from label studio and generates a dataset compatible with YOLO models.

2. **experimentation_yolo.ipynb**: Workflow to train the yolov8 model with your own data, perform tests and record license plates for text extraction.

3. **time_real.py**: Conducting video or real-time testing of Colombian license plates for tracking and detection

# Execution steps

1. Create and activate the virtual training environment using the document requirements_train.txt
2. Run the generate_dataset_yolo.ipynb document
3. Run the experimentation_yolo.ipynb document
4. Deactivate the training environment
5. Create and activate a new virtual environment using the requirements_time_real.txt document
6. Run the time_real.py document