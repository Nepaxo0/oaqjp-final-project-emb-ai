from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion(self):
        result_joy = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(result_joy, "joy")

        result_anger = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(result_anger, "anger")

        result_disgust = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(result_disgust, "disgust")

        result_sadness = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(result_sadness, "sadness")

        result_fear = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(result_fear, "fear")

unittest.main()
