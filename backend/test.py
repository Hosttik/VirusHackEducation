from tasks.mathematic import task11
from skimage.viewer import ImageViewer

result = task11()
print(result['text'])
print(result['answer'])

# if result['image'] is not None:
#     viewer = ImageViewer(result['image'])
#     viewer.show()
