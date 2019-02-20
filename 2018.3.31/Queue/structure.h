typedef int QElemType;

typedef struct QNode{
	QElemType data;
	QNode * next;
	
}QNode,* QueuePtr;

struct LinkQueue{
	QueuePtr front,rear;
};

