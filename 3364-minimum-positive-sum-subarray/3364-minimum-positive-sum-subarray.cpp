class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {

        int n = nums.size();
        int lowestSum = INT_MAX;

        for (int start = 0; start < n; start++) {

            int sum = 0;

            for (int end = start; end < n && end < start + r; end++) {

                sum += nums[end];

                int length = end - start + 1;

                if (length >= l && sum > 0) {
                    lowestSum = min(lowestSum, sum);
                }
            }
        }

        return (lowestSum == INT_MAX) ? -1 : lowestSum;
    }
};