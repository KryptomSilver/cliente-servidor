# Clase que muestra la herencia de ruby

load "hola.rb"


class Circunferencia < Punto

    def initialize(vRadio)
        @radio = vRadio
    end

    def getRadio()
        return @radio
    end

    def setRadio(vRadio)
        @radio = vRadio
    end
    def getArea()
        return Math::PI * vRadio**2
    end
   
    # Escribir un metodo que calcule el area de la circunfera

end

#cir = Circunferencia.new(3)

#puts "El radio es: #{cir.getRadio()}"
# Invocamos Métodos de la clase Punto
#cir.setX(10)
#cir.setY(10)
#puts "Las Coordenadas: #{cir.getX()}, #{cir.getY}"
#puts "El area de la circunferencia es: #{cir.getArea(cir.getRadio)}"
#puts "EL volumen "