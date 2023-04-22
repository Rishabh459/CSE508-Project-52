// a cli interface to take n as input and then 1(relevant doc) and 0(irrelevant doc) for each doc and calculate the precision @ n

#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin>>n;
    float p;
    float sum=0;
    int k =n;
    while(n--){
        cin>>p;
        sum+=p;
    }
    cout<<(sum/k);
}