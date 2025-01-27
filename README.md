Entrega final - Playground Final project - Daniel Greyling
============================================

Página para crear vales de combustible, para generar control de movimientos de combustible en una empresa de helicópteros.

Cuenta con app principal 'fuel', que contiene CRUD para los modelos necesarios para crear vales de combustible, un CRUD aparte especializado para crear los vales de combustile, un buscador de vales que funciona con id, matricula, patente, nombre de despachador o receptor.

Tiene app 'accounts' que gestiona el CRUD de usuarios (que son los despachadores y receptores de la app 'fuel'), además de tener perfil con avatares.

Todo en base a app 'main', que tiene el html padre del cual se hace herencia en toda la app, pagina acerca de, vistas estructurales para llegar donde quieres ir, header, footer, etc.

El proyecto entero trabaja con mezcla de vistas basadas en funciones y clases, con mixins personalizados, getión de errores 403 y 404.

Se iba a desarrollar app 'chat' de mensajería, pero por tiempo no se pudo. No afecta funcionalidad de la página.

Para utilizar la página, primero se debe crear superuser, usuario con el que se creará un modelo ModeloHelicóptero, seguido de un modelo Aeronave, luego un modelo Camion. Todo esto a través de la página 'Registrar datos' que aparece en el inicio de la página.

Posteriormente, es necesario crear por lo menos un usuario a través del gestor de usuarios de la página (pestaña cuentas del navbar).

Teniendo estos requisitos, y estando con sesión iniciada, se podrá ir a control de combustible y crear un vale.
Ahí se deben rellenar todos los campos, menos id y despachador que se rellenan automáticamente. Id verá el número correlativo de vale según la cantidad generada anteriormente, y despachador será el usuario con sesión iniciada.

Teniendo registrado por lo menos un vale, se podrá usar el resto de las funciones, de ver en lista y detalle, editar y borrar los vales (siendo superuser estos ultimos dos), al igual que el resto de los modelos.

También funcionará la barra de búsqueda del navbar.

En caso de no tener usuario logeado mandará a la página de registro, y en caso de no tener los permisos correspondientes aparecerá una pantalla de error 403 que permite cerrar sesión y volver a abrir sesión con otro usuario.




Video demostrativo: 