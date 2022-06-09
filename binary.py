#binary search 
def binary(arr,low,high,elem):
	if high>=low:
		mid=(high+low)//2
		if(arr[mid]==elem):
			return mid
		elif(arr[mid]>elem):
			return binary(arr,low,mid-1,elem)
		else:
			return binary(arr,mid+1,high,elem)
	else:
		return 0
arr=[2,4,18,21,33,45,66]
print("the list is",arr)
elem=int(input("enter an element to search"))

output=binary(arr,0,len(arr)-1,elem)
if output !=0:
	print("the element is found at",output);
else:
	print("the element is not present in the list");

