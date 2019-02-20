#include "head.h"
#include "structure.h"
#include "LNode.h"
#include "func.h"

int main(){
	LinkList L;
	InitList(L);
	int i,j;
	ElemType e,e0;
	for (int j=0;j<10;j++){
		AddElemTail(L,j);	
	}
	printf("ListTraverse(L,print)");
	ListTraverse(L,print);
	
	
	i=ListLength(L);
	printf("ListLength(L):%d\n",i);
	
	GetElem(L,5,e);
	printf("GetElem(L,5,e);e=%d\n",e);
	
	i=LocateElem(L,9,equal);
	printf("LocateElem(L,9,equal),i=%d\n",i); 
	
	PriorElem(L,e,e0);
	printf("PriorElem(L,e,e0);e0=%d\n",e0);
	
	NextElem(L,e,e0);
	printf("NextElem(L,e,e0);e0=%d\n",e0);
	
	ListDelete(L,6,e0);
	printf("ListDelete(L,6,e0),e0=%d\n",e0);
	printf("ListTraverse(L,print)");
	ListTraverse(L,print);
	
	ClearList(L);
	ListTraverse(L);
	
	
	
	
	
	
	
	
	
	
	return 0;
}
