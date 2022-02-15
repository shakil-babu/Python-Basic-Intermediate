var hasAlternatingBits = function (n) {
  let bin = n.toString(2);
  if (bin.includes("00") || bin.includes("11")) {
    return false;
  }
  return true;
};

let ans = hasAlternatingBits(6);
console.log(ans);
