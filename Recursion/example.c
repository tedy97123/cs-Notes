



public void recursion() {
    if (someValue == 10){ // base case a.k.a stopping point ; if this wasnt here the method would call itself eitehr for infitinty or untill stack over flow happens
        return;
    }
    return recursion( someValue + 1);  // recursive call ;  method that inches the value your looking for towards the base case 
}