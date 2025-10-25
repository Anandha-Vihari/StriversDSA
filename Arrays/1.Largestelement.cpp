#include <bits/stdc++.h>
using namespace std;

int LargestNumber (int arr[],int n){
    int max=arr[0];
    for(int i=0;i<n;i++){
        if(max < arr[i]){
            max=arr[i];
        }
    }
    return max;
}





int main() {
    int arr1[]={1,2,3,5,6,9,10,1,4};
    int n=9;
    int max=LargestNumber(arr1,n);
    cout<<max<<'\n';
    return 0;
}