rem git init
rem git config --global user.email "stefan.bjornanderoutlook.com"
rem git config --global user.name "Stefan Bjornander"

c:
cd "C:\Users\stefa\Documents\A A C_Compiler_CSharp_8"
git add .
git commit -m "Backup"
git remote remove origin
git remote add origin https://github.com/StefanBjornander/CCompilerX.git
git push origin master
pause
