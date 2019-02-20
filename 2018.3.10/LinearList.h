//Linearlist  创建线性表的基础操作

#define LIST_INIT_SIZE 10
#define INCREMENT 2


typedef struct Sqlist{
	ElemType * elem;
	int length;
	int listsize;	
}Sqlist;


void InitList(Sqlist L){
	L.elem=(ElemType *)malloc(LIST_INIT_SIZE*sizeof(ElemType));
	L.length=0;
	L.listsize=LIST_INIT_SIZE;
}

void DestroyList(Sqlist L){
	free(L.elem);
	L.elem=NULL;
	L.length=0;
	L.listsize=0;
}

void ClearList(Sqlist L){
	L.length=0;
}

Status ListEmpty(Sqlist L){
	if (L.length==0) return TRUE;
	else return FALSE;
}

int ListLength(Sqlist L){
	return L.length;
}

Status GetElem(Sqlist L,int i){
	if (i<1 || i>L.length-1) return FALSE;
	ElemType e;
	e=L.elem[i-1];
	return e;
}

int LocateElem(Sqlist L,ElemType e,Status (* compare)(ElemType,ElemType)){
	ElemType * p=L.elem;
	for(int i=1;i<L.length ;i++){
		if (compare(*p++,e)) return i;
		i++;
	}
	return 0;
}

Status PriorElem(Sqlist L,ElemType cur_e,ElemType &pre_e){
	ElemType * p=L.elem+1;
	for(int i=2;i<L.length;i++,p++){
		if(cur_e==p[i-1]) return i-1;
	}
	return ERROR;
}

Status NextElem(Sqlist L,ElemType cur_e,ElemType &next_e){
	ElemType * p=L.elem+1;
	for(int i=1;i<L.length-1;i++,p++){
		if(cur_e==p[i-1]) return i-1;
	} 
	return ERROR;	
}

Status ListInsert(Sqlist L,int i,ElemType e){
	ElemType * newbase,* p,* q;
	if (i<1 || i>L.length) return ERROR;
	if (L.length==L.listsize){
		newbase=(ElemType *)realloc(L.elem,(L.listsize+INCREMENT)*sizeof(ElemType));
		if (!newbase)
		   exit(OVERFLOW);
		L.elem=newbase;
		L.listsize+=INCREMENT;
	}
	q=L.elem+i-1;
	for(p=L.elem+L.length-1;p>q;p--){
		*(p+1)=*p;
	}
	*q=e;
	L.length++;
	return OK;
}

Status ListDelete(Sqlist L,int i,ElemType &e){
	ElemType * p,* q;
	if (i<1 || i>L.length) return ERROR;
	p=L.elem+i-1;
	e=*p;

	
	for(q=L.elem+L.length-1;p<q;p++){
		*p=*(p+1);
	}
	L.length--;
	return OK;	
}

void ListTraverse(Sqlist L,void(* visit)(ElemType &)){
	
	
	ElemType * p=L.elem;
	int i;
	for (i=1;i<=L.length;i++){
		visit(* p++);
		printf("\n");
	}
}


