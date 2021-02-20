#include <stdio.h> 
#include <math.h>
#include <cstdlib> 
typedef uint64_t k;int main(int _,char** a){k i=atoi(a[1]);k n=i+1;k f3,f2=0;k f1=1;while(n>1){f3=f2;f2=f1;f1+=f3;n--;}k o=f1*log2(f1)-f3*log2(f3)-f2*log2(f2);if(i<2)o=0;printf("%llu",o);}