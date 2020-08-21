load "arreglos.rb"

vec = Arreglo.new()

vec.insert("first")
vec.insert(12)
vec.insert(false)
vec.insert("C")
vec.insert(12.45)

vec.printAll()


vec.buscar(0)