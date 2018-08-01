from PIL import Image

def load_img(filename):
    im= Image.open(filename)
    return im

def show_img(im):
    im.show()

def save_img(im,filename):
    im.save(filename, "jpeg")
    show_img(im)

def obamicon(im):
        #load the pixel data from im
        pixels = im.getdata()

        #create a list to hold the new image pixel data
        new_pixels =[]

        #Define color constants to use for recoloring
        darkBlue = (0, 51, 76)
        red= (217, 26, 33)
        lightBlue = (112, 150, 158)
        yellow = (252, 227, 166)

        #process the pixels in the Image
        for p in pixels:
            #Pixel intensity = R Value + G Value + B Value
            intensity = p[0] + p[1] + p[2]

            if intensity < 182:
                new_pixels.append(darkBlue)

            elif intensity>=182 and intensity < 364:
                new_pixels.append(red)

            elif intensity >= 364 and intensity < 546:
                new_pixels.append(lightBlue)

            elif intensity >=546:
                new_pixels.append(yellow)

                #save the filtered pixels as a new image
        newim = Image.new("RGB", im.size )
        newim.putdata(new_pixels)
        return newim
