

Status Equal(ElemType c1,ElemType c2){
	if (c1==c2) return TRUE;
	else return FALSE;
}

int Compare(ElemType b1,ElemType b2){
	if(b1==b2) return 0;
	else return (b1-b2)/abs(b1-b2);
}

void print(ElemType c){
	printf("%d",c);
}

void Print_int_1(ElemType &c){
	printf("%d",c);
}

void Print_char(ElemType c){
	printf("%c",c);
}

Status Sq(ElemType c1,ElemType c2){
	if (c1==c2*c2) return TRUE;
	else return FALSE;
}

void Dbl(ElemType * c){
	* c*=2;
}
