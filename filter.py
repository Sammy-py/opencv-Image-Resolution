import  cv2

def ImgSave(path,image,jpg_quality=None,png_compress=None):
    if jpg_quality:
        cv2.imwrite(path,image,[int(cv2.IMWRITE_JPEG_QUALITY),jpg_quality])
    elif png_compress:
        cv2.imwrite(path,image,[int(cv2.IMWRITE_PNG_COMPRESSION),png_compress])
    else:
        cv2.imwrite(path,image)
        
        
def main():
    path="IMG_20211017_112341.jpg"   # yours picture name  
    image=cv2.imread(path)
    cv2.imshow('showed pic',image)
 
    son_jpg="filteredJPG.jpg"
    ImgSave(son_jpg,image,jpg_quality=7) #1 - 10 scale
 
 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__=="__main__":
    main()        

#https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
    