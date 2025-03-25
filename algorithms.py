#Levenshtein distance Alghorithm

def levemshtein_distance (s1,s2):
    m,n = len(s1) , (s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range (m + 1):
        dp[i][0]=1
        for j in range (n + 1):
            dp[0][j]=j


            #know about distance 

            for i in range (1, m + 1 ):
                for j in range (1 , n +1 ):
                    if s1[i - 1] == s2 [j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else :
                        dp [i][j] = min (dp [i - 1][j], dp[i][j - 1], dp[i -1][j-1])+1
            return dp[m][n]
        
        #get input 
        s1 = input ("please insert 1st input")
        s2 = input ("please insert 2nd input ")
        distance = levemshtein_distance(s1 , s2)
        print(f"levenshtein distance between '{s1}' & '{s2} is equal = {distance}' ")
    
