# 🔔 Automated Smart Doorbell (Face Detection)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey?style=for-the-badge)
![Dependency Manager](https://img.shields.io/badge/Poetry-Recommended-purple?style=for-the-badge&logo=poetry&logoColor=white)

A high-performance **Smart Doorbell System** powered by Computer Vision. It detects human faces in real-time using a webcam and automatically plays a doorbell sound. Built with **OpenCV**, **Face Recognition**, and **Pygame** for cross-platform stability.

---

## 🚀 Features

* **🧑 Real-time Face Detection:** Utilizes HOG (Histogram of Oriented Gradients) via `dlib` for high accuracy.
* **🔊 Automated Audio Alert:** Instantly plays a notification sound upon detection.
* **🧠 Smart Anti-Spam Logic:** Intelligent loop control ensures the bell rings **once per session** (doesn't spam while the person is standing there).
* **🐧🪟 Cross-Platform:** Fully optimized for **Linux (Ubuntu/Debian)** and **Windows 10/11**.

---

## ⚙️ Prerequisites (System Dependencies)

**⚠️ Critical Step:** This project relies on `face_recognition` which depends on `dlib` (C++ code). You **must** install the system-level compilers below before installing Python packages.

### 🐧 For Linux Users (Ubuntu/Debian)
Run the following in your terminal to install CMake and Graphics libraries:
```bash
sudo apt update
sudo apt install cmake build-essential pkg-config libx11-dev libatlas-base-dev gtk2.0
````

### 🪟 For Windows Users

Windows requires a specific build environment for C++. Please follow these steps carefully:

1.  **Install Python:** [Download Python 3.12](https://www.python.org/downloads/windows/).
      * ✅ **Must Check:** "Add Python to PATH" during installation.
2.  **Install CMake:** [Download from cmake.org](https://cmake.org/download/).
      * ✅ **Must Select:** "Add CMake to system PATH for all users".
3.  **Install Visual Studio Build Tools:**
      * Download [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
      * Run the installer and select the **"Desktop development with C++"** workload.
      * Ensure **Windows 10/11 SDK** and **C++ Build Tools** are checked on the right side.
      * Click **Install/Modify**.

-----

## 📦 Installation & Setup (The "Poetry" Way)

I strongly recommend using **[Poetry](https://python-poetry.org/)** for dependency management instead of standard `pip`. It handles virtual environments and dependency conflicts much better.

### 1\. Install Poetry (If not installed)

```bash
pip install poetry
```

### 2\. Project Setup

If you are cloning this repo:

```bash
git clone https://github.com/mdwasikhan54/AI-Powered-Automated-Smart-Doorbell.git
cd AI-Powered-Automated-Smart-Doorbell
```

### 3\. Activate Virtual Environment

Poetry automatically creates and manages a virtual environment for you.

```bash
poetry shell
```

### 4\. Install Dependencies

Install all required packages (OpenCV, Face Recognition, Pygame, Setuptools) with a single command:

```bash
poetry add opencv-python face_recognition pygame setuptools
```

> **☕ Coffee Break:** Installing `face_recognition` triggers a build process for `dlib`. It might take **5-15 minutes** depending on your CPU. Do not close the terminal\!

-----

## 🏃‍♂️ Usage

1.  Make sure you have a sound file named `doorbell.wav` in the project root.
2.  Run the application using Poetry:

<!-- end list -->

```bash
python main.py
```

*(Or if you are outside the shell: `poetry run python main.py`)*

3.  **Controls:**
      * Look at the camera to trigger the bell.
      * Press **`q`** to quit the application.

-----

## 🔧 Troubleshooting Hall of Fame

Stuck? Here are the solutions to the most common errors we faced during development.

| Error Message | Likely Cause | Solution |
| :--- | :--- | :--- |
| **`CMake is not installed`** | System PATH issue | **Win:** Install CMake & add to PATH.<br>**Lin:** `sudo apt install cmake` |
| **`Build tools not found`** | Missing C++ compilers | **Win:** Install VS Build Tools (Desktop C++ workload). |
| **`No module named 'pkg_resources'`** | Python 3.12+ change | Run `poetry add setuptools` or `pip install setuptools`. |
| **`No module named 'gi'`** | `playsound` library issue | We switched to `pygame`. Ensure you run `poetry add pygame`. |
| **`face_recognition_models` not found** | Bad download | Force reinstall: `pip install --force-reinstall face_recognition` |
| **Installation hangs forever** | Compiling `dlib` | It's not frozen. It's calculating math. **Wait 15 mins.** |

-----

## 👨‍💻 For Developers (How to start from scratch)

If you want to build a similar project using Poetry, here is the cheat sheet:

1.  **Create Project:** `poetry new my-project`
2.  **Start Shell:** `cd my-project && poetry shell`
3.  **Add Packages:**
    ```bash
    poetry add opencv-python
    poetry add face_recognition
    poetry add pygame
    ```

-----

### 👨‍💻 Developed by [MD Wasi Khan](https://mdwasikhan-portfolio.netlify.app/)

*Aspiring Python Backend Developer | FastAPI Enthusiast*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mdwasikhan54)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/mdwasikhan54)
</div>

If you find this project helpful, please drop a ⭐ star on the repo! Contributions and feedback are welcome. 🚀


