import cv2
from ultralytics import YOLO

# 1. Cargar tu modelo ajustado
model = YOLO('runs/detect/proyecto_placas/experimento_1-2/weights/best.pt')

# 2. Configurar la fuente de video
# Usa 'ruta/al/video.mp4' para un archivo o 0 para la webcam
video_path = 'placa_video.mp4' 
cap = cv2.VideoCapture(video_path)#o indice de la camara 0 para la webcam

# Verificar si el video abrió correctamente
if not cap.isOpened():
    print("Error al abrir el video")
    exit()

print("Presiona 'q' para salir...")

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        # 3. Realizar la detección
        # stream=True es más eficiente para videos largos
        results = model.track(frame, persist=True, conf=0.4, imgsz=640)
        
        # 4. Visualizar los resultados en el frame
        annotated_frame = results[0].plot()
        
        # Mostrar el frame procesado
        cv2.imshow("YOLOv8 Real-Time Plate Detection", annotated_frame)
        
        # Romper el bucle si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()