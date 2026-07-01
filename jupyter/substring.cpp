#include <iostream>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(std::string s)
    {
        int size = s.size();
        int maxx = 0;
        std::set<int> mpp;
        for (int i = 0; i < size; i++)
        {
            int j = i;
            mpp.clear();
            while (j < size)
            {
                if (!mpp.contains(s[j]))
                {
                    mpp.insert(s[j]);
                }
                else
                {
                    break;
                }
                j++;
            }
            maxx = max<int>(maxx, mpp.size());
        }
        return maxx;
    }
};

int main()
{

    std::string s = "pwwkew";
    Solution sol;
    std::cout << (sol.lengthOfLongestSubstring(s)) << std::endl;
}