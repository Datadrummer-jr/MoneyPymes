# include <iostream>
// Las funciones en esta cabecera existen dentro del espacio de nombres std::

namespace mi_paquete{
   int mi_valor;
};

int main()
{
   int mi_valor = 3;
   mi_paquete::mi_valor = mi_valor * mi_valor;

   std::cout << mi_valor << '\n'; // imprime '3'
   std::cout << mi_paquete::mi_valor << '\n'; // imprime '4'

   return 0;
}
