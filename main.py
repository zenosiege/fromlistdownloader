import dnd

print("Hello, welcome to another Zeno's software(not original, maybe it was already made by someone).\nFLD - From List Downloader can download all the files you wrote in the list(a txt file)")
print("Type a number to choose an option")

chooseParam = 0

while chooseParam == 0:

    print (" 1. Start downloading\n 2. Help\n 3. Exit")

    try:
        duraduma = 0
        duraduma = int(input())

        if duraduma == 1:
            dnd.TakeFromListAndDownload()
            print("Done!")
        elif duraduma == 2:
            print("Don't rename list.txt, please. Supported formats: png, jpg, mp4, webm\n P.S. If you will check the code of this program, you can see I've used some segments from zeTU(my first python software)")    
        elif duraduma == 3:
            sys.exit()
            
        else:
            print('Wrong number!')    

    except ValueError:
        print("That's not even an int value!")
        duraduma = 0