# PDF to DOCX Converter and Form Field Extractor

This Python script converts a PDF file to a DOCX file and extracts form field values from the PDF.

## Features
- Converts PDF files to DOCX format.
- Extracts filled form fields from the PDF.
- Saves extracted form data in a structured format.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.9

## Installation

Install Python dependencies:
```sh
pip install -r requirements.txt
```

## Usage

Run the script with the following command:

```sh
python script.py --input input.pdf --output output.docx
```

### Arguments
- `--input` (Required): Path to the input PDF file.
- `--output` (Required): Path to save the converted DOCX file.

## Example

```sh
python script.py --input form.pdf --output result.docx
```

## Notes
- The script processes the PDF and generates an output DOCX file.
- It also extracts filled form fields and prints them as a structured dictionary.

## License
This project is licensed under the MIT License.

## Author
Bharani Yeleswarapu

