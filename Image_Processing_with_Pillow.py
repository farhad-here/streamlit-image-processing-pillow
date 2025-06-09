#=======================================================================
#library
import streamlit as st
from PIL import Image,ImageFilter,ImageDraw
#=======================================================================
#function for load image with pillow
def image_processing():
    #pillow load image
    with Image.open(file) as pic:
        pic.load()
    return pic
#function for show image checkbox
def checkOne():
    pic = image_processing()
    with left_1:
        st.image(pic)
# check box for show it in a app
def checkTwo():
    pic = image_processing()
    return pic.show()
#check box for tell format
def checkThree():
    pic = image_processing()
    with center_1:
        st.write('imag format is:',pic.format)
#check box for tell size
def checkFour():
    pic = image_processing()
    with right_1:
        st.write('imag size is:',pic.size)
#check box for tell mode
def checkFive():
    pic = image_processing()
    with right_2:
        st.write('imag mode is:',pic.mode)
#button for blur
def buttonBlur():
    pic = image_processing()
    if blurButton == True:
        blurImg = pic.filter(ImageFilter.BLUR)
        blurImg.show()
#input for boxblur
def inpBoxBlur():
    pic = image_processing()
    boxB = pic.filter(ImageFilter.BoxBlur(boxBlur_inp))
    boxB.show()
#button for grayscale 
def buttonGrayScale():
    global img_gray
    pic = image_processing()
    img_gray = pic.convert("L")
    edges = img_gray.filter(ImageFilter.FIND_EDGES)
    edges.show()
#button for smoothing
def buttonSmooth():
    pic = image_processing()
    img_gray = pic.convert("L")
    img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH)
    edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    edges_smooth.show()
#butto for enhance the edges
def edgeEnhance():
    pic = image_processing()
    img_gray = pic.convert("L")
    img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH)
    edge_enhance = img_gray_smooth.filter(ImageFilter.EDGE_ENHANCE)
    edge_enhance.show()
#butto for  enhance the edgese emboss
def edgeEnhanceEmboss():
    pic = image_processing()
    img_gray = pic.convert("L")
    img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH)
    emboss = img_gray_smooth.filter(ImageFilter.EMBOSS)
    emboss.show()
#input and button for crop
def crop():
    pic = image_processing()
    x_crop,y_crop,z_crop,h_crop = crop_input.split(' ')
    img_cat = pic.crop((int(x_crop), int(y_crop), int(z_crop), int(h_crop)))
    img_cat.show()
#button and input for save crop image
def saveCropImage():
    pic = image_processing()
    x_crop,y_crop,z_crop,h_crop = crop_input.split(' ')
    img_cat = pic.crop((int(x_crop), int(y_crop), int(z_crop), int(h_crop)))
    pathNameCrop = save_crop_input_path_name
    img_cat.save(f'{pathNameCrop}.jpg'.replace('\\','/'))
#button for Threshholding
def threshHolding():
    pic = image_processing()
    img_cat_gray = pic.convert("L")
    img_cat_gray.show()
    threshold = 100
    img_cat_threshold = img_cat_gray.point(
        lambda x: 255 if x > threshold else 0
    )
    img_cat_threshold.show()
#red_green_blue and cmyk and rgb gray scale button
def rgb():
    pic = image_processing()
    red, green, blue =pic.split()
    Im_1 = ImageDraw.Draw(red)
    Im_1.text(xy=(20, 30), text="Red",fill='red')
    Im_2 = ImageDraw.Draw(green)
    Im_2.text(xy=(20, 30), text="Green",fill='Green')
    Im_3 = ImageDraw.Draw(blue)
    Im_3.text(xy=(20, 30), text="Blue",fill='blue')
    red.show()
    green.show()
    blue.show()
def cmyk():
    pic = image_processing()
    x = pic.convert("CMYK")
    x.show()
    
def redGreenBlue():
    pic = image_processing()
    red, green, blue = pic.split()
    zeroed_band = red.point(lambda _: 0)
    red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
    green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
    blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))
    red_merge.show()
    green_merge.show()
    blue_merge.show()
#Image Segmentation Using Thresholding button button
# button segment_thresh_button
def erode(cycles, image):
        for _ in range(cycles):
            image = image.filter(ImageFilter.MinFilter(int(min_filter)))
        return image

def dilate(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(int(max_filter)))
    return image

def segmentThreshButton():
    pic = image_processing()
    img_cat_gray = pic.convert("L")
    threshold = 100
    img_cat_threshold = img_cat_gray.point(
        lambda x: 255 if x > threshold else 0
    )
    step_1 = erode(int(erd), img_cat_threshold)
    step_1.show()

def fillGaps():
    pic = image_processing()
    img_cat_gray = pic.convert("L")
    threshold = float(threshold_1)
    img_cat_threshold = img_cat_gray.point(
        lambda x: 255 if x > threshold else 0
    )
    step_1 = erode(int(erd), img_cat_threshold)
    step_2 = dilate(int(dil), step_1)
    step_2.show()

def sharpEdgeRemove():
    pic = image_processing()
    img_cat_gray = pic.convert("L")
    threshold = float(threshold_2)
    img_cat_threshold = img_cat_gray.point(
        lambda x: 255 if x > threshold else 0
    )
    step_1 = erode(int(erd), img_cat_threshold)
    step_2 = dilate(int(dil), step_1)
    cat_mask = erode(int(erd), step_2)
    cat_mask = cat_mask.convert("L")
    cat_mask = cat_mask.filter(ImageFilter.BoxBlur(float(input_box_blur)))
    cat_mask.show()
def removeFromBack():
    pic = image_processing()
    img_cat_gray = pic.convert("L")
    threshold = float(threshold_3)
    img_cat_threshold = img_cat_gray.point(
        lambda x: 255 if x > threshold else 0
    )
    step_1 = erode(int(erd), img_cat_threshold)
    step_2 = dilate(int(dil), step_1)
    cat_mask = erode(int(erd), step_2)
    cat_mask = cat_mask.convert("L")
    cat_mask = cat_mask.filter(ImageFilter.BoxBlur(float(input_box_blur)))
    blank = pic.point(lambda _: 0)
    cat_segmented = Image.composite(pic, blank, cat_mask)
    cat_segmented.show()

#=======================================================================

#Noting just for page in streamlit
st.markdown("# Image processing with pillow")
st.sidebar.markdown("# Image processing with pillow")
#header sm in web
'---------------------------------------------------------------------------------------------------------------'
'### In this section drag the file'
#upload file
img = st.file_uploader("file")
'---------------------------------------------------------------------------------------------------------------'
#pillow start
file = img


#=========================================================

'### image info'
#check box
#place checkbox with columns
left_1,left_2,center_1,right_1,right_2 = st.columns(5)
check_1 = left_1.checkbox('Show image')
check_2 = left_2.checkbox('show it in a app')
check_3 = center_1.checkbox('format')
check_4 = right_1.checkbox('size')
check_5 = right_2.checkbox('mode')
'---------------------------------------------------------------------------------------------------------------'

'### blur and boxblur'
#blur button
b_left_1,i_left_1,ch_right = st.columns(3) 
blurButton = b_left_1.button('blur')
    #box blur input
boxBlur_inp = i_left_1.number_input('How much boxblur: ',placeholder='34')
    #check show image for box blur
check_6 = ch_right.checkbox('show')
'---------------------------------------------------------------------------------------------------------------'

'### Edge Detection, Edge Enhancement, and Embossing'
#grayscale Button
b_left_1,b_left_2,b_left_3,b_left_4 = st.columns(4) 
grayScaleButton = b_left_1.button('grayscale')
#smooth button
smoothButton = b_left_2.button('smoothing')
#enhance the edges button
enhnace_edge_button = b_left_3.button('enhnace edge')
#enhance the edges emboss button
enhnace_edge_emboss_button = b_left_4.button('enhnace edge emboss')
'---------------------------------------------------------------------------------------------------------------'

'### Image Segmentation and Superimposition'
#crop input
i_left_1,i_left_2,b_left_1= st.columns(3)
b_left_2,b_left_3 = st.columns(2) 
crop_input = i_left_1.text_input('coord',placeholder='400 100 800 600')
#crop button
crop_button = b_left_2.button('crop')
#save crop img button
save_crop_button = b_left_3.button('save')
    #save crop path wiht name input
save_crop_input_path_name = i_left_2.text_input('Path and Name',placeholder='Path+\+name')
#Thresholding 
thresh_holding_button = b_left_1.button('gray and threshhold')
#red green blue and CMYK
b_left_1,b_left_2,b_left_3= st.columns(3)
rgb_button = b_left_1.button('RGB Grayscale')
cmyk_button = b_left_2.button('CMYK')
    #for CMYK AFTER I CLICKED THE BUTTON
if cmyk_button == True:
    pic = image_processing()
    xx = pic.convert("CMYK")
    st.write('imag mode is:',xx.mode)
r_g_b = b_left_3.button('RedGreenBlue')
'---------------------------------------------------------------------------------------------------------------'
'### Image Segmentation Using Thresholding'
# Image Segmentation Using Thresholding input
#place of input
col_1,col_2,col_3,col_4 = st.columns(4)
min_filter = col_1.text_input('number of min filter',placeholder='3',key='nminfliter')
max_filter = col_2.text_input('number of max filter',placeholder='3',key='nmaxfliter')
erd = col_3.text_input('number for erdo',placeholder='12',key='nerdo')
dil = col_4.text_input('number of dilate',placeholder='58',key='ndilate')

# Image Segmentation Using Thresholding buttons
    #info sec 1
st.info('The eroded threshold image no longer contains white pixels representing the background of the image')
    #button for bg of image
segment_thresh_button = st.button('background of the image')
    #info sec2
st.info('You can perform dilations to fill the gaps')
st.info('The fifty-eight cycles of dilation filled all the holes in the mask')
    #threshold for fill gap
threshold_1 = st.text_input('Threshold',placeholder='100')
    # button for fill gap
fill_gap_button = st.button('fill gap')
    #info sec 3
st.info('However, this mask is too big. You can therefore finish the process with a series of erosions')
st.info('However, this mask is too big. You can therefore finish the process with a series of erosions')
st.info('You can avoid the sharp edges of a binary mask by blurring this mask')
    #threshold for evoide sharp edge
threshold_2 = st.text_input('Threshold_2',placeholder='100',key='threshold2')
#input for boxblur
col1,col2 = st.columns(2)
    #input box blur
input_box_blur = col1.text_input('box blur number',placeholder='20',key='boxblurnumber for ecoide sharp edge')
    #button for evoide sharp edge
evoide_sharp_button = col2.button('evoide sharp edges')
    #info sec 4
st.info(' Now you are ready to extract the image of the cat from its background')
    #threshold for remove from background
threshold_3 = st.text_input('Threshold_3',placeholder='100',key='threshold3')
    #button for remove from background
remove_back_button = st.button('remove from background')
#=========================================================

#if image was upload lets work
if img != None:
    #checkbox = True show pic in a web
    if check_1 == True:
        checkOne()
    # #checkbox = True show pic in a app
    if check_2 == True:
        checkTwo()
    #checkbox = True show img format
    if check_3 == True:
        checkThree()
    #checkbox = True show img size
    if check_4 == True:
        checkFour()
    #checkbox = True show img mode
    if check_5 == True:
        checkFive()
    #button = True show img blur
    if blurButton == True:
        buttonBlur()
    #chekbox = True show img boxblur with in input number for how much boxblur
    if check_6 == True:
        inpBoxBlur()
    #button = True show img grayscale
    if grayScaleButton == True:
        buttonGrayScale()
    #button = True show img smooth
    if smoothButton == True:
        buttonGrayScale()
    #button = True show img enhance
    if enhnace_edge_button == True:
        edgeEnhance()
    #button = True show img enhance
    if enhnace_edge_emboss_button == True:
        edgeEnhanceEmboss()
    #button = true image crop
    if crop_input != None:
        if crop_button == True:
            crop()
        if save_crop_button == True:
            saveCropImage()
    #button = true show image gray and treshhold
    if thresh_holding_button == True:
        threshHolding()
    #button = true show image red green blue  
    if rgb_button == True:
        rgb()
    #button = true show image red green blue  and cmyk
    if cmyk_button == True:
        cmyk()
    if r_g_b == True:
        redGreenBlue()
    #Image Segmentation Using Thresholding button
    if segment_thresh_button == True:
        segmentThreshButton()
    if fill_gap_button == True:
        fillGaps()
    if evoide_sharp_button == True:
        sharpEdgeRemove()
    if remove_back_button == True:
        removeFromBack()