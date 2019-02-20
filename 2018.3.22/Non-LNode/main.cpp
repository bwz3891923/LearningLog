#include "head.h"
#include "structure.h"
#include "Non-LNode.h"
#include "func.h"

int main(){
	srand(time(0));
	LinkList L;
	InitList(L);
	ElemType e,e0;
	for(int j=0;j<8;j++){
        e=random();
		CreatListHead(L,e);
	}
	ListInsert(L,2,45);
	int len=ListLength(L);
	printf("当前列表长度为%d\n",len);
	GetElem(L,3,e0);
	printf("第3个元素是%d\n",e0);
	int j=LocateElem(L,45,equal);
	printf("数值为45的元素在第%d个\n",j);
	
	

	ListTraverse(L,print);
	ListDelete(L,5,e0);
	printf("删除第5个元素，为：%d\n",e0);
	ListTraverse(L,print);
	
	
	
	
	return 0;
}
