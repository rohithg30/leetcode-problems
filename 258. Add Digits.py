# APPROACH 1 : LOOP

 def addDigits(self, num: int) -> int:
        
        res=0
        while num>0:
            res+=num%10         
            num//=10  

            if res>9 and num==0:
                num=res
                res=0
        return res
      
      
 # APPROACH  2: 
    def addDigits(self, num: int) -> int:
        
        if num==0:
            return 0
        if num % 9==0:
            return 9
        return num % 9
      
      
        
        
        
        
         
