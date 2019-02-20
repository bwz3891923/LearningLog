
#include "head.h"
#include "structure.h"
#include "SqStack.h"
#include "func.h"
#include <ctype.h>

int main(){
	SqStack q;
	InitStack(q);
	char c;
	int * a;
	int * b;
	
	printf("Imput your parameter(included Num and Operator):");
	while(c!='#'){
		if(isdigit(c))
		    switch(c){
			    case('+'):{
				    Pop(q,b);
				    Pop(q,a);
				    Push(q,*a+*b);
				    break;
			    }
			    case('-'):{
				    Pop(q,b);
				    Pop(q,a);
				    Push(q,*a-*b);
				    break;
			    }
			    case('*'):{
				    Pop(q,b);
				    Pop(q,a);
				    Push(q,*a+*b);
				    break;
			    }
			    case('/'):{
				    Pop(q,b);
				    Pop(q,a);
				    Push(q,*a/b*);
				    break;
			    };
			else{
				int(c);
				Push(q,c);
			}  
			
			    Push(q,c);
			    scanf("%c",c);
				
		}
		
		
	}
	
	
	
}
