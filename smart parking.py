import cv2
import numpy as np

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    # Perform image processing to detect parking spot occupancy
    # For this example, let's say a parking spot is occupied if there's a car with specific color characteristics
    # You can use more advanced object detection techniques, machine learning, or deep learning for better accuracy

    # Example: Find red cars in the frame
    lower_red = np.array([0, 0, 100])
    upper_red = np.array([100, 100, 255])
    mask = cv2.inRange(frame, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Count the number of white pixels in the result
    white_pixels = cv2.countNonZero(mask)

    if white_pixels > 1000:  # Adjust the threshold as needed
        print("Parking spot occupied")
        # Here, you can implement further actions, like updating a database or sending a notification
    else:
        print("Parking spot vacant")

    # Display the processed frame
    cv2.imshow("Smart Parking", result)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
