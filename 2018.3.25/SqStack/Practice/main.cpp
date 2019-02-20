//main
#include "head.h"
#include "structure.h"
#include "SqStack.h"
#include "func.h"

int main(){
	SqStack S;
	InitStack(S);
	
	int data,times,turn=1;
	while(turn){
		
		times=StackLength(S)+1;
		printf("\n正在收集第%d位数(输入0/1以外的数时终止):",times);
		scanf("%d",&data);
		if(data==1 || data==0)
		   Push(S,data);
		else
		   turn=0;
	}
	printf("二进制为");
	StackTraverse(S,print);
	
	int i=StackLength(S);
	SElemType * p=S.base;
	int sum;
	for(int j=0;j<i;j++){
		int expo=int(S.top-S.base);
		sum+=*(p++)*expo;
			
	}
	printf("转为十进制后为：%d",sum);
	
	return 0;
}
