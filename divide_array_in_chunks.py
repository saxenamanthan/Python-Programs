arr = [1,4,3,2,1,0,3,4,9]
chunks = int(input("Enter chunk value - "))
index = 0
chunk_array = []
final_chunks_array = []

if len(arr)%chunks != 0:
    no_of_loops = (len(arr)//chunks)+1
else:
    no_of_loops = len(arr)//chunks

for k in range(0, no_of_loops):
    for _ in range(0, chunks):
        if index == len(arr):
            break
        chunk_array.append(arr[index])
        index += 1
    final_chunks_array.append(chunk_array)
    chunk_array = []

print(final_chunks_array)