
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        
        const int MOD = 1e9 + 7;

        long long even = 1;
        long long odd = 0;
        long long ans = 0;

        int parity = 0;

        for (int i = 0; i < arr.size(); i++) {

            parity = (parity + arr[i]) % 2;

            if (parity == 1) {
                ans += even;
                odd++;
            }
            else {
                ans += odd;
                even++;
            }

            ans %= MOD;
        }

        return ans;
    }
};
