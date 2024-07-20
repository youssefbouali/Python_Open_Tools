import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in the frame
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return frame

# Initialize the video capture object
#cap = cv2.VideoCapture("v.mp4")  # 0 is the default camera
cap = cv2.VideoCapture(1)  # 0 is the default camera

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is captured successfully
    if ret:
        # Detect faces in the frame
        frame_with_faces = detect_faces(frame)

        # Display the resulting frame
        cv2.imshow('Face Detection', frame_with_faces)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()
