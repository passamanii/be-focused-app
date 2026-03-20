# BeFocused

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

The **Be Focused App** is a real-time attention monitoring tool that uses Artificial Intelligence to detect the user's gaze and emit sound alerts when they become distracted. Ideal for students and professionals who want to stay focused during their activities on the computer.


## Features

-   **Gaze Tracking:** Uses MediaPipe Face Landmarker to accurately detect where you are looking.
-   **Distraction Alerts:** If you look away for a set time (e.g., 5 seconds), the app emits a sound alert.
-   **Interactive HUD:** An intuitive interface that shows your current state (*FOCUSED*, *ATTENTION...*, *DISTRACTED!*).
-   **Real-Time Settings Menu:**
    -   Adjust **Volume** of alerts.
    -   Adjust **Sensitivity** of detection.
    -   Adjust **Delay** for sound activation.
    -   Choose between **5 different** alert sounds.


## Technologies Used

-   [Python 3.12+](https://www.python.org/)
-   [OpenCV](https://opencv.org/) for image processing and UI.
-   [MediaPipe](https://mediapipe.dev/) for facial landmark detection.
-   [Pygame](https://www.pygame.org/) for robust audio management.
-   [NumPy](https://numpy.org/) for mathematical calculations.
-   [uv](https://github.com/astral-sh/uv) for dependency management.


## Installation

- You can download the executable in the Releases section.


## How to Use

1.  When launched, the application will open your webcam.
2.  Keep your face visible and look at the screen. The system will mark your eyes and iris.
3.  **Settings:**
    -   Click the **gear icon/top right corner** of the window to open the side menu.
    -   Drag the sliders to adjust Volume, Sensitivity, and Delay.
    -   Click the sound buttons to test and select your preferred alert.
4.  Press `ESC` or close the window to exit.


## Project Structure

```text
be-focused-app/
├── core/                # Main system logic
│   ├── audio_manager.py # Sound management
│   ├── gaze_detector.py # MediaPipe integration
│   ├── gaze_tracking.py # Main loop and business logic
│   ├── ui_components.py # HUD and sliders rendering
│   └── utils.py         # Utility functions (file paths)
├── models/              # ML models (face_landmarker.task)
├── sounds/              # Audio files (.wav)
├── main.py              # Entry point
├── pyproject.toml       # Project configuration and dependencies
└── README.md            # You are here! 
```


## License

This project is licensed under the GNU General Public License v3.0. 
See the LICENSE file for more details.

---

Made by Luís Felipe Passamani Santos, a student passionate about programming.
