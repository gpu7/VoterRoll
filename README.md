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
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```sh
        source venv/bin/activate
        ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Ensure you have the `voters_moved.xlsx` file in the same directory as `VoterRoll.py`.
2. Run the main script:
    ```sh
    python VoterRoll.py
    ```

## Features
- Compares county voter roll files with the NCOA database.
- Identifies voters who moved out-of-state or out-of-country.
- Copies and renames voter roll files for each county.
- Processes data to ensure accurate and up-to-date voter information.

## Contributing
### Contribution Guidelines
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information
If you have any questions, feel free to contact the project maintainer at your.email@example.com.

## Acknowledgements
This project uses the following third-party libraries:
- `pandas`
- `openpyxl`
- `numpy`
- And others listed in `requirements.txt`.
