/*Non-LNode*/  

void InitList(LinkList &L){
	L=NULL;	
}

Status CreatListHead(LinkList &L,ElemType e){
	LinkList q,p;
	p=(LinkList)malloc(sizeof(LNode));
	q=L;
	if(p){
		
		p->data=e;
		p->next=q;
		L=p;
		return OK;
	}
	else
	   exit(OVERFLOW);
}

Status ListEmpty(LinkList L){
	if(L)
	   return TRUE;
	else
	   return FALSE;
}

int ListLength(LinkList &L){
	LinkList p=L;
	int len=0;
	while(p){
		len++;
		p=p->next;
	}
	return len;
}

Status GetElem(LinkList L,int i,ElemType &e){
	LinkList p=L;
	int j=1;
	
	while(p && j<i){
		p=p->next;
		j++;
	}
	if(j==i && p){
		e=p->data;
		return OK;
	}
	return ERROR;
}

int LocateElem(LinkList L,ElemType e,Status (* compare)(ElemType,ElemType)){
	LinkList p=L;
	int i=1;
	while(p){
		if(compare(p->data,e))
		  return i;
		else
		   p=p->next;
		   i++;
	}
	return ERROR;
}


Status ListInsert(LinkList &L,int i,ElemType e){
	LinkList s,p=L;
	int j=1;
	s=(LinkList)malloc(sizeof(LNode));
	s->data=e;
	
	if(i==1){
		s->next=L;
		L=s;
	}
		
	else{
		while(p && j<i){
			j++;
			p=p->next;
		}
		if(!p)
		   return ERROR;
		
		s->next=p->next;
		p->next=s;
		return OK;
	}	
}

Status ListDelete(LinkList &L,int i,ElemType &e){
	int j=1;
	LinkList s,p=L;
	if(i==1){
		L=p->next;
		e=p->data;
		free(p);
		
	}
	
	else{
		while(p && j<i){
			s=p;
			p=p->next;
			j++;
		}
		if(!p && j>i)
		   return ERROR;
		
		s->next=p->next;
		e=p->data;
		free(p);
		return OK;
		
	}

}


void ListTraverse(LinkList L,void (* visit)(ElemType)){
	LinkList p=L;
	while(p){
		visit(p->data);
		p=p->next;
	}
	printf("\n");
}










