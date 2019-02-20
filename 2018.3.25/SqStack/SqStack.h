

void InitStack(SqStack &S){
	S.base=(SElemType *)malloc(STACK_INIT_SIZE*sizeof(SElemType));
	if(!S.base)
	   exit(OVERFLOW);
	   
	S.top=S.base;
	S.stacksize=STACK_INIT_SIZE;
}

Status Push(SqStack &S,ElemType e){
	if(S.top-S.base>=S.stacksize){
		S.base=(SElemType *)realloc(S.base,(S.stacksize+STACK_INCREMENT)*sizeof(SElemType));
		if(!S.base) exit(OVERFLOW);
		S.top=S.base+S.stacksize;
		S.stacksize+=STACK_INCREMENT;
		
	}
	*(S.top)++=e;
}

Status Pop(SqStack &S,SElemType &e){
	if(S.base==S.top) return ERROR;
	e=*--(S.top);
	return OK;
}

void DestroyStack(SqStack &S){
	free(S.base);
	S.top=S.base=NULL;
	S.stacksize=0;
}

void ClearStack(SqStack &S){
	S.top=S.base;
} 

Status StackEmpty(SqStack &S){
	if(S.base==S.top)
	   return TRUE;
	else
	   return FALSE;
}

int StackLength(SqStack S){
	return S.top-S.base;
}

Status GetTop(SqStack S,SElemType &e){
	if(S.top>S.base){
		e=*(S.top-1);
		return OK;
	}
	else
	   return ERROR;
}


void StackTraverse(SqStack S,void (* visit)(ElemType)){
	SElemType * p=S.base;
	while(p<S.top)
		visit(*p++);	
	printf("\n");
	
}
