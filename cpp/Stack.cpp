#include <iostream>
#include <stdlib.h>
#include <conio.h>
using namespace std;
#define Max 5

class Stack
{
    private:
        int top;
        int arr[Max];
    public:
        Stack();
        void pop();
        void push(int input);
        void ls();
};

Stack::Stack(){
    top = 0;
    for(int i = 0;i < Max;i++){
        arr[i] = 0;
    }
}

void Stack::pop(){
    if(top <= 0)
        cout << "Empty" << endl;
    else{
        cout << "pop " << arr[top--] << " from stack" << endl;
    }
}

void Stack::push(int input){
    if(top >= Max-1)
        cout << "Full" << endl;
    else{
        arr[top++] = input;
    }
}

void Stack::ls(){
    for(int i = Max-1;i >= 0;i--){
        cout << i << " : " << arr[i] << endl;
    }
}

int main(){
    Stack stk;
    stk.ls();
    stk.pop();
    stk.pop();

    stk.push(10);
    stk.pop();
    stk.push(10);
    stk.push(10);

    stk.ls();
    return 0;
}
