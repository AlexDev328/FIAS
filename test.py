# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


def parseXML(xml_file):
    """
    Парсинг XML используя ElementTree
    """
    tree = ET.ElementTree(file=xml_file)
    print(tree.getroot())
    root = tree.getroot()
    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

    for child in root:
        print(child.tag, child.attrib)
        if child.tag == "appointment":
            for step_child in child:
                print(step_child.attrib)






if __name__ == "__main__":
    parseXML('./01/AS_ADDR_OBJ_20220221_29b5b8fb-4081-46d4-a898-36bcd31e59ed.XML')