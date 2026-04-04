import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# read image
model_path = './model/blaze_face_short_range.tflite' 
img_path = './data/Human_image_test.jpg'


# the Face Detector
base_options = python.BaseOptions(model_asset_path=model_path) 
options = vision.FaceDetectorOptions(base_options=base_options)
detector = vision.FaceDetector.create_from_options(options)

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit")

mode = 'blur'

while True:
    ret, img = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Convert to MediaPipe Image
    mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Detect faces
    detection_result = detector.detect(mp_img)

    
    # process detections 
    if detection_result.detections:
        for detection in detection_result.detections:
            bbox = detection.bounding_box
            x,y = int(bbox.origin_x), int(bbox.origin_y)
            w,h = int(bbox.width), int(bbox.height)
            
            h_img, w_img= img.shape[:2]
            
            # ensure valid region
            x,y = max(0, x), max(0, y)
            
            # Clamp width and height
            w = min(w, w_img - x)
            h = min(h, h_img - y)
            
            # Extract face ROI
            face = img[y:y+h, x:x+w]

            if face.size != 0:
                if mode == 'blur':
                    # Apply blur
                    face_processed  = cv2.GaussianBlur(face, (51, 51), 0)
                elif mode == 'pixelate':
                    small = cv2.resize(face, (16, 16), interpolation=cv2.INTER_LINEAR)
                    face_processed = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
                elif mode == 'black':
                    face_processed = np.zeros_like(face)
                
                # Put processed face back
                face_processed = cv2.resize(face_processed, (w, h))
                img[y:y+h, x:x+w] = face_processed
            # draw bounding box
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, f"Mode: {mode}",(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    
    # Show output
    cv2.imshow('Face Anonymizer', img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('b'):
        mode = 'blur'
    elif key == ord('p'):
        mode = 'pixelate'
    elif key == ord('m'):
        mode = 'black'
    
# Cleanup
cap.release()
cv2.destroyAllWindows()

