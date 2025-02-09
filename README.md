# 1099B parser

Written and tested using Python 3.13.1.

This script takes a flattened 1099B PDF and converts into a TaxSlayer compatible CSV.

## How to flatten a PDF

1. Open it in your PDF reader.
2. Click File -> Print.
3. Choose the option to save as PDF.

## How to install required modules
pip install -r requirements.txt

## How to run
python 1099B-parser.py /path/to/input_file.pdf output_filename.csv

## Notes
This was written specifically for a 1099B received from Landa Holdings, with the output format in a CSV format accepted by TaxSlayer. I do not know to what extent it may be compatible with other 1099B forms or tax programs.
