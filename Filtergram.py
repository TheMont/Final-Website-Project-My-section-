import filters

def main():
    #Ask what image the user wants to edit
    filename = input("Enter the name of the image file to edit:")

    # load the image from the specified filename
    img = filters.load_img(filename)

#Apply filters!!
    newimg = filters.obamicon(img)

    # Save the final filtered image
    filters.save_img(newimg, "recolored.jpg")

    #SetUp Code
if __name__ == "__main__":
    main()
