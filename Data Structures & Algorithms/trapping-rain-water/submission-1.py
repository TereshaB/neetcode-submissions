class Solution:
    def trap(self, height: List[int]) -> int:
        max_val_l,max_val_r,=0,0
        max_arr_l,max_arr_r=[],[]
        for i in range (len(height)):
            max_val_l=max(max_val_l,height[i])
            max_arr_l.append(max_val_l)
        
        for i in range(len(height)-1,-1,-1):
            max_val_r=max(max_val_r,height[i])
            max_arr_r.append(max_val_r)
        max_arr_r=max_arr_r[::-1]
        tot_water_trapped=0
        for i in range(1,len(height)):
            left=max_arr_l[i]
            right=max_arr_r[i]
            tot_water_trapped+=min(left,right)-height[i]
        return tot_water_trapped

        
        