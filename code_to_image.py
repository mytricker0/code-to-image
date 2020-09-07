#!/usr/bin/env python3
import argparse
import sys,os




png_header = bytearray([
0x89,
0x50, 
0x4e, 	
0x47, 
0x0d, 
0x0a, 
0x1a, 
0x0a
])


jpeg_header = bytearray([
0xFF, 
0xD8, 
0xFF
])


#pdf_header = bytearray([
#0x25, 
#0x50, 
#0x44, 
#0x46, 
#0x2d
#])



gif_header = bytearray([
0x47, 
0x49, 
0x46, 
0x38, 
0x37, 
0x61
])

def main():
	
	parser = argparse.ArgumentParser()
	



	parser.add_argument("file", help="code you need to convert", type=str)

	# can't spec png jpeg pdf and gij at he same time 
	group= parser.add_mutually_exclusive_group()

	group.add_argument("-png",help='put code into png file', required=False,type=str)

	group.add_argument("-jpeg",help='put code into jpeg file', required=False,type=str)

	group.add_argument("-gif",help='put code into gif file', required=False,type=str)



	args = parser.parse_args()

	

	#verify the path

	if os.path.exists(args.file):
		print('path to the file is ok')
		
	else:
		print('path to the file is not ok')
		sys.exit()

	
	
	#verif if one og args is given
	#for png ---------------------------------------------------
	if not args.png :
		pass
	
	elif args.png:

 		with open(args.file, 'rb') as file:
 			user = file.read()
 		with open(args.png, 'wb') as out:
 			out.write(png_header + user)
 			
 	#for jpeg ---------------------------------------------------
	if not args.jpeg :
		pass
	elif args.jpeg:

 		with open(args.file, 'rb') as file:
 			user = file.read()
 			
 		with open(args.jpeg, 'wb') as out:
 			out.write(jpeg_header + user)
 			
    #for gif ---------------------------------------------------

	if not args.gif :
		pass
		


	elif args.gif:

 		with open(args.file, 'rb') as file:
 			user = file.read()
 			
 		with open(args.gif, 'wb') as out:
 			out.write(gif_header + user)
 	




if __name__ == '__main__':

	main()
