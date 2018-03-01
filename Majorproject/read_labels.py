import re

text_file = open("labels.txt", "r")
lines = text_file.read().split('\n')
lines = lines[0:len(lines)-1]
labels_list = {}
for line in lines:
	string = re.split(r'\t+',line)
	imagename = string[0]
	label = string[1]
	#print imagename
	#print label
	labels_list[imagename]=label

#for key,value in labels_list.iteritems():
	#print (key)
	#print (value)

wnet_text = open("words.txt","r")
lines = wnet_text.read().split('\n')
wnet_text_dict = {}
for line in lines:
	string = re.split(r'\t+',line)
	wnet = string[0]
	text = string[1]
	wnet_text_dict[wnet]=text

image_text = {}
for key,value in labels_list.iteritems():
	image_text[key] = wnet_text_dict[value]
	print (str(key)+'\t'+str(image_text[key]))
