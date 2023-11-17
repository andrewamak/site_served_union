import os
import pandas as pd
import datetime
from QA_Script import aso_QA
from QA_Script import shape_QA

current_datetime = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
print("Started running: " + current_datetime)

# Base Directory
base_dir = r"\\umwazrfs01\group\BMW\1. Decision Sciences\x1. Sandbox\Andy\Python Ad Server Override Test"

# Seed file
seed = r"Output\Archive\Ad Server Override Base File\Ad Server Override.xlsx"

# Define the source folder containing the files to be unioned
source_folder = os.path.join(base_dir,r'Input')

# Define the destination folder where the unioned file will be saved
destination_folder = os.path.join(base_dir,r'Output\Export Ad Server File')

# Shape QA
print(shape_QA(base_dir, source_folder, seed))

# Run the QA python script
QA_readout_text = aso_QA(base_dir, source_folder, seed)
QA_readout_filename = rf'Output\QA Documentation\QA_file - {current_datetime}.txt'
QA_readout_directory = os.path.join(base_dir, QA_readout_filename)

with open(QA_readout_directory, "w") as file:
    for errors in QA_readout_text:
        file.write(errors + "\n")



# Initialize an empty Ad Server DataFrame to store the concatenated data and union
cd_df = pd.read_excel(os.path.join(base_dir,seed))
file_list = os.listdir(source_folder)

for file in file_list:
    # Assuming that the files are Excel files; you can change the format if needed
    df = pd.read_excel(source_folder + r'\\' + file)
    cd_df = pd.concat([cd_df, df], ignore_index=True)


# Define the name of the unioned file (Excel format in this example)
unioned_filename = 'Ad Server Override.xlsx'

# Define the full path for the unioned file in the destination folder
unioned_file_path = os.path.join(destination_folder, unioned_filename)

# Export the concatenated data to the unioned file in the destination folder
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all rows

print(cd_df.shape)

cd_df_cleaned = cd_df.dropna(how='all')
print("removed blanks: " + str(cd_df_cleaned.shape))

print(cd_df_cleaned.head(10))

cd_df_cleaned.to_excel(unioned_file_path, index=False)

print("Union Complete. File saved to:")
print(str(unioned_file_path))



