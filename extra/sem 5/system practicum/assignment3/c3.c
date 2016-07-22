#include <stdio.h>
/*#include <conio.h>*/
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}
void read(); 
void cpuusage();
int main(int argc,char* argv[]) {
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
 
   printf("File copied Successfully!\n");
   fclose(fp1);
   fp3 = fopen("Output.txt","r");
   printf("output is :\n");
   char c;
   while (1) {
      c = fgetc(fp3);
 
      if (c == EOF)
         break;
      else
        printf("%c",c );
   }
   fclose(fp2);
      fclose(fp3);
   read();
      return 0;
}
void read()
{
        FILE * file = fopen("Output.txt","r");
        char ch;
        char *c = (char *)malloc(100); 
        while(1)
        {
                ch = fgetc(file);
                c = fgets(c,100,file);
                if (ch == EOF)
               		{
                		printf("\n");
                	    break;
                    }
                else
                	printf("%s\n",c );
                        printf("%c",ch);
                        continue;
        }
          system("espeak -f Output.txt");

}
void cpuusage()
{
	FILE *cpuinfo = fopen("/proc/cpuinfo", "rb");
   char *arg = 0;
    char  **c = (char **)malloc(1000);
    int i=0;
   size_t size = 0;
   while(getdelim(&arg, &size, 0, cpuinfo) != -1)
   {
      c[i]  = (char* )(intptr_t) arg;
      // puts(arg);
      printf("%s\n",c[i]);

   }
   free(arg);

   fclose(cpuinfo);
}