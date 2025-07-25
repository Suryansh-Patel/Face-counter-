# import cv2

# # Load the pre-trained Haar Cascade classifier for face detection
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Initialize webcam
# cap = cv2.VideoCapture(0)

# # Check if the camera opened successfully
# if not cap.isOpened():
#     print("Error: Could not open camera.")
#     exit()

# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Error: Failed to grab frame.")
#         break
    
#     # Flip the frame horizontally for mirror view
#     frame = cv2.flip(frame, 1)
    
#     # Convert to grayscale (Haar Cascade works on grayscale images)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detect faces in the grayscale image
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
#     # Start a counter for faces
#     i = 0
#     for (x, y, w, h) in faces:
#         # Increment face count for each detected face
#         i += 1
        
#         # Draw a rectangle around the face
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
#         # Display face count near the face
#         cv2.putText(frame, f'Face {i}', (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#         print(f"Face {i}: x={x}, y={y}, w={w}, h={h}")
    
#     # Display the resulting frame
#     cv2.imshow('Face Detection', frame)
    
#     # Quit with the "q" key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the capture and destroy windows
# cap.release()
# cv2.destroyAllWindows()



import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab frame.")
        break
    
    # Flip the frame horizontally for mirror view
    frame = cv2.flip(frame, 1)
    
    # Get frame dimensions (height, width)
    height, width, _ = frame.shape
    
    # Convert to grayscale (Haar Cascade works on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Start a counter for faces
    i = 0
    for (x, y, w, h) in faces:
        # Increment face count for each detected face
        i += 1
        
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display face count near the face
        cv2.putText(frame, f'Face {i}', (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(f"Face {i}: x={x}, y={y}, w={w}, h={h}")
        
        # Calculate the area of the face
        face_area = w * h
        
        # Calculate the total area of the frame
        frame_area = width * height
        
        # Calculate the percentage of the frame that the face occupies
        face_percentage = (face_area / frame_area) * 100
        
        # If the face occupies 60% or more of the frame, display a message
        if face_percentage >= 60:
            cv2.putText(frame, "Face occupies >= 60% of frame", (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Display the resulting frame
    cv2.imshow('Face Detection', frame)
    
    # Quit with the "q" key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
