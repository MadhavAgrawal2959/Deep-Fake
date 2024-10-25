# Deep-Fake
This project implements an AI model that helps in detecting whether a video is a deepfake or not.


This project implements an AI model that helps in detecting whether a video is a deepfake or not. Using cutting-edge machine learning techniques, the model analyzes video frames to identify subtle

artifacts or inconsistencies often present in deepfake videos. The model is trained on a dataset containing real and manipulated videos and is optimized to differentiate between genuine and deepfake content with high accuracy.

Features-
    1.Deepfake Detection: Identifies manipulated videos by detecting anomalies in the visual data.
    2.Frame-Level Analysis: Processes individual frames from a video to detect signs of deepfake tampering.
    3.Real-Time Evaluation: Capable of processing videos for real-time or batch-mode deepfake detection.
    4.Robust Model: Trained on a diverse dataset of real and fake videos to improve generalization across different types of deepfake techniques.

Technologies-
    1.Model Framework: TensorFlow-based model architecture.
    2.Dataset: Trained on publicly available deepfake video datasets.
    3.Preprocessing: Video frames are extracted, resized, and fed into the model for analysis.
    4.Evaluation: Results are evaluated using metrics like accuracy, precision, and recall, specifically tailored for binary classification tasks (real vs. fake).

Setup-
  Requirements-
    1.Python 3.12
    2.Jupyter Notebook
    3.TensorFlow 
    4.OpenCV (for video processing)
    5.NumPy, Pandas, Matplotlib

We are achieving the accuracy of 50%