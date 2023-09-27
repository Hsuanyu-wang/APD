#include <iostream>
#include <stdlib.h>
#include <conio.h>
using namespace std;

class Test
{
    private:
        int a[5];

    public:
//        int b;
        Test();
//        void show();
        void get_sum();
};

Test::Test(){
    for(int i = 0; i < 5 ;i++){
        a[i] = i;
    }
}

//void Test::show(){
//    cout << a << endl;
//}

void Test::get_sum(){
    int sum = 0;
    for(int i = 0;i < n;i++){
        sum += a[i];
    }
    cout << sum << endl;
}

int main(){
    Test obj;
    obj.get_sum();

    return 0;
}
