
def max_list_iter(int_list):  # must use iteration not recursion
   if type(int_list) != list:
      raise ValueError
   if len(int_list) == 0:
      return None
   max_int = int_list[0]
   for i in range(1, len(int_list)):
      if int_list[i] > max_int:
         max_int = int_list[i]
   return max_int  

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if type(int_list) != list:
      raise ValueError
   if len(int_list) <= 1:
      return int_list 
   else:
      return int_list[-1:] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if type(int_list) != list:
      raise ValueError
   check_range = high - low
   middle = low + check_range // 2
   if int_list[middle] == target:
      return middle
   elif high < low:
      return None
   elif check_range == 2:
      if int_list[low] == target:
         return low
      elif int_list[high] == target:
         return high
   elif target > int_list[middle]:
      return bin_search(target, middle + 1, high, int_list)
   else:
      return bin_search(target, low, middle - 1, int_list)
      
