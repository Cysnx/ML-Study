print ("Data Types")
print ("1. Categorical")
print ("2. Numerical")
print ("1.1 Nominal")
print ("1.2 Ordinal")
print ("2.1. Ratio")
print ("2.2 Interval")

# ...existing code...
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 600, 900
GAP, GAP_V=50,100
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

x1_rect1, y1_rect1 = 50, 50
x2_rect1, y2_rect1 = 200, 150

draw.rectangle((x1_rect1, y1_rect1, x2_rect1, y2_rect1), fill="lightblue", outline="black")
draw.text((x1_rect1+10, y1_rect1+(y2_rect1-y1_rect1)/2), "1. Categorical", fill="black")

################# First Box Done - CATEGORICAL #################

x1_rect2, y1_rect2 = 250, y1_rect1
x2_rect2, y2_rect2 = 400, y2_rect1

draw.rectangle((x1_rect2, y1_rect2, x2_rect2, y2_rect2), fill="lightgreen", outline="black")
draw.text((x1_rect2+10, y1_rect2+(y2_rect2-y1_rect2)/2), "2. Numerical", fill="black")


################# Second Box Done - NUMERICAL #################


x1_rect3, y1_rect3 = x1_rect1, y2_rect2 + GAP
x2_rect3, y2_rect3 = x2_rect1, y1_rect3 + GAP_V

draw.rectangle((x1_rect3, y1_rect3, x2_rect3, y2_rect3), fill="lightcoral", outline="black")
draw.text((x1_rect3+10, y1_rect3+(y2_rect3-y1_rect3)/2), "1.1 Nominal", fill="black")


################# Third Box Done - NOMINAL #################


x1_rect4, y1_rect4 = x1_rect3, y2_rect3 + GAP
x2_rect4, y2_rect4 = x2_rect3, y1_rect4 + GAP_V

draw.rectangle((x1_rect4, y1_rect4, x2_rect4, y2_rect4), fill="lightyellow", outline="black")
draw.text((x1_rect4+10, y1_rect4+(y2_rect4-y1_rect4)/2), "1.2 Ordinal", fill="black")


################# Fourth Box Done - ORDINAL #################


x1_rect5, y1_rect5 = x1_rect2, y1_rect3
x2_rect5, y2_rect5 = x2_rect2, y2_rect3

draw.rectangle((x1_rect5, y1_rect5, x2_rect5, y2_rect5), fill="lightpink", outline="black")
draw.text((x1_rect5+10, y1_rect5+(y2_rect5-y1_rect5)/2), "2.1. Ratio", fill="black")


################# Fifth Box Done - RATIO #################


x1_rect6, y1_rect6 = x1_rect2, y2_rect5 + GAP
x2_rect6, y2_rect6 = x2_rect2, y1_rect6 + GAP_V

draw.rectangle((x1_rect6, y1_rect6, x2_rect6, y2_rect6), fill="lightgray", outline="black")
draw.text((x1_rect6+10, y1_rect6+(y2_rect6-y1_rect6)/2), "2.2 Interval", fill="black")    


################# Sixth Box Done - INTERVAL #################


#draw.ellipse((250, 50, 380, 150), fill="salmon", outline="black")

try:
    font = ImageFont.truetype("DejaVuSans.ttf", 16)
except Exception:
    font = None


out = "canvas_DATA_TYPES.png"
img.save(out)
print(f"DISPLAY yok — çıktı '{out}' olarak kaydedildi.")
# ...existing code...