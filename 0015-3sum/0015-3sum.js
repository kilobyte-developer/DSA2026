/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);

    let ans = [];

    for (let i = 0; i < nums.length - 2; i++) {

        // Skip duplicate anchors
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let anchr = nums[i];
        let pt1 = i + 1;
        let pt2 = nums.length - 1;

        while (pt1 < pt2) {

            let sum = nums[pt1] + nums[pt2];

            if (sum === -anchr) {

                ans.push([anchr, nums[pt1], nums[pt2]]);

                pt1++;
                pt2--;

                // Skip duplicate left values
                while (pt1 < pt2 && nums[pt1] === nums[pt1 - 1]) {
                    pt1++;
                }

                // Skip duplicate right values
                while (pt1 < pt2 && nums[pt2] === nums[pt2 + 1]) {
                    pt2--;
                }

            } else if (sum > -anchr) {
                pt2--;
            } else {
                pt1++;
            }
        }
    }

    return ans;
};