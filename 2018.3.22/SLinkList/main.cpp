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
	printf("��ȡ��Ԫ��Ϊ�� %d\n",e);
	
	ListTraverse(L,print);
	
	GetElem(L,3,e);
	printf("λ��λ��Ϊ3��Ԫ��Ϊ%d\n",e);
	
	ListInsert(L,6,152);
	ListTraverse(L,print);
	
	j=LocateElem(L,152);
	printf("��ֵΪ152��Ԫ���ڵ�%d��\n",j);
	
	
	PriorElem(L,e,e0);
	printf("��ֵ%d��ǰ��Ϊ%d\n",e,e0);
	
	NextElem(L,e,e1);
	printf("��ֵ%d�ĺ���Ϊ%d\n",e,e1);


	
	
	

	
	return 0;
	
}
