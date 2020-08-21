load "area.rb"


class Volumen < Circunferencia
    def initialize(vAltura)
        @altura = vAltura
    end

    def getAltura()
        return @altura
    end

    def setAltura(vAltura)
        @valtura = vAltura
    end
    def getVolumen()
        return getArea() * getAltura()
    end
end

vol = Volumen.new(12)
vol.setRadio(12)

puts "El altura es:  #{vol.getAltura()}"
puts "El area es:  #{vol.getVolumen()}"