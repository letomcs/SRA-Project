import fitz
import pandas as pd
import os

class DataEntry:
    def process_data(self, pathname, pdf_file, output_dir):
        try:
            # Read the CSV file
            data_list = pd.read_csv(pathname)

            # Print column names for debugging
            print("Column names in the CSV file:", data_list.columns)

            required_columns = ['Permit Number', 'Contact First Name', 'Contact Last Name', 'Address', 'Contact Home Phone', 'Subdivision', 'Section No', 'Lot', 'Footage/Acreage', 'Water Pump', 'Permit Status', 'Property Description']
            missing_columns = [col for col in required_columns if col not in data_list.columns]

            if missing_columns:
                return f"Missing columns in the CSV file: {', '.join(missing_columns)}"
            
            # Ensure the output directory exists
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            sra_form = pdf_file
            for index, row in data_list.iterrows():
                document = fitz.open(sra_form)
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
                            field.field_value = str(row['Contact Home Phone']) if pd.notna(row['Contact Home Phone']) else ' '
                            field.update()
                        if field_indx == 6:
                            field.field_value = str(row['Subdivision'])
                            field.update()
                        if field_indx == 7:
                            field.field_value = str(row['Section No']) if pd.notna(row['Section No']) else ' '
                            field.update()
                        if field_indx == 8:
                            field.field_value = str(row['Lot']) if pd.notna(row['Lot']) else ' '
                            field.update()
                        if field_indx == 9:
                            field.field_value = str(row['Footage/Acreage'])
                            field.update()
                        if field_indx == 11:
                            field.field_value = 'Yes' if row['Water Pump'] else 'No'
                            field.update()
                        if field_indx == 13:
                            field.field_value = str(row['Property Description']) if pd.notna(row['Property Description']) else ' '
                            field.update()

                # Save the document in the specified directory
                output_file = os.path.join(output_dir, f'Inspection_Report_{row["Permit Number"]}.pdf')
                document.save(output_file)
                print(f"Report saved to {output_file}")

            return "Success"
        
        except Exception as e:
            return str(e)
