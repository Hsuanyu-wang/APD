#include <iostream>
#include <stdlib.h>
#include <conio.h>
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

//        void delete_f();
//        void modify_f(int, int);

};

SLKLS::SLKLS(){
    head = new struct node();
    head->next = NULL;

//    cur = new struct node();
//    pre = new struct node();
//    cur = head;
//    pre = head->next;

}

//void SLKLS::delete_f(){
//
//}

//void SLKLS::modify_f(int old_num, int new_num){
//
//}

//tail
void SLKLS::insert_f(int input){
    struct node* new_node;
    new_node = new struct node();
    new_node->next = NULL;
    new_node->data = input;

    cur = new struct node();
    for(cur = head; cur->next != NULL; cur = cur->next);
//    current != NULL && current->data > ptr->data
    cur->next = new_node;

}

void SLKLS::display_f(){
    struct node *cur;
    cur = new struct node();

    if(head->next==NULL){
        cout << "No record" << endl;

    }
    else{
        int cnt = 0;
        for(cur = head->next; cur != NULL; cur = cur->next){
            cout << cnt << " : " << cur->data << endl;
            cnt++;
        }
    }
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
    return 0;
}
