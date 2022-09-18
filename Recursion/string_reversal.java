
/* 
                Explanation
public String reverseString(String input){
        // What is the base case? (When can i no longer continue)
        if (input.equals("")){  
            return ""; // if the input is an empty string then return the empyty string (base case)
        }
        // What is the smallest amout of work I can do in each iteration ( Between each invocation, what's the smallest "unit" I can reverse)
        return reversalString(input.substring(1)) + input.chatAt(0) // taking the first charter from the input string and we concat it after the recursive call. 
            }                 //↑                            //↑
            //(Shrinking the problem space)    //Smallest unit of work to contribute

    //goal = reversedString

    reverseString("ello") + "h" 
*/