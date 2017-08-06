# Criptografia-Caotica

   A idéia de um sistema ser determinístico e imprevisível, proposto por Poicaré com o problema dos três corpos, não foi aceito
   pela comunidade científica em sua epoca. Lorenz estudando problemas atmosféricos mostrou, utilizando cálculos computacionais,
   que pequenas variações nas condições iniciais poderiam acarretar grandes diferenças na evolução do sistema. 
    
   As equações de Lorentz na forma simplifica:
   
      dx/dt = s*( y - x )     
      
      dy/dt = x*( r - z ) - y
      
      dz/dt = x*y - b*z

   Dada uma condição inicial (chave inicial), podemos criptografar a mensagem misturando com a dinâmica caótica destas equações
   diferenciais, tal que para descriptografar a mensgaem é necessário termos a mesma chave inicial, pois qualquer diferença não
   retornamos a mensgaem original.
