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
	printf("��ǰ�б���Ϊ%d\n",len);
	GetElem(L,3,e0);
	printf("��3��Ԫ����%d\n",e0);
	int j=LocateElem(L,45,equal);
	printf("��ֵΪ45��Ԫ���ڵ�%d��\n",j);
	
	

	ListTraverse(L,print);
	ListDelete(L,5,e0);
	printf("ɾ����5��Ԫ�أ�Ϊ��%d\n",e0);
	ListTraverse(L,print);
	
	
	
	
	return 0;
}
