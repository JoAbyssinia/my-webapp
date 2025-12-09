import mediapipe as mp
import numpy as np

class GestureRecognizer:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Emoji mappings for gestures
        self.gesture_emojis = {
            'thumbs_up': '👍',
            'thumbs_down': '👎',
            'peace': '✌️',
            'open_palm': '🖐️',
            'fist': '✊',
            'pointing_up': '👆',
            'ok_sign': '👌',
            'rock_on': '🤘',
            'pinky_up': '🤙',
            'none': '🤔'
        }
    
    def get_finger_states(self, hand_landmarks):
        """
        Determine which fingers are extended.
        Returns a list of booleans [thumb, index, middle, ring, pinky]
        """
        finger_tips = [4, 8, 12, 16, 20]  # Landmark indices for fingertips
        finger_pips = [3, 6, 10, 14, 18]  # Landmark indices for finger PIPs
        
        fingers = []
        landmarks = hand_landmarks.landmark
        
        # Thumb - compare x coordinates (works for right hand)
        # Check if thumb tip is to the left or right of thumb IP joint
        if landmarks[finger_tips[0]].x < landmarks[finger_pips[0]].x:
            fingers.append(True)  # Thumb extended (right hand)
        else:
            fingers.append(False)
        
        # Other fingers - compare y coordinates (tip above pip = extended)
        for i in range(1, 5):
            if landmarks[finger_tips[i]].y < landmarks[finger_pips[i]].y:
                fingers.append(True)
            else:
                fingers.append(False)
        
        return fingers
    
    def is_thumb_up(self, fingers, hand_landmarks):
        """Check if gesture is thumbs up"""
        landmarks = hand_landmarks.landmark
        # Thumb extended, all other fingers closed
        # Also check thumb is pointing upward
        thumb_tip = landmarks[4]
        thumb_base = landmarks[2]
        
        return (fingers[0] and not any(fingers[1:]) and 
                thumb_tip.y < thumb_base.y)
    
    def is_thumb_down(self, fingers, hand_landmarks):
        """Check if gesture is thumbs down"""
        landmarks = hand_landmarks.landmark
        thumb_tip = landmarks[4]
        thumb_base = landmarks[2]
        
        return (fingers[0] and not any(fingers[1:]) and 
                thumb_tip.y > thumb_base.y)
    
    def is_peace(self, fingers):
        """Check if gesture is peace sign (index and middle extended)"""
        return (not fingers[0] and fingers[1] and fingers[2] and 
                not fingers[3] and not fingers[4])
    
    def is_open_palm(self, fingers):
        """Check if all fingers are extended"""
        return all(fingers)
    
    def is_fist(self, fingers):
        """Check if all fingers are closed"""
        return not any(fingers)
    
    def is_pointing_up(self, fingers):
        """Check if only index finger is extended"""
        return (not fingers[0] and fingers[1] and not fingers[2] and 
                not fingers[3] and not fingers[4])
    
    def is_ok_sign(self, hand_landmarks, fingers):
        """Check if gesture is OK sign (thumb and index form circle)"""
        landmarks = hand_landmarks.landmark
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        
        # Calculate distance between thumb and index tips
        distance = np.sqrt((thumb_tip.x - index_tip.x)**2 + 
                          (thumb_tip.y - index_tip.y)**2)
        
        # OK sign: thumb and index close, other fingers extended
        return (distance < 0.05 and fingers[2] and fingers[3] and fingers[4])
    
    def is_rock_on(self, fingers):
        """Check if gesture is rock on (index and pinky extended)"""
        return (not fingers[0] and fingers[1] and not fingers[2] and 
                not fingers[3] and fingers[4])
    
    def is_pinky_up(self, fingers):
        """Check if only pinky is extended"""
        return (not fingers[0] and not fingers[1] and not fingers[2] and 
                not fingers[3] and fingers[4])
    
    def recognize_gesture(self, hand_landmarks):
        """
        Recognize the gesture based on hand landmarks.
        Returns tuple of (gesture_name, emoji)
        """
        fingers = self.get_finger_states(hand_landmarks)
        
        # Check each gesture
        if self.is_ok_sign(hand_landmarks, fingers):
            return 'ok_sign', self.gesture_emojis['ok_sign']
        elif self.is_thumb_up(fingers, hand_landmarks):
            return 'thumbs_up', self.gesture_emojis['thumbs_up']
        elif self.is_thumb_down(fingers, hand_landmarks):
            return 'thumbs_down', self.gesture_emojis['thumbs_down']
        elif self.is_peace(fingers):
            return 'peace', self.gesture_emojis['peace']
        elif self.is_rock_on(fingers):
            return 'rock_on', self.gesture_emojis['rock_on']
        elif self.is_pointing_up(fingers):
            return 'pointing_up', self.gesture_emojis['pointing_up']
        elif self.is_pinky_up(fingers):
            return 'pinky_up', self.gesture_emojis['pinky_up']
        elif self.is_open_palm(fingers):
            return 'open_palm', self.gesture_emojis['open_palm']
        elif self.is_fist(fingers):
            return 'fist', self.gesture_emojis['fist']
        else:
            return 'none', self.gesture_emojis['none']
    
    def process_frame(self, frame):
        """
        Process a frame and return results.
        Returns: (processed_frame, gesture_name, emoji)
        """
        # Convert BGR to RGB
        rgb_frame = frame[:, :, ::-1]
        
        # Process the frame
        results = self.hands.process(rgb_frame)
        
        gesture_name = 'none'
        emoji = self.gesture_emojis['none']
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                self.mp_draw.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS
                )
                
                # Recognize gesture
                gesture_name, emoji = self.recognize_gesture(hand_landmarks)
        
        return frame, gesture_name, emoji
    
    def release(self):
        """Release resources"""
        self.hands.close()
