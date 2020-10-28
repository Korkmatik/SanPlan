echo Running Tests ...
CALL runTests.bat
if errorlevel 1 (
    echo Tests failed!
    exit /b %errorlevel%
)
echo Tests passed!

echo Running Coverage ...
CALL runCoverage.bat
if errorlevel 1 (
    echo Coverage failed!
    exit /b %errorlevel%
)
echo Coverage passed!

echo Running coding style checks ...
CALL runStyleChecks.bat
if errorlevel 1 (
    echo Coding Style Check failed!
    exit /b %errorlevel%
)
echo Coding Style passed!