import os
import uuid
from PIL import Image

def process_and_save_image(file, upload_folder, max_width=1400, quality=82):
    """
    Processes uploaded image:
    - Resizes to max_width
    - Maintains aspect ratio
    - Converts to WebP
    - Strips metadata
    - Returns saved filename
    """
    
    
    # Ensure upload folder exists
    os.makedirs(upload_folder, exist_ok=True)

    # Generate unique filename
    filename = f"{uuid.uuid4().hex}.webp"
    save_path = os.path.join(upload_folder, filename)

    # Open image
    img = Image.open(file)

    # Convert to RGB (important for PNG with transparency)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # Resize if wider than max_width
    if img.width > max_width:
        ratio = max_width / float(img.width)
        new_height = int(float(img.height) * ratio)
        img = img.resize((max_width, new_height), Image.LANCZOS)

    # Save as WebP (compressed)
    img.save(
        save_path,
        "WEBP",
        quality=quality,
        optimize=True
    )

    return filename
import base64
from io import BytesIO
from PIL import Image

def process_and_overwrite_cropped_image(base64_data, save_path, max_width=1400, quality=82):
    """
    Takes base64 cropped image,
    resizes if needed,
    converts to WebP,
    overwrites existing file.
    """

    header, encoded = base64_data.split(",", 1)
    binary_data = base64.b64decode(encoded)

    img = Image.open(BytesIO(binary_data))

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    if img.width > max_width:
        ratio = max_width / float(img.width)
        new_height = int(float(img.height) * ratio)
        img = img.resize((max_width, new_height), Image.LANCZOS)

    img.save(
        save_path,
        "WEBP",
        quality=quality,
        optimize=True
    )
import base64
from io import BytesIO

def process_and_save_base64_image(base64_data, upload_folder, max_width=1400, quality=82):

    header, encoded = base64_data.split(",", 1)
    binary_data = base64.b64decode(encoded)

    img = Image.open(BytesIO(binary_data))

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    if img.width > max_width:
        ratio = max_width / float(img.width)
        new_height = int(float(img.height) * ratio)
        img = img.resize((max_width, new_height), Image.LANCZOS)

    filename = f"{uuid.uuid4().hex}.webp"
    save_path = os.path.join(upload_folder, filename)

    img.save(
        save_path,
        "WEBP",
        quality=quality,
        optimize=True
    )

    return filename

