/* 
++++++++++++++++   compile with gcc kahan.c     ++++++++++++++++++++++++
========================================================================
     W. Kahan's example of finite precision arithmetic failings 
  from C. Van Loan, Intro. to Computational Science, 1995; p.xxiv     
________________________________________________________________________
*/ 

#include <stdio.h>
#include <math.h>

  int main() {

  double h, x, y, u, v, q; 

 	h = 1.0/2;
 	x = 2.0/3 - h;
 	y = 3.0/5 - h;
	u = (x + x + x) - h;
	v = (y + y + y + y + y) - h;
	q = u/v;

  	printf("\nC:\n");
  	printf("h = %0.16f\n",h);
  	printf("x = %0.16f\n",x);
  	printf("y = %0.16f\n",y);
  	printf("u = %0.16f\n",u);
  	printf("v = %0.16f\n",v);
  	printf("q = %0.16f\n",q);
  	printf("\n");

}
