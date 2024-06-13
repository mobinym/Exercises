# Importing the numpy library
import numpy as np 

# Defining a class to handle file operations
class File:
    def __init__(self, file_path, file_mode):
      # Initializing the file path and mode
      self.file_path = file_path
      self.file_mode = file_mode
      self.file_object = None
      
    def __enter__(self):
        # Opening the file and returning the file object
        self.file_object = open(self.file_path,self.file_mode)
        return self.file_object
    
    def __exit__(self,*exc):
        # Closing the file when we're done with it
        if self.file_object:
           self.file_object.close()
#-----------------------------------------------------------------------------
# Function to read a file and return its contents as a list of lines
def read_file(file):
    try:
        with open(file,"r") as file1:
            data_list = []
            for line in file1.readlines():
                if line != "":
                    line_list = line.split("\n")
                    data_list.append(line_list[0])
            return data_list
    except Exception as error:
        print("Error:",error)                
    finally:
         file1.close()          

#-----------------------------------------------------------------------------
# Function to convert a list into a numpy array
def create_array(filelist):
    array = np.array(filelist)
    return array
#-----------------------------------------------------------------------------

# Function to change the data type of the array elements to float
def change_array_and_reshape(array):
    arraychange = array.astype('f')
    print(arraychange)

#-----------------------------------------------------------------------------
# Function to reshape the array into a 3x5 matrix
def reshape(arraychange):
    reshapearray = arraychange.reshape(3,5)
    return reshapearray

#-----------------------------------------------------------------------------
# Function to calculate the mean of each row in the reshaped array
def Mean_array(reshapearray):
    arraymean = reshapearray.mean(axis=1)
    return arraymean
    
#-----------------------------------------------------------------------------
# Reading data from text files and printing it
datalist2019 = read_file('Homework 13/precipitation_fall_2019.txt')
datalist2020 = read_file('Homework 13/precipitation_fall_2020.txt')
datalist2021 = read_file('Homework 13/precipitation_fall_2021.txt')
print(datalist2019)
print(datalist2020)
print(datalist2021)
print(100*'-')

#-----------------------------------------------------------------------------
# Converting the data lists into numpy arrays and printing them
array2019 = create_array(datalist2019)
array2020 = create_array(datalist2020)
array2021 = create_array(datalist2021)
print(array2019)
print(array2020)
print(array2021)
print(100*'-')

#-----------------------------------------------------------------------------
# Changing the data type of the array elements to float and printing it
change_array_and_reshape(array2019)
print(100*'-')
#-----------------------------------------------------------------------------

# Reshaping the array into a 3x5 matrix and printing it
arrayreshape = reshape(array2019)
print(arrayreshape)
print(100*'-')

#-----------------------------------------------------------------------------
