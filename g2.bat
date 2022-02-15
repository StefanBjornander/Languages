@rem git init
@rem git config --global user.email "stefan.bjornanderoutlook.com"
@rem git config --global user.name "Stefan Bjornander"

@c:
@cd "C:\Users\stefa\Documents\A A C_Compiler_CSharp_10"
@git add C_Compiler_CSharp_10
@git add Calculator_CS_10
@git add C_Compiler_CSharp_10.sln
@git commit -m "Backup"
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/CCompiler.git
@git push origin master
@rem pause

@cd "C:\Users\Stefa\Documents\A A A C_Compiler_Assembler - CSharp 0 Assembly"
@git add C_Compiler_CSharp_Assembly
@git commit -m "Backup"
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/CCompiler_Assembly.git
@git push origin master
@rem pause

@cd "C:\Users\Stefa\Documents\vagrant\homestead\code"
@git add Test.result
@git add code
@git add code_old
@git add code_very_old
@git add objectivec
@git add smalltalk-3.2
@git add lua
@git add haskell
@git add scala
@git commit -m "Backup"
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/Code.git
@git push origin master
@rem pause

@cd "C:\Users\Stefa\Documents\GenerateAssembler"
@git add GenerateAssembler
@git add build
@git add nbproject
@git add src
@git add build.xml
@git add manifest.mf
@git commit -m "Backup"
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/GenerateAssembler.git
@git push origin master
@rem pause

@cd "C:\Users\stefa\Documents\ObjectCodeTableGeneratorCSharp"
@git add nbproject
@git add src
@git add test
@git add build
@git add build.xml
@git add manifest.mf
@git commit -m "Backup"
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/ObjectCodeTableGeneratorCSharp.git
@git push origin master
@rem pause

@cd "C:\Users\stefa\Documents\ObjectCodeTableGeneratorJava"
@git add nbproject
@git add src
@git add test
@rem git add build
@git add build.xml
@git add manifest.mf
@git commit -m "Backup"
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/ObjectCodeTableGeneratorJava.git
@git push origin master
@rem pause

@cd "C:\Users\stefa\Documents\Languages"
@git add CPlusPlus
@git add CSharp
@git add Dart
@git add Elixir
@git add Erlang
@git add Go
@git add Haskell
@git add Java
@git add Julia
@git add Kotlin
@git add Python
@git add Ruby
@git add Rust
@git add Scala
@git add Swift
@git add V
@git add g.bat
@git add languages.txt
@git commit -m "Backup"
@git remote remove origin
@git remote add origin https://github.com/StefanBjornander/Languages.git
@git push origin master
@pause
