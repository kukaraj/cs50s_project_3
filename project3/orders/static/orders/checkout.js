document.addEventListener('DOMContentLoaded',function(){

	document.querySelectorAll('.table tbody tr').forEach( tr => {

		tr.onclick = function() {

			

			const name = td.innerHTML
			alert(name)
			return false;
		}

	});
});