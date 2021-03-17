import cv2
import imutils
import numpy as np
import tensorflow as tf
model=tf.keras.models.load_model("trained_model2.h5")
model_wire=tf.keras.models.load_model("trained_model_wire.h5")

def predict(img):

    img=cv2.resize(img,(64,64))
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (3, 3), 0)
    #ret, im_th = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite(r'C:\Users\surya\Desktop\Projects\zf_python\junction_box\new\temp\t\trmp.jpg',img)
    gen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255.,validation_split=0.05)
    train=gen.flow_from_directory(r"C:\Users\surya\Desktop\Projects\zf_python\junction_box\new\temp",target_size=(28,28),subset="training",batch_size=16,color_mode="grayscale")
    x,y=train.next()

    pred=model.predict(x)
    # print(np.argmax(pred)+1)
    return np.argmax(pred)+1

def predict_wire(img):

    array=[1,2,3,5,6,7]
    cv2.imwrite(r'C:\Users\surya\Desktop\Projects\zf_python\junction_box\new\temp\t\trmp.jpg',img)
    gen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255.,validation_split=0.05)
    train=gen.flow_from_directory(r"C:\Users\surya\Desktop\Projects\zf_python\junction_box\new\temp",target_size=(28,28),subset="training",batch_size=16,color_mode="grayscale")
    x,y=train.next()
    pred=model_wire.predict(x)
    return array[np.argmax(pred)]

#intersection area between two bounding boxes
def p_intersection(boxA, boxB):
    #img2=img.copy()
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
    #print(f"interArea{interArea}")
    bb2_area= abs(boxB[1]-boxB[3])* abs(boxB[0]-boxB[2])
    #cv2.rectangle(img2,(xA,yA),(xB,yB),(0,255,0),2)
    #cv2.imshow('a',img2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    p_of_inter=interArea/bb2_area
    return p_of_inter
#returns union bounding box
def bbbox(boxA,boxB):
    xA=min(boxA[0],boxB[0])
    yA=min(boxA[1],boxB[1])
    xB=max(boxA[2],boxB[2])
    yB=max(boxA[3]-50,boxB[3])
    return xA,yA,xB,yB
img = cv2.imread(r'C:\Users\surya\Desktop\Projects\object_detection\wire_data\IMG_20201223_120539.jpg')

img3=img.copy()
row_shape=img3.shape[0]
col_shape=img3.shape[1]
img=cv2.resize(img,(500,500))
img2=img.copy()
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
light_yellow = (90, 100, 100)
dark_yellow = (100, 255, 255)
mask1 = cv2.inRange(hsv, light_yellow, dark_yellow)
contours, hierarchy = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
wireArr = []
wireNum=[]
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) >= 4 and len(approx) <=6:
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        #print(area)
        if area>100 and w<h:
            he=int(np.round(h*0.35))
            num = predict_wire(img[y:y+he, x:x+w])
            wireArr.append([x,y,x+w,y+h])
            wireNum.append(num)
            #cv2.putText(img, str(num), (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255), 1)

light_yellow = (0, 100, 100)
dark_yellow = (40, 255, 255)
mask = cv2.inRange(hsv, light_yellow, dark_yellow)
m2=mask+mask1
contours, hierarchy = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#img=cv2.drawContours(img, contours, -1, (0,255,0), 3)
yb_boxes=[]
col=0
for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        #if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)

        if area>600:
            #print(area)
            col=col+25
            #cv2.rectangle(img2,(x,y),(x+w,y+h+100),(0,col,0),2)
            d=img[y:y+h,x:x+w]
            d=cv2.resize(d,(300,300))
            #digits.append(d)

            yb_boxes.append([x,y,x+w,y+h+50])
light_white = (200, 200, 200)
dark_white = (255, 255,255)
mask5 = cv2.inRange(img, light_white, dark_white)
contours, hierarchy = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
white_boxes=[]
white_num=[]
#print("len ="+str(len(contours)))
for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.035 * peri, True)

    #if len(approx) >=4 and len(approx) <=6:
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        #print(area)
        if(area > 150 and area<200 and max(w,h)-min(w,h)<15):
            #cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
            x1=int((x/500)*col_shape)
            x2=int(((x+w)/500)*col_shape)
            y1=int((y/500)*row_shape)
            y2=int(((y+h)/500)*row_shape)
            white_boxes.append([x,y,x+w,y+h])
            num = predict(img3[y1:y2, x1:x2])
            #cv2.imshow('a',img3[y1:y2, x1:x2])
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #print(num)
            white_num.append(num)
            #numArr.append([x,x+w,y,y+h])
            #num = predict(img[y:y+h, x:x+w])
            #cv2.putText(img, str(num), (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255), 1)
i=0
#print(len(wireArr))
#print(len(yb_boxes))
bb_wire_num={}
#calculate intersection between bb of yellow and yellow+blue and to assign predicted number"
while (i<len(wireArr)):
    j=0
    #print(wireNum[i])
    while(j<len(yb_boxes)):
        p_area=p_intersection(yb_boxes[j],wireArr[i])
        #print(f"inter area = {p_area}")
        if p_area==1:
            #print("accepted")
            bb_wire_num[str(j)]=wireNum[i]
        j+=1
    i+=1

i=0
print(len(white_boxes))
print(len(yb_boxes))
#calculate intersection between bb of yellow+blue and white and check if both belong to single number
while (i<len(white_boxes)):
    j=0
    #print(white_num[i])
    while(j<len(yb_boxes)):
        p_area=p_intersection(yb_boxes[j],white_boxes[i])
        #print(f"inter area = {p_area}")
        if(p_area>0.7):
            yb_box=yb_boxes[j]
            white_box=white_boxes[i]
            xA,yA,xB,yB=bbbox(yb_boxes[j],white_boxes[i])
            xA=int((xA/500)*col_shape)
            xB=int((xB/500)*col_shape)
            yA=int((yA/500)*row_shape)
            yB=int((yB/500)*row_shape)
            #print(white_num[i] , bb_wire_num[str(j)])
            if white_num[i]==bb_wire_num[str(j)]:
                #print("entered")
                cv2.rectangle(img3,(xA,yA),(xB,yB),(0,255,0),4)
            else:
                cv2.rectangle(img3,(xA,yA),(xB,yB),(0,0,255),4)

            #cv2.imshow("output",img2)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
        j+=1
    i+=1

light_yellow = (0, 50, 100)
dark_yellow = (40, 255, 255)
mask = cv2.inRange(hsv, light_yellow, dark_yellow)
light_yellow = (30, 50, 100)
dark_yellow = (50, 255, 255)
m2 = cv2.inRange(hsv, light_yellow, dark_yellow)
r_mask=m2+mask
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
result = cv2.bitwise_and(img, img, mask=m2)
#img=cv2.drawContours(img, contours, -1, (0,255,0), 3
b_boxes=[]
b_bb=[]
g_boxes=[]
col=0
for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        #if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        #print(area)
        if area>50:
            print(area)
            col=col+25
            #cv2.rectangle(result,(x,y-30),(x+w,y+h),(0,0,255),2)
            d=img[y:y+h,x:x+w]
            d1=result[y-30:y+h,x:x+w]
            #cv2.imshow("aab",d)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            b_boxes.append(d)
            g_boxes.append(d1)
            b_bb.append([x,y,x+w,y+h])
            d=cv2.resize(d,(300,300))
light_white = (200, 200, 200)
dark_white = (255, 255,255)
mask5 = cv2.inRange(img, light_white, dark_white)
contours, hierarchy = cv2.findContours(mask5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
white_boxes=[]
white_num=[]
#print("len ="+str(len(contours)))
for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.035 * peri, True)

    #if len(approx) >=4 and len(approx) <=6:
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        #print(area)
        if(area > 150 and area<200 and max(w,h)-min(w,h)<15):
            #cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
            x1=int((x/500)*col_shape)
            x2=int(((x+w)/500)*col_shape)
            y1=int((y/500)*row_shape)
            y2=int(((y+h)/500)*row_shape)
            white_boxes.append([x,y-60,x+w,y+h])
            num = predict(img3[y1:y2, x1:x2])
            #cv2.imshow('a',img3[y1:y2, x1:x2])
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #print(num)
            white_num.append(num)
sbg=[]
for box in range(len(g_boxes)):
    #cv2.imshow('a',g_boxes[box])
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    s=np.sum(np.ravel(g_boxes[box].astype("int32")))
    #print(s)
    if s >10000:
        sbg.append([g_boxes[box],b_bb[box]])
for i in range(len(sbg)):
    for j in range(len(white_boxes)):
        aoi=p_intersection(white_boxes[j],sbg[i][1])
        if aoi==1:
            x,y1,x2,y2=bbbox(white_boxes[j],sbg[i][1])
            x1=int((x/500)*col_shape)
            x2=int(((x2)/500)*col_shape)
            y1=int((y1/500)*row_shape)
            y2=int(((y2)/500)*row_shape)
            if white_num[j] in [4,8]:
                cv2.rectangle(img3,(x1,y1),(x2,y2),(0,255,0),4)
            else:
                cv2.rectangle(img3,(x1,y1),(x2,y2),(0,0,255),4)
            print(white_num[j])

cv2.imwrite("output.jpg",img3)
cv2.imshow("output",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
