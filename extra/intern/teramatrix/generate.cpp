#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    float vhigh = 14.50;
    float vlow = 9.00;
    float ahigh = 2.50;
    float alow = 0.00;
    float hhigh = 400.00;
    float hlow = 300.00;
    float dhigh = 123.00;
    float dlow = 92.00;
    float opvolts = 13.00;
    float op =0.0;

    ofstream file("output.txt");
    while(vlow!=vhigh)
    {
        while(alow!=ahigh)
        {
            while(hlow!=hhigh)
            {
                while(dlow!=dhigh)
                {
                    while(op!=opvolts)
                    {
                        file << "500000"<< ",";
                        file <<vlow << ","<<alow<< ","<<hlow<< ","<<dlow<< ","<<op ;
                        op+=0.01;
                    }
                    dlow+=0.01;
                }
                hlow+=0.01;
            }
            alow+=0.01;
        }
        vlow+=0.01;
    }
    cout << "Successfull"<<endl;
}
