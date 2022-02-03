    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
       
        #  Approach 1
        
        dic={}
        for i in nums1:
            for j in nums2:
                s=i+j                                           # using two dictionary  
                if s not in dic:
                    dic[s]=1
                else:
                    dic[s]+=1
        dic2={}
        for i in nums3:
            for j in nums4:
                s=i+j
                if s not in dic2:
                    dic2[s]=1
                else:
                    dic2[s]+=1
        ans=0
        for i in dic.keys():
            if -i in dic2.keys():
                ans+=dic[i]*dic2[-i]
        return ans
      
      #--------------------------------------------------------------------------------
      
      # Approach  2 
      
          see={}
        for i in nums1:
            for j in nums2:
                sum_=i+j
                if sum_ not in see:
                    see[sum_]=0
                see[sum_]+=1
            
        count=0
        for a in nums3:
            for b  in nums4:
                sum_=a+b
                if -sum_ in see:
                    count+=see[-sum_]
        return count
