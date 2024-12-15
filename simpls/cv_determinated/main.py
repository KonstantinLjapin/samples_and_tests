import pprint

from mtcnn import MTCNN
from mtcnn.utils.images import load_image
import json
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"

detector = MTCNN(device="CPU:0")

# Load an image
image = load_image("ivan.jpg")

# Detect faces in the image
result = detector.detect_faces(image)


with open("mydata.json", "w", encoding="utf-8") as final:
    json.dump(str(result), final, indent=4)

with open("mydata.json", "r", encoding="utf-8") as final:
    data = json.load(final)
    print(json.dumps(data, indent=4))
    pprint.pprint(data, compact=True)
