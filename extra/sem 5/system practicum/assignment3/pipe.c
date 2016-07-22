#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
 #define USE_PORTAUDIO
#include <sys/types.h>
#define N 1000000
void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}
char * mapping();
char** cpuusage();
char* copy();
char* readfile();
int main()
{
       int     fd1[2],fd2[2],fd3[2],fd4[2],fd5[2], nbytes[10];
        pid_t   pid;
        char    buf1[N];
        char    buf2[N];
        char    buf3[N];
        char    buf5[N];
        char    buf4[N];


        pipe(fd1);
        pipe(fd2);
        pipe(fd3);
        pipe(fd4);
        pipe(fd5);
        if((pid = fork()) == -1)
        {
                perror("fork");
                exit(1);
        }
        if(pid == 0)
        {
               char* s1 = mapping();
              write(fd1[1], s1, (strlen(s1)+1));
              char* s2 = readfile();
                write(fd2[1], s2, (strlen(s2)+1));
                char* s3  = copy();
                write(fd3[1], s3, (strlen(s3)+1));   
              char ** s4 = cpuusage();
                write(fd4[1], *s4, (strlen(*s4)+1));
                write(fd5[1], *(s4) + 1, (strlen(*(s4)+1)+1)); 
                exit(0);
        }
        else
        {
                /* Parent process closes up output side of pipe 
                close(fd[1]);*/

                /* Read in a s from the pipe */
                 nbytes[0] = read(fd1[0], buf1, sizeof(buf1));
                printf("From Child C1 :  Received Input (User).... %s\n", buf1);
                sleep (5);
                 nbytes[2] = read(fd2[0], buf2, sizeof(buf2));
                printf("From Child C2 : Received File Input......\n %s\n", buf2);
                system("espeak -f Output.txt");
                sleep(5);
                 nbytes[1] = read(fd3[0], buf3, sizeof(buf3));
                printf("From Child C3 Received Copied File Input..... \n%s\n", buf3);
                sleep(5);
                nbytes[3] = read(fd4[0], buf4, sizeof(buf4));
                nbytes[4] = read(fd5[0], buf5, sizeof(buf5));
                printf("From Child C4 : Received CPU Usage.........\n %s%s\n", buf4, buf5);
        }
        return(0);
}
char* copy()
{
         FILE *fp1, *fp2,*fp3;
   char ch;
  /* clrscr();*/
 
   fp1 = fopen("sample.txt", "r");
   fp2 = fopen("Output.txt", "w");
 
   while (1) {
      ch = fgetc(fp1);
 
      if (ch == EOF)
         break;
      else
         putc(ch, fp2);
   }
 
   /*printf("File copied Successfully!\n");*/
   fclose(fp1);
   fclose(fp2);
    char *c= malloc(N) ;
         int i=0;
   fp3 = fopen("Output.txt","r");
  /* printf("output is :\n");*/
    while(1)
        {
                ch = fgetc(fp3);
                if (ch == EOF)
                        {
                         /*printf("Successfully read from copied file!\n"); */
                                return c;
                        }
                else
                      { 
                       c[i] = ch;
                                                     /*printf("%c",ch);*/

                          i++;
                          continue;
                     }      
        }
}
char* readfile()
{
        FILE * file = fopen("Output.txt","r");
        char ch;
         char *c = malloc(N)  ;
         int i=0;
        while(1)
        {
                ch = fgetc(file);
                if (ch == EOF)
                        {
                        /* printf("Successfully read!\n"); */
                                /*system("espeak -f Output.txt");*/
                                return c;
                        }
                else
                      { 
                       c[i] = ch;
                                                     /*printf("%c",ch);*/

                          i++;
                          continue;
                     }      
        }
       
        return 0;
       

}
char **cpuusage()
{
      FILE *cpuinfo = fopen("/proc/cpuinfo", "rb");
   char *arg = 0;
    char  **c = (char **)malloc(N);
    int i=0;
   size_t size = 0;
   while(getdelim(&arg, &size, 0, cpuinfo) != -1)
   {
      c[i]  = (char* )(intptr_t) arg;
      // puts(arg);
      //printf("%s\n",c[i]);

   }
   free(arg);
   return c;
}
char * mapping()
{
        printf("Input For Child C1 = ");
        char * s = malloc(N);
        scanf("%[^\n]",s);
        int m=strlen(s);
        while(m>0){
                s[m-1]=s[m-1]+3;
                m--;       
        }
        return s;
}