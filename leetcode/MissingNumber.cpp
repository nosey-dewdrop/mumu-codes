#include <vector>
using namespace std;

class MissingNumber {
public:
      int missingNumber(vector<int>& nums) {
            int n = nums.size();
            int expected = n * (n + 1) / 2;

            int actual = 0;
            for (int i = 0; i < n; i++) {
                  actual += nums[i];
            }

            return expected - actual;
      }
};