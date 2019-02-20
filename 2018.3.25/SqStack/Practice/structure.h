#define STACK_INIT_SIZE 10
#define STACK_INCREMENT 2
typedef int SElemType;


typedef struct{
	SElemType * base;
	SElemType * top;
	int stacksize;
	
}SqStack;
