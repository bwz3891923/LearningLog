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
		printf("\n�����ռ���%dλ��(����0/1�������ʱ��ֹ):",times);
		scanf("%d",&data);
		if(data==1 || data==0)
		   Push(S,data);
		else
		   turn=0;
	}
	printf("������Ϊ");
	StackTraverse(S,print);
	
	int i=StackLength(S);
	SElemType * p=S.base;
	int sum;
	for(int j=0;j<i;j++){
		int expo=int(S.top-S.base);
		sum+=*(p++)*expo;
			
	}
	printf("תΪʮ���ƺ�Ϊ��%d",sum);
	
	return 0;
}
