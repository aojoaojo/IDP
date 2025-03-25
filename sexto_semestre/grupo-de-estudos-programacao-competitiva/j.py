hm = {}
for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        
# sort the dictionary by value
sorted_hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)

# return the top k frequent elements
return [sorted_hm[i][0] for i in range(k)]