// ConsoleApplication1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include "stdio.h"
#include <iostream>
#include <conio.h>
#include <math.h>
using namespace std;

int main()
{
	double eps = 0.001; /*10^-5*/   /*10^-7*/
	double x,z,w;   /*аргумент для всех функций*/
	double n = 1,y = 0, y0 = 1; /*расчет у*/
	double x0 = -0.787;
	double h = 0.157;
	cout.width(30);
	cout << "_________________________________________________________";
	cout << "\n";
	cout << "|______x______|______y______|______z______|______w______|";
	cout << "\n";
	x = x0;
	while (x < 0.759)
	{
		cout << "|    ";
		cout << x;
		cout << "    |";
		cout << "   ";
		while (y0>eps)
		{
			y0 = pow(x, n);
			y = y + y0;
		}
		cout << y;
		cout << "   |";
		cout << "  ";
		z = sin(2*x);
		cout << z;
		cout << "    |";
		w = y - z;
		cout << w;
		cout << "   |";
		cout << "\n"; /*переход на новую строку*/


		x = x + h;
	}
	cin >> n;
    return 0;
}

