// main2-1.cpp ����bo2-1.h��������
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
  printf("��ʼ��L��L.length=%d��L.listsize=%d��L.elem=%u\n",
  L.length, L.listsize, L.elem);
  for(j=1; j<=5; j++)
    i=ListInsert(L, 1, j); 
  printf("\n����ListTraverse()���������������L�е�Ԫ�أ�");
  ListTraverse(L, print1); 
  
}

