from pymongo import MongoClient

try: 
    conn = MongoClient() 
    print("Connected successfully!") 
except:   
    print("Could not connect to MongoDB") 

db=conn.database

collection=db.useer

dictionary = { "_id, name", "phone", "address", "age", "sex"}

x = collection.insert_one(dictionary)

def binarySearch(number, SortedList):
      Low = 0
      High = len(SortedList) - 1
      while Low <= High :
            Mid = (High + Low) / 2
            if SortedList[Mid] == number:
                  return Mid
            elif SortedList[Mid] > number :
                  High=Mid - 1
            else :
                   Low = Mid + 1
      return "X";

def main():
      my_list = [_id]
      my_list = sorted(my_list)
      print my_list
      Sort = binarySearch(number, my_list)
      print Sort


if _id == "__main__":
      main()