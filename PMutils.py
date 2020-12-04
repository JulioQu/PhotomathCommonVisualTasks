import xml.etree.ElementTree as ET

ignorable = ['ViewportBottomleft',
           'ViewportBottonRight',
           'step']

def setDefault(construction):
    for element in construction.findall('element'):
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

"""Makes blue the elements in (x, y],
while making gray all the other elements."""
def colorBlueBetween(x, y, construction):
    inside = False;
    for element in construction.findall('element'):
        color = element.find('objColor')
        if color is None:
            color = ET.SubElement(element, 'objColor')
        if inside:
            colorBlue(color)
        else:
            colorGray(color)

        if element.get('label') == x:
            inside = True

        if(element.get('label') == y):
            inside = False

"""Remove all break points but the element
labeled as y"""
def setOnlyBreakPoint(y, construction):
    for element in construction:
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
    for element in construction.findall('element'):
        show = element.find('show')
        if show is None:
            show = ET.SubElement(element, 'show')
        if passed:
            show.set('object', 'false')
        else:
            show.set('object', 'true')

        if(element.get('label') == y):
            passed = True

def hideScaling(construction):
    for element in construction.findall('element'):
        if element.get('label') in ignorable:
            if element.find('show') is not None:
                element.find('show').set('object','false')

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
