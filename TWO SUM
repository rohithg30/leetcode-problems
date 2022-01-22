#  brute force approach: T=O(n^2),S=O(1)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
          if nums[i]+nums[j]==target:
                return i,j



#  optimize by using hashmap : T=O(N),S=O(1)

hashm={}
for i in range(len(nums)):
      c=target-nums[i]
      if c in hashm:
          return hashm[c],i
      hashm[nums[i]]=i
      
