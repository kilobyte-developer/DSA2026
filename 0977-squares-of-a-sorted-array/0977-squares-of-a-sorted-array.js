/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let pt1 = 0
    let pt2 = nums.length-1
    let ans = []
    let idx = nums.length -1
    
    function sqr(n){
        return n*n
    }
    while(pt1<=pt2){
       if(Math.abs(nums[pt1])>Math.abs(nums[pt2])){
            ans[idx] = Math.abs(sqr(nums[pt1]))
            pt1++
            idx--
       }
       else{
        ans[idx] = Math.abs(sqr(nums[pt2]))
        pt2--
        idx--
       }
    }
    return ans
};