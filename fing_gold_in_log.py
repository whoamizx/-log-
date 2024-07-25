import requests

# url="http://www.webhack123.com/App/Runtime/Logs/18_07_02.log"

url="http://www.webhack123.com/App/Runtime/Logs"
def addurls(url,year):
    urls=[]
    for i in range(1,13):
        for j in range(1,32):
            if i<10:
                if j<10:
                    urls.append(url+"/%s_0%s_0%s.log"%(year,i,j))
                else:
                    urls.append(url+"/%s_0%s_%s.log"%(year,i,j))
            else:
                if j<10:
                    urls.append(url+"/%s_%s_0%s.log"%(year,i,j))
                else:
                    urls.append(url+"/%s_%s_%s.log"%(year,i,j))
    for url in urls:
        print(url)

addurls(url,19)
