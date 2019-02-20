#include "head.h"
#include "structure.h"
#include "SLinkList.h"
#include "func.h"

int main(){
	srand(time(0));
	
	
	SLinkList L;
	InitList(L);
	
	for(int i=0;i<10;i++){
		int j=random();
		CreatList(L,j);
	}
	
	int j=ListLength(L);
	
	ListTraverse(L,print); 
	
	int e,e0,e1;
	ListDelete(L,3,e);
	printf("提取的元素为： %d\n",e);
	
	ListTraverse(L,print);
	
	GetElem(L,3,e);
	printf("位于位序为3的元素为%d\n",e);
	
	ListInsert(L,6,152);
	ListTraverse(L,print);
	
	j=LocateElem(L,152);
	printf("数值为152的元素在第%d个\n",j);
	
	
	PriorElem(L,e,e0);
	printf("数值%d的前驱为%d\n",e,e0);
	
	NextElem(L,e,e1);
	printf("数值%d的后驱为%d\n",e,e1);


	
	
	

	
	return 0;
	
}
