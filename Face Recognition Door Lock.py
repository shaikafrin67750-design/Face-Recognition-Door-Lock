# Face Recognition Door Lock using Python

# Install required libraries:

# pip install face_recognition opencv-python

import cv2
import face_recognition

# Load the authorized person's image

known_image = face_recognition.load_image_file("authorized_person.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

known_faces = [known_encoding]

# Start webcam

camera = cv2.VideoCapture(0)

print("Face Recognition Door Lock Started...")
print("Press 'q' to exit.")

door_unlocked = False

while True:
ret, frame = camera.read()

```
if not ret:
    print("Camera error!")
    break

# Convert BGR image to RGB
rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Detect faces
face_locations = face_recognition.face_locations(rgb_frame)
face_encodings = face_recognition.face_encodings(
    rgb_frame, face_locations
)

for face_encoding, location in zip(face_encodings, face_locations):

    matches = face_recognition.compare_faces(
        known_faces, face_encoding
    )

    top, right, bottom, left = location

    if True in matches:
        name = "Authorized Person"
        door_unlocked = True

        print("Face recognized!")
        print("Door UNLOCKED")

        cv2.putText(
            frame,
            "DOOR UNLOCKED",
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    else:
        name = "Unknown Person"
        door_unlocked = False

        print("Unknown face detected!")
        print("Door LOCKED")

        cv2.putText(
            frame,
            "DOOR LOCKED",
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Draw rectangle around the face
    cv2.rectangle(
        frame,
        (left, top),
        (right, bottom),
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        name,
        (left, bottom + 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

cv2.imshow("Face Recognition Door Lock", frame)

if cv2.waitKey(1) & 0xFF == ord("q"):
    break
```

camera.release()
cv2.destroyAllWindows()
