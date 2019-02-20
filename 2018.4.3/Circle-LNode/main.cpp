#include "head.h"
#include "structure.h"
#include "func.h"
#include "Circle_LNode.h"

int main(){
	srand(time(0));
	LinkList L;
	InitList(L);
	ElemType e,e0;
	
	for(int j=0;j<8;j++)
	   ListInsert(L,1,random());
	
	ListTraverse(L,print);
	int len=ListLength(L);
	printf("当前当前长度为%d",len);
	
	
	return 0;
}
