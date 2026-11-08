document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript cargado correctamente");

  // Elementos del DOM
  const loginForm = document.getElementById("loginForm");
  const togglePassword = document.getElementById("togglePassword");
  const passwordInput = document.getElementById("password");
  const usernameInput = document.getElementById("username");
  const loginButton = document.getElementById("loginButton");
  const usernameError = document.getElementById("usernameError");
  const passwordError = document.getElementById("passwordError");

  // Verificar que todos los elementos existen
  if (!loginForm || !togglePassword || !passwordInput || !usernameInput) {
    console.error("No se encontraron algunos elementos del DOM");
    return;
  }

  console.log("Todos los elementos del DOM encontrados");

  // Mostrar/ocultar contraseña
  togglePassword.addEventListener("click", function () {
    console.log("Botón de mostrar contraseña clickeado");

    const type =
      passwordInput.getAttribute("type") === "password" ? "text" : "password";
    passwordInput.setAttribute("type", type);

    // Cambiar icono
    const icon = this.querySelector("i");
    if (icon.classList.contains("fa-eye")) {
      icon.classList.remove("fa-eye");
      icon.classList.add("fa-eye-slash");
    } else {
      icon.classList.remove("fa-eye-slash");
      icon.classList.add("fa-eye");
    }
  });

  // Validación del formulario
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    console.log("Formulario enviado");

    // Remover mensajes de error previos
    clearErrors();

    // Validar campos
    let isValid = true;

    // Validar username
    if (!usernameInput.value.trim()) {
      showError(
        usernameInput,
        usernameError,
        "El nombre de usuario es requerido"
      );
      isValid = false;
    } else if (usernameInput.value.trim().length < 3) {
      showError(
        usernameInput,
        usernameError,
        "El usuario debe tener al menos 3 caracteres"
      );
      isValid = false;
    }

    // Validar password
    if (!passwordInput.value.trim()) {
      showError(passwordInput, passwordError, "La contraseña es requerida");
      isValid = false;
    } else if (passwordInput.value.length < 6) {
      showError(
        passwordInput,
        passwordError,
        "La contraseña debe tener al menos 6 caracteres"
      );
      isValid = false;
    }

    // Si es válido, procesar login
    if (isValid) {
      console.log("Formulario válido, procesando login...");
      processLogin();
    } else {
      console.log("Formulario inválido");
    }
  });

  // Limpiar errores al escribir
  usernameInput.addEventListener("input", function () {
    clearError(usernameInput, usernameError);
  });

  passwordInput.addEventListener("input", function () {
    clearError(passwordInput, passwordError);
  });

  // Funciones de ayuda
  function showError(input, errorElement, message) {
    input.classList.add("error");
    errorElement.textContent = message;
    console.log("Error mostrado:", message);
  }

  function clearError(input, errorElement) {
    input.classList.remove("error");
    errorElement.textContent = "";
  }

  function clearErrors() {
    clearError(usernameInput, usernameError);
    clearError(passwordInput, passwordError);
    console.log("Errores limpiados");
  }

  function processLogin() {
    const originalText = loginButton.innerHTML;

    // Deshabilitar botón y mostrar loading
    loginButton.disabled = true;
    loginButton.innerHTML =
      '<i class="fas fa-spinner fa-spin"></i> Iniciando sesión...';

    console.log("Procesando login...");

    // Simular proceso de login (2 segundos)
    setTimeout(() => {
      // Aquí iría la lógica real de autenticación
      const username = usernameInput.value;
      const password = passwordInput.value;
      const remember = document.getElementById("remember").checked;

      console.log("Datos de login:", {
        username: username,
        password: "*".repeat(password.length),
        remember: remember,
      });

      // Simular respuesta exitosa
      alert(
        `¡Bienvenido ${username}! Login exitoso.\n\n(Esta es una simulación)`
      );

      // Restaurar botón
      loginButton.disabled = false;
      loginButton.innerHTML = originalText;

      console.log("Login completado");

      // Aquí redirigirías al usuario a la página principal
      // window.location.href = 'dashboard.html';
    }, 2000);
  }
});
