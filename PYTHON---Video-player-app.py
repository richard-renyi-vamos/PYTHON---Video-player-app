import cv2

def play_video(video_path):
    # Create a VideoCapture object to read the video
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('Video Player', frame)

        # Check for the 'q' key to quit the video
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close the video window
    cap.release()
    cv2.destroyAllWindows()

# Replace 'video_path' with the path to your video file
video_path = 'path/to/your/video.mp4'
play_video(video_path)
