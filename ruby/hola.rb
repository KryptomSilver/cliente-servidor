class Punto

    # constructor
    def initialize(valorX, valorY)
        #Creamos atributos de la clase
        @x = valorX
        @y = valorY
    end

    # Métodos get para regresar los valores de los atributos del objeto
    def getX()
        return @x 
    end 

    def getY()
        return @y
    end

    # Metodos set para modificar el valor de los atributos del objeto
    def setX(valorX)
        @x = valorX
    end

    def setY(valorY)
        @y = valorY
    end
end

# Crear un objeto de la clase punto y llamar a sus metodos
pa = Punto.new(0,0)
pb = Punto.new(10,10)

# Imprimimos atributos
puts "Coordenadas del punto pa: #{pa.getX()}, #{pa.getY()}"
puts "Coordenadas del punto pb: #{pb.getX()}, #{pb.getY()}"