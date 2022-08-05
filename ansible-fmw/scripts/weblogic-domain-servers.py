import xml.etree.ElementTree as ET
import os


def serverDetails():
    config = os.getenv('CONFIG_FILE')
    tree = ET.parse(config)
    root = tree.getroot()
    fileName = 'serverDetails.txt'
    namespace = root.tag.split('}')[0]
    # Remove Previous File
    if os.path.exists(fileName):
        os.remove(fileName)
    f = open(fileName, "a")
    for server in root.findall(namespace+"}"+"server"):
        name = server.find(namespace+"}"+"name")
        # Skip Adminserver
        # if name.text.lower().find('adminserver') == -1:
        #     
        f.write(f'{name.text}\n')
    f.close


if __name__ == '__main__':
    serverDetails()
