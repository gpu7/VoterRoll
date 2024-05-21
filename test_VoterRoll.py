# Standard library imports
import os
import unittest
from   unittest.mock import patch

# Third-party imports
import pandas as pd

# Assuming the script is named VoterRoll.py and is in the same directory as this test script
from VoterRoll import main, BASE_DIR, VOTERS_MOVED_FILE, COLORADO_VOTERS_MOVED_DIR, colorado_counties # type: ignore

# voter roll class
class TestVoterRoll(unittest.TestCase):

    @patch('VoterRoll.pd.read_excel')
    @patch('VoterRoll.pd.DataFrame.to_excel')
    @patch('VoterRoll.os.path.exists')
    @patch('VoterRoll.os.makedirs')
    @patch('VoterRoll.os.path.isdir')
    @patch('VoterRoll.os.listdir')
    @patch('VoterRoll.shutil.copy2')
    @patch('VoterRoll.os.remove')
    @patch('VoterRoll.os.rename')
    def test_main(self, mock_rename, mock_remove, mock_copy2, mock_listdir, mock_isdir, mock_makedirs, mock_exists, mock_to_excel, mock_read_excel):
        # Setup mock behaviors
        mock_exists.side_effect  = lambda path: True if path == VOTERS_MOVED_FILE else False
        mock_isdir.side_effect   = lambda path: path.startswith(BASE_DIR)
        mock_listdir.side_effect = lambda path: ['NCOA_20240101.xlsx', 'VR_20240101.xlsx'] if path.startswith(BASE_DIR) else []

        # Mock DataFrames for read_excel
        voters_moved_df = pd.DataFrame({'VoterID': [1],  'NEW State': ['TX']})
        ncoa_df         = pd.DataFrame({'VoterID': [1],  'NEW State': ['TX']})
        vr_df           = pd.DataFrame({'VOTER_ID': [1], 'EFFECTIVE_DATE': ['2024-01-01'], 'REGISTRATION_DATE': ['2024-01-01'], 'PARTY_AFFILIATION_DATE': ['2024-01-01'], 'MAILING_STATE': ['TX'], 'MAILING_COUNTRY': ['USA']})

        # Mock read_excel to return different DataFrames for each call
        mock_read_excel.side_effect = [voters_moved_df] + [ncoa_df, vr_df] * len(colorado_counties)

        # Run the main function
        main()

        # Check if files are copied and renamed
        for county in colorado_counties:
            sub_dir_path      = os.path.join(BASE_DIR, county)
            old_path          = os.path.join(sub_dir_path, "voters_moved.xlsx")
            new_path          = os.path.join(sub_dir_path, f"{county}_voters_moved.xlsx")
            moved_county_file = os.path.join(COLORADO_VOTERS_MOVED_DIR, f"{county}_voters_moved.xlsx")

            mock_read_excel.assert_any_call(VOTERS_MOVED_FILE)
            mock_to_excel.assert_any_call(old_path, index=False)

            try:
                mock_rename.assert_any_call(old_path, new_path)
            except AssertionError:
                print(f"Expected rename call not found: rename({old_path}, {new_path})")
                print(f"Actual rename calls: {mock_rename.call_args_list}")
                raise

            mock_copy2.assert_any_call(new_path, moved_county_file)

        # Check if directories are created
        mock_makedirs.assert_called_with(COLORADO_VOTERS_MOVED_DIR)

if __name__ == '__main__':
    unittest.main()
