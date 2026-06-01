class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        tcost = 0 
        cost.sort(reverse=True)

        lenght = len(cost)

        num3 = lenght // 3
        mod3 = lenght % 3

        pos =0 

        for i in range (0 , num3):
            F_candy = cost[pos]
            tcost = tcost + F_candy
            pos+=1
            
            S_candy = cost[pos]
            tcost = tcost + S_candy
            pos+=2

        for i in range(0 , mod3):
            candy = cost[pos]
            tcost = tcost + candy
            pos+=1

        return tcost