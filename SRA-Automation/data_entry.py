import fitz
import pandas as pd
import os

# Read the CSV file
data_list = pd.read_csv('SearchResult.csv')

# Print column names for debugging
print("Column names in the CSV file:", data_list.columns)

sra_form = 'PLUP Inspection Report.pdf'

document = fitz.open(sra_form)

# Check if all required columns are present
required_columns = ['Permit Number', 'Contact First Name', 'Contact Last Name', 'Address', 'Contact Home Phone', 'Subdivision', 'Section No', 'Lot', 'Footage/Acreage', 'Water Pump', 'Permit Status', 'Property Description']
missing_columns = [col for col in required_columns if col not in data_list.columns]

if missing_columns:
    print(f"Missing columns in the CSV file: {missing_columns}")
else:
    # Ensure the output directory exists
    output_dir = './Inspection_Reports/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for row_indx, row in data_list.iterrows():
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            for field_indx, field in enumerate(page.widgets()):
                if field_indx == 0:
                    field.field_value = str(row['Permit Number'])
                    field.update()
                
                if field_indx == 3:
                    field.field_value = str(row['Contact First Name'] + ' ' + row['Contact Last Name'])
                    field.update()

                if field_indx == 4:
                    field.field_value = str(row['Address'])
                    field.update()

                if field_indx == 5:
                    if pd.isna(row['Contact Home Phone']) or row['Contact Home Phone'] == '':
                        field.field_value = ' '
                    else:
                        field.field_value = str(row['Contact Home Phone'])
                    field.update()

                if field_indx == 6:
                    field.field_value = str(row['Subdivision'])
                    field.update()

                if field_indx == 7:
                    if pd.isna(row['Section No']) or row['Section No'] == '':
                        field.field_value = ' '
                    else:
                        field.field_value = str(row['Section No'])
                    field.update()

                if field_indx == 8:
                    if pd.isna(row['Lot']) or row['Lot'] == '':
                        field.field_value = ' '
                    else:
                        field.field_value = str(row['Lot'])
                    field.update()

                if field_indx == 9:
                    field.field_value = str(row['Footage/Acreage'])
                    field.update()

                if field_indx == 11:
                    field.field_value = str(row['Water Pump'])
                    if str(row['Water Pump']) == 'True':
                        field.field_value = 'Yes'
                    else:
                        field.field_value = 'No'
                    field.update()

                # if field_indx == 13:
                #     field.field_value = str(row['Permit Status'])
                #     field.update()

                if field_indx == 13:
                    if pd.isna(row['Property Description']) or row['Property Description'] == '':
                        field.field_value = ' '
                    else:
                        field.field_value = str(row['Property Description'])
                    field.update()

        # Save the document in the correct directory
        document.save(os.path.join(output_dir, 'Inspection_Report_{0}.pdf'.format(row['Permit Number'])))
