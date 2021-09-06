const registro = document.getElementById('registro');
const inputs = document.querySelectorAll('#registro input');

const expresiones = {
  nombre_apellidos: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
  nick: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
  password: /^.{4,12}$/, // 4 a 12 digitos.
  rfc: /^[A-Z0-9]{10}$/, // Letras, numeros, guion y guion_bajo
  correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
  direccion: /^[a-zA-ZÀ-ÿ\s\/]{10,100}$/, // Letras y espacios, pueden llevar acentos.
}

const validarFormulario = (e) => {
  switch (e.target.name) {
    case "nombre":
      validarCampo(expresiones.nombre_apellidos, e.target, 'nombre')
      break;

    case "apellidos":
      validarCampo(expresiones.nombre_apellidos, e.target, 'apellidos')
      break;

    case "nick":
      validarCampo(expresiones.nick, e.target, 'nick')
      break;

    case "password":
      validarCampo(expresiones.password, e.target, 'password')
      validarPassword2();
      break;

    case "password2":
      validarPassword2();
      break;

    case "correo":
      validarCampo(expresiones.correo, e.target, 'correo')
      break;

    case "rfc":
      validarCampo(expresiones.rfc, e.target, 'rfc')
      break;

    case "direccion":
      validarCampo(expresiones.direccion, e.target, 'direccion')
      break;
  }
}

const validarCampo = (expresion, input, campo) => {
  field = document.getElementById(campo)
  if (expresion.test(input.value)) {
    field.classList.remove('is-invalid');
    field.classList.add('is-valid');
  } else {
    field.classList.add('is-invalid');
    field.classList.remove('is-valid');
  }
}

const validarPassword2 = () => {
  const password1 = document.getElementById('password');
  const password2 = document.getElementById('password2');

  console.log(password1.value)
  console.log(password2.value)

  if (password1.value !== password2.value) {
    password2.classList.remove('is-valid');
    password2.classList.add('is-invalid');
    // campos['password'] = false;
  } else {
    password2.classList.add('is-valid');
    password2.classList.remove('is-invalid');
    // campos['password'] = true;
  }
}
inputs.forEach((input) => {
  input.addEventListener('keyup', validarFormulario);
  input.addEventListener('blur', validarFormulario)
});

registro.addEventListener('submit', (e) => {
  e.preventDefault();
});

console.log(inputs)