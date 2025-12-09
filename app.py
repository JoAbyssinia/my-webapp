from flask import Flask, render_template, Response
import cv2
import time
from gesture_recognition import GestureRecognizer

app = Flask(__name__)

# Global variables
gesture_recognizer = GestureRecognizer()
current_gesture = 'none'
current_emoji = '🤔'

def generate_frames():
    """Generate video frames with gesture recognition"""
    global current_gesture, current_emoji
    
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 30)

    frame_delay = 1.0 / 30  # 30 FPS
    last_frame_time = time.time()

    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # Throttle frames to 30 FPS
        current_time = time.time()
        time_elapsed = current_time - last_frame_time
        if time_elapsed < frame_delay:
            time.sleep(frame_delay - time_elapsed)
        last_frame_time = time.time()

        # Flip frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)
        
        # Process frame for gesture recognition
        frame, gesture_name, emoji = gesture_recognizer.process_frame(frame)
        current_gesture = gesture_name
        current_emoji = emoji
        
        # Add gesture text to frame
        cv2.putText(frame, f'{emoji} {gesture_name}', (10, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    camera.release()

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route"""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/current_gesture')
def get_current_gesture():
    """API endpoint to get current gesture"""
    return {'gesture': current_gesture, 'emoji': current_emoji}

if __name__ == '__main__':
    print("Starting Finger Tracking Emoji App...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
