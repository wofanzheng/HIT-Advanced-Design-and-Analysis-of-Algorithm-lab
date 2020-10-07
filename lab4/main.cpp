#pragma comment(linker,"/STACK:1024000000,1024000000")
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn=3e5+5e4;
//const int maxn=30;

void QuickSort(int i, int j,vector<int> &A);
int Partition(int i,int j,int pivort,vector<int> &A);
int FindPivort(int i,int j,vector<int> &A);
void Quick_Sort_3_Way(vector<int> &A, int left, int right);

int cmp(const void *a,const void *b)
{
    return *(int *)a-*(int *)b;//这是从小到大排序，若是从大到小改成： return *(int *)b-*(int *)a;
}

int main()
{
    vector< vector<int> > A;
    clock_t start,endn;
    //生成数据
    for(int i=1;i<=11;i++)
    {
        vector<int> temp;
        int num1=maxn*(1-i*0.01);
        int num2=maxn-num1;
        for(int j=0;j<num1;j++)
        {
            temp.push_back(j);
        }
        for(int j=0;j<num2;j++)
        {
            temp.push_back(num1+1);
        }
        std::random_shuffle(temp.begin(),temp.end());
        A.push_back(temp);
    }
    /* 
    for(int i=0;i<11;i++)
    {
        
        cout<<"dataset"<<i+1<<":";
        for(int j=0;j<maxn;j++)
        {
            cout<<A[i][j]<<" ";
        }
        cout<<endl;
    } */
    cout<<"Radom quick sort:"<<endl; 
    for(int i=0;i<11;i++)
    {
        
        /*for(int j=0;j<maxn;j++)
        {
            cout<<A[i][j]<<" ";
        }
        cout<<endl;*/
        start = clock();
        QuickSort(0,maxn-1,A[i]);
        //cout<<"OK"<<endl;
        endn = clock();
        double duration = (double)(endn - start) / CLOCKS_PER_SEC;
        /*for(int j=0;j<maxn;j++)
        {
            cout<<A[i][j]<<" ";
        }*/
        cout<<i<<": "<<duration<<"s"<<endl;
    }
    //生成数据
    A.clear();
    for(int i=1;i<=11;i++)
    {
        vector<int> temp;
        int num1=maxn*(1-i*0.01);
        int num2=maxn-num1;
        for(int j=0;j<num1;j++)
        {
            temp.push_back(j);
        }
        for(int j=0;j<num2;j++)
        {
            temp.push_back(num1+1);
        }
        std::random_shuffle(temp.begin(),temp.end());
        A.push_back(temp);
    }
    cout<<"c++ qsort():"<<endl;
    for(int i=0;i<11;i++)
    {
        start = clock();
        int arr[A[i].size()];
        std::copy(A[i].begin(), A[i].end(), arr);
        start = clock();
        qsort(arr,A[i].size(),sizeof(int),cmp);
        //cout<<"OK"<<endl;
        endn = clock();
        double duration = (double)(endn - start) / CLOCKS_PER_SEC;
        /*for(int j=0;j<maxn;j++)
        {
            cout<<arr[j]<<" ";
        }*/
        cout<<i<<": "<<duration<<"s"<<endl;
    }
    //生成数据
    A.clear();
    for(int i=1;i<=11;i++)
    {
        vector<int> temp;
        int num1=maxn*(1-i*0.01);
        int num2=maxn-num1;
        for(int j=0;j<num1;j++)
        {
            temp.push_back(j);
        }
        for(int j=0;j<num2;j++)
        {
            temp.push_back(num1+1);
        }
        std::random_shuffle(temp.begin(),temp.end());
        A.push_back(temp);
    }
    cout<<"Quick_Sort_3_Way:"<<endl; 
    for(int i=0;i<11;i++)
    {
        /*
        for(int j=0;j<maxn;j++)
        {
            cout<<A[i][j]<<" ";
        }*/
        //cout<<endl;
        start = clock();
        Quick_Sort_3_Way(A[i],0,maxn-1);
        //cout<<"OK"<<endl;
        endn = clock();
        double duration = (double)(endn - start) / CLOCKS_PER_SEC;
        /*for(int j=0;j<maxn;j++)
        {
            cout<<A[i][j]<<" ";
        }*/
        cout<<i<<": "<<duration<<"s"<<endl;
    }
    getchar();
    return 0;
}

int FindPivort(int i,int j,vector<int> &A)
{
    if(i>j)
        return -1;
    return rand()%(j-i+1)+i;
}

int Partition(int i,int j,int pivort,vector<int> &A)
{
    int l=i,r=j;
    while(1){
        while(A[r] >= pivort&&r>l)
            r--;
        if(l<r)
        {
            A[l]=A[r];
        }
        /*for(int i=0;i<maxn;i++)
            printf("%d ",A[i]);
        printf("\n");
        printf("%d %d\n",l,r);*/
        while(A[l]<pivort&&r>l)
            l++;
        if(l<r)
        {
            A[r]=A[l];
        }
        /*for(int i=0;i<maxn;i++)
            printf("%d ",A[i]);
        printf("\n");
        printf("%d %d\n",l,r);*/
        if(r<=l)
            break;
    }
    A[l]=pivort;
    return l;
}

void QuickSort(int i, int j,vector<int> &A)
{
    int pivort;
    int k;
    int pivortindex;
    pivortindex=FindPivort(i,j,A);
    if(pivortindex!=-1&&i<j)
    {
        if(pivortindex!=i)
            swap(A[i],A[pivortindex]);
        pivort = A[i];
        k=Partition(i,j,pivort,A);
        QuickSort(i,k-1,A);
        QuickSort(k+1,j,A);
    }
}

void Quick_Sort_3_Way(vector<int> &A, int left, int right)
{
    if (left < right)
    {
        int pivortindex;
        pivortindex=FindPivort(left,right,A);
        int l = left - 1;
        int j = left;
        int r = right;
        if(pivortindex!=right)
            swap(A[right],A[pivortindex]);
        int pivot = A[right];
        /*
        [left, l] 小于主元
        [l+1, j] 等于主元
        [j+1, right] 大于主元
        */

        while (j < r)
        {
            if (A[j] < pivot)
            {
                swap(A[j], A[++l]);
                j++;
            }
            else if (A[j] > pivot)
                swap(A[j], A[--r]);
            else    j++;
        }
        swap(A[j], A[right]);
        Quick_Sort_3_Way(A, left, l);
        Quick_Sort_3_Way(A, j+1, right);
    }
}