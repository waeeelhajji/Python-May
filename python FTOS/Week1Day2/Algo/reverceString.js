/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(string) {
    var str = ""
    for (var i = string.length - 1; i >= 0; i--) {
        str += string[i]
        // console.log(str)
    }
    console.log(string, str)
    return str
}

reverseString(str3)