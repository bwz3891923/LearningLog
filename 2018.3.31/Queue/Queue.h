//SqStack.h

void InitQueue(LinkQueue &Q){
	Q.front=Q.rear=(QueuePtr)malloc(sizeof(QNode));
	if(!Q.front && !Q.rear)
	   exit(OVERFLOW);
	Q.front->next=NULL;
	
}


void DestroyQueue(LinkQueue &Q){
	QueuePtr p;
	while(Q.front){
		p=Q.front;
		Q.front=Q.front->next;
		free(p);
	}
}

Status QueueEmpty(LinkQueue Q){
	if(Q.front==Q.rear)
	   return TRUE;
	else
	   return FALSE;
}

void ClearQueue(LinkQueue &Q){
	DestroyQueue(Q);
	InitQueue(Q);
}

int QueueLength(LinkQueue Q){
	int len=0;
	QueuePtr p=Q.front->next;
	while(p){
		len++;
		p=p->next;
	}
	return len;
}

Status GetHead(LinkQueue Q,QElemType &e){
	if(QueueEmpty(Q))
	   return ERROR;
	else
	   e=Q.front->next->data;
	   return OK;
}


void EnQueue(LinkQueue &Q,QElemType e){
	QueuePtr p=(QueuePtr)malloc(sizeof(QNode));
	if(!p)
	   exit(OVERFLOW);
	
	Q.rear->next=p;
	p->data=e;
	p->next=NULL;
	Q.rear=p;
}

Status DeQueue(LinkQueue &Q,QElemType &e){
	if(Q.front==Q.rear) return ERROR;
	
	QueuePtr p;
	p=Q.front->next;
	e=p->data;
	Q.front->next=p->next;
	free(p);
	return OK;
}


void QueueTraverse(LinkQueue Q,void (* visit)(QElemType)){
	QueuePtr p=Q.front->next;
	while(p){
		visit(p->data);
		p=p->next;

	}
	printf("\n");	
} 
