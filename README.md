# YOLOV3
YOLOv3 training &amp; inference on custom data


> YOLOV3 Custom Classes HardHat --> Boot --> Vest --> Mask


Link to dataset - 

* 3K+ Images --> https://drive.google.com/file/d/1sVSAJgmOhZk6UG7EzmlRjXfkzPxmpmLy/view?usp=sharing
* 100 Images --> custom_data100.zip



### Model Training

> ! python train.py --data data/customdata/custom.data --batch 10 --cache --cfg cfg/yolov3-custom.cfg --epochs 200 --nosave


    12/199     7.38G      2.39      1.27     0.447       4.1        26       512: 100% 314/314 [05:38<00:00,  1.08s/it]
               Class    Images   Targets         P         R   mAP@0.5        F1:   0% 0/32 [00:00<?, ?it/s]
               Class    Images   Targets         P         R   mAP@0.5        F1: 100% 32/32 [00:09<00:00,  3.51it/s]
                 all       318  1.53e+03     0.521     0.651      0.53     0.577

     Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
     
     
     
 ### Model Inference on custom data
 
 [image.png](https://postimg.cc/PLZLTZHL)
 
 [image.png](https://postimg.cc/9rMrzsVH)
 
 [image.png](https://postimg.cc/SJ2kB4kR)
 
 [image.png](https://postimg.cc/sGBCCPFq)
 
 
 
 ### Video to Frames -- ffmeg
 
 
 > ! ffmpeg -i /content/yolo_vid_trimmed.mp4 yolovid/image-%03d.jpg
 
 
 ffmpeg version 3.4.8-0ubuntu0.2 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 7 (Ubuntu 7.5.0-3ubuntu1~18.04)
  configuration: --prefix=/usr --extra-version=0ubuntu0.2 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/content/yolo_vid_trimmed.mp4':
  Metadata:
    major_brand     : mp42
    minor_version   : 1
    compatible_brands: isommp41mp42
    creation_time   : 2021-07-22T19:26:45.000000Z
  Duration: 00:00:13.22, start: -0.006259, bitrate: 2332 kb/s
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709), 1280x720 [SAR 1:1 DAR 16:9], 2186 kb/s, 24 fps, 24 tbr, 12288 tbn, 48 tbc (default)
    Metadata:
      creation_time   : 2021-07-22T19:26:45.000000Z
      handler_name    : Core Media Video
    Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 127 kb/s (default)
    Metadata:
      creation_time   : 2021-07-22T19:26:45.000000Z
      handler_name    : Core Media Audio
Stream mapping:
  Stream #0:0 -> #0:0 (h264 (native) -> mjpeg (native))
Press [q] to stop, [?] for help
[swscaler @ 0x559b7075e000] deprecated pixel format used, make sure you did set range correctly
Output #0, image2, to 'yolovid/image-%03d.jpg':
  Metadata:
    major_brand     : mp42
    minor_version   : 1
    compatible_brands: isommp41mp42
    encoder         : Lavf57.83.100
    Stream #0:0(und): Video: mjpeg, yuvj420p(pc), 1280x720 [SAR 1:1 DAR 16:9], q=2-31, 200 kb/s, 24 fps, 24 tbn, 24 tbc (default)
    Metadata:
      creation_time   : 2021-07-22T19:26:45.000000Z
      handler_name    : Core Media Video
      encoder         : Lavc57.107.100 mjpeg
    Side data:
      cpb: bitrate max/min/avg: 0/0/200000 buffer size: 0 vbv_delay: -1
frame=  317 fps= 98 q=24.8 Lsize=N/A time=00:00:13.20 bitrate=N/A speed=4.08x    
video:8034kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown






### Inference on Frames

> ! python detect.py --conf-thres 0.25 --output yolovid_out
 
image 1/317 yolovid/image-001.jpg: 320x512 2 hardhats, 2 vests, Done. (0.033s)
image 2/317 yolovid/image-002.jpg: 320x512 2 hardhats, 2 vests, Done. (0.033s)
image 3/317 yolovid/image-003.jpg: 320x512 2 hardhats, 2 vests, Done. (0.026s)
image 4/317 yolovid/image-004.jpg: 320x512 2 hardhats, 2 vests, Done. (0.025s)
image 5/317 yolovid/image-005.jpg: 320x512 3 hardhats, 2 vests, Done. (0.025s)
image 6/317 yolovid/image-006.jpg: 320x512 3 hardhats, 2 vests, Done. (0.025s)
image 7/317 yolovid/image-007.jpg: 320x512 3 hardhats, 2 vests, Done. (0.021s)
image 8/317 yolovid/image-008.jpg: 320x512 2 hardhats, 2 vests, Done. (0.021s)
image 9/317 yolovid/image-009.jpg: 320x512 2 hardhats, 2 vests, Done. (0.021s)
image 10/317 yolovid/image-010.jpg: 320x512 2 hardhats, 2 vests, Done. (0.021s)
image 11/317 yolovid/image-011.jpg: 320x512 2 hardhats, 2 vests, Done. (0.021s)
image 12/317 yolovid/image-012.jpg: 320x512 2 hardhats, 2 vests, Done. (0.021s)
image 13/317 yolovid/image-013.jpg: 320x512 2 hardhats, 2 vests, Done. (0.021s)
image 14/317 yolovid/image-014.jpg: 320x512 3 hardhats, 2 vests, Done. (0.021s)
image 15/317 yolovid/image-015.jpg: 320x512 3 hardhats, 2 vests, Done. (0.021s)



### Frames to Video - ffmeg

> ! ffmpeg -i yolovid_out/image-%03d.jpg video.mp4


ffmpeg version 3.4.8-0ubuntu0.2 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 7 (Ubuntu 7.5.0-3ubuntu1~18.04)
  configuration: --prefix=/usr --extra-version=0ubuntu0.2 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --enable-gpl --disable-stripping --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librubberband --enable-librsvg --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-omx --enable-openal --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libopencv --enable-libx264 --enable-shared
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libavresample   3.  7.  0 /  3.  7.  0
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Input #0, image2, from 'yolovid_out/image-%03d.jpg':
  Duration: 00:00:12.68, start: 0.000000, bitrate: N/A
    Stream #0:0: Video: mjpeg, yuvj420p(pc, bt470bg/unknown/unknown), 1280x720 [SAR 1:1 DAR 16:9], 25 fps, 25 tbr, 25 tbn, 25 tbc
Stream mapping:
  Stream #0:0 -> #0:0 (mjpeg (native) -> h264 (libx264))
Press [q] to stop, [?] for help
[libx264 @ 0x5597a9217e00] using SAR=1/1
[libx264 @ 0x5597a9217e00] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2
[libx264 @ 0x5597a9217e00] profile High, level 3.1
[libx264 @ 0x5597a9217e00] 264 - core 152 r2854 e9a5903 - H.264/MPEG-4 AVC codec - Copyleft 2003-2017 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=3 lookahead_threads=1 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
Output #0, mp4, to 'video.mp4':
  Metadata:
    encoder         : Lavf57.83.100
    Stream #0:0: Video: h264 (libx264) (avc1 / 0x31637661), yuvj420p(pc), 1280x720 [SAR 1:1 DAR 16:9], q=-1--1, 25 fps, 12800 tbn, 25 tbc
    Metadata:
      encoder         : Lavc57.107.100 libx264
    Side data:
      cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: -1
frame=  317 fps= 12 q=-1.0 Lsize=    5166kB time=00:00:12.56 bitrate=3369.5kbits/s speed=0.482x    
video:5162kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.089454%
[libx264 @ 0x5597a9217e00] frame I:5     Avg QP:19.98  size: 37678
[libx264 @ 0x5597a9217e00] frame P:84    Avg QP:23.38  size: 22345
[libx264 @ 0x5597a9217e00] frame B:228   Avg QP:26.32  size: 14120
[libx264 @ 0x5597a9217e00] consecutive B-frames:  3.2%  2.5%  0.9% 93.4%
[libx264 @ 0x5597a9217e00] mb I  I16..4: 41.4% 53.1%  5.5%
[libx264 @ 0x5597a9217e00] mb P  I16..4: 23.5% 39.7%  3.1%  P16..4: 10.0%  6.1%  4.8%  0.0%  0.0%    skip:12.8%
[libx264 @ 0x5597a9217e00] mb B  I16..4:  9.5% 25.5%  0.7%  B16..8: 20.0%  8.6%  3.3%  direct: 5.7%  skip:26.9%  L0:51.5% L1:41.4% BI: 7.1%
[libx264 @ 0x5597a9217e00] 8x8 transform intra:66.3% inter:83.8%
[libx264 @ 0x5597a9217e00] coded y,uvDC,uvAC intra: 49.5% 54.6% 6.9% inter: 19.3% 18.4% 1.8%
[libx264 @ 0x5597a9217e00] i16 v,h,dc,p: 47% 36% 16%  1%
[libx264 @ 0x5597a9217e00] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 28% 20% 41%  3%  1%  1%  1%  1%  5%
[libx264 @ 0x5597a9217e00] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 50% 30% 10%  2%  2%  2%  2%  2%  2%
[libx264 @ 0x5597a9217e00] i8c dc,h,v,p: 40% 28% 29%  3%
[libx264 @ 0x5597a9217e00] Weighted P-Frames: Y:0.0% UV:0.0%
[libx264 @ 0x5597a9217e00] ref P L0: 54.0% 12.1% 16.4% 17.5%
[libx264 @ 0x5597a9217e00] ref B L0: 74.4% 18.2%  7.4%
[libx264 @ 0x5597a9217e00] ref B L1: 89.3% 10.7%
[libx264 @ 0x5597a9217e00] kb/s:3334.19
