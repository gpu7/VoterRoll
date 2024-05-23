# VoterRoll

## Description
VoterRoll is a Python application that compares county voter roll files with the National Change of Address (NCOA) database and identifies voters who moved out-of-state or out-of-country.

## Features
- Compares county voter roll files with the NCOA database.
- Identifies voters who moved out-of-state or out-of-country.
- Copies and renames voter roll files for each county.

## Installation

## Software Engineering
The descriptions below are intended primarily for software engineers and software maintainers. 

### Prerequisites
- Python 3.6 or higher

### Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/VoterRoll.git
    ```
2. Navigate to the project directory:
    ```sh
    cd VoterRoll
    ```
3. Create a virtual environment:
    ```sh
    python -m venv voterroll
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        voterroll\Scripts\activate
        ```
5. Install the required packages:
    ```sh
    pip3 install -r requirements.txt
    ```

### Usage
1. Ensure the `voters_moved.xlsx` file is in the same directory as `VoterRoll.py`.
2. Run the main script:
    ```sh
    python VoterRoll.py
    ```

### Create Windows .exe File
1. Install pyinstaller
    ```sh
    pip3 install pyinstaller
    ```

2. Run pyinstaller
    ```sh
    pyinstaller --onefile --add-data "voters_moved.xlsx;." VoterRoll.py
    ```

    or, to clear cache and temp files,

    ```sh
    pyinstaller --onefile --clean --add-data "voters_moved.xlsx;." VoterRoll.py
    ```

3. Locate VoterRoll.exe file in dist directory
     ```sh
    cd dist
    ls
    ```

### Directories and Files
1. County directory file naming convention:
    ```
    countyname_X

    where:
    countyname = name of Colorado county
    X = an integer value representing the relative population size of the county
    ```

2. NCOA (National Change of Address) file naming convention:
    ```
    YYYYMMDDNCOAXXtoXX_countyname.xlsx

    where:
    YYYY = year
    MM = month
    DD = day
    NCOA = constant string
    XX = integer
    countyname = name of Colorado county
    ```

3. County voter roll (VR) file naming convention:
    ```
    VRYYYY_MM_countyname.xlsx

    where:
    VR = constant string
    YYYY = year
    MM = month
    countyname = name of Colorado county
    ```

4. voters_moved file naming convention:

    ```
    countyname_voters_moved.xlsx

    where:
    countyname = name of Colorado county
    voters_moved = constant string
    ```

5. colorado_voters_moved directory
    This directory contains one file for each county.  It collects all voters_moved.xlsx files in one directory.

6. VoterRoll.py is the main Python script for processing voter roll and NCOA files.

7. Log files
    Log files are located in the "logs" directory in file "logs.txt".  "logs.txt" is in JSON format.

8. requirements.txt
    Dependencies file for VoterRoll project.

9. Dockerfile
    Docker configuration file.

### Docker
1. Create or modify Dockerfile as required.

2. Build the docker image file.
   ```
   docker build -t voterroll-app .
   ```

3. Run the docker image file.
   ```
   docker run -it --rm --name voterroll-container voterroll-app
   ```


### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact Information
Richard Casey
richardcaseyhpc@protonmail.com

### Acknowledgements
This project uses third-party libraries listed in `requirements.txt`.
