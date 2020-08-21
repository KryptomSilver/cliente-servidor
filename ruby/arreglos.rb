#clase para el manejo de arreglos en ruby

class Arreglo
    def initialize()
        @vector = []
    end
    # insertar elemento en el arreglo
    def insert(elem)
        @vector.push(elem)
    end
    def buscar(elem)
        puts"Elemento buscado es: [#{@vector.index(elem)}]=#{elem}"

        @vector.each do |elemento|
            if @vector[elemento] == elem
                puts "El elemento buscado es: #{@vector[elemento]}"
            end
        end
        if elemento == @vector.length
            puts "Elemento buscado no existe: #{elem}"
        end
    end
    def printAll()
        if @vector.length > 0 
            @vector.each_with_index do |elemento,index|
                puts "Elemento[#{index}]=#{elemento}"
            end
        else
            puts "El arreglo esta vacio"
        end
    end

end
