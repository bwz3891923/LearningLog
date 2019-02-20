// main2-1.cpp 检验bo2-1.h的主程序
#include"c1.h"
typedef int ElemType; 
#include"c2-1.h" 
#include"bo2-1.h" 
#include"func2-2.h" 

int main()
{
  SqList L;
  ElemType e, e0;
  Status i;
  int j, k;
  InitList(L); 
  printf("初始化L后，L.length=%d，L.listsize=%d，L.elem=%u\n",
  L.length, L.listsize, L.elem);
  for(j=1; j<=5; j++)
    i=ListInsert(L, 1, j); 
  printf("\n调用ListTraverse()函数，依次输出表L中的元素：");
  ListTraverse(L, print1); 
  
}

