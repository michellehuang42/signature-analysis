from PIL import Image
from tesserocr import PyTessBaseAPI, RIL, PSM, iterate_level

image = Image.open('writing2.jpg')
with PyTessBaseAPI() as api:
    api.SetImage(image)
    boxes = api.GetComponentImages(RIL.TEXTLINE, True)
    print 'Found {} textline image components.'.format(len(boxes))
    for i, (im, box, _, _) in enumerate(boxes):
        # im is a PIL image object
        # box is a dict with x, y, w and h keys
        api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
        ocrResult = api.GetUTF8Text()
        conf = api.MeanTextConf()
        print (u"Box[{0}]: x={x}, y={y}, w={w}, h={h}, "
               "confidence: {1}, text: {2}").format(i, conf, ocrResult, **box)
'''
with PyTessBaseAPI(psm=PSM.AUTO_OSD) as api:
    image = Image.open("baselinetest.jpg")
    api.SetImage(image)
    api.Recognize()

    it = api.AnalyseLayout()
    orientation, direction, order, deskew_angle = it.Orientation()
    print "Orientation: {:d}".format(orientation)
    print "WritingDirection: {:d}".format(direction)
    print "TextlineOrder: {:d}".format(order)
    print "Deskew angle: {:.4f}".format(deskew_angle)


with PyTessBaseAPI() as api:
    api.SetImageFile('baselinetest.jpg')
    api.SetVariable("save_blob_choices", "t")
    #api.SetRectangle(37, 228, 548, 31)
    api.Recognize()

    ri = api.GetIterator()
    level = RIL.SYMBOL
    for r in iterate_level(ri, level):
        symbol = r.GetUTF8Text(level)  # r == ri
        conf = r.Confidence(level)
        if symbol:
            print u'symbol {}, conf: {}'.format(symbol, conf),
        indent = False
        ci = r.GetChoiceIterator()
        for c in ci:
            if indent:
                print '\t\t ',
            print '\t- ',
            choice = c.GetUTF8Text()  # c == ci
            print u'{} conf: {}'.format(choice, c.Confidence())
            indent = True
        print '---------------------------------------------'
'''
