import os
import cv2

dir_path = os.getcwd()

for file in os.listdir(dir_path):
	if file.endswith(".jpg"):
		image = cv2.imread(file)
		width, height = image.shape[:2]
		filename = os.path.splitext(file)[0]
		print("file {}, W = {}, H = {}" .format(filename, width, height))
		xml_filename = filename + ".xml"
		xml_file = open(xml_filename, "w")
		xml_file.write("<annotation>\n")
		xml_file.write("	<folder>test</folder>\n")
		xml_file.write("	<filename>" + file + "</filename>\n")
		xml_file.write("	<path>" + dir_path + "/" + file + "</path>\n")
		xml_file.write("	<source>\n")
		xml_file.write("		<database>Unknown</database>\n")
		xml_file.write("	</source>\n")
		xml_file.write("	<size>\n")
		xml_file.write("		<width>" + str(width) + "</width>\n")
		xml_file.write("		<height>" + str(height) + "</height>\n")
		xml_file.write("		<depth>3</depth>\n")
		xml_file.write("	</size>\n")
		xml_file.write("	<segmented>0</segmented>\n")
		xml_file.write("	<object>\n")
		xml_file.write("		<name>Cat</name>\n")
		xml_file.write("		<pose>Unspecified</pose>\n")
		xml_file.write("		<truncated>0</truncated>\n")
		xml_file.write("		<difficult>0</difficult>\n")
		xml_file.write("		<bndbox>\n")
		xml_file.write("			<xmin>2</xmin>\n")
		xml_file.write("			<ymin>2</ymin>\n")
		xml_file.write("			<xmax>" + str(width-2) + "</xmax>\n")
		xml_file.write("			<ymax>" + str(height-2) + "</ymax>\n")
		xml_file.write("		</bndbox>\n")
		xml_file.write("	</object>\n")
		xml_file.write("</annotation>\n")

		xml_file.close()
