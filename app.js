var bitwiseComplement = function (n) {
  let binary = n.toString(2);
  let str = "";
  for (let item of binary) {
    if (item === "0") str += "1";
    else str += "0";
  }
  return parseInt(str, 2);
};
let ans = bitwiseComplement(5);
console.log(ans);
