import cv2
import argparse
import sys
import time

video_capture_name = sys.argv[1]
video_capture = sys.argv[2]
video_framerate = int(sys.argv[3])
video_fourcc = sys.argv[4]
sink_host_ip = sys.argv[5]
sink_host_port = sys.argv[6]

video_input = cv2.VideoCapture(video_capture)
video_input_size = (int(video_input.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(video_input.get(cv2.CAP_PROP_FRAME_HEIGHT)))

if video_fourcc == 'XVID':
    file_extension = 'vid'
elif video_fourcc == 'FMP4':
    file_extension = 'mp4'
elif video_fourcc == 'MPEG':
    file_extension = 'mp4'
elif video_fourcc == 'MJPG':
    file_extension = 'mjpg'
else:
    print('Invalid FOURCC')
    sys.exit(1)

video_fourcc = cv2.VideoWriter_fourcc(*video_fourcc)

now = time.gmtime()
video_record_filename = 'gateway-%s-' % video_capture_name + time.strftime("%Y%m%d-%H%M%S", now) + '.%s' % file_extension
video_record_path = '/home/user/repository/' + video_record_filename
video_record = cv2.VideoWriter()
video_record.open(video_record_path, video_fourcc, video_framerate, video_input_size, True)

video_stream_pipeline = "appsrc ! videoconvert ! matroskamux streamable=true ! tcpserversink host=" + sink_host_ip + " port=" + sink_host_port + " sync=false sync-method=2"
video_stream = cv2.VideoWriter(video_stream_pipeline, video_fourcc, video_framerate, video_input_size)

while(True):
    stime = time.time()
    success, frame = video_input.read()
    if success:
        video_record.write(frame)
        banner = 'Gateway ' + '%s' % video_capture_name.capitalize() + ' FPS {:.1f}'.format(1 / (time.time() - stime))
        cv2.putText(frame, banner, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,177,1), 3)
        cv2.imshow('frame',frame)
        video_stream.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_input.release()
video_record.release()
video_stream.release()
cv2.destroyAllWindows()
