import requests

def TakeFromListAndDownload():
    #Taking information from the list
    theFile = open("list.txt", "r")
    arrayLink = theFile.readlines()
    theFile.close()
    

    #New line prefix reducer
    arrayLinkLen = len(arrayLink)
    rangedArray = arrayLinkLen - 1 #Beside the last element!
    
    for i in range(rangedArray):
        arrayLink[i] = arrayLink[i].replace("\n", "") 

    #Downloader
    for i in range(len(arrayLink)):
        send_request = requests.get(arrayLink[i])
        content_type = send_request.headers['Content-Type']
        if content_type == "image/jpeg":
            with open('files\\' + str(i) + "_file.jpg", 'wb') as f: 
                f.write(send_request.content)
        if content_type == "image/png":
            with open('files\\' + str(i) + "_file.png", 'wb') as f: 
                f.write(send_request.content)
        if content_type == "video/mp4":
            with open('files\\' + str(i) + "_file.mp4", 'wb') as f: 
                f.write(send_request.content)
        if content_type == "video/webm":
            with open('files\\' + str(i) + "_file.webm", 'wb') as f: 
                f.write(send_request.content)
        if content_type == "image/gif":
            with open('files\\' + str(i) + "_file.gif", 'wb') as f: 
                f.write(send_request.content)
