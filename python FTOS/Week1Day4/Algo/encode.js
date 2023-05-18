/* 
  Given in an alumni interview.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

const str1 = "aaaabbcddd";
const expected1 = "a4b2cd3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
  var newStr = ""
  var counter = 1 // to account for the fist letter start at 1
  for (var i = 0; i < str.length; i++) {
    if (str[i] == str[i + 1]) {
      counter++
    } else {
      if (counter <= 1) { // if only 1 letter just add it
        newStr += str[i]
      } else {
        newStr += (str[i] + counter) // add the current letter + current count
      }
      counter = 1 // reset counter for the next loop
    }
  }
  if (newStr.length >= str.length) { // if it's not shorter
    return str
  }
  console.log(newStr)
  return newStr
}

encodeStr(str1)