import cv2
import numpy as np
cap = cv2.VideoCapture(0)
if cap.isOpened():
    cv2.namedWindow('win', cv2.WINDOW_FULLSCREEN)
    play = True
    image_filter = 'PREVIEW'
    while play:
        has_frame, frame = cap.read()
        if image_filter == 'PREVIEW':
            result = frame
        elif image_filter == 'CANNY':
            result = cv2.Canny(frame, 60, 150)
        elif image_filter == 'BLUR':
            result = cv2.blur(frame, (15, 15))
        elif image_filter == 'CORNERS':
            result = frame
            gray_framework = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            corners = cv2.goodFeaturesToTrack(gray_framework, maxCorners=50, qualityLevel=0.1, minDistance=10)
            if corners is not None:
                corners = np.int0(corners)
                for corner in corners:
                    x, y = corner.ravel()
                    cv2.circle(result, (x,y), 10, (0,0,255), 2)
        
        cv2.imshow('win', result)

        key = cv2.waitKey(1)
        if key == ord('Q') or key == ord('q') or key == 27:
            play = False
        elif key == ord('C') or key == ord('c'):
            image_filter = 'CANNY'
        elif key == ord('B') or key == ord('b'):
            image_filter = 'BLUR'
        elif key == ord('k') or key == ord('k'):
            image_filter = 'CORNERS'
        elif key == ord('P') or key == ord('p'):
            image_filter = 'PREVIEW'


cap.release()
cv2.destroyWindow('win')