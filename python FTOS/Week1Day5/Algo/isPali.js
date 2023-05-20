/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

// level
// bob
// tacocat
// 

//            v
const str1 = "a x a";
//            a x a
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
//            duD
const expected3 = false;

const str4 = "ohox";
const expected4 = false;

function isPalindrome(str) {
  for (let i = 0; i < Math.floor(str.length / 2); i++) {
    // Looping inwards from both sides.
    const leftChar = str[i];
    const rightChar = str[str.length - 1 - i];

    if (leftChar !== rightChar) {
      return false; // early exit
    }
  }
  return true;
}