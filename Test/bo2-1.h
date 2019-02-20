// bo2-1.h 顺序存储的线性表（存储结构由c2-1.h定义）的基本操作（12个），包括算法2.3～2.6
void InitList(SqList &L) 
{ 
  L.elem=(ElemType*)malloc(LIST_INIT_SIZE*sizeof(ElemType));
  if(!L.elem) 
    exit(OVERFLOW);
  L.length=0; 
  L.listsize=LIST_INIT_SIZE; 
}

Status ListInsert(SqList &L, int i, ElemType e) 
{ 
  
  ElemType *newbase, *q, *p;
  if(i<1 || i>L.length+1) 
    return ERROR;
  if(L.length==L.listsize) 
  { newbase=(ElemType*)realloc(L.elem, (L.listsize+LIST_INCREMENT)*
    sizeof(ElemType));
    if(!newbase) 
      exit(OVERFLOW);
    L.elem=newbase; 
    L.listsize+=LIST_INCREMENT; 
  }
  q=L.elem+i-1; 
  for(p=L.elem+L.length-1; p>=q; --p) 
    *(p+1)=*p;
  *q=e; 
  L.length++; 
  return OK;
}

void ListTraverse(SqList L, void(*visit)(ElemType&))
{ 
  
  
  ElemType *p=L.elem; 
  for(int i=1; i<=L.length; i++) 
    visit(*p++); 
  printf("\n");
}

