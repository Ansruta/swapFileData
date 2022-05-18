def swappingFile():
    file1=input("Enter file name:")
    data_a=open(file1,'r')

    file2=input("Enter second file name:")
    data_b=open(file2,'r')

    a=open(file1,'w')
    a.write(data_b)

    b=open(file2,'w')
    b.write(data_a)

    print("file1="+ a)
    print("file2"+ b)

swappingFile()