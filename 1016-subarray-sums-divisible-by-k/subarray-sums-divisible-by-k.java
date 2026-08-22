class Solution {
    public int subarraysDivByK(int[] nums, int k) {

        int[] remainderCount = new int[k];

        remainderCount[0] = 1;

        int prefixSum = 0;
        int answer = 0;

        for (int num : nums) {

            prefixSum += num;

            int remainder = ((prefixSum % k) + k) % k;

            answer += remainderCount[remainder];

            remainderCount[remainder]++;
        }

        return answer;
    }
}