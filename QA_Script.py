#this function QA's the files listed in the directory
import os
import pandas as pd
import datetime

def shape_QA(base_dir,source_folder,seed):

    file_list = os.listdir(source_folder)
    cd_df = pd.read_excel(os.path.join(base_dir,seed))


    for file in file_list:
        df = pd.read_excel(os.path.join(source_folder,file))
        print("shape:"+ str(df.shape) + " - " + str(file))

    for file in file_list:
        df = pd.ExcelFile(os.path.join(source_folder,file))
        print("num of sheets:"+ str(len(df.sheet_names)) + " - " + str(file))

def aso_QA(base_dir,source_folder,seed):
    errors = []

    file_list = os.listdir(source_folder)
    cd_df = pd.read_excel(os.path.join(base_dir,seed))


    for file in file_list:
        
        df = pd.read_excel(os.path.join(source_folder,file))


        # Looking at columns matching or not (shape and values)
        # print('shape and values')

        
        try:    
            if all(df.columns == cd_df.columns):
                pass
            elif df.shape[1] == cd_df.shape[1]:
                 errors.append(str(file + ' ' + "shape matches, but not columns."))
            
                    
        except ValueError:
                errors.append(str(file + ' ' + "shape and/or columns do not match."))
                
        # Looking at blank rows or typos on the sheet
        # print('blank rows and typos')
        
        blank_rows = df[df.isnull().all(axis=1)]
        if blank_rows.empty:
            pass
        else:
            errors.append(str(file + " " + "has blank rows."))

        # Check for missing values in certain columns: Advertiser Name, Site Name, Campaign Name, Placement Name, Date
        # print('col correct')
        #blank_AN_cells = df['Advertiser Name'].isna()
        #blank_SN_cells = df['Site Name'].isna()
        #blank_CN_cells = df['Campaign Name (DCM)'].isna()
        #blank_PN_cells = df['Placement Name (DCM)'].isna()
        #blank_Date_cells = df['Date'].isna()

        #if blank_AN_cells.any() or blank_SN_cells.any() or blank_CN_cells.any() or blank_PN_cells.any():
        #    errors.append(str(file + ' ' + 'There are blank cells in one of the dimension columns'))
        #else:
        #    pass
 

        # Looking for duplicate values within the file
        # print('dupes')
        
        #duplicates = df[df.duplicated()]
        #if duplicates.empty:
       #     pass
        #else:
        #    errors.append(str(file + " " + "has duplicate rows."))

    return errors

    
    
    
    
