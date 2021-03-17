import cv2
import tensorflow as tf
import numpy as np


# def predict(img):
#     image = img.copy()
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     image = cv2.bitwise_not(image)
    
#     image = cv2.resize(image, (28, 28))
#     cv2.imshow("num",image)
#     image = image.astype('float32')
#     image = image.reshape(1, 28, 28, 1)
    
#     cv2.waitKey()
#     image /= 255
#     model = keras.models.load_model('C:/Users/surya/Desktop/Projects/object_detection/Handwritten digit recognizer/cnn.h5')
#     pred = model.predict(image.reshape(1, 28, 28, 1), batch_size=1)
    
#     print("Predicted Number: ", pred.argmax())
model=tf.keras.models.load_model("C:/Users/surya/Desktop/Projects/zf_python/junction_box/new/trained_model.h5")
model_wire=tf.keras.models.load_model("C:/Users/surya/Desktop/Projects/zf_python/junction_box/new/trained_model_wire.h5")

def predict(img):
    img=cv2.resize(img,(64,64))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    ret, im_th = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite(r'C:/Users/surya/Desktop/Projects/zf_python/junction_box/new/temp/t/trmp.jpg',im_th)
    gen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255.,validation_split=0.05)
    train=gen.flow_from_directory(r"C:/Users/surya/Desktop/Projects/zf_python/junction_box/new/temp/",target_size=(28,28),subset="training",batch_size=16,color_mode="grayscale")
    x,y=train.next()

    pred=model.predict(x)
    # print(np.argmax(pred)+1)
    return np.argmax(pred)+1

def predict_wire(img):

    array=[1,2,3,5,6,7]
    cv2.imwrite(r'C:/Users/surya/Desktop/Projects/zf_python/junction_box/new/temp/t/trmp.jpg',img)
    gen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255.,validation_split=0.05)
    train=gen.flow_from_directory(r"C:/Users/surya/Desktop/Projects/zf_python/junction_box/new/temp/",target_size=(28,28),subset="training",batch_size=16,color_mode="grayscale")
    x,y=train.next()
    pred=model_wire.predict(x)
    return array[np.argmax(pred)]

img = cv2.imread(r'C:\Users\surya\Desktop\Projects\object_detection\wire_data\IMG_20201223_120539.jpg')
img = cv2.resize(img,(1500,1000))
img_cp = img.copy()
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

light_yellow = (90, 100, 100)
dark_yellow = (100, 255, 255)
mask = cv2.inRange(hsv, light_yellow, dark_yellow)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

wireArr = []

for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.03 * peri, True)
    if len(approx) >= 4 and len(approx) <=6:
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
    
        if area>2000 and h > w:
            wireArr.append([x,x+w,y,y+h])
            he=int(np.round(h*0.35))
            num = predict_wire(img[y:y+he, x:x+w])
            cv2.putText(img, str(num), (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255), 1)
            # crop_img = img[y:y+h, x:x+w]
            # cv2.imshow("wire",crop_img)
            # cv2.waitKey()
            # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            
light_white = (200, 200, 200)
dark_white = (255, 255,255)
mask = cv2.inRange(img, light_white, dark_white)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

numArr = []
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.035 * peri, True)
    
    if len(approx) >=4 and len(approx) <=6:
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        
        if(area > 700 and max(w,h)-min(w,h) <30):
            numArr.append([x,x+w,y,y+h])
            num = predict(img[y:y+h, x:x+w])
            cv2.putText(img, str(num), (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255), 1)
            # print(str(y)+" "+str(y+h)+" "+str(x)+" "+str(x+w))
            # crop_img = img[y+10:y+h-10, x+5:x+w-10]
            # crop_img = img[y:y+h, x:x+w]
            # cv2.imshow("num",crop_img)
            # cv2.waitKey()
            # predict(crop_img)
            # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


pre_final = []
post_final = []
for wire in wireArr: 
    for num in numArr:
        if((wire[0]<num[0] and wire[1]>num[0]) or (wire[0]<num[1] and wire[1]>num[1])):
            pre_final.append([wire,num])
            if(wire[0]<num[0] and wire[1]>num[1]):
                cv2.rectangle(img,(wire[0],wire[2]),(wire[1],num[3]),(0,255,0),3)
                post_final.append([wire,num])
                
                # cv2.imshow("output_wire",img[num[2]:num[3], num[0]:num[1]])
                # cv2.waitKey()
            # crop_wire = img[wire[2]:wire[3], wire[0]:wire[1]]
            # cv2.imshow("wire",crop_wire)
            # crop_wire = img[num[2]:num[3], num[0]:num[1]]


            # crop_final = img_cp[wire[2]:num[3],min(wire[0],num[0]):max(wire[1],num[1])]
            # cv2.imshow("num",crop_final)
            # cv2.waitKey()
for i in range(len(pre_final)-1):
    for j in range(i+1,len(pre_final)):
        if(pre_final[i][0] == pre_final[j][0]):
            diff1 = min(pre_final[i][0][1],pre_final[i][1][1]) - max(pre_final[i][0][0],pre_final[i][1][0])
            diff2 = min(pre_final[j][0][1],pre_final[j][1][1]) - max(pre_final[j][0][0],pre_final[j][1][0])
            if(diff1>diff2):
                if(not post_final.__contains__(pre_final[i])):
                    cv2.rectangle(img,(pre_final[i][0][0],pre_final[i][0][2]),(pre_final[i][0][1],pre_final[i][1][3]),(255,0,0),2)
                    post_final.append(pre_final[i])
                    # cv2.imshow("output_wire",img)
                    # cv2.waitKey()
            else:
                if(not post_final.__contains__(pre_final[j])):
                    cv2.rectangle(img,(pre_final[j][0][0],pre_final[j][0][2]),(pre_final[j][0][1],pre_final[j][1][3]),(255,0,0),2)
                    post_final.append(pre_final[j])
                    # cv2.imshow("output_wire",img)
                    # cv2.waitKey()

cv2.imshow("output_wire",img)
cv2.waitKey()



