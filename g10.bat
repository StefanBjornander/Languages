@C:
@cd "C:\Users\stefa\Documents\A A C_Compiler_CSharp_10"
@rem echo "# CCompiler10" > README.md
@rem git init
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/CCompiler10.git
@git push -u origin master
@pause