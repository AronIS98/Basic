
# # Main program starts here
# class IntList:
#     def __init__(self,other):
#         self.max_len = other
#         self.numbers = []
#     def add(self,other):
#         if len(self.numbers) < self.max_len:
#             self.numbers.append(other)

#     def __len__(self):
#         return len(self.numbers)

#     def __add__(self,other):
#         if len(self) < len(other):
#             length = len(self)
#         else:
#             length = len(other)
#         outcome = [self.numbers[each]+self.numbers[other] for each in range(length)]
#         return outcome
#     def full(self):
#         if len(self.numbers = self.max_len):
#             return True


# list1 = IntList(5)  # Constructs an IntList that can hold 5 integers
# list2 = IntList(12) # Constructs and IntList that can hold 12 integers

# for i in range(10):
#     list1.add(i)
#     list2.add(i)

# print(list1)
# print(list2)

# print("Length of list1 is: {}".format(len(list1)))
# print("Length of list2 is: {}".format(len(list2)))

# if list1.full():
#     print("list1 is full")
# if list2.full():
#     print("list2 is full")

# list3 = list1 + list2
# print(list3)

# list4 = list2 + list1
# print(list4)

class Distribution:

    def __init__(self,other = None):
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
        else:
            self.__distribution = other

    def set_distribution(self, distribution):
        self.__distribution = distribution

    def average(self):
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
        return self.average() >= other.average()
    
    def __add__(self,other):
        temp_list = []
        temp_dict = {}
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


        return self





    def __str__(self):
        string = ""
        if self.__distribution != None:
            for each in self.__distribution:
                string += ("{}: {}\n".format(each,self.__distribution[each]))
        return string

dist1 = Distribution()

dist1.set_distribution({1:4, 2:5, 3:3, 4:5, 5:7, 6:2})

dist2 = Distribution()

dist2.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4, 7:2})

dist3 = dist1 + dist2
print(dist3)