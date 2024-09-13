# FRIDAY and Homey: Advanced Home Automation Robots

Welcome to the repository for the FRIDAY and Homey projects. This repository contains code, documentation, and resources for two advanced home automation robots designed to enhance daily living through voice recognition, remote control, and automation.

## Folder Structure

      ├── LICENSE.txt 
      ├── README.md 
      ├── StandardFirmata │ 
         ├── LICENSE.txt │ 
         ├── StandardFirmata.ino 
      ├── final code.py 
      └── INTRODUCING_FRIDAY[1].docx

## Overview

### FRIDAY
FRIDAY is a versatile robot that can be controlled through voice commands, wireless remote, or fully automatic mode. It is designed to assist users, especially those with physical disabilities, by performing tasks as per the user's commands.

### Homey
Homey is another advanced robot system aimed at home automation. It can recognize voice commands and perform various tasks around the home. It can be controlled remotely via a smartphone application or any internet-enabled device.

## Features

- **Voice Command Recognition**: Both FRIDAY and Homey can understand and act on voice commands.
- **Remote Control**: Operate the robots manually using a smartphone application or any internet-enabled device.
- **Automation**: Fully automatic mode for predefined tasks.
- **Accessibility**: Designed to be particularly beneficial for individuals with physical disabilities.
- **Energy Efficiency**: Integrates with energy-efficient home systems.

## Getting Started

### Prerequisites

- A compatible robot prototype
- Android smartphone or any internet-enabled device
- Development environment setup (see Installation section)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/FRIDAY-Homey-Robot.git
   cd FRIDAY-Homey-Robot
2.  **Set Up the Development Environment**
3.  Ensure you have Python 3.x installed.
4.   Install the required packages:


         pip install -r requirements.txt
## Configure the Robot

Arduino Firmware: Use the StandardFirmata folder to upload the StandardFirmata.ino to your Arduino for basic communication.
Python Code: Modify and use the final code.py for the robot's control logic.

#### Run the Application Start the server or application based on the provided instructions:


      python final code.py
      Connect Your Device Download the corresponding mobile app (if available) and connect your device to the robot.

## Documentation
INTRODUCING_FRIDAY[1].docx: Detailed documentation introducing the FRIDAY robot and its features.
## Usage
Voice Commands: Speak commands clearly within the robot's range to control its actions.
Remote Control: Use the smartphone application to manage the robot remotely.
Automation: Configure tasks and schedules through the robot's settings.
## Contributing
We welcome contributions to enhance FRIDAY and Homey. To contribute, please follow these steps:

      Fork the repository.
      Create a new branch (git checkout -b feature-branch).
      Commit your changes (git commit -am 'Add new feature').
      Push to the branch (git push origin feature-branch).
      Create a new Pull Request.
## Acknowledgments
Thanks to the open-source community for the tools and libraries used in this project.
