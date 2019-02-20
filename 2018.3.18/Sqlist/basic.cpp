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
  printf("��ʼ��L��L.length=%d��L.listsize=%d��L.elem=%u\n",
  L.length, L.listsize, L.elem);
  for(j=1; j<=10; j++)
    i=ListInsert(L, 1, j); 
  printf("\n����ListTraverse()���������������L�е�Ԫ�أ�");
  ListTraverse(L, print); 
  
  e=ListLength(L);
  printf("����ĳ���Ϊ��%d\n",e);
  
  GetElem(L,4,e0);
  printf("ѡȡ�˵�4��Ԫ�أ�Ϊ��%d\n",e0);
  
  j=LocateElem(L,5,equal);
  printf("��ֵΪ6��λ���ڣ�%d\n",j);
  
  PriorElem(L,4,e0);
  printf("��ֵΪ4��ǰ��Ϊ��%d\n",e0);
  
  NextElem(L,2,e0);
  printf("��ֵΪ2�ĺ���Ϊ��%d",e0);
  
  ListDelete(L,2,e0);
  printf("λ��Ϊ2����ֵɾ����ֵΪ��%d",e0);
  
  printf("\n����ListTraverse()���������������L�е�Ԫ�أ�");
  ListTraverse(L,print);
  
  i=ListEmpty(L);
  printf("�����Ƿ�Ϊ���أ�%d",i);
  ClearList(L);
  printf("ִ��ClearList(L)��L.length=%d��L.listsize=%d��L.elem=%u\n",
  L.length, L.listsize, L.elem);
  i=ListEmpty(L);
  printf("ִ��ClearList(L)�������Ƿ�Ϊ���أ�%d",i);
  
  
  
  
}
