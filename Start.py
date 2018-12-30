import os
import time
import datetime
import videosplit
import Main
import cv2
from PIL import Image
import pymongo
import pprint
from pymongo import MongoClient
# These are the parameters to set the naming of the database.
"""
host = 'localhost'
database = 'ALPR'
collection = 'videosTest'    
"""
"""
def mongo_connection():
    con = pymongo.MongoClient(host)
    col = con[database][collection]
    if col.count()==0:
        con[database].create_collection(collection)
    return col
def mongo_query(s):
   """ 

if __name__ == '__main__':
    """
    name = str(input('Enter the name of the video: '))
    (vdolength,totalFrames) = videosplit.Launch(name)
	# The name of the folder to store the frames of the video
    os.chdir('data')

    result = {}
    result_imag = {}
    #startTime = datetime.now()
    startTime = time.time()
    for f in os.listdir():
        pred, img = Main.main(f)
        if pred in result.keys():
            result[pred] = result[pred] + 1
        elif pred != ' ':
            result[pred] = 1
            result_imag[pred] = img

    #endTime = datetime.now()
    endTime = time.time()
    # Sort the list of number plates by the frequency of their occurance
    l = {x: y for y, x in result.items()}
    r = list(sorted(l.keys()))
    index = r[len(r) - 1]
    plate = l[index]
    img = result_imag[plate]
    executionTime = "{0:.2f}".format(endTime - startTime)
    print('The name plate is :', plate, ' frequency is: ', result[plate])
    try:
        Image.fromarray(img).show()
    except:
        print("Problem in displaying license plate")
    print('execution time is : ' + executionTime)
    
    os.chdir('..')
    licensePlatePath = './LicensePlates/'+name.split('.')[0]+'.jpg'
    try:
        cv2.imwrite(licensePlatePath,img)
    except:
        print("Problem in writing license plate image")
    """    
    # If u want to see the freqiencies for predictions then uncomment the below 2 lines.
    """
    for i in result.keys():
        print(i, ' : ', result[i])
    """
    
    # Store the result into mongodb
    #if the  query is successful put the time and the litres of gas used
    """
    try:
        col = mongo_connection()
        #dict = {}
        dict['date and time'] = time.ctime()
        dict['video'] = name
        dict['video length'] = vdolength
        dict['image'] = plate
        dict['Total Frames in video'] = totalFrames
        dict['execution_time'] = executionTime
        dict['frequency ratio'] = "{0:.2f}".format(result[plate] / len(result))
        
        col.insert(dict)
    except Exception as e:
        print(e)
    """
    client = MongoClient('localhost',27017)
    db = client['users']
    collections_users = db['costco']
    name = str(input('enter the name of the file: '))
    for filename in os.listdir(name):
        
        img = Main.main(filename)
        query = {"LPR":img}
        member_found= collections_users.find(query)
        for i in member_found:
            pprint.pprint(i)
                
    
                
    