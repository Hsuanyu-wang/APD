#include <iostream>
#include <stdlib.h>
#include <conio.h>
using namespace std;
#define Max 5
#define Full 1
#define Empty 0

class Queue
{
    private:
        bool tag;
        int rear;
        int cur;
        int arr[Max];
    public:
        Queue();
        void dequeue();
        void enqueue(int);
        void ls();
};

Queue::Queue(){
    tag = Empty;
    cur = rear = Max-1;
    for(int i = 0;i < Max;i++){
        arr[i] = 0;
    }
}

void Queue::dequeue(){
    if(cur == rear && tag == Empty)
        cout << "Queue is empty\n";
    else{
        cur = (cur+1)%Max;
        cout << arr[cur] << "deleted\n";
        if(cur == rear)
            tag = Empty;
    }
}

void Queue::enqueue(int input){
    if(cur == rear && tag == Full){
        cout << "Full" << endl;
    }
    else{
        rear = (rear+1)%Max;
//        cout << "enter element" << endl;
        arr[rear] = input;
        if(cur == rear)
            tag = Full;
    }
}
//
void Queue::ls(){
    int i;
    if(cur == rear && tag == Empty)
        cout << "Empty\n";
    else{
        for(i = (cur+1)%Max; i != rear; i = (i+1)%Max){
            cout << arr[i] << endl;
        }
        cout << arr[i] << endl;
    }
    cout << "front:" << cur << "    rear:" << rear << endl;
}

int main(){
    Queue que;

    que.ls();
    que.dequeue();
    que.dequeue();
    que.enqueue(3);
    que.enqueue(4);
    que.enqueue(5);
    que.enqueue(6);
    que.enqueue(7);
    que.enqueue(8);
    que.ls();
    que.dequeue();
    que.dequeue();
    que.dequeue();
    que.ls();
    que.enqueue(9);
    que.enqueue(10);
    que.enqueue(11);
    que.ls();

    return 0;
}
