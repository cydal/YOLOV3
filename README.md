# YOLOV3
YOLOv3 training &amp; inference on custom data


> YOLOV3 Custom Classes HardHat --> Boot --> Vest --> Mask


Link to dataset - 

* 3K+ Images --> https://drive.google.com/file/d/1sVSAJgmOhZk6UG7EzmlRjXfkzPxmpmLy/view?usp=sharing
* 100 Images --> https://github.com/cydal/YOLOV3/blob/main/custom_data100.zip



### Model Training

> ! python train.py --data data/customdata/custom.data --batch 10 --cache --cfg cfg/yolov3-custom.cfg --epochs 200 --nosave


    12/199     7.38G      2.39      1.27     0.447       4.1        26       512: 100% 314/314 [05:38<00:00,  1.08s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1:   0% 0/32 [00:00<?, ?it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 32/32 [00:09<00:00,  3.51it/s]
                 all       318  1.53e+03     0.521     0.651      0.53     0.577

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     
     
     
 ### Model Inference on custom data
 
 [![image.png](https://i.postimg.cc/Bv725cwC/image.png)](https://postimg.cc/PLZLTZHL)
 
 [![image.png](https://i.postimg.cc/gkyRtPTj/image.png)](https://postimg.cc/9rMrzsVH)
 
 [![image.png](https://i.postimg.cc/yYnxS6Gm/image.png)](https://postimg.cc/SJ2kB4kR)
 
 [![image.png](https://i.postimg.cc/prCW8ksW/image.png)](https://postimg.cc/sGBCCPFq)
 
 [![image.png](https://i.postimg.cc/zfvqmR5P/image.png)](https://postimg.cc/pmwwzrmD)
  
 [![image.png](https://i.postimg.cc/CL0Yh2S8/image.png)](https://postimg.cc/hh2NMpJ4)
 
 [![image.png](https://i.postimg.cc/6pjNh5RV/image.png)](https://postimg.cc/w1mPqzw3)
 
 [![image.png](https://i.postimg.cc/0jx3sLD2/image.png)](https://postimg.cc/YGn8NDdJ)
 
 [![image.png](https://i.postimg.cc/sf9qcgCB/image.png)](https://postimg.cc/nMr3VZzZ)
 
 [![image.png](https://i.postimg.cc/280ts96r/image.png)](https://postimg.cc/PP8KZ4YR)
 
 [![image.png](https://i.postimg.cc/LXkCNNwd/image.png)](https://postimg.cc/S2sfK7mV)
 
 [![image.png](https://i.postimg.cc/5N27S5mG/image.png)](https://postimg.cc/jCB4s7mQ)
 
 [![image.png](https://i.postimg.cc/t41BLXwN/image.png)](https://postimg.cc/75k1zyx5)
 
 [![image.png](https://i.postimg.cc/mD4Vz7Dm/image.png)](https://postimg.cc/KK9tCktT)
 
 [![image.png](https://i.postimg.cc/qvCG116m/image.png)](https://postimg.cc/3kYpRCBp)
 
 [![image.png](https://i.postimg.cc/ZqS6V4SR/image.png)](https://postimg.cc/LJxqsdhK)
 
 
 ### Video to Frames -- ffmeg
 
 
 > ! ffmpeg -i /content/yolo_vid_trimmed.mp4 yolovid/image-%03d.jpg

### Inference on Frames

> ! python detect.py --conf-thres 0.25 --output yolovid_out

### Frames to Video - ffmeg

> ! ffmpeg -i yolovid_out/image-%03d.jpg video.mp4



### Video

[![YOLOV3 Object detection](http://img.youtube.com/vi/4P38yxDNdtA/0.jpg)](http://www.youtube.com/watch?v=4P38yxDNdtA "YOLOV3 Object detection")
