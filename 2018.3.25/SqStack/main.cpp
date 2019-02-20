//main
#include "head.h"
#include "structure.h"
#include "SqStack.h"
#include "func.h"


int main(){
	srand(time(0));
	SqStack S;
	InitStack(S);
	for(int i=0;i<10;i++){
		Push(S,random());
	}
	StackTraverse(S,print);
	
	SElemType e;
	for(int j=0;j<5;j++){
		Pop(S,e);
		printf("�Ƴ�Ԫ��:%d  \n",e);
	}
	
	StackTraverse(S,print);
	GetTop(S,e);
	printf("ջ����Ԫ��Ϊ��%d\n",e);
	
	int len=StackLength(S);
	printf("Stack�ĳ���Ϊ��%u\n",len);
	
	int state=StackEmpty(S);
	printf("�Ƿ�Ϊ�գ�%d\n",state);
	
	ClearStack(S);
	state=StackEmpty(S);
	printf("����������Ƿ�Ϊ�գ�%d\n",state);
	
	DestroyStack(S);
	

	
	
	
	
	return 0;
}
