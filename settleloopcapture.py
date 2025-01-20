import cv2
import csv
from datetime import datetime

water_quant = int(input("Enter the quantity of water:"))
silt_quant = int(input("Enter the quantity of silt:"))

cam_port0 = 0
cam_port1 = 2

cam1 = cv2.VideoCapture(cam_port0)
cam2 = cv2.VideoCapture(cam_port1)

#cam1.set(cv2.CAP_PROP_FRAME_WIDTH,160)
#cam2.set(cv2.CAP_PROP_FRAME_HEIGHT,120)

cv2.namedWindow("Without Silt")
cv2.namedWindow("With Silt")

img_counter = 0

while True:

    result1, image1 = cam1.read()
    result2, image2 = cam2.read()
    
    print(result1)
    print(result2)
    
    if not result1 and not result2:
        print("Failed to capture image.")
        break

    cv2.imshow("Without_Silt" , image1)
    cv2.imshow("With_Silt" , image2)

    
    k = cv2.waitKey(1)
    
    if k%256 == 27:
        print("Escape hit, Terminated.")
        break
    
    elif k%256 == 32:
        current_date_time = datetime.now()
        
        img_path1 = '/home/coe-re/Photos/Without Silt/'
        img_path2 = '/home/coe-re/Photos/Settle With Silt/'

        
        img_name1 = f"Without_Silt_{img_counter}_{water_quant}.png"
        img_name2 = f"Settle_With_Silt_{img_counter}_{water_quant}_{silt_quant}.png"
        
        
        #when settle
        with open (r'Settle_With_Silt_Experiment_Data.csv', 'a', newline='') as file:
            file_write = csv.writer(file)
            file_write.writerow([current_date_time,img_name2,silt_quant,water_quant])
            
        cv2.imwrite(img_path2+img_name2, image2)
        
        print(f"{img_name2} written!!!")
        img_counter += 1


cam1.release()
cam2.release()
cv2.destroyAllWindows()
