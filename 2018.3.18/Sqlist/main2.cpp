#include "head.h"
#include "structure.h"
#include "SqList.h"
#include "func.h"
#include "advanced.h"

int main(){
	SqList La;
	SqList Lb;
	
	InitList(La);
	InitList(Lb);
	
	for(int i=2;i<10;i+=2) {
		int j=i+1;
		ListInsert(La,1,i);
		ListInsert(Lb,1,j);
	}
	
	ListTraverse(La,print);
	ListTraverse(Lb,print);
	
	Union(La,Lb);
	ListTraverse(La,print);
	
	
	
	
	
	return 0;
}
