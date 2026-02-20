print ("CRISP-DM")
print ("Cross-Industry Standard Process for Data Mining")
print ("1. Business Understanding +-")
print ("2. Data Understanding")
print ("3. Data Preparation +-")
print ("4. Modeling")
print ("5. Evaluation")
print ("6. Deployment")

# Yapılacaklar:
# - Her aşama için kutular çizilecek
# - Kutuların içine aşama isimleri yazılacak
# - Kutular arasında oklar çizilecek
# - Çevreye dönel ok çizilecek
# - Sonuç bir PNG dosyasına kaydedilecek
# - Sonrasında GIF'e dönüştürülecek
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 900, 900
GAP, GAP_V=50,100
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

x1_rect1, y1_rect1 = 100, 50
x2_rect1, y2_rect1 = 250, 150

draw.rectangle((x1_rect1, y1_rect1, x2_rect1, y2_rect1), fill="lightblue", outline="black")
draw.text((x1_rect1+10, y1_rect1+(y2_rect1-y1_rect1)/2), "Business Understanding", fill="black")

#########################################

x1_rect2, y1_rect2 = x2_rect1+GAP, y1_rect1
x2_rect2, y2_rect2 = x2_rect1+2*GAP+GAP_V, y2_rect1

draw.rectangle((x1_rect2, y1_rect2, x2_rect2, y2_rect2), fill="lightgreen", outline="black") #Kaydırmayı içeri burada içeri yapalım
draw.text((x1_rect2+10, y1_rect2+(y2_rect2-y1_rect2)/2), "Data Understanding", fill="black")

#########################################

x1_rect3, y1_rect3 = x1_rect2, y2_rect2 + GAP
x2_rect3, y2_rect3 = x2_rect2, y1_rect3 + GAP_V

draw.rectangle((x1_rect3+50, y1_rect3, x2_rect3+50, y2_rect3), fill="lightcoral", outline="black")
draw.text((x1_rect3+60, y1_rect3+(y2_rect3-y1_rect3)/2), "Data Preparation", fill="black")

#########################################

x1_rect4, y1_rect4 = x1_rect2, y2_rect3 + GAP
x2_rect4, y2_rect4 = x2_rect2, y1_rect4 + GAP_V

draw.rectangle((x1_rect4, y1_rect4, x2_rect4, y2_rect4), fill="lightyellow", outline="black")
draw.text((x1_rect4+10, y1_rect4+(y2_rect4-y1_rect4)/2), "Modeling", fill="black")

#########################################

x1_rect5, y1_rect5 = x1_rect2, y2_rect4 + GAP
x2_rect5, y2_rect5 = x2_rect2, y1_rect5 + GAP_V

draw.rectangle((x1_rect5, y1_rect5, x2_rect5, y2_rect5), fill="lightpink", outline="black")
draw.text((x1_rect5+10, y1_rect5+(y2_rect5-y1_rect5)/2), "Evaluation", fill="black")

#########################################

x1_rect6, y1_rect6 = x1_rect2, y2_rect5 + GAP
x2_rect6, y2_rect6 = x2_rect2, y1_rect6 + GAP_V

draw.rectangle((x1_rect6, y1_rect6, x2_rect6, y2_rect6), fill="lightgray", outline="black")
draw.text((x1_rect6+10, y1_rect6+(y2_rect6-y1_rect6)/2), "Deployment", fill="black")    

#########################################


#draw.ellipse((250, 50, 380, 150), fill="salmon", outline="black")

try:
    font = ImageFont.truetype("DejaVuSans.ttf", 16)
except Exception:
    font = None


out = "canvas_CRISP-DM.png"
img.save(out)
print(f"DISPLAY yok — çıktı '{out}' olarak kaydedildi.")