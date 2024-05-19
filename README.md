# VoterRoll

## Description
VoterRoll is a Python application that compares county voter roll files with the National Change of Address (NCOA) database and identifies voters who moved out-of-state or out-of-country.

## Installation

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

## Usage
1. Ensure you have the `voters_moved.xlsx` file in the same directory as `VoterRoll.py`.
2. Run the main script:
    ```sh
    python VoterRoll.py
    ```

## Create Windows .exe File
1. Install pyinstaller
    ```sh
    pip3 install pyinstaller
    ```

2. Run pyinstaller
    ```sh
    pyinstaller --onefile VoterRoll.py
    ```

3. Locate VoterRoll.exe file in dist directory
     ```sh
    cd dist
    ls
    ```

## Directories and Files
1. County directories use this naming convention:
    ```
    "countyname"_X

    countyname = name of Colorado county
    X = an integer value representing the relative population size of the county
    ```

## Log Files
Log files are located in the "logs" directory in file "logs.txt".  

## Features
- Compares county voter roll files with the NCOA database.
- Identifies voters who moved out-of-state or out-of-country.
- Copies and renames voter roll files for each county.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information
Richard Casey
richardcaseyhpc@protonmail.com

## Acknowledgements
This project uses the following third-party libraries:
- `pandas`
- `openpyxl`
- `numpy`
- And others listed in `requirements.txt`.
