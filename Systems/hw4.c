//JacobSiepker
//Computer Systems 1

#include <stdio.h>

 //does random math operations
int f1(int x, int y) {
  int output = x;
  output += y;
  output *= (x - y);
  return output;
}

//flips the two variables pointers
void f2(int *x, int *y) {
	int temp = *x;
	*x = *y;
	*y = temp;
}

//returns if both x and y are zero
//I possibly have the returns flipped
int f3(int x, int y) {
	if (x == 0 & y == 0){
		return 1;
	}
	return 0;
}
 
 //initializes array to 1000000*n for each n in the array
void f4(int *xPtr, int len) {
  if (len == 0){
  	return;
  }
  
  long num = 0;
  long maxFill = (int)len * 1000000;
  
  while (num < maxFill){
  	*xPtr = num;
  	num += 1000000;
  	xPtr++;
  }
}
  
  
//returns length of string
int f5(char *x) {
  if (*x == 0){return 0;}
  x++;
  int count = 0;
  
  while (*x != 0){
  	x++;
  	count ++;
  }
  return count;
}

