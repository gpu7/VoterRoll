# Author:  Anonymous
# Date:    10-05-2024 (DD-MM-YYYY)
# Purpose: VoterRoll compares county voter roll files with the National Change of Address (NCOA) database 
#          and identifies voters who moved out-of-state or out-of-country.

# Standard library imports
import os
import shutil
import sys
import warnings
from   typing import List

# Third-party imports
import pandas as pd
from   pandas import DataFrame

# Local application/library specific imports
from utilities.loggerUtilVoterRoll import logger

# suppress the warning "Workbook contains no default style, apply openpyxl's default"
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")
# suppress specific FutureWarnings related to pandas DataFrame concatenation
warnings.filterwarnings('ignore', category=FutureWarning, message='The behavior of DataFrame concatenation with empty or all-NA entries is deprecated.')

# data directories and files
COLORADO_COUNTIES_DIR      = r"C:\Users\gpu7\VoterRoll\data\colorado_counties"
COLORADO_VOTERS_MOVED_DIR  = r"C:\Users\gpu7\VoterRoll\data\colorado_voters_moved"
VOTERS_MOVED_FILE          = "voters_moved.xlsx"

# main
def main() -> None:
    # check if voters_moved.xlsx exists in same directory as VoterRoll.py
    if not os.path.exists(VOTERS_MOVED_FILE):
        logger.error("ERROR: 'voters_moved.xlsx' file does not exist.")
        sys.exit(1)
    
    # Check if "voters_moved.xlsx" exists in each subdirectory under "colorado_counties". Delete if exists.
    logger.info("Checking Colorado county directories for voters_moved.xlsx file...")
    try:
        for sub_dir in os.listdir(COLORADO_COUNTIES_DIR):
            if sub_dir.startswith('.'):  # ignore hidden files and directories
                continue
            voters_moved_excel: str = os.path.join(COLORADO_COUNTIES_DIR, sub_dir, VOTERS_MOVED_FILE)
            if os.path.exists(voters_moved_excel):
                os.remove(voters_moved_excel)
    except Exception as e:
        logger.error(f"ERROR: error checking or deleting voters_moved.xlsx file: {e}")
        sys.exit(1)
    
    # copy voters_moved.xlsx to each directory under colorado_counties
    logger.info("Copy voters_moved.xlsx to Colorado county directories...")
    try:
        for sub_dir in os.listdir(COLORADO_COUNTIES_DIR):
            if sub_dir.startswith('.'):  # ignore hidden files and directories
                continue
            dest_path: str = os.path.join(COLORADO_COUNTIES_DIR, sub_dir, VOTERS_MOVED_FILE)
            pd.read_excel(VOTERS_MOVED_FILE).to_excel(dest_path, index=False)
    except Exception as e:
        logger.error(f"ERROR: error copying voters_moved.xlsx file: {e}")
        sys.exit(1)

    # rename voters_moved.xlsx to county_name_voters_moved.xls
    logger.info("Renaming voters_moved.xlsx to county_name_voters_moved.xlsx...")
    try:
        for sub_dir in os.listdir(COLORADO_COUNTIES_DIR):
            if sub_dir.startswith('.'): # ignore hidden files and directories
                continue
            old_path: str = os.path.join(COLORADO_COUNTIES_DIR, sub_dir, VOTERS_MOVED_FILE)
            new_path: str = os.path.join(COLORADO_COUNTIES_DIR, sub_dir, f"{sub_dir}_voters_moved.xlsx")
            if os.path.exists(new_path): # target file exists, remove it
                os.remove(new_path)
            os.rename(old_path, new_path)
    except Exception as e:
        logger.error(f"ERROR: error renaming files: {e}")
        sys.exit(1)
    
    # process each county directory
    logger.info("Processing Colorado county directories...")
    try:
        for sub_dir in os.listdir(COLORADO_COUNTIES_DIR):
            if sub_dir.startswith('.'): # ignore hidden files and directories
                continue
            
            # add _voters_moved.xlsx suffix to county file
            county_file: str = os.path.join(COLORADO_COUNTIES_DIR, sub_dir, f"{sub_dir}_voters_moved.xlsx")
            county_df = pd.read_excel(county_file)
            logger.info(f"Processing: {os.path.basename(county_file)}")

            # search for NCOA file in county directory
            county_dir_path: str = os.path.join(COLORADO_COUNTIES_DIR, sub_dir)
            ncoa_files = [f for f in os.listdir(county_dir_path) if 'NCOA' in f and f.endswith('.xlsx')]
            if not ncoa_files:
                logger.info(f"No NCOA file found in {sub_dir}.")
                continue
            ncoa_file:     str = ncoa_files[0]
            ncoa_df: DataFrame = pd.read_excel(os.path.join(COLORADO_COUNTIES_DIR, sub_dir, ncoa_file))
            logger.info(f"Processing NCOA file: {ncoa_file} in {sub_dir}")
            
            # search for voter roll (VR) file in county directory
            county_dir_path: str = os.path.join(COLORADO_COUNTIES_DIR, sub_dir)
            vr_files = [f for f in os.listdir(county_dir_path) if f.startswith('VR') and f.endswith('.xlsx')]
            if not vr_files:
                logger.info(f"No voter roll (VR) file found in {sub_dir}.")
                continue
            vr_file:     str = vr_files[0]
            vr_df: DataFrame = pd.read_excel(os.path.join(county_dir_path, vr_file))
            logger.info(f"Processing voter roll (VR) file: {vr_file} in {sub_dir}")

            # search for voters who moved out-of-state or out-of-country
            for _, row in ncoa_df.iterrows():
                if row['NEW State'] != 'CO':
                    voter_id: int = row['VoterID']
                    matching_record: DataFrame = vr_df[vr_df['VOTER_ID'] == voter_id]
                    county_df = pd.concat([county_df, matching_record], ignore_index=True)
            
            # Sort by MAILING_STATE, then by MAILING_COUNTRY
            county_df = county_df.sort_values(by=["MAILING_STATE", "MAILING_COUNTRY"])

            # Format date columns to YYYY-MM-DD without time
            county_df['EFFECTIVE_DATE']         = pd.to_datetime(county_df['EFFECTIVE_DATE']).dt.strftime('%m/%d/%Y')
            county_df['REGISTRATION_DATE']      = pd.to_datetime(county_df['REGISTRATION_DATE']).dt.strftime('%m/%d/%Y')
            county_df['PARTY_AFFILIATION_DATE'] = pd.to_datetime(county_df['PARTY_AFFILIATION_DATE']).dt.strftime('%m/%d/%Y')

            # Save the county file
            county_df.to_excel(county_file, index=False)

            # Copy each county file from each county subdirectory into colorado_voter_rolls_moved subdirectory.
            moved_county_file: str = os.path.join(COLORADO_VOTERS_MOVED_DIR, f"{sub_dir}_voters_moved.xlsx")
            shutil.copy2(county_file, moved_county_file)

    except Exception as e:
        logger.error(f"ERROR: error during processing of county directories: {e}")
        sys.exit(1)

# main entry point
if __name__ == "__main__":
    logger.info("Starting VoterRoll...")
    main()
    logger.info("Finished VoterRoll.")