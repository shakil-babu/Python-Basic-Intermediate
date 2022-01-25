/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function (nums) {
  let arr = nums.sort((a, b) => a - b);
  let l = 0,
    r = nums.length - 1,
    res = 0;
  while (l < r) {
    res = Math.max(res, arr[l] + arr[r]);
    l++;
    r--;
  }

  return res;
};
