import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "mercury",
            (40,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "venus",
            (60,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "earth",
            (80,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "mars",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "jupiter",
            (120,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "saturn",
            (140,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "uranus",
            (160,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "neptune",
            (180,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.imshow("output",img)

cv2.waitkey(0)