@echo off
title Pac-Man Search Algorithms - Group_AI_28
color 0A
cd /d "%~dp0Group_Project\search"

:MENU
cls
echo =====================================================================
echo           SE3062 / IT3012 - INTELLIGENT SYSTEMS (PAC-MAN)
echo                       GROUP: Group_AI_28
echo =====================================================================
echo.
echo   [1] Play Pac-Man Manually (Arrow Keys)
echo   [2] Q1: Depth First Search (DFS) on mediumMaze
echo   [3] Q2: Breadth First Search (BFS) on mediumMaze
echo   [4] Q3: Uniform Cost Search (UCS) on mediumMaze
echo   [5] Q4: A* Search with Manhattan Heuristic on bigMaze
echo   [6] Q5 & Q6: Corners Problem with A* on mediumCorners
echo   [7] Q7: Food Search with A* (Farthest Dot) on trickySearch
echo   [8] Run Full Autograder (Score 40/40 Verification)
echo   [0] Exit
echo.
echo =====================================================================
set /p choice="Enter your choice [0-8]: "

if "%choice%"=="1" (
    cls
    echo Starting Manual Pac-Man (Use Arrow Keys to move)...
    python pacman.py
    pause
    goto MENU
)
if "%choice%"=="2" (
    cls
    echo Running Q1: Depth First Search (DFS)...
    python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
    pause
    goto MENU
)
if "%choice%"=="3" (
    cls
    echo Running Q2: Breadth First Search (BFS)...
    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
    pause
    goto MENU
)
if "%choice%"=="4" (
    cls
    echo Running Q3: Uniform Cost Search (UCS)...
    python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
    pause
    goto MENU
)
if "%choice%"=="5" (
    cls
    echo Running Q4: A* Search on bigMaze...
    python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    pause
    goto MENU
)
if "%choice%"=="6" (
    cls
    echo Running Q5 & Q6: Corners Problem with A*...
    python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
    pause
    goto MENU
)
if "%choice%"=="7" (
    cls
    echo Running Q7: Food Search with A* (Eating All Dots)...
    python pacman.py -l trickySearch -p AStarFoodSearchAgent
    pause
    goto MENU
)
if "%choice%"=="8" (
    cls
    echo Running Autograder...
    python autograder.py
    pause
    goto MENU
)
if "%choice%"=="0" exit
goto MENU
