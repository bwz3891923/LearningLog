#include "head.h"
#include "structure.h"
#include "func.h"
#include "Queue.h"



int main(){
	srand(time(0));
	LinkQueue Q;
	InitQueue(Q);
	QElemType e;
	
	for(int i=0;i<7;i++){
		e=random();
		EnQueue(Q,e);
	}
	QueueTraverse(Q,print);
	printf("目前的长度为：%d\n",QueueLength(Q));
	
	for(int i=0;i<4;i++){
		DeQueue(Q,e);
		printf(" 取出了%d\n",e);
		
	}
	QueueTraverse(Q,print);
	
	GetHead(Q,e);
	printf("头元素为：%d\n",e);
	
	
	
	return 0;
}
