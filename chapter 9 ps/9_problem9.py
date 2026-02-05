# ish mai sirf do file ko compare kar rahe hai ke wo identical hai ki nhi txt wale file ko

with  open("file.txt") as f:
    content1=f.read()

with  open("poem.txt") as f:
    content2=f.read() 

if(content1==content2):
    print("Yes these files are identical")

else:
    print("No these files are not identical") 


