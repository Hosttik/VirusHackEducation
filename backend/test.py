from tasks.mathematic import task2
from skimage.viewer import ImageViewer

result = task2()
print(result['text'])
print(result['answer'])

if result['image'] is not None:
    viewer = ImageViewer(result['image'])
    viewer.show()
