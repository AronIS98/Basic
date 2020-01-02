class Distribution:
    
    def __init__(self,other = None):
        #if fed a data stream, creates a dictionary out of the information
        if other:
            the_file = other.read()
            file_stream_list = the_file.split()
            keys = set(file_stream_list)
            key_list = list(keys)
            key_list.sort()
            for keys in range(len(key_list)):
                key_list[keys] = int(key_list[keys])

            the_dict = {}
            for key_number in range(len(key_list)):
                key_amount = 0
                for a_number in file_stream_list:
                    if int(a_number) == key_list[key_number]:
                        key_amount +=1
                the_dict.update({key_list[key_number]:key_amount})
            self.__distribution = the_dict

        else: # if not fed anything, self.__distribution becomes None
            self.__distribution = other

    def set_distribution(self, distribution):
        #allows user to change the value of self.__distribution
        self.__distribution = distribution

    def average(self):
        #finds the average by multiplying every number by its counter and then devided by the sum of all the counters
        average = 0
        total_numbers = 0
        current_value = 0
        if self.__distribution != None:
            for each in self.__distribution:
                current_value += (self.__distribution[each])*each
                total_numbers += self.__distribution[each]
            average = current_value/total_numbers
        return average

    def __ge__(self, other):
        #allows you to compare two instances of this class by comparing their average.
        return self.average() >= other.average()
    
    def __add__(self,other):
        #allows you to add to gether two instances of the class by creating merging the dicts in self.__distribution and other.__distribution into a new dict
        #then returns a new instance of itself with the new dict as self.__distribution.
        temp_list = []
        temp_dict = {}
        #merging the dicts:
        for each in other.__distribution:
            if each in self.__distribution:
                self.__distribution[each] += other.__distribution[each]
            else:
                self.__distribution.update({each:other.__distribution[each]})
        
        for each in self.__distribution:
            temp_list.append([each,self.__distribution[each]])
        temp_list.sort()
        for each in temp_list:
            temp_dict.update({each[0]:each[1]})
        self.__distribution = temp_dict
        #returns a new instance of itself:
        return self

    def __str__(self):
        #delivers the data in self.__distribution as a neat string.
        string = ""
        if self.__distribution != None:
            for each in self.__distribution:
                string += ("{}: {}\n".format(each,self.__distribution[each]))
        return string