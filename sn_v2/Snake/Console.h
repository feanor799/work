#ifndef CONSOLE_H
#define CONSOLE_H

#define NOMINMAX
#define WIN32_LEAN_AND_MEAN
#include <Windows.h>
#include <iostream>
#include <iomanip>

void setCursorPosition(int x, int y);
void setConsoleColour(unsigned short colour);

#endif // !CONSOLE_H
