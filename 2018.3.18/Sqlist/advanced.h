//针对多个链表的操作

void Union(SqList &La,SqList Lb){
	ElemType *p=Lb.elem;
	ElemType e;
	int len_a=ListLength(La);
	int len_b=ListLength(Lb);
	
	
	for(int i=1;i<=len_b;i++){
		GetElem(Lb,i,e);
		if (!LocateElem(La,e,equal))
		   ListInsert(La,++len_a,e);	   
	}

} 

