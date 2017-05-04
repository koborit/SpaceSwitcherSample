# **Maya Tool: ** _**Space Swithcer**_ **Sample**

**Maya Tool: ** _**Space Switcher**_ **Sample** is Autodesk Maya environment where simple animator's tool _**spaceSwitcher**_ can be tested.

## Supported Platforms:
* Autodesk Maya and its supported platforms.

## Setup Instructions

### Prerequisites
Python 2.7.x (64bit) and Autodesk Maya must be installed on your computer.

### Installation
* Clone or download "SpaceSwitcherSample".

* Make sure the path to python 2.7.x interpreter is added to PATH environment variable, otherwise do one of the followings:

    * Add python 2.7.x interpreter path to PATH environment variable as a system variable.

    * Edit launch script so that PATH environment variable includes the path to python 2.7.x interpreter.  
      Launch scripts for recent maya versions on Windows and Linux are provided as:  
        `run_maya####.bat` (for Windows)  
        `run_maya####` (for Linux)  
      Where `"####"` stands for maya version number.

### Verifying Installation
* Launch maya with one of the launch scripts that fits to your environment.

* In maya script editor, run the following MEL script to launch UI:

    ```
    spaceSwitcher;
    ```

### Usage
* User's guide: [spaceSwitcher User's Guide](./tools/spaceSwitcher/README.md)

* Python script interface is also available: [spaceSwitcher Script Interface](./tools/spaceSwitcher/README.md)

### Dependencies
* [mottosso/Qt.py](https://github.com/mottosso/Qt.py)  
    By [Qt.py](https://github.com/mottosso/Qt.py), one UI implementation using Qt bindings runs on all versions of Qt-based Maya.  
    [Qt.py](https://github.com/mottosso/Qt.py) is used for this project and the files are included in this repository under the MIT license.

* [PeregrineLabs/Ecosystem](https://github.com/PeregrineLabs/Ecosystem)  
    As environment management system, [PeregrineLabs Ecosystem](https://github.com/PeregrineLabs/Ecosystem) is used for this project and the files are included in this repository under the BSD-3-Clause license.
