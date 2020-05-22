import csv
url="./pdftotext/Chapter_0.txt"

with open("./dataset.csv",mode="a") as dataset_file:
        dataset_writer=csv.writer(dataset_file,delimiter=',')
        dataset_writer.writerow(["title","paragraphs"])

for i in range(8):
    URL=list(url)
    URL[-5]=str(i+1)
    url=''.join(URL)

    with open(url,"r",errors="ignore") as fp:
        lines=fp.readlines()

        #with open("C:/Users/mathe/Desktop/NLP Project/out.txt","w") as fwp:
        #     fwp.writelines(lines)

    doc=[]
    para=""
    for elem in lines:
        if elem=="\n":
            doc.append(para)
            para=""
        else:
            elem=elem.strip()
            para+=(elem+" ")
    title=doc[0]+doc[1]
    paralst=[]
    paralst.append(title)
    paralst.append(doc)
    
    with open("C:/Users/mathe/Desktop/NLP Project/dataset.csv",mode="a") as dataset_file:
        dataset_writer=csv.writer(dataset_file,delimiter=',')
        dataset_writer.writerow(paralst)

    # print(doc[0],"next one\n",doc[1],"next\n",doc[2])