# Credit Ankit Sachan @ Blogs https://github.com/sankit1/cv-tricks.com
# With modifications to get frame from RTP

import cv2
import argparse
import numpy as np
import sys
import time

min_confidence = 0.14
model = 'yolov2.weights'
config = 'yolov2.cfg'

framerate=25
service_name=sys.argv[1]
video_capture=sys.argv[2]
sink_host_ip=sys.argv[3]
sink_host_port=sys.argv[4]

cap = cv2.VideoCapture(video_capture)

display="appsrc ! videoconvert ! matroskamux streamable=true ! tcpserversink host=" + sink_host_ip + " port=" + sink_host_port + " sync=false sync-method=2"
displayout = cv2.VideoWriter(display, 0, framerate, (640, 480))

classes = None
with open('coco.names', 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')
print(classes)

net = cv2.dnn.readNetFromDarknet(config, model)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

while(True):

    stime = time.time()

    ret, frame = cap.read()
    frame_resized = cv2.resize(frame,(300,300))

    height,width,ch=frame.shape

    blob = cv2.dnn.blobFromImage(frame_resized, 1.0/255.0, (416, 416), True, crop=False)
    net.setInput(blob)
    predictions = net.forward()
    probability_index=5

    for i in range(predictions.shape[0]):
        prob_arr=predictions[i][probability_index:]
        class_index=prob_arr.argmax(axis=0)
        confidence= prob_arr[class_index]
        if confidence > min_confidence:
            x_center=predictions[i][0]*width
            y_center=predictions[i][1]*height
            width_box=predictions[i][2]*width
            height_box=predictions[i][3]*height

            x1=int(x_center-width_box * 0.5)
            y1=int(y_center-height_box * 0.5)
            x2=int(x_center+width_box * 0.5)
            y2=int(y_center+height_box * 0.5)

            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,255,255),1)
            cv2.putText(frame,classes[class_index]+" "+"{0:.1f}".format(confidence),(x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),1,cv2.LINE_AA)

    banner = service_name + ' FPS {:.1f}'.format(1 / (time.time() - stime))
    cv2.putText(frame, banner, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,177,1), 3)
    cv2.imshow(service_name, frame)
    displayout.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
out.release()
