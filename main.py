import cv2
import numpy as np
import glob
import os

#'logo3_preview_rev_1.png'
logo = cv2.imread(str(input("enter the path of the logo: ")))
logo = cv2.resize(logo, (0, 0), fx = 0.6, fy = 0.6)
h_logo, w_logo, _ = logo.shape
#"photos/*.*"
#
images_path = glob.glob(str(input("enter the path of the file that contains the photos: "))+ "/*.*")
saved_path = str(input("enter the location of the file you want to save to: "))
print("adding the logo to all photos please wait.....")

for img_path in images_path:
    print("logo add to " + img_path )
    img = cv2.imread(img_path)
    img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
    h_img,w_img, _ = img.shape

    bottom_y = 0 + h_logo
    right_x = 0 + w_logo

    roi = img[0:bottom_y,0:right_x]
    result = cv2.addWeighted(roi, 1,logo,0.3,0)
    img[0:bottom_y,0:right_x] = result
    result = img[0:bottom_y,0:right_x]
    filename = os.path.basename(img_path)
    
    cv2.imwrite(f"{saved_path}/photo_" + filename,img)
    


print("the logo has been added to all photos")
print("all photos are saved in " + saved_path)



# center_y = int(h_img / 2)
# center_x = int(w_img / 2)
# top_y = center_y - (h_logo // 2)
# left_x = center_x - (w_logo // 2)
# cv2.circle(img,(0,0),10,(0,255,0),-1)
# cv2.circle(img,(right_x,bottom_y),10,(0,255,0),-1)
# cv2.imshow("logo",logo)
# cv2.imshow("img",img)
# cv2.imshow("ROi",roi)
# cv2.imshow("result",result)
# cv2.imwrite('finaltest.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
