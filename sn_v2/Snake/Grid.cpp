#include "Grid.h"

Grid::Grid()
{
}

Grid::Grid(Point & start, Point & end)
{
	start_ = start;
	end_ = end;

	for (int i = 1; i <= end.row - start.row; i++) {
		border_.push_back(Point{ start.row + i, 1 });
		border_.push_back(Point{ start.row + i, end.column });
	}

	for (int i = 1; i <= end.column - start.column; i++) {
		border_.push_back(Point{ 1, start.column + i });
		border_.push_back(Point{ end.row, start.column + i });
	}
}

Point Grid::getCenter()
{
	return Point{ end_.row / 2, end_.column / 2 };
}

Point Grid::getStart()
{
	return start_;
}

Point Grid::getEnd()
{
	return end_;
}

bool Grid::isBorder(Point &p)
{
	return (find(border_.begin(), border_.end(), p) != border_.end());
}
