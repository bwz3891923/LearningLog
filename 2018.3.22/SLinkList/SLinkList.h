# define DestroyList ClearList


int Malloc(SLinkList space){
	int i=space[0].cur;
	if (i){
		space[0].cur=space[i].cur;
	}
	return i;
}

void Free(SLinkList space,int k){
	space[k].cur=space[0].cur;
	space[0].cur=k;
}


void InitList(SLinkList L){
	int i;
	L[MAX_SIZE-1].cur=0;
	for(i=0;i<MAX_SIZE-2;i++){
		L[i].cur=i+1;	
	}
	L[MAX_SIZE-2].cur=0;
}


Status ClearList(SLinkList L){
	int j,i=L[0].cur;
	while(i){
		j=i;
		i=L[i].cur;
	}
	L[j].cur=L[MAX_SIZE-1].cur;
	L[MAX_SIZE-1].cur=0;
	
}

Status ListEmpty(SLinkList L){
	if(L[MAX_SIZE-1].cur==0)
	   return TRUE;
	else
	   return FALSE;
}


int ListLength(SLinkList L){
	int i=0,p=L[MAX_SIZE-1].cur;
	while(p){
		p=L[p].cur;
		i++;
	}
	return i;	
}

Status GetElem(SLinkList L,int i, ElemType &e){
	int m,k=MAX_SIZE-1;
	if (i<1 || i>ListLength(L)) return ERROR;
	for (m=0;m<i;m++){
		k=L[k].cur;
	}
	e=L[k].data;
	
	return OK;
	
	
}

int LocateElem(SLinkList L,ElemType e){
	int i=0,k=MAX_SIZE-1;
	
	while(k){
		if(L[k].data==e)
		   return i;
		
		k=L[k].cur;
		i++; 	
	}
	return ERROR;
}

Status PriorElem(SLinkList L,ElemType cur_e,ElemType &pre_e){
	int m=0,k=MAX_SIZE-1;
	
	while(k){
		if(L[k].data==cur_e){
			pre_e=L[m].data;
			return OK;
		}
		
		m=k;
		k=L[k].cur;	
	}
	return ERROR;
}

Status NextElem(SLinkList L,ElemType cur_e,ElemType &next_e){
	int k=MAX_SIZE-1;
	
	while(k){
		if(L[k].data==cur_e){
			k=L[k].cur;
			next_e=L[k].data;
			return OK;
		}	
		k=L[k].cur;
	}
	return ERROR;
}

Status CreatList(SLinkList L,ElemType e){
	int m,p=MAX_SIZE-1;	
	m=Malloc(L);
	
	if(!L[p].cur){
		L[p].cur=1;
	}
	
	if(m){
		L[m].data=e;
		while(L[p].cur)
		   p=L[p].cur;
		L[p].cur=m;
		L[m].cur=0;
	}
	return ERROR;
		
}
Status ListInsert(SLinkList L,int i, ElemType e){
	int m,j,k=MAX_SIZE-1;
	if(i<1 || i>ListLength(L)+1)
	  return ERROR;
	
	j=Malloc(L);
	if(j)
	{
		L[j].data=e;
		for(m=1;m<i;m++)
		   k=L[k].cur;
		L[j].cur=L[k].cur;
		L[k].cur=j;
		
		return OK;
	}
	return ERROR;
	
}

void ListDelete(SLinkList L,int i,ElemType &e){
	int m,j,k=MAX_SIZE-1;
	for(j=0;j<i-1;j++){
		k=L[k].cur;
	}
	m=L[k].cur;
	e=L[m].data;
	L[k].cur=L[m].cur;
	Free(L,m);
	

}

void ListTraverse(SLinkList L,void (* visit)(ElemType)){
	int p=L[MAX_SIZE-1].cur;
	while(p){
		visit(L[p].data);
		p=L[p].cur; 
	}
	printf("\n");
}























