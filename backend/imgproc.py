import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow
from skimage.draw import rectangle_perimeter, rectangle, circle_perimeter_aa, set_color, circle
from skimage.transform import resize
from PIL import Image, ImageDraw, ImageFont

# Create image with specified color
def create_image(w, h, color=(0, 0, 0)):
    image = np.zeros((h, w, len(color)), dtype=np.uint8)
    for i in range(len(color)):
        image[:, :, i] = color[i]
    return image

# Create image with text only
def create_text_image(text, fontname='arial', fontsize=24, textcolor=(0, 0, 0), backcolor=(255, 255, 255)):
    font = ImageFont.truetype(font=fontname, size=fontsize)
    w, h = font.getsize(text)
    image = numpy2pil(create_image(2 * w, 2 * h, backcolor))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, fill=textcolor, font=font)

    image = pil2numpy(image)
    mask = image - create_image(image.shape[1], image.shape[0], backcolor)

    top = 0
    for i in range(mask.shape[0]):
        if np.sum(mask[i, :, :]) > 0:
            if i > 0:
                top = i - 1
            break
    bottom = mask.shape[0] - 1
    for i in reversed(range(mask.shape[0])):
        if np.sum(mask[i, :, :]) > 0:
            if i < mask.shape[0] - 1:
                bottom = i + 1
            break
    left = 0
    for i in range(mask.shape[1]):
        if np.sum(mask[:, i, :]) > 0:
            if i > 0:
                left = i - 1
            break
    right = mask.shape[1] - 1
    for i in reversed(range(mask.shape[1])):
        if np.sum(mask[:, i, :]) > 0:
            if i < mask.shape[1] - 1:
                right = i + 1
            break

    return image[top:bottom + 1, left:right + 1, :]

# Create image with text only. Width of text is less or equal to maxwidth parameter
def create_text_image_maxwidth(text, maxwidth, fontname='arial', fontsize=24, textcolor=(0, 0, 0), backcolor=(255, 255, 255)):
    image = create_text_image(text, fontname=fontname, fontsize=fontsize, textcolor=textcolor, backcolor=backcolor)
    index = 1
    while image.shape[1] > maxwidth:
        image = create_text_image(text, fontname=fontname, fontsize=fontsize - index, textcolor=textcolor, backcolor=backcolor)
        index += 1
    return image

# Create image with text only. Height of text is less or equal to maxheight parameter
def create_text_image_maxheight(text, maxheight, fontname='arial', fontsize=24, textcolor=(0, 0, 0), backcolor=(255, 255, 255)):
    image = create_text_image(text, fontname=fontname, fontsize=fontsize, textcolor=textcolor, backcolor=backcolor)
    index = 1
    while image.shape[0] > maxheight:
        image = create_text_image(text, fontname=fontname, fontsize=fontsize - index, textcolor=textcolor, backcolor=backcolor)
        index += 1
    return image

# Show image (as numpy array) using pyplot
def show_image(image, title=None):
    plt.figure()
    imshow(image, cmap='gray')
    if title is not None:
        plt.title(title)
    plt.show()

# Show images (as list of numpy arrays) using pyplot
def show_images(images, nrows=None, ncols=None, titles=None):
    if nrows is None:
        if ncols is None:
            size = int(np.ceil(np.sqrt(len(images))))
            nrows, ncols = size, size
        else:
            nrows = int(np.ceil(len(images) / ncols))
    else:
        if ncols is None:
            ncols = int(np.ceil(len(images) / nrows))

    plt.figure()
    for i in range(nrows):
        for j in range(ncols):
            index = ncols * i + j
            if index >= len(images):
                continue
            plt.subplot(nrows, ncols, index + 1)
            imshow(images[index], cmap='gray')
            if titles is not None:
                plt.title(titles[index])
    plt.tight_layout()
    plt.show()

# Save list of images as gif
def save_gif(imgs, path: str, loop=False, fps=10):
    imgs = [numpy2pil(im) for im in imgs]
    imgs[0].save(path, format='GIF', append_images=imgs[1:], loop=loop, duration=1000 / fps, save_all=True)

# Convert numpy array to cv2 format
def numpy2cv(image):
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#Convert cv2 image to numpy
def cv2numpy(image):
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert numpy array to PIL format
def numpy2pil(image):
    return Image.fromarray(image)

# Convert PIL image to numpy format
def pil2numpy(image):
    return np.array(image)

# Image transparency check
def is_alpha(image):
    return image.shape[2] == 4

# Correct skimage resize
def resize_image(image, shape):
    return (255 * resize(image, shape)).astype(np.uint8)

# Correct skimage rotate
def rotate_image(image, angle, resize=False):
    return (255 * rotate(image, angle, resize=resize)).astype(np.uint8)

# Draw mask on image using specified color
def draw_mask(image, rows, cols, color, val=None):
    result = image.copy()
    set_color(result, (rows, cols), color, alpha=val if val is not None else 1)
    return result

# Draw rectangle on image
def draw_rect(image, x, y, w, h, color=(255, 255, 255)):
    r, c = rectangle_perimeter((y, x), extent=(h, w), shape=image.shape, clip=True)
    return draw_mask(image, r, c, color)

# Draw rectangle with bold lines defined by width parameter (filled inside the rect)
def draw_boldrect(image, x, y, w, h, width, color=(255, 255, 255)):
    image = draw_fillrect(image, x, y, w, width, color)
    image = draw_fillrect(image, x, y + h - width, w, width, color)
    image = draw_fillrect(image, x, y + width, width, h - 2 * width, color)
    image = draw_fillrect(image, x + w - width, y + width, width, h - 2 * width, color)
    return image

# Draw filling rectangle on image
def draw_fillrect(image, x, y, w, h, color=(255, 255, 255)):
    r, c = rectangle((y, x), extent=(h, w), shape=image.shape)
    return draw_mask(image, r, c, color)

# Draw circle on image
def draw_circle(image, x, y, radius, color=(255, 255, 255)):
    r, c, val = circle_perimeter_aa(y, x, radius, shape=image.shape)
    return draw_mask(image, r, c, color, val=val)

def draw_fillcircle(image, x, y, radius, color=(255, 255, 255)):
    r, c = circle(y, x, radius, shape=image.shape)
    return draw_mask(image, r, c, color)

# Draw one image on another
def draw_image(image, inserted_image, x, y):
    assert image.shape[2] == inserted_image.shape[2], 'Different types of images!!'
    w, h = inserted_image.shape[1], inserted_image.shape[0]
    if image.shape[2] == 3:
        result = image.copy()
        result[y:y + h, x:x + w, :] = inserted_image
    elif image.shape[2] == 4:
        result = image.copy() / 255
        template = np.zeros((image.shape[0], image.shape[1], 4))
        template[y:y + h, x:x + w, :] = inserted_image / 255
        mask = np.stack([template[:, :, 3]] * 4, axis=2)
        inv_mask = 1.0 - mask
        result = result * inv_mask + template * mask
        result = (255 * result).astype(np.uint8)
    else:
        return None
    return result

# Add borders with specified width and color
def draw_borders(image, width, color=(0, 0, 0)):
    back = np.ones((image.shape[0] + 2 * width, image.shape[1] + 2 * width, image.shape[2]), dtype=np.uint8)
    for i in range(len(color)):
        back[:, :, i] *= color[i]
    back[width:width + image.shape[0], width:width + image.shape[1], :] = image
    return back

# Draw bounding box on image
def draw_box(image, x, y, w, h, width=5, title=None, color=(30, 180, 40)):
    image = draw_boldrect(image, x, y, w, h, width, color)
    if title is not None:
        npix = 3
        title_image = create_text_image_maxwidth(title, w - 2 * npix, fontsize=32, textcolor=(255, 255, 255), backcolor=color)
        title_image = draw_borders(title_image, npix, color=color)
        image = draw_image(image, title_image, x, y - title_image.shape[0])
    return image

# Draw multiple boxes on image
# boxes - list of tuples (x, y, w, h, title)
def draw_boxes(image, boxes, width=5, color=(30, 180, 40)):
    for box in boxes:
        title = box[4] if len(box) > 4 else None
        image = draw_box(image, box[0], box[1], box[2], box[3], width=width, title=title, color=color)
    return image

# Draw multiple points on image
# points - 2d numpy array
def draw_points(image, points, radius=5, color=(200, 30, 10)):
    for point in points:
        image = draw_fillcircle(image, point[0], point[1], radius, color=color)
    return image