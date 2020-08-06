/*
Nombre: holamnundo.c
Objetivo: mi primer programa en ansi c
Autor:
Fecha:
*/
#include <stdio.h>
#include <string.h>
/**
Función para regresar un mensaje
**/

char* getMessage()
{
	return "Hola mundo";
}
int suma (int n1, int n2)
{
	return n1+n2;
}
char* main()
{
	printf("El mensaje es: %s\n",getMessage());
	printf("La suma es:%d\n",suma(2,5));
	return 0;
}
