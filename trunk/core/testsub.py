import submit

def main():
    problem='4104'
    userid='17642OV'
    language='C'
    code='''
        
#include <stdio.h>

int main(){
    int cas;
    int x,y,n,r;
    scanf("%d",&cas);
    while (cas--){
        scanf("%d%d%d",&x,&y,&n);
        r=1;
        while (y){
            if (y&1) r=(r*x)%n;
            x=(x*x)%n;
            y/=2;
        }
        printf("%d\n",r);
    }
    return 0;
}

    '''
    submit.UVA_Submit(problem,userid,language,code);
    return 0

if __name__=='__main__':main()
