import cv2
import numpy as np
import itertools
import pandas as pd

path = "D:/opencv/template_matchgin/"
csv_path = "D:\python projects\color\colors\colors\spiders\colors.csv"

def spelling_colors(new_num):
	df = pd.read_csv(csv_path)
	for i in new_num:
		for index in df.index:
			if i == (df['R,G,B (Decimal code)'][index]):
				print(df['R,G,B (Decimal code)'])

def main():
	img = cv2.imread(path+"messi.jpg")
	list1 = img.tolist()
	l1 = []
	for i in list1:
	    l1.append((i[0]))
	l1.sort()
	new_num = list(tuple(l1) for l1,_ in itertools.groupby(l1))
	font = cv2.FONT_HERSHEY_SIMPLEX
	  
	# org
	org = (50, 50)
	  
	# fontScale
	fontScale = 1
	   
	# Blue color in BGR
	color = (255,255,255)
	  
	# Line thickness of 2 px
	thickness = 2
	   
	# Using cv2.putText() method
	img = cv2.putText(img, f"This image has {len(new_num)} different types of colors", org, font, 
	                   fontScale, color, thickness, cv2.LINE_AA)

	spelling_colors(new_num)
	cv2.imshow("image",img)
	cv2.waitKey(0)

	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()