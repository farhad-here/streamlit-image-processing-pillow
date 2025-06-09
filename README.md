# 🖼️ Streamlit Image Processing with Pillow

A powerful and interactive image processing web app built with [Streamlit](https://streamlit.io) and [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/). This tool allows users to upload an image and apply various transformations and filters, including edge detection, segmentation, format analysis, grayscale conversion, cropping, and background removal.

---

## 🚀 Features

- ✅ Upload and display image info (format, size, mode)
- 🔍 Apply Blur and BoxBlur filters
- 🎨 Convert to Grayscale, Smooth, Enhance edges, Emboss
- ✂️ Crop images and save with custom path and name
- 📐 Thresholding and segmentation (Erosion/Dilation)
- 🔄 RGB & CMYK color manipulation
- 🎭 Background removal using `rembg`
- 🌾 Interactive cropping using `streamlit-cropper`

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/streamlit-image-processing-pillow.git
   cd streamlit-image-processing-pillow
   ```
2. Create a virtual environment (optional but recommended):
```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

3.Install the required libraries:

```bash

pip install -r requirements.txt


```


# 🛠️ Requirements

streamlit
pillow
rembg
streamlit-cropper

# 📷 Screenshots

![i1](https://github.com/user-attachments/assets/17d628e3-a01a-445c-af2c-5c70d6cd0105)

![i2](https://github.com/user-attachments/assets/ebee7f01-b2e4-4f41-977e-0bf76a37e61b)

![i3](https://github.com/user-attachments/assets/1162c8f5-129a-4b1a-ab1b-536154583ad2)

![i3](https://github.com/user-attachments/assets/761d9a10-1b04-44ff-bc2d-783be44379f7)

![i4](https://github.com/user-attachments/assets/e794fcab-2523-4870-aa33-e1f15378f527)

![i5](https://github.com/user-attachments/assets/65d5e956-d369-4590-87ff-0cfbc250fb13)

![i6](https://github.com/user-attachments/assets/2a7eb9c2-8566-4015-b8a9-7c8aac214d94)



# 🛸 Some error if occur:

```bash

ImportError: DLL load failed while importing onnxruntime_pybind11_state: A dynamic link library (DLL) initialization routine failed.

```


```bash
pip uninstall onnxruntime
pip install onnxruntime --upgrade


```

# ✍️ Author
Created by FarhadGaherdoost
For image lovers, researchers, students, and anyone interested in computer vision made simple.


