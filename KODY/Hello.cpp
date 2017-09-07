/*
 * Hello.cpp
 * 
 */


#include <iostream>

using namespace std;

#define ROK_TERAZ 2017
#define ROK_CPP 1983

int parzysta(int n)
{
    int i = 0;
    for(i=0; i<=n; i+=2)
        cout << i << " ";
    return i / 2;
}
int main(int argc, char **argv)
{   
    char imie[20];
    int a = 0;
    int rok_urodzenia;
    
    cout << "imie?" << endl;
    cin.getline(imie, 20);
	cout << "hello" << imie << endl;
    cout << "Ile masz lat? ";
    cin >> a;
    rok_urodzenia = ROK_TERAZ - a;
    cout << "Urodziłeś się w: " << rok_urodzenia << endl;
    if(ROK_CPP < rok_urodzenia)
       cout << "Jestem starszy" << endl;
    else if(ROK_CPP  > rok_urodzenia)
        cout << "Jestem młodszy";
       
    int n;
    cout << "Podaj liczbę naturalną: ";
    cin >> n;
    cout << "Ilość parzystych: " << parzysta(n);
    
	return 0;
}

