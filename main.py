import cv2
image = cv2.imread("C:\\Users\\Public\\Downloads\\spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg")
cv2.imshow("JPEG Dosyası", image)



blue_channel, green_channel, red_channel = cv2.split(image)
cv2.imshow("Blue Channel", blue_channel)
cv2.imshow("Green Channel", green_channel)
cv2.imshow("Red Channel", red_channel)



original_green_channel = green_channel.copy()



green_channel[:] = 0

red_blue = cv2.merge((blue_channel, green_channel, red_channel))



cv2.imshow("Red and Blue Channels Only", red_blue)

combined_image = cv2.merge((blue_channel, original_green_channel, red_channel))

cv2.imshow("Combined image that like original one ", combined_image)



cv2.waitKey(0)
