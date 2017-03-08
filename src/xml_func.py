import xml.etree.ElementTree as ET
from _elementtree import tostring
from src.crypto import encryption, decryption


def write_xml(xml_doc):
    xmlfile = open('passcrypt.enc', 'w')
    xmlfile.write(encryption(xml_doc))
    xmlfile.close()


def read_xml():
    xmlfile = open('passcrypt.enc', 'r')
    xml_doc = xmlfile.read()
    return xml_doc


def get_root():
    return ET.fromstring(decryption(read_xml()))


def create_xml(entrylist=None):
    xml_root = None
    try:
        xml_root = ET.Element('passcrypt')
        for pass_entry in entrylist:
            xml_entry = ET.SubElement(xml_root, 'pass_entry')
            xml_entry.set('name', pass_entry.entry_name)
            xml_entry.set('url', pass_entry.url)
            xml_entry.set('username', pass_entry.username)
            xml_entry.set('password', pass_entry.password)

        doc = tostring(xml_root)
        write_xml(doc)

    except:
        print("Error writing file!")
