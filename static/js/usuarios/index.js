//mostrar los registros de la bd por ajax
function listadoUsuarios(){
    $.ajax({
        url: "/usuarios/listado_usuarios/",
        type:"get",
        dataType: "json",
        success: function(response){
            //En caso de que se regisre un usuario de nuevo, este lo destrulle
            if($.fn.DataTable.isDataTable('#tabla_usuarios')){
                $('#tabla_usuarios').DataTable().destroy();
            }    
            $('#tabla_usuarios tbody').html("");
            for(let i = 0; i < response.length; i++){
                let fila = '<tr>';
                fila += '<td>' + (i +1) + '</td>';
                fila += '<td>' + response[i]["fields"]["username"] + '</td>';
                fila += '<td>' + response[i]["fields"]["nombres"] + '</td>';
                fila += '<td>' + response[i]["fields"]["apellidos"] + '</td>';
                fila += '<td>' + response[i]["fields"]["email"] + '</td>';
                fila += '<td><button> EDITAR </button><button> ELIMINAR </button>'


                fila += '</tr>';
                $('#tabla_usuarios tbody').append(fila);
            }
            $('#tabla_usuarios').DataTable({
                //Todo esto para traducirlo al español
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de _MAX_ total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                      first: "Primero",
                      last: "Ultimo",
                      next: "Siguiente",
                      previous: "Anterior",
                    },
                  },
            });
        },
        error: function(error){
            console.log(error);
        }
    });
}
//registrar usuarios, (listado es el nombre del parametro que le vamos a enviar por el archivo listado_usuario 
//en la parte de enviar el resistro)
function registrar(){
    activarBoton();
	$.ajax({
		data: $('#form_creacion').serialize(),
		url: $('#form_creacion').attr('action'),
		type: $('#form_creacion').attr('method'),
		success: function(response){
            notificacionSuccess(response.mensaje);
			listadoUsuarios();
			cerrar_modal_creacion();
		},
		error: function (error){
            notificacionError(error.mensaje);
            mostrarErroresCreacion(error); 
            activarBoton();
		}
	})
}

$(document).ready(function (){
    listadoUsuarios();
});