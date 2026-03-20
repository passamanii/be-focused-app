import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from .utils import resource_path

class GazeDetector:
    def __init__(self, model_relative_path='models/face_landmarker.task'):
        """ Inicializa o detector MediaPipe com o modelo especificado """
        model_path = resource_path(model_relative_path)
        with open(model_path, 'rb') as f:
            model_data = f.read()

        base_options = python.BaseOptions(model_asset_buffer=model_data)
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.VIDEO,
            num_faces=1,
            min_face_detection_confidence=0.5,
            min_face_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.detector = vision.FaceLandmarker.create_from_options(options)

    def detect(self, rgb_frame, timestamp_ms):
        """ Processa o frame e retorna o resultado da detecção facial """
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        return self.detector.detect_for_video(mp_image, timestamp_ms)

    def close(self):
        """ Finaliza o detector """
        self.detector.close()
