#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<assert.h>
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

int main(){
  int T, G, I, N, Q, res;

  assert( scanf("%d",&T)==1 );
  assert( 0 <= T && T <= 10 );
  while(T--){
    assert( scanf("%d",&G)==1 );
    assert( 1<=G && G<=20000 );
    while(G--){
      assert( scanf("%d%d%d",&I,&N,&Q)==3 );
      assert( I==1 || I==2 );
      assert( N <= 1000000000 );
      assert( Q==1 || Q==2 );
      
      res = N / 2;
      if(N%2 && I!=Q) res++;
      printf("%d\n",res);
    }
  }

  return 0;
}