//LNode.h


void InitList(LinkList &L){
	L=(LinkList)malloc(sizeof(LNode));
	if(!L) exit(OVERFLOW);
	L->next=NULL;
	
}

void DestroyList(LinkList &L){
	LinkList q;
	while(L){
		q=L->next;
		free(L);
		L=q;
	}
}

void ClearList(LinkList &L){
	LinkList p;
	p=L->next;
	L->next=NULL;
	
	DestroyList(p);
	
}

int ListLength(LinkList L){
	LinkList p=L->next;
	int j=0;
	while(p){
		p=p->next;
		j++;
	}
	return j;
	
}

Status GetElem(LinkList &L,int i,ElemType &e){
	LinkList p=L->next;
	int j=1;
	while(p && j<i){
		p=p->next;
		j++;
	}
	if(!p || j>i){
		return ERROR;
	}
	e=p->data;
	return OK;
	
	
	
}

Status ListEmpty(LinkList L){
	if (L->next)
	  return FALSE;
	else
	  return TRUE;
}

int LocateElem(LinkList &L,ElemType e,Status(* compare)(ElemType,ElemType)){
	int i=1;
	LinkList p=L->next;
	while(p){
		if(compare(p->data,e))
		  return i;
		i++;
		p=p->next;
	}
	return 0;
}

Status PriorElem(LinkList L,ElemType cur_e,ElemType &pre_e){
	LinkList q,p=L->next;
	while(p && p->next){
		q=p->next;
		if(q->data==cur_e){
		   pre_e=p->data;
		   return OK;
		}
		p=q;
	}
	return ERROR;
}

Status NextElem(LinkList L,ElemType cur_e,ElemType &next_e){
	LinkList p=L->next;
	while(p && p->next){
		if(p->data==cur_e){
			next_e=p->next->data;
			return OK;
		}
		p=p->next;
	}
	return ERROR;
}

Status ListInsert(LinkList &L,int i,ElemType e){ 
	LinkList s,p=L;
	int j;
	while(p && j<i-1){
		j++;
		p=p->next;
	}
	if (!p || j>i-1 ) return ERROR;
	s=(LinkList)malloc(sizeof(LNode));
	s->data=e;
	s->next=p->next;
	p->next=s;
	
	return OK;
}

Status AddElemTail(LinkList &L,ElemType e){
	LinkList s,p=L;
	while(p->next){
		p=p->next;
	}
	s=(LinkList)malloc(sizeof(LNode));
	s->data=e;
	p->next=s;
	s->next=NULL;
}

Status AddElemHead(LinkList &L,ElemType e){
	LinkList s,p=L;
	s=(LinkList)malloc(sizeof(LNode));
	s->data=e;
	
	s->next=p->next;
	p->next=s;	
}

Status ListDelete(LinkList &L,int i,ElemType &e){
	LinkList p,q=L->next;
	int j=1;
	while(q && j<i ){
		j++;
		p=q;
		q=q->next;
	}
	if(!p || j>i) return ERROR;
	e=q->data;
	p->next=q->next;
	free(q);
	
	return OK;
	
	
	
	
	
	
}

void ListTraverse(LinkList L,void (* visit)(ElemType)){
	LinkList p=L->next;
	while(p){
		visit(p->data);
		p=p->next;
	}
	printf("\n");
}
