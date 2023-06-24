var total=0;

function addToCart(event) {
    event.preventDefault();
    
    // Obtener los detalles del producto
    var card = event.target.closest('.card');
    var title = card.querySelector('.card-text').textContent;
    var price = card.querySelector('.andes-money-amount__fraction').textContent;

   var id = event.target.dataset.id;
   
   // Crear un elemento para mostrar los detalles del producto en el carrito

var product = document.createElement('div');
product.classList.add('product-item');
product.innerHTML = `
  <h3>${title} - $${Math.floor(parseFloat(price))}</h3>
  <button class="btn btn-sm btn-outline-secondary remove-from-cart" data-id="${id}">Eliminar</button>
`;

  

  
   // Agregar el producto al carrito
   var carrito = document.getElementById('carrito');
   carrito.appendChild(product);

   total += parseFloat(price);
   var totalCarrito = document.getElementById('total-carrito');
   totalCarrito.textContent = 'Total: $' + parseFloat(total).toFixed(0);
   
   // Actualizar el contador de productos
   var contador = document.getElementById('contador-productos');
   contador.textContent = parseInt(contador.textContent) + 1;
   
   // Asignar el evento click al botón de eliminación
   var removeButtons = document.getElementsByClassName('remove-from-cart');
   for (var i = 0; i < removeButtons.length; i++) {
     removeButtons[i].addEventListener('click', removeFromCart);
   }
    
  }
  
  // Función para eliminar un producto del carrito
  function removeFromCart(event) {
    event.preventDefault();
    
    var id = event.target.dataset.id;
    
    // Eliminar el producto del carrito
    var product = event.target.closest('.product-item');
    var price = product.querySelector('h3').textContent.split('$')[1];
    product.remove();
    
    // Actualizar el contador de productos
    var contador = document.getElementById('contador-productos');
    contador.textContent = parseInt(contador.textContent) - 1;

    total -= parseFloat(price);
    var totalCarrito = document.getElementById('total-carrito');
    totalCarrito.textContent = 'Total: $' + parseFloat(total).toFixed(0);

    if(total === 0){
    totalCarrito.textContent = 'Carrito Vacío'}

  }
  
  // Obtener todos los enlaces "Añadir a carrito"
  var addToCartLinks = document.getElementsByClassName('add-to-cart');
  // Asignar el evento click a cada enlace
  for (var i = 0; i < addToCartLinks.length; i++) {
    addToCartLinks[i].addEventListener('click', addToCart);
  }