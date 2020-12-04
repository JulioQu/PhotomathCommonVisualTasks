from zipfile import ZipFile
import sys
import xml.etree.ElementTree as ET
import PMutils as PM
import os

filen = sys.argv[1]
filename = filen.replace('.ggb','')

DEFAULTS = ["defaultDocs/geogebra_defaults2d.xml",
            "defaultDocs/geogebra_defaults3d.xml",
            "defaultDocs/geogebra_javascript.js"]

with ZipFile(filen, 'r') as zip:
    geogebraFile = ET.fromstring(zip.read('geogebra.xml'))
    
construction = geogebraFile.find('construction')
PM.setDefault(construction)

os.mkdir("./" + filename)

bpElements = ['step']

for ele in construction.findall('element'):
    bp = ele.find('breakpoint')
    if bp is not None:
        if bp.get('val') == 'true':
            bpElements.append(ele.get('label'))

for i in range(0,len(bpElements)-1):
    PM.colorBlueBetween(bpElements[i],
                        bpElements[i+1],
                        construction)
    
    PM.setOnlyBreakPoint(bpElements[i+1],
                         construction)

    PM.showUntil(bpElements[i+1],
                 construction)

    PM.hideScaling(construction)

    ET.ElementTree(geogebraFile).write('geogebra.xml')

    resultFile = "./" + filename + "/" + str(i) + ".ggb"
    with ZipFile(os.path.join(resultFile),'w') as zip:
        for s in DEFAULTS:
            zip.write(s);
        zip.write('geogebra.xml')
    os.remove('geogebra.xml')
