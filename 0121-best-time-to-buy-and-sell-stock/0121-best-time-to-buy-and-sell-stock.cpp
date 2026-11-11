class Solution {
public:
    int maxProfit(vector<int>& prices) {
       int lowest = prices[0];
       int maxProfit = 0;

       for(int i = 1; i<prices.size(); i++){

            int profit = prices[i] - lowest;

            if(profit>maxProfit){
                maxProfit = profit;
            }

            if(prices[i] < lowest){
                lowest = prices[i];
            }
       }
       return maxProfit;
    }
};