fp=open('loc.jpeg','rb')
image_data=fp.read()
fp1=open('new_loc.jpeg','wb')
fp1.write(image_data)
print("binary data")
fp.close()
fp1.close()