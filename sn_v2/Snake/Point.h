#ifndef POINT_H
#define POINT_H

struct Point {
	int row;
	int column;
	
	bool operator==(const Point& second) {
		return row == second.row && column == second.column;
	}
};

#endif // !POINT_H
