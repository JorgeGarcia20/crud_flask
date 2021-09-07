const nombre = document.getElementById('campo_nombre')
const categoria = document.getElementById('campo_categoria')
const total = document.getElementById('campo_total')
let id_producto = document.getElementById('id').responseText
console.log(id_producto)

function cargar(id) {
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 & this.status == 200) {
      document.getElementById('campo_nombre').innerHTML = this.responseText;
    }
  };

  xhttp.open('GET', `/agregar/${id}`, true);
  xhttp.send();
}

const btnCargar = document.getElementById('btn');
btnCargar.addEventListener("click", cargar(2))








// productos = []

// function consultar(id) {
//   fetch(`agregar/${id}`)
//     .then(data => data.json())
//     .then(producto => {
//       productos = producto.data;
//       console.log(productos)
//     });
// }

// const btn = document.getElementById('btn')
// btn.addEventListener('click', consultar(1))




// $(document).ready(function () {

//   function ajax_products(id) {
//     $.ajax({
//       url: `agregar/${id}`,
//       data: $('form').serialize(),
//       type: 'POST',
//       success: function (response) {
//         console.log(response);
//       },
//       error: function (error) {
//         console.log(error)
//       }
//     });
//   }

//   $("#btn").trigger("click", function (event) {
//     event.preventDefault();
//     ajax_products();
//   });
// })