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
		printf("移除元素:%d  \n",e);
	}
	
	StackTraverse(S,print);
	GetTop(S,e);
	printf("栈顶的元素为：%d\n",e);
	
	int len=StackLength(S);
	printf("Stack的长度为：%u\n",len);
	
	int state=StackEmpty(S);
	printf("是否为空？%d\n",state);
	
	ClearStack(S);
	state=StackEmpty(S);
	printf("清除操作后，是否为空？%d\n",state);
	
	DestroyStack(S);
	

	
	
	
	
	return 0;
}
