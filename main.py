import cv2
import face_recognition
import pygame
import threading
import time

pygame.mixer.init()

cap = cv2.VideoCapture(0)
sound_played = False

def ring_bell():
    try:
        pygame.mixer.music.load('doorbell.wav')
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy(): 
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Error playing sound: {e}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    faces = face_recognition.face_locations(small_frame)
    
    if faces and not sound_played:
        print("Face Detected! Ringing Bell...")
        threading.Thread(target=ring_bell).start()
        sound_played = True
        
    elif not faces and sound_played:
        print("No Face. Resetting...")
        sound_played = False
        
    # To see around of face (Optional)
    # for (top, right, bottom, left) in faces:
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('Smart Doorbell', frame)
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()