#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

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
    vector<int> B,C;
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