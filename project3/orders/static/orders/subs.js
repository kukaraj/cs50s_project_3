var cart = false;

document.addEventListener('DOMContentLoaded',function(){

	document.querySelectorAll('.dropdown-menu li a').forEach( link => {

		link.onclick = function() {

			const name = this.innerText
			this.parentElement.parentElement.previousElementSibling.innerText = name;
			check_field(cart);
			return false;
		}

	});

	

    document.querySelector('.add_to_cart').onclick = ()=>{

    	cart = true;
    	check_field(cart)
    }

    document.querySelectorAll('.navbar .nav-link').forEach(function(link) {
    		if (link == window.location.href)
    			link.parentElement.classList.add('active')
    	});


});

function check_field(cart){

	topping = document.querySelectorAll('.btn')[0].innerText
	add_on = document.querySelectorAll('.btn')[1].innerText
	size = document.querySelectorAll('.btn')[2].innerText

	if (topping=='_ _ _ _ _ _ '){
		document.querySelector('.total_msg').innerHTML = "Please select a prefered pizza type"
	}

	else if(size=='_ _ _ _ _ _ '){
		document.querySelector('.total_msg').innerHTML = "Please select the prefered toppings"
	}

	else{

		if (add_on=='_ _ _ _ _ _ '){
			add_on="empty";
		}
		document.querySelector('.total_msg').innerHTML = " "
		
		const price = new XMLHttpRequest();
		price.open('POST', '/order/price');
			price.onload = () => {
				const response = JSON.parse(price.responseText);
				document.querySelector('.total_value').innerHTML = response.price
				document.querySelector('.total_basket_value').innerHTML = response.total_price
			};

			var el = document.getElementsByName("csrfmiddlewaretoken");
			csrf_value = el[0].getAttribute("value");

			const data = new FormData();

			data.append('menu', "subs");
		    data.append('data1', topping);
            data.append('data2', add_on);
            data.append('data3', size);
            data.append('csrfmiddlewaretoken',csrf_value)

            if (cart){
            	data.append('cart',true)
            }

            price.send(data);
	}


}


