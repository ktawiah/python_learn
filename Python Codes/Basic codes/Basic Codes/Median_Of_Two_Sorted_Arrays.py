nums1 = []
nums2 = []
list1_size = input('How many elments would you enter for the first array: ')
list1_size = int(list1_size)
prompt = input('Enter list\n')
for value in range(0, list1_size):
    element = input()
    element = int(element)
    nums1.insert(value, element)
list2_size = input('How many elments would you enter for the first array: ')
list2_size = int(list2_size)
prompt = input('Enter list\n')
for value in range(0, list2_size):
    element = input()
    element = int(element)
4    nums2[value] = element
print(nums1)
print(nums2)
nums3 = nums1 + nums2
print(sorted(nums3))
