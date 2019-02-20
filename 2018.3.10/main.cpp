#include "head.h"
#include "LinearList.h" 
#include "func.h"

int main(){
	Sqlist L;
	Status i;
	ElemType j,k;
	ElemType e,e0;
	InitList(L);
	printf("%d  %u   %d   ",L.length,L.listsize,L.elem);
	for(j=1;j<8;j++){
		ListInsert(L,1,j);
	} 

	return 0;
}
