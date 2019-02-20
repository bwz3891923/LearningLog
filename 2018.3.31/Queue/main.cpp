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
	printf("Ŀǰ�ĳ���Ϊ��%d\n",QueueLength(Q));
	
	for(int i=0;i<4;i++){
		DeQueue(Q,e);
		printf(" ȡ����%d\n",e);
		
	}
	QueueTraverse(Q,print);
	
	GetHead(Q,e);
	printf("ͷԪ��Ϊ��%d\n",e);
	
	
	
	return 0;
}
