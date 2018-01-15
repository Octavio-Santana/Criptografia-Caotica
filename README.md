# Criptografia Caótica

   Ao estudar o problema de 3 corpos Poincaré propos que um sistema de equações diferenciais determinístico pode ser imprevisível,
   apesar de não ser aceito pela comunidade cientifica de sua época. Somente quanto Lorentz ao estudar problemas atmosféricos
   mostrou que pequenas variações nas condições inicias no sistema pode acarretar em grandes diferenças na evolução temporal do
   sistema.
    
   As equações de Lorentz na forma simplifica:
   
         dx/dt = s*( y - x )
      
         dy/dt = x*( r - z ) - y
      
         dz/dt = x*y - b*z

   Dada uma condição inicial (chave inicial), podemos criptografar a mensagem misturando com a dinâmica caótica destas equações
   diferenciais, tal que para descriptografar a mensgaem é necessário termos a mesma chave inicial, pois qualquer diferença não
   retornamos a mensagem original.
   
   
# Dicas

   Os arquivos com extensão ipython são ilustrativos e foi testado apenas na versão 2.7 do python. Para proposito de aplicação utilize apenas o arquivo com nome codificador.py.  
   
   O arquivo exemplo.py ilustra bem como ultulizar.
