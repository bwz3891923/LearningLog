//Circle_LNode

void InitList(LinkList &L){
	L=(LinkList)malloc(sizeof(LNode));
	if(!L)
	   exit(OVERFLOW);
	L->next=L;
}

int ListLength(LinkList L){
	int len=0;
	LinkList p=L->next;
	while(p!=L){
		p=p->next;
		len++;
	}
	return len;
}


Status ListInsert(LinkList &L,int i,ElemType e){
	int j=0;
	LinkList s,p=L->next;
	if(i<0 || i>ListLength(L)+1)
	   return ERROR;
	
	s=(LinkList)malloc(sizeof(LNode));
	if(!s)
	   exit(OVERFLOW);
	
	while(j<i-1){
		p=p->next;
		j++;
	}
	s->data=e;
	s->next=p->next;
	p->next=s;
	return OK;
}

void ListTraverse(LinkList L,void (* visit)(ElemType)){
	LinkList p=L->next;
	while(p!=L){
		visit(p->data);
		p=p->next;
	}
	printf("\n");
}


