#ffmpeg -i input.mp4 -vcodec png image_%03d.png
#ffmpeg -r 30 -i image_%03d.png -vcodec libx264 -pix_fmt yuv420p -r 30 out.mp4

import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageDraw

#draw ball line
track = []

#img file
pic_start = 88
pic_finish = 120

for i in np.arange(pic_start,pic_finish):
  #open .xml file
  fp = ET.parse("image_{:0=3}.xml".format(i))
  root = fp.getroot()

  #place of bounding box
  x_min = int(root[6][4][0].text)
  x_max = int(root[6][4][2].text)

  y_min = int(root[6][4][1].text)
  y_max = int(root[6][4][3].text)

  #open image
  im = Image.open("image_{:0=3}.png".format(i))
  draw = ImageDraw.Draw(im)
  #draw circle
  draw.ellipse((x_min, y_min ,x_max, y_max),fill=(255,0,0))
  
  #draw line
  #recode center of bounding box
  plot_rec = (int((x_min + x_max)/2), int((y_min + y_max)/2) )
  track.append(plot_rec)
  for j in range(len(track)):
      if j == 0:
        pass
      else:
        draw.line( (track[j-1][0], track[j-1][1], track[j][0], track[j][1] ), fill=(255,0,0) ,width= 10 )
  #draw.line( (track[j-1][0], track[j-1][1], track[j][0], track[j][1] ), fill=(255,0,0) ,width= 10 ) if j != 0 else 0
  
  #save image
  im.save("movie/image_{:0=3}.png".format(i))

