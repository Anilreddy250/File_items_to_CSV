
import os
import csv

def list_directory_to_csv(directory_path, output_csv_file):
    try:
        # Get a list of all items in the specified directory
        items = os.listdir(directory_path)

        # Create or overwrite the CSV file
        with open(output_csv_file, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Item Name', 'Type'])  # Write header row

            # Write each item's name and type (file or directory) to the CSV
            for item in items:
                item_path = os.path.join(directory_path, item)
                item_type = 'File' if os.path.isfile(item_path) else 'Directory'
                csv_writer.writerow([item, item_type])

        print "Items listed in '{}' successfully.".format(output_csv_file)
    except Exception as e:
        print "Error: {}".format(e)

# Example usage
# directory_path = ''
directory_path = 'C:\\anil\\data'

output_csv_file = 'C:\\anil\\directory_items_name.csv'
list_directory_to_csv(directory_path, output_csv_file)
