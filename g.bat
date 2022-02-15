@rem git init
@rem git config --global user.email "stefan.bjornanderoutlook.com"
@rem git config --global user.name "Stefan Bjornander"

@C:
@cd "C:\Users\stefa\Documents\A A C_Compiler_CSharp_8"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/CCompiler8.git
@git push origin master

@cd "C:\Users\stefa\Documents\A A C_Compiler_CSharp_10"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/CCompiler10.git
@git push origin master

@cd "C:\Users\stefa\Documents\A A C_Compiler_Assembler - CSharp 0 Assembly"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/CCompiler_Assembly.git
@git push origin master

@cd "C:\Users\stefa\Documents\vagrant\homestead\code"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/Code.git
@git push origin master

@cd "C:\Users\Stefa\Documents\GenerateAssembly"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/GenerateAssembly.git
@git push origin master

@cd "C:\Users\stefa\Documents\ObjectCodeTableGeneratorCSharp"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/ObjectCodeTableGeneratorCSharp.git
@git push origin master

@cd "C:\Users\stefa\Documents\ObjectCodeTableGeneratorJava"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/ObjectCodeTableGeneratorJava.git
@git push origin master

@cd "C:\Users\stefa\Documents\Languages"
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/Languages.git
@git push origin master

@cd "C:\Users\stefa\Documents\Check"
@git init
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/Check.git
@git push origin master

@cd "C:\Users\stefa\Documents\Books"
@git init
@git add .
@git commit -m "Backup"
@git branch -M master
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/Books.git
@git push origin master
@pause
