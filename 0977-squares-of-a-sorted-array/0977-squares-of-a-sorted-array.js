/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let pt1 = 0
    let pt2 = nums.length-1
    let ans = []
    
    for(let i = 0; i<nums.length; i++){
        ans.push(nums[i]*nums[i])
    }
    ans.sort((a,b)=>a-b)
    return ans
};