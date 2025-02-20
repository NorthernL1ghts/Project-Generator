# Project Generator

[![Python Version](https://img.shields.io/badge/Python-3.12.4-blue.svg)](https://www.python.org/downloads/release/python-3124/)
[![Windows Support](https://img.shields.io/badge/Windows-Supported-brightgreen.svg)](https://www.microsoft.com/en-us/windows)
[![macOS Support](https://img.shields.io/badge/macOS-Supported-brightgreen.svg)](https://www.apple.com/macos/)
[![Linux Support](https://img.shields.io/badge/Linux-Supported-brightgreen.svg)](https://www.linux.org/)
![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat&logo=github&link=https://github.com/NorthernL1ghts/Project-Generator/blob/main/LICENSE)


A tool to generate random project ideas based on a specified field or topic and difficulty level. This is perfect for developers looking to practice or explore new project ideas in various domains such as Web Development, AI, Automation, and more.

## Features

- Generate random project ideas based on selected fields (e.g., Web, AI, Data, Game, Automation).
- Specify the difficulty level of the project (e.g., Beginner, Moderate, Hard, Advanced, Expert).
- Easily set up a development environment using a `requirements.txt` file for managing dependencies.

## Prerequisites

Before running the tool, ensure you have the following installed:

- Python 3.6 or higher
- pip (Python's package installer)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/NorthernL1ghts/Project-Generator
cd Project-Generator
```

### Step 2: Set up the environment

For both Windows and Unix-based systems, you can set up a virtual environment with the following steps:

#### On Windows
Run the `SetupEnv.bat` file located in the `Scripts` directory:

```bash
Scripts/SetupEnv.bat
```

This will create a virtual environment, activate it, and install the required dependencies.

#### On Linux/macOS
Make the `SetupEnv.sh` script executable:

```bash
chmod +x Scripts/SetupEnv.sh
```

Run the `SetupEnv.sh` script located in the `Scripts` directory:

```bash
./Scripts/SetupEnv.sh
```

This will create a virtual environment, activate it, and install the required dependencies.

### Step 3: Run the Project Generator

Once the environment is set up and dependencies are installed, you can run the `ProjectGenerator.py` script to generate random project ideas.

Navigate to the `src` directory:

```bash
cd src
```

Run the script:

```bash
python ProjectGenerator.py
```

The script will prompt you to enter:

- A field/topic (e.g., Web, AI, Data, Game, Automation).
- A difficulty level (Beginner, Moderate, Hard, Advanced, Expert).

Based on your input, it will generate a random project idea that matches your selected field and difficulty level.

### Example

```bash
Enter a field/topic (e.g., Web, AI, Data, Game, Mobile, Automation):
AI
Enter a difficulty level (Beginner, Moderate, Hard, Advanced, Expert):
Expert
Random Project Idea: Build a Scalable AI System for Healthcare Data Analysis
```

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements, bug fixes, or new features are always welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
