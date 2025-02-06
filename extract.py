from spire.pdf.common import *
from spire.pdf import *

import argparse
import sys


from xml.etree import ElementTree
from pprint import pprint
import os

def extract(filename, outputname):
    print('Processing PDF file')
    o = open(outputname, "w")
    o.close()

    doc = PdfDocument()

    doc.LoadFromFile(filename)

    doc.SaveToFile(outputname)

    doc.Dispose()


    print("DOCX file saved")
    os.system(f"dumppdf.py -a {filename} > out.xml")

    o = open("output.xml", "w")
    for line in open("out.xml"):
        line = line.replace("&#", "Invalid_XML")
        o.write(line)
    o.close()

    tree = ElementTree.parse('output.xml')
    lastnode = ""
    lastnode2 = ""
    list = {}
    entry = {}

    for node in tree.iter():
        if node.tag == "key" and node.text == "T":
            lastnode = node.tag + node.text
        elif lastnode == "keyT":
            for child in node.iter():
                entry["ID"] = child.text
            lastnode = ""

        if node.tag == "key" and node.text == "V":
            lastnode2 = node.tag + node.text
        elif lastnode2 == "keyV":
            for child in node.iter():
                if (child.tag == "string" or child.tag == 'literal') and 'ID' in entry:
                    entry["Value"] = child.text
                    list[entry["ID"]] = entry["Value"]
                    #pprint(child.keys())
                    entry = {}
            lastnode2 = ""

    pprint(list)
    os.remove('out.xml')
    os.remove('output.xml')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert PDF to DOCX and extract filled form fields')

    parser.add_argument('--input',
                        type=str,
                        help="Provide input file path, should be a PDF file, eg: test.pdf",
                        default=None,
                        required=True)

    parser.add_argument('--output',
                        type=str,
                        help="Provide output file path, should be a DOCX file, eg: out.docx",
                        default=None,
                        required=True)

    args = parser.parse_args()

    extract(filename=args.input, outputname=args.output)
