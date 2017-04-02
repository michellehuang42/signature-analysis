#api key = bf265b6982c2f88c4997785cd6480ed225e7171d

#import line to: from /usr/local/lib/python2.7/dist-packages/watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2017-04-02', api_key='{bf265b6982c2f88c4997785cd6480ed225e7171d}')

print(json.dumps(visual_recognition.classify(images_url="https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg"), indent=2))