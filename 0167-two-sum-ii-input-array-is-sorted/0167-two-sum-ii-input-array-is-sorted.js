/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let ans = []
    let pt1 = 0
    let pt2 = numbers.length-1

    while(pt2>pt1){
        if(numbers[pt1]+numbers[pt2]==target){
            ans.push(pt1+1)
            ans.push(pt2+1)
            return ans
        }
        else if(numbers[pt1]+numbers[pt2]>target){
            pt2--
        }
        else{
            pt1++
        }
    }
    return 0
    
};