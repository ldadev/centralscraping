



var formulario = document.getElementById('formulario')
var respuesta = document.getElementById("respuesta")

$('#btn-create,#btn-update').click(function(){
	var datos = new FormData(formulario);
	$('#datatable tr').click(function () {

			var currentRow=$(this).closest("tr"); 
			var col_id=currentRow.find("td:eq(0)").text(); // get current row 1st TD value
			var col_name=currentRow.find("td:eq(1)").text(); // get current row 2nd TD
			var col_author=currentRow.find("td:eq(2)").text(); // get current row 3rd TD
			$('input[name="id"]').val(col_id);
			$('input[name="name"]').val(col_name);
			$('input[name="author"]').val(col_author);
	  });
    $('#ModalCreate').modal('show');
});



var msgs = (alert_type,msg) => '<div class="alert ' + alert_type + ' alert-dismissible fade show" role="alert">' + msg +
'</div>';

function close_alert(){
	setTimeout(function() {
		$(".alert").remove().fadeOut(2000);
    },1000);
};


formulario.addEventListener('submit',function(e){
	e.preventDefault();

	var datos = new FormData(formulario);

	const get_data = async() =>{
		try{
			const res = await fetch('/books/add/',{method: 'POST',body:datos})
			const data = await res.json()

			if(data.msg){
				respuesta.innerHTML = msgs('alert-success',data.msg)
				close_alert();
				var URLsearch = '/books/list/' + window.location.search + ' #contenido';
				$("#contenido").load(URLsearch);
			}
			else{
				respuesta.innerHTML = msgs('alert-warning',data.msg)
			}

		}catch(error){
			console.log(error)
		}
	}
	get_data()
	});


	/*
	fetch('/books/add/',{
		method: 'POST',
		body:datos,
	})
	.then(response => response.json())
	.then(data => {

		if(data.msg){
			respuesta.innerHTML = msgs('alert-success',data.msg);
		}
		else{
			respuesta.innerHTML = msgs('alert-warning',data.msg);
		};
		

	});
	});
	*/



