import xml.etree.ElementTree as ET

def isIgnorable(element):
    lis = ['ViewportBottomleft',
           'ViewportBottonRight',
           'step']
    s = element.get('label')
    return s in lis

def setDefault(construction):
    for element in construction:
        if isIgnorable(element):
            return
        show = element.find('show')
        if show is not None:
            show.set('label', 'false')
        color = element.find('objColor')
        if color is not None:
            colorGray(color)
        else:
            ET.SubElement(element, 'objColor')
            colorGray(element.find('objColor'))
        if element.get('type') == 'point':
            setDefaultPoint(element)
        if element.find('lineStyle') is not None:
            element.find('lineStyle').set('thickness', '7')

def setDefaultPoint(point):
    pointSize = point.find('pointSize')
    if pointSize is not None:
        point.set('val', '5')
    ET.SubElement(point, 'pointSize')
    point.find('pointSize').set('val', '5')

    pointStyle = point.find('pointStyle')
    if pointStyle is not None:
        pointStyle.set('val', '10')
    ET.SubElement(point, 'pointStyle')
    point.find("pointStyle").set('val', '10')

"""Makes blue the elements between x and y, including them,
while making gray all the other elements."""
def colorBlueBetween(x, y, construction):
    inside = False
    for element in construction:
        if(isIgnorable(element)):
            return
        color = element.find('objColor')
        if color is None:
            color = ET.SubElement(element, 'objColor')

        if element.get('label') == x:
            inside = True

        if inside:
            colorGray(color)
        else:
            colorBlue(color)

        if(element.get('label') == y):
            inside = False

"""Remove all break points but the element
labeled as y"""
def setOnlyBreakPoint(y, construction):
    for element in construction:
        if(isIgnorable(element)):
            return
    bp = element.find('breakpoint')
    if bp is None:
        bp = ET.SubElement(element, 'breakpoint')

    if(element.get('label') == y):
        bp.set('val', 'true')
    else:
        bp.set('val', 'false')

"""Show all the elements until y, including y, and
hide all the others."""
def showUntil(y, construction):
    passed = False
    for element in construction:
        if(isIgnorable(element)):
            return
        show = element.find('show')
        if show is None:
            show = ET.SubElement(element, 'show')
        if passed:
            show.set('object', 'false')
        else:
            show.set('object', 'true')

        if(element.get('label') == y):
            passed = True

def colorGray(color):
    color.set('r', '127')
    color.set('g', '127')
    color.set('b', '127')

def colorBlue(color):
    color.set('r', '13')
    color.set('g', '162')
    color.set('b', '204')

def colorOrange(color):
    return

def colorGreen(color):
    return

tree.write('geogebra.xml')
