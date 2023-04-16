class Carrito:
    #inicializar
    def __init__(self, request):
        #el request va ser igual al request que vamo a reciber
        self.request = request
        #la session igual la session de nuestro request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            # si no existe carrito  va ser igual a un deccionario vacio
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        #si el carrito no esta vacio
        else:
            self.carrito = carrito
    # agregar un nuevo producto al carrito
    def agregar(self, producto):
        pk = str(producto.nombre)
        # si el pk no esta en el carrito
        if pk not in self.carrito.keys():
            self.carrito[pk]={
                "producto_pk": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
            }
        else:
            #self.carrito[pk]["carrito"] += 1
            self.carrito[pk]["precio"] += producto.precio
        self.guardar_carrito()
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    def eliminar(self, producto):
        pk = str(producto.nombre)
        if pk in self.carrito:
            del self.carrito[pk]
            self.guardar_carrito();
    def restar(self, producto):
        pk = str(producto.nombre)
        if pk in self.carrito.keys():
            self.carrito[pk]["cantidad"] -= 1
            self.carrito[pk]["precio"] -= producto.precio
            if self.carrito[pk]["cantidad"] <= 0:
                self.eliminar(producto)
                self.guardar_carrito()
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True




