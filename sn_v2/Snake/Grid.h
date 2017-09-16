#ifndef GRID_H
#define GRID_H

#include <vector>
#include <algorithm>

#include "Point.h"

using namespace std;

class Grid {
public:
	Grid();
	Grid(Point &start, Point &end);
	
	Point getCenter();
	Point getStart();
	Point getEnd();

	bool isBorder(Point &p);

private:
	Point start_;
	Point end_;

	vector<Point> border_;
};

#endif // !GRID_H
