from tasks.mathematic import task11
from tasks.russian import task15
from skimage.viewer import ImageViewer
import pickle

# with open('data/accents.txt', 'r') as f:
#     lines = f.readlines()
#
# allwords = []
# for line in lines:
#     if line.startswith(' '):
#         continue
#     split = line.split('|')
#     word = split[1]
#     word_split = word.split("'")
#     if len(word_split) > 2:
#         continue
#     word_filtered = []
#     for ws in word_split[:-1]:
#         s = ws[:-1].lower() + ws[-1].upper()
#         word_filtered.append(s)
#     word_filtered.append(word_split[-1])
#     word_filtered = ''.join(word_filtered)
#     allwords.append(word_filtered)
#
# with open('accents.pkl', 'wb') as f:
#     pickle.dump(allwords, f)
#
# print(len(allwords))


result = task15()
print(result['text'])
print(result['answer'])

# if result['image'] is not None:
#     viewer = ImageViewer(result['image'])
#     viewer.show()
