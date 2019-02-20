#include "head.h"
#include "structure.h"
#include "SqList.h"
#include "func.h"

int main()
{
  SqList L;
  ElemType e, e0;
  Status i;
  int j, k;
  InitList(L); 
  printf("初始化L后，L.length=%d，L.listsize=%d，L.elem=%u\n",
  L.length, L.listsize, L.elem);
  for(j=1; j<=10; j++)
    i=ListInsert(L, 1, j); 
  printf("\n调用ListTraverse()函数，依次输出表L中的元素：");
  ListTraverse(L, print); 
  
  e=ListLength(L);
  printf("链表的长度为：%d\n",e);
  
  GetElem(L,4,e0);
  printf("选取了第4个元素，为：%d\n",e0);
  
  j=LocateElem(L,5,equal);
  printf("数值为6的位置在：%d\n",j);
  
  PriorElem(L,4,e0);
  printf("数值为4的前驱为：%d\n",e0);
  
  NextElem(L,2,e0);
  printf("数值为2的后驱为：%d",e0);
  
  ListDelete(L,2,e0);
  printf("位置为2的数值删除，值为：%d",e0);
  
  printf("\n调用ListTraverse()函数，依次输出表L中的元素：");
  ListTraverse(L,print);
  
  i=ListEmpty(L);
  printf("链表是否为空呢？%d",i);
  ClearList(L);
  printf("执行ClearList(L)，L.length=%d，L.listsize=%d，L.elem=%u\n",
  L.length, L.listsize, L.elem);
  i=ListEmpty(L);
  printf("执行ClearList(L)，链表是否为空呢？%d",i);
  
  
  
  
}
