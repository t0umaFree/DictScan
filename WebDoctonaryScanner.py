import requests
import sys
url = sys.argv[1]
dict = sys.argv[2]

with open(dict,'r') as f:
    for line in f.readlines():
        line = line.strip()
        r =requests.get(url+line)
        if r.status_code == 200:
            print('url:'+ r.url+' success')
            f = open('success.txt', 'a')
            f.write(url+line)
            f.write("\n")


        elif r.status_code == 403:
            print('url:' + r.url+ '403 forbitten!')


        elif r.status_code == 404:
            print('url' + r.url + ' not exist')

        elif  r.status_code == 503:
            print('url' + r.url + 'service is not avilable for your region')

        else:
            print("UNKNOWN CODE")

    f.close()
