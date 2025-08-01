# This script merges the contents of two text files.
# The contents of the second file are appended to the first file.

# Import system library for error handling.
import sys

# Prompt the user to enter the relative paths of both files.
file_1 = input('Enter the relative path of the first file\n')
file_2 = input('Enter the relative path of the second file\n')
file_type = input('Enter the type of files (txt or pdf)\n')

# Check if the file type is 'txt'.
if file_type == 'txt':
    try:
        # Open the second file in read mode.
        with open(file_2, 'r') as file:
            # Store the contents of the second file in a variable.
            file_2_text = file.read()

        # Open the first file in append mode.
        with open(file_1, 'a') as file:
            # Append the contents of the second file to the first file.
            file.write('\n' + file_2_text)

        # Print the success message.
        print('Merge successful.')
    
    except FileNotFoundError:
        # Print an error message if the file is not found.
        print('File not found. Please check the file paths and try again.')
        # Exit the script with an error code.
        sys.exit(1)

elif file_type == 'pdf':
    try:
        # Import the PyPDF2 library to handle PDF operations.
        from PyPDF2 import PdfReader, PdfWriter

        # Create a PdfWriter object to write the merged PDF.
        pdf_writer = PdfWriter()

        # Open both files one by one.
        for file in [file_1, file_2]:
            # Create a PdfReader object for each file.
            reader = PdfReader(file)

            # Add each page of the file to the PdfWriter.
            for page in reader.pages:
                pdf_writer.add_page(page)

        # Write the contents of the merged file to the first file.
        with open(file_1, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        # Print the success message.
        print('Merge successful.')

    except FileNotFoundError:
        # Print an error message if the file is not found.
        print('File not found. Please check the file paths and try again.')
        # Exit the script with an error code.
        sys.exit(1)

else:
    # Print an error message if the file type is not recognized.
    print('Error: Unsupported file type. Please enter "txt" or "pdf".')
    # Exit the script with an error code.
    sys.exit(1)