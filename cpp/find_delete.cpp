#include <iostream>
#include <stdlib.h>
#include <conio.h>
#include <cstring>
#include <cstdio>
using namespace std;

struct node{
    int data;
    struct node* next;
};

class SLKLS{
    private:
        struct node* head;

        struct node* cur;
        struct node* pre;

    public:
        SLKLS();
        void display_f(void);
        void insert_f(int);

        void delete_f(int);
//        void modify_f(int, int);

};

SLKLS::SLKLS(){
    head = new struct node();
    head->next = NULL;

    cur = new struct node();
    pre = new struct node();
}
//
void SLKLS::delete_f(int num){
    pre=head;
    cur=head->next;
    while(cur != NULL && cur->data != num){
        pre=cur;
        cur=cur->next;
    }
    if (cur != NULL) { /* Delete the current node */
        pre->next=cur->next;
        cout << num << "deleted\n";
        free(cur);
    }
    else
        cout << num << "the data is not found\n";
}

//void SLKLS::modify_f(int old_num, int new_num){
//
//}

void SLKLS::insert_f(int input){
    struct node* new_node;
    new_node = new struct node();
    new_node->next = NULL;
    new_node->data = input;

    pre = head;
    cur = head->next;

    while(cur != NULL && cur->data > new_node->data)
    {
        pre=cur;
        cur=cur->next;
    }

    new_node->next = cur;
    pre->next = new_node;
}

void SLKLS::display_f(){
    int cnt = 0;
    if(head->next==NULL){
        cout << "No record" << endl;
    }
    else{

        for(cur = head->next; cur != NULL; cur = cur->next){
            cout << cnt++ << " : " << cur->data << endl;
        }
    }
    cout << endl;
}

int main(){
    SLKLS obj;
    obj.display_f();
    obj.insert_f(20);
    obj.insert_f(50);
    obj.insert_f(30);
    obj.insert_f(80);
    obj.insert_f(40);
    obj.display_f();

    obj.delete_f(22);
    obj.delete_f(30);
    obj.delete_f(40);
    obj.display_f();

    return 0;
}
