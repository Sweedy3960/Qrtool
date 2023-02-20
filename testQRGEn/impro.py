import csv
import urllib as u
import requests

def Reader ():
     with open ('Mac.csv', newline ='') as f:
        reader =csv.reader(f)
        for row in reader :
            print(row)
def Writter (MacAdd):
     with open('Mac.csv', 'w', newline='') as f:
          writer = csv.writer(f, dialect='unix')
          writer.writerow(MacAdd)
          f.close()
     
def Scan():
     SerieNb = int(input( ' Less go! combien cette fois ?' ))
     while(SerieNb != 0 ): 
          mac.insert(macCnt,input('Enter MacAdd'))
          SerieNb = SerieNb - 1
     print('Thx, faster NXTTME')
     
def QrGenAs(Msgtosend,macCnt):
     
     img_url = 'https://api.qr-code-generator.com/v1/create?access-token=PmL7EjAdbM_KJ5HT90sSUKVQpw0kn9nhuR25C1jZQEyGUXKI-gVnJuj6gWs2_bb8'
     a= str(Msgtosend)
     param = {
         "frame_name": "no-frame",
         "qr_code_text": " {} ".format(a),
         "image_format": "JPG",
         "qr_code_logo": "scan-me-square",
         "image_width" : "500"
         
     }
     response = requests.get(img_url , param)
     with open("QrResp{}.jpg".format(macCnt), "wb") as f:
         f.write(response.content)
         macCnt = macCnt + 1
     return macCnt 
if __name__== "__main__" :
     macCnt = 0
     mac = []
     Scan()
     Writter(mac)
     for i in mac:
        macCnt = QrGenAs(mac[macCnt],macCnt)
        
        
          
