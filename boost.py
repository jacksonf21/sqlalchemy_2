from PIL import Image, ImageFilter, ImageEnhance 

#Read image
image = Image.open('./images/example.png')
#Display image  
# im.show()

# enh = ImageEnhance.Contrast(im)  
# enh.enhance(1.8).show("30% more contrast"
# ​
enhancer1 = ImageEnhance.Sharpness(image)
enhancer2 = ImageEnhance.Brightness(image)
enhancer3 = ImageEnhance.Contrast(image)
# enhancer2.enhance(2.0).show("Sharpness 2x")
enhancer2.enhance(2).save("images/more-bright.png")
# for i in range(8):
#     factor = i / 4.0
#     enhancer.enhance(factor).show("Sharpness %f" % factor)