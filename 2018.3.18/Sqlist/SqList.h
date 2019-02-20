
void InitList(SqList &L) 
{ 
  L.elem=(ElemType*)malloc(LIST_INIT_SIZE*sizeof(ElemType));
  if(!L.elem) 
    exit(OVERFLOW);
  L.length=0; 
  L.listsize=LIST_INIT_SIZE; 
}

void DestoryList(SqList &L){
	free(L.elem);
	L.elem=NULL;
	L.length=0;
	L.listsize=0;
}

void ClearList(SqList &L){
	L.length=0;
	
}

Boolean ListEmpty(SqList &L){
	if (L.length=0 )return TRUE;
	else return FALSE;
	
}

int ListLength(SqList L){
	return L.length;
}

Status GetElem(SqList L,int i,ElemType &e){
	ElemType * p=L.elem;
	if (i<1 || i>L.length) return FALSE;
	else
	   e=*(p+i-1);
	   return OK;
}

int LocateElem(SqList L,ElemType e,Status (* compare)(ElemType,ElemType)){
	ElemType * p=L.elem;
	for(int i=1;i<=L.length;i++){
		if(compare(e,*(p++))) return i;	
	}
	return FALSE;
}

int PriorElem(SqList L,ElemType cur_e,ElemType &pre_e){
	ElemType * p=L.elem;
	int i=2;
	while(i<=L.length && cur_e!=*p){
		i++,p++;
	}
	if(i>L.length) return ERROR;
	else {
		pre_e=*(--p);
		return OK;
	}
}

int NextElem(SqList L,ElemType cur_e,ElemType &next_e){
	ElemType * p=L.elem;
	int i=1;
	while(i<=L.length-1 && cur_e!=*p){
		i++,p++;
	}
	if(i==L.length) return ERROR;
	else {
		next_e=*(++p);
		return OK;
	}
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

Status ListDelete(SqList &L,int i,ElemType &e){
	ElemType *q,*p;
	p=L.elem+1;
	e=*p;
	q=L.elem+L.length-1;
	for(++p;p<=q;p++){
		*(p-1)=*p;
	}
	L.length--;
	return OK;
	
}

void ListTraverse(SqList L, void(*visit)(ElemType&))
{ 
  
  
  ElemType *p=L.elem; 
  for(int i=1; i<=L.length; i++) 
    visit(*p++); 
  printf("\n");
}

































