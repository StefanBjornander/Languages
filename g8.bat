@C:
@cd "C:\Users\stefa\Documents\A A C_Compiler_CSharp_8"
@rem echo "# CCompiler8" > README.md
@rem git init
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/CCompiler8.git
@git push -u origin master
@pause
