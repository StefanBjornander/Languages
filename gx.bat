cd "C:\Users\Stefa\Documents\vagrant\homestead\code\code"
git add .
git commit -m "Backup"
git remote remove origin
git remote add origin https://github.com/StefanBjornander/Code.git
git branch -M master
git push origin master
pause
